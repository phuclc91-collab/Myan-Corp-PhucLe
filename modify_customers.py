import os
from bs4 import BeautifulSoup

file_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend/customers.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Clear tbody
tbody = soup.find('tbody')
if tbody:
    tbody.clear()
    tbody['id'] = 'customer-table-body'

# 2. Add an ID to the Add button
add_btn = soup.find(lambda tag: tag.name == "button" and "Thêm khách hàng" in tag.text)
if add_btn:
    add_btn['id'] = 'btn-add-customer'

# 3. Add Modal HTML just before closing body
modal_html = """
<!-- Create Customer Modal -->
<div id="customer-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm transition-opacity">
    <div class="bg-surface-container-lowest rounded-xl shadow-lg w-full max-w-md p-lg transform transition-all">
        <div class="flex justify-between items-center mb-md border-b border-outline-variant pb-sm">
            <h3 class="text-headline-sm font-bold text-on-surface">Thêm khách hàng mới</h3>
            <button type="button" id="btn-close-modal" class="text-outline hover:text-on-surface">
                <span class="material-symbols-outlined">close</span>
            </button>
        </div>
        <form id="form-add-customer" class="space-y-md">
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Họ và tên *</label>
                <input type="text" id="cust-name" required class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="Nhập họ và tên">
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Số điện thoại *</label>
                <input type="text" id="cust-phone" required class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="Nhập số điện thoại">
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Email</label>
                <input type="email" id="cust-email" class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" placeholder="Nhập email">
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Giá trị ước tính (VNĐ)</label>
                <input type="number" id="cust-value" value="0" class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20">
            </div>
            <div class="pt-md flex justify-end gap-sm">
                <button type="button" id="btn-cancel-modal" class="px-md py-2 border border-outline-variant rounded-lg text-on-surface hover:bg-surface-variant font-medium">Hủy</button>
                <button type="submit" id="btn-submit-modal" class="px-md py-2 bg-primary text-white rounded-lg hover:opacity-90 font-medium">Lưu khách hàng</button>
            </div>
        </form>
    </div>
</div>
"""
modal_soup = BeautifulSoup(modal_html, 'html.parser')
if soup.body:
    soup.body.append(modal_soup)

# 4. Add JS logic
script_logic = """
<script>
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

    // Load Customers
    const loadCustomers = async () => {
        try {
            tbody.innerHTML = '<tr><td colspan="7" class="text-center py-4">Đang tải dữ liệu...</td></tr>';
            // Lấy danh sách khách hàng cùng với tên người phụ trách từ bảng profiles
            const { data, error } = await supabase
                .from('leads')
                .select(`
                    *,
                    profiles!leads_assigned_to_fkey (full_name)
                `)
                .order('created_at', { ascending: false });
                
            if (error) throw error;
            
            tbody.innerHTML = '';
            if (data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" class="text-center py-4">Chưa có khách hàng nào.</td></tr>';
                return;
            }

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
        } catch (err) {
            console.error('Error loading customers:', err);
            tbody.innerHTML = '<tr><td colspan="7" class="text-center py-4 text-error">Lỗi tải dữ liệu: ' + err.message + '</td></tr>';
        }
    };

    // Add Customer
    formAdd.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btnSubmit = document.getElementById('btn-submit-modal');
        btnSubmit.disabled = true;
        btnSubmit.innerText = 'Đang lưu...';

        try {
            const newLead = {
                name: document.getElementById('cust-name').value,
                phone: document.getElementById('cust-phone').value,
                email: document.getElementById('cust-email').value,
                expected_value: document.getElementById('cust-value').value || 0,
                assigned_to: user.id, // Assign cho chính mình
                created_by: user.id
            };

            const { data, error } = await supabase.from('leads').insert([newLead]);
            if (error) throw error;
            
            closeModal();
            loadCustomers();
        } catch (err) {
            alert('Lỗi thêm khách hàng: ' + err.message);
        } finally {
            btnSubmit.disabled = false;
            btnSubmit.innerText = 'Lưu khách hàng';
        }
    });

    // Load initial data
    loadCustomers();
});
</script>
"""
script_soup = BeautifulSoup(script_logic, 'html.parser')
if soup.body:
    soup.body.append(script_soup)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Modified customers.html successfully.")
