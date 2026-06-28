import os
from bs4 import BeautifulSoup

file_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend/customers.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Add PapaParse
if not soup.find(src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"):
    script_tag = soup.new_tag("script", src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js")
    soup.head.append(script_tag)

# 2. Search Input ID
search_input = soup.find("input", placeholder="Tìm theo tên, SĐT, Email")
if search_input:
    search_input['id'] = 'search-input'

# 3. Phân khúc filter -> hide
span_phan_khuc = soup.find(lambda tag: tag.name == "span" and "Phân khúc:" in tag.text)
if span_phan_khuc and span_phan_khuc.parent:
    span_phan_khuc.parent['class'] = span_phan_khuc.parent.get('class', []) + ['hidden']

# 4. Người phụ trách filter -> Add ID
span_phu_trach = soup.find(lambda tag: tag.name == "span" and "Người phụ trách:" in tag.text)
if span_phu_trach and span_phu_trach.find_next_sibling("select"):
    select_staff = span_phu_trach.find_next_sibling("select")
    select_staff['id'] = 'filter-staff'

# 5. Import CSV button and hidden input
btn_import = soup.find(lambda tag: tag.name == "button" and "Import CSV" in tag.text)
if btn_import:
    btn_import['id'] = 'btn-import-csv'
    # Add hidden file input after it
    if not soup.find(id="csv-upload"):
        csv_input = BeautifulSoup('<input type="file" id="csv-upload" accept=".csv" class="hidden">', 'html.parser')
        btn_import.insert_after(csv_input)

# 6. Pagination UI
# Find p tag showing text like "Hiển thị 1 - 5 trong tổng số"
page_info = soup.find(lambda tag: tag.name == "p" and "Hiển thị" in tag.text)
if page_info:
    page_info['id'] = 'page-info'

# Find chevron_left and chevron_right buttons
prev_btn_icon = soup.find(lambda tag: tag.name == "span" and "chevron_left" in tag.text)
if prev_btn_icon and prev_btn_icon.parent:
    prev_btn_icon.parent['id'] = 'btn-prev-page'

next_btn_icon = soup.find(lambda tag: tag.name == "span" and "chevron_right" in tag.text)
if next_btn_icon and next_btn_icon.parent:
    next_btn_icon.parent['id'] = 'btn-next-page'

# Find page numbers container
if prev_btn_icon:
    page_numbers_container = prev_btn_icon.parent.find_next_sibling("div")
    if page_numbers_container:
        page_numbers_container['id'] = 'page-numbers'

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

# 7. Replace Script block via Regex/string manipulation
with open(file_path, "r", encoding="utf-8") as f:
    raw_html = f.read()

# We need to replace the entire <script> block at the bottom
start_idx = raw_html.find("<script>\ndocument.addEventListener('DOMContentLoaded', async () => {")
end_idx = raw_html.find("</script>\n</body></html>")

if start_idx != -1 and end_idx != -1:
    new_script = """<script>
document.addEventListener('DOMContentLoaded', async () => {
    const { data: { session } } = await supabase.auth.getSession();
    if (!session) return;
    const user = session.user;

    const tbody = document.getElementById('customer-table-body');
    const modal = document.getElementById('customer-modal');
    const btnAdd = document.getElementById('btn-add-customer');
    const btnClose = document.getElementById('btn-close-modal');
    const btnCancel = document.getElementById('btn-cancel-modal');
    const formAdd = document.getElementById('form-add-customer');
    
    // Pagination & Filter States
    let currentPage = 1;
    let pageSize = 50;
    let totalCount = 0;
    let searchQuery = '';
    let staffFilter = '';

    // Mở / Đóng Modal
    if(btnAdd) btnAdd.addEventListener('click', () => modal.classList.remove('hidden'));
    const closeModal = () => {
        modal.classList.add('hidden');
        formAdd.reset();
    };
    if(btnClose) btnClose.addEventListener('click', closeModal);
    if(btnCancel) btnCancel.addEventListener('click', closeModal);

    // Format tiền
    const formatCurrency = (val) => new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(val || 0);

    // Get Initials
    const getInitials = (name) => {
        if(!name) return '??';
        const parts = name.trim().split(' ');
        if(parts.length >= 2) return (parts[0][0] + parts[parts.length-1][0]).toUpperCase();
        return name.substring(0,2).toUpperCase();
    };

    // Load Staffs into dropdown
    const loadStaffs = async () => {
        const sel = document.getElementById('filter-staff');
        if(!sel) return;
        const { data } = await supabase.from('profiles').select('id, full_name, role');
        if(data) {
            sel.innerHTML = '<option value="">Tất cả nhân viên</option>';
            data.forEach(p => {
                sel.innerHTML += `<option value="${p.id}">${p.full_name} (${p.role})</option>`;
            });
        }
    };
    loadStaffs();

    // Load Customers
    const loadCustomers = async () => {
        try {
            tbody.innerHTML = '<tr><td colspan="7" class="text-center py-4">Đang tải dữ liệu...</td></tr>';
            
            let query = supabase.from('leads').select(`*, profiles!leads_assigned_to_fkey (full_name)`, { count: 'exact' });
            
            // Filters
            if(searchQuery) {
                query = query.or(`name.ilike.%${searchQuery}%,phone.ilike.%${searchQuery}%,email.ilike.%${searchQuery}%`);
            }
            if(staffFilter) {
                query = query.eq('assigned_to', staffFilter);
            }
            
            // Pagination
            const from = (currentPage - 1) * pageSize;
            const to = from + pageSize - 1;
            
            query = query.order('created_at', { ascending: false }).range(from, to);

            const { data, count, error } = await query;
            if (error) throw error;
            
            totalCount = count;
            
            tbody.innerHTML = '';
            if (data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" class="text-center py-4">Không tìm thấy khách hàng nào.</td></tr>';
            } else {
                data.forEach(lead => {
                    const tr = document.createElement('tr');
                    tr.className = 'hover:bg-surface-container transition-colors group';
                    tr.innerHTML = `
                        <td class="px-lg py-md">
                            <div class="flex items-center gap-md">
                                <div class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-label-md">${getInitials(lead.name)}</div>
                                <span class="text-body-md font-bold text-on-surface">${lead.name}</span>
                            </div>
                        </td>
                        <td class="px-lg py-md text-body-md">${lead.phone || ''}</td>
                        <td class="px-lg py-md text-body-md text-outline">${lead.email || ''}</td>
                        <td class="px-lg py-md">
                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-[#3B82F6]/10 text-[#3B82F6] uppercase tracking-wide">Mới</span>
                        </td>
                        <td class="px-lg py-md text-body-md font-semibold text-primary">${formatCurrency(lead.expected_value)}</td>
                        <td class="px-lg py-md">
                            <div class="flex items-center gap-sm">
                                <div class="w-6 h-6 rounded-full bg-surface-dim overflow-hidden flex items-center justify-center text-[10px] text-white">👤</div>
                                <span class="text-body-sm">${lead.profiles ? lead.profiles.full_name : 'Unknown'}</span>
                            </div>
                        </td>
                        <td class="px-lg py-md text-right">
                            <button class="p-1 hover:bg-outline-variant rounded transition-colors text-outline">
                                <span class="material-symbols-outlined">more_vert</span>
                            </button>
                        </td>
                    `;
                    tbody.appendChild(tr);
                });
            }
            
            updatePaginationUI(from, data.length);
        } catch (err) {
            console.error('Error loading customers:', err);
            tbody.innerHTML = '<tr><td colspan="7" class="text-center py-4 text-error">Lỗi tải dữ liệu: ' + err.message + '</td></tr>';
        }
    };
    
    // Render Pagination
    const updatePaginationUI = (from, currentCount) => {
        const info = document.getElementById('page-info');
        const btnPrev = document.getElementById('btn-prev-page');
        const btnNext = document.getElementById('btn-next-page');
        const pageNums = document.getElementById('page-numbers');
        
        if(info) {
            info.innerText = `Hiển thị ${totalCount === 0 ? 0 : from + 1} - ${from + currentCount} trong tổng số ${totalCount} khách hàng`;
        }
        
        const totalPages = Math.ceil(totalCount / pageSize);
        if(btnPrev) {
            btnPrev.disabled = currentPage <= 1;
            btnPrev.onclick = () => { if(currentPage > 1) { currentPage--; loadCustomers(); } };
        }
        if(btnNext) {
            btnNext.disabled = currentPage >= totalPages;
            btnNext.onclick = () => { if(currentPage < totalPages) { currentPage++; loadCustomers(); } };
        }
        
        if(pageNums) {
            pageNums.innerHTML = `<button class="w-10 h-10 rounded-lg bg-primary text-white font-bold text-body-sm">${currentPage}</button>`;
            if (totalPages > 1) {
               pageNums.innerHTML += `<span class="px-2 text-outline">/ ${totalPages}</span>`;
            }
        }
    };

    // Filter Listeners
    const searchInput = document.getElementById('search-input');
    let searchTimeout;
    if(searchInput) {
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                searchQuery = e.target.value.trim();
                currentPage = 1;
                loadCustomers();
            }, 500); // debounce 500ms
        });
    }
    
    const staffSelect = document.getElementById('filter-staff');
    if(staffSelect) {
        staffSelect.addEventListener('change', (e) => {
            staffFilter = e.target.value;
            currentPage = 1;
            loadCustomers();
        });
    }

    // Import CSV via PapaParse
    const btnImport = document.getElementById('btn-import-csv');
    const csvUpload = document.getElementById('csv-upload');
    if(btnImport && csvUpload) {
        btnImport.addEventListener('click', () => csvUpload.click());
        csvUpload.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if(!file) return;
            
            Papa.parse(file, {
                header: true,
                skipEmptyLines: true,
                complete: async function(results) {
                    const rows = results.data;
                    if(rows.length === 0) {
                        alert("File CSV trống!");
                        return;
                    }
                    
                    const btnOriginalText = btnImport.innerHTML;
                    btnImport.innerText = 'Đang tải lên...';
                    btnImport.disabled = true;
                    
                    try {
                        const insertData = rows.map(r => ({
                            name: r.name || r['Họ Tên'] || r.Name,
                            phone: r.phone || r['SĐT'] || r.Phone,
                            email: r.email || r.Email || r['Email'],
                            expected_value: parseFloat(r.expected_value || r['Giá trị'] || 0),
                            assigned_to: user.id,
                            created_by: user.id
                        })).filter(r => r.name && r.phone); // Require name and phone
                        
                        if(insertData.length === 0) {
                            alert("Không tìm thấy dòng hợp lệ. Vui lòng đảm bảo cột Tên và SĐT (name, phone) tồn tại.");
                            return;
                        }
                        
                        const { error } = await supabase.from('leads').insert(insertData);
                        if(error) throw error;
                        
                        alert(`Nhập thành công ${insertData.length} khách hàng!`);
                        currentPage = 1;
                        loadCustomers();
                    } catch(err) {
                        alert('Lỗi import CSV: ' + err.message);
                    } finally {
                        btnImport.innerHTML = btnOriginalText;
                        btnImport.disabled = false;
                        csvUpload.value = '';
                    }
                }
            });
        });
    }

    // Add Customer Form Submit
    formAdd.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btnSubmit = document.getElementById('btn-submit-modal');
        const origText = btnSubmit.innerText;
        btnSubmit.disabled = true;
        btnSubmit.innerText = 'Đang lưu...';

        try {
            const newLead = {
                name: document.getElementById('cust-name').value,
                phone: document.getElementById('cust-phone').value,
                email: document.getElementById('cust-email').value,
                expected_value: document.getElementById('cust-value').value || 0,
                assigned_to: user.id,
                created_by: user.id
            };

            const { error } = await supabase.from('leads').insert([newLead]);
            if (error) throw error;
            
            closeModal();
            currentPage = 1;
            loadCustomers();
        } catch (err) {
            alert('Lỗi thêm khách hàng: ' + err.message);
        } finally {
            btnSubmit.disabled = false;
            btnSubmit.innerText = origText;
        }
    });

    // Load initial data
    loadCustomers();
});
"""
    raw_html = raw_html[:start_idx] + new_script + raw_html[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(raw_html)

print("Customers module updated successfully.")
