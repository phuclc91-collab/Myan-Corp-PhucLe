import os
from bs4 import BeautifulSoup

file_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend/payments.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Add IDs to Stats
# Find all h3 tags inside the stats grid
h3s = soup.find_all("h3", class_=lambda x: x and "font-headline-md" in x)
if len(h3s) >= 4:
    h3s[0]['id'] = 'stat-expected'
    h3s[1]['id'] = 'stat-paid'
    h3s[2]['id'] = 'stat-overdue'
    h3s[3]['id'] = 'stat-pending'

# 2. Add ID to Add Button
add_btn = soup.find(lambda tag: tag.name == "button" and "Tạo phiếu thu mới" in tag.text)
if add_btn:
    add_btn['id'] = 'btn-add-payment'

# 3. Empty the table body and add ID
tbody = soup.find("tbody")
if tbody:
    tbody['id'] = 'payment-table-body'
    tbody.clear()

# 4. Inject Modal HTML just before the scripts
modal_html = """
<!-- Create Payment Modal -->
<div class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm transition-opacity" id="payment-modal">
    <div class="bg-surface-container-lowest rounded-xl shadow-lg w-full max-w-md p-lg transform transition-all">
        <div class="flex justify-between items-center mb-md border-b border-outline-variant pb-sm">
            <h3 class="text-headline-sm font-bold text-on-surface">Tạo phiếu thu mới</h3>
            <button class="text-outline hover:text-on-surface" id="btn-close-modal" type="button">
                <span class="material-symbols-outlined">close</span>
            </button>
        </div>
        <form class="space-y-md" id="form-add-payment">
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Khách hàng / Hợp đồng *</label>
                <select class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="payment-lead" required="">
                    <option value="">-- Chọn khách hàng --</option>
                </select>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Đợt thanh toán (Tên gói) *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="payment-plan" placeholder="VD: Tạm ứng đợt 1" required="" type="text"/>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Số tiền (VNĐ) *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="payment-amount" required="" type="number" min="0" step="1000"/>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Hạn thanh toán *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="payment-date" required="" type="date"/>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Trạng thái</label>
                <select class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="payment-status">
                    <option value="active" selected>Chưa thanh toán</option>
                    <option value="completed">Đã thanh toán</option>
                </select>
            </div>
            <div class="pt-md flex justify-end gap-sm">
                <button class="px-md py-2 border border-outline-variant rounded-lg text-on-surface hover:bg-surface-variant font-medium" id="btn-cancel-modal" type="button">Hủy</button>
                <button class="px-md py-2 bg-primary text-white rounded-lg hover:opacity-90 font-medium" id="btn-submit-modal" type="submit">Lưu phiếu thu</button>
            </div>
        </form>
    </div>
</div>
"""
main_tag = soup.find('main')
if main_tag:
    main_tag.append(BeautifulSoup(modal_html, 'html.parser'))

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

# 5. Replace Script block via string manipulation
with open(file_path, "r", encoding="utf-8") as f:
    raw_html = f.read()

start_idx = raw_html.find("<script>\n        // Interactive scripts for demonstration")
end_idx = raw_html.find("</script></body></html>")

if start_idx != -1 and end_idx != -1:
    new_script = """<script>
document.addEventListener('DOMContentLoaded', async () => {
    const { data: { session } } = await supabase.auth.getSession();
    if (!session) {
        window.location.href = 'index.html';
        return;
    }
    
    // Hook up logout
    const logoutLinks = document.querySelectorAll('a, button');
    logoutLinks.forEach(link => {
        if (link.innerText && link.innerText.includes('Đăng xuất')) {
            link.addEventListener('click', async (e) => {
                e.preventDefault();
                await supabase.auth.signOut();
                window.location.href = 'index.html';
            });
            if (link.tagName === 'BUTTON') link.removeAttribute('onclick');
            if (link.tagName === 'A') link.setAttribute('href', '#');
        }
    });

    // --- PAYMENTS LOGIC ---
    const formatCurrency = (val) => new Intl.NumberFormat('vi-VN').format(val || 0);
    const formatDate = (dateStr) => {
        if(!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleDateString('vi-VN');
    };

    const tbody = document.getElementById('payment-table-body');
    const statExpected = document.getElementById('stat-expected');
    const statPaid = document.getElementById('stat-paid');
    const statOverdue = document.getElementById('stat-overdue');
    const statPending = document.getElementById('stat-pending');

    const renderRow = (payment) => {
        let statusHtml = '';
        let actionHtml = '';
        
        if (payment.status === 'completed') {
            statusHtml = `
            <span class="inline-flex items-center px-3 py-1 rounded-full text-label-sm font-semibold bg-[#D1FAE5] text-[#10B981]">
                <span class="w-1.5 h-1.5 rounded-full bg-[#10B981] mr-1.5"></span>Đã thanh toán
            </span>`;
            actionHtml = `
            <button class="p-2 text-on-surface-variant hover:text-primary transition-colors" title="Xem chứng từ">
                <span class="material-symbols-outlined text-[20px]">receipt_long</span>
            </button>`;
        } else if (payment.status === 'past_due') {
            statusHtml = `
            <span class="inline-flex items-center px-3 py-1 rounded-full text-label-sm font-semibold bg-[#FEE2E2] text-[#EF4444]">
                <span class="w-1.5 h-1.5 rounded-full bg-[#EF4444] mr-1.5"></span>Quá hạn
            </span>`;
            actionHtml = `
            <button onclick="confirmPayment('${payment.id}')" class="bg-white border border-outline-variant px-md py-1.5 rounded text-label-sm text-on-surface-variant font-semibold hover:border-primary hover:text-primary transition-all active:scale-95">
                Xác nhận nhận tiền
            </button>`;
        } else if (payment.status === 'active') {
            statusHtml = `
            <span class="inline-flex items-center px-3 py-1 rounded-full text-label-sm font-semibold bg-[#FEF3C7] text-[#F59E0B]">
                <span class="w-1.5 h-1.5 rounded-full bg-[#F59E0B] mr-1.5"></span>Chưa thanh toán
            </span>`;
            actionHtml = `
            <button onclick="confirmPayment('${payment.id}')" class="bg-white border border-outline-variant px-md py-1.5 rounded text-label-sm text-on-surface-variant font-semibold hover:border-primary hover:text-primary transition-all active:scale-95">
                Xác nhận nhận tiền
            </button>`;
        } else {
            statusHtml = `
            <span class="inline-flex items-center px-3 py-1 rounded-full text-label-sm font-semibold bg-surface-container text-on-surface-variant">
                Đã hủy
            </span>`;
        }

        return `
        <tr class="hover:bg-surface-container-low transition-colors group">
            <td class="px-lg py-md">
                <div class="flex flex-col">
                    <span class="font-headline-sm text-headline-sm text-primary">#PMT-${payment.id.substring(0,6).toUpperCase()}</span>
                    <span class="font-body-sm text-body-sm text-on-surface-variant">${payment.leads?.name || 'Không rõ khách hàng'}</span>
                </div>
            </td>
            <td class="px-lg py-md font-body-md text-body-md text-on-surface">${payment.plan_name}</td>
            <td class="px-lg py-md font-headline-sm text-headline-sm text-primary">${formatCurrency(payment.amount)} <span class="text-xs font-normal">VND</span></td>
            <td class="px-lg py-md font-body-md text-body-md text-on-surface">${formatDate(payment.start_date)}</td>
            <td class="px-lg py-md text-center">
                ${statusHtml}
            </td>
            <td class="px-lg py-md text-right">
                ${actionHtml}
            </td>
        </tr>
        `;
    };

    const loadData = async () => {
        try {
            tbody.innerHTML = '<tr><td colspan="6" class="text-center py-10 text-outline">Đang tải dữ liệu...</td></tr>';
            
            // Auto update past_due
            const today = new Date().toISOString().split('T')[0];
            await supabase.from('subscriptions').update({status: 'past_due'}).eq('status', 'active').lt('start_date', today);

            // Fetch
            const { data, error } = await supabase.from('subscriptions').select('*, leads(name)').order('start_date', { ascending: false });
            if (error) throw error;
            
            // Calculate Stats
            let totalExpected = 0;
            let totalPaid = 0;
            let totalOverdue = 0;
            let totalPending = 0;

            data.forEach(p => {
                const amt = parseFloat(p.amount) || 0;
                if (p.status !== 'canceled') totalExpected += amt;
                if (p.status === 'completed') totalPaid += amt;
                if (p.status === 'past_due') totalOverdue += amt;
                if (p.status === 'active') totalPending += amt;
            });

            if(statExpected) statExpected.innerHTML = `${formatCurrency(totalExpected)} <span class="text-body-sm font-normal">VND</span>`;
            if(statPaid) statPaid.innerHTML = `${formatCurrency(totalPaid)} <span class="text-body-sm font-normal">VND</span>`;
            if(statOverdue) statOverdue.innerHTML = `${formatCurrency(totalOverdue)} <span class="text-body-sm font-normal">VND</span>`;
            if(statPending) statPending.innerHTML = `${formatCurrency(totalPending)} <span class="text-body-sm font-normal">VND</span>`;

            if (data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" class="text-center py-10 text-outline">Không có phiếu thu nào.</td></tr>';
                return;
            }
            
            tbody.innerHTML = data.map(p => renderRow(p)).join('');
            
        } catch(err) {
            console.error(err);
            tbody.innerHTML = '<tr><td colspan="6" class="text-center py-10 text-error">Lỗi tải dữ liệu.</td></tr>';
        }
    };

    window.confirmPayment = async (id) => {
        if(!confirm('Xác nhận đã nhận được tiền cho khoản này?')) return;
        try {
            const { error } = await supabase.from('subscriptions').update({ status: 'completed' }).eq('id', id);
            if(error) throw error;
            loadData();
        } catch(err) {
            alert('Lỗi cập nhật: ' + err.message);
        }
    };

    // Modal Logic
    const btnAdd = document.getElementById('btn-add-payment');
    const modal = document.getElementById('payment-modal');
    const formAdd = document.getElementById('form-add-payment');
    const btnClose = document.getElementById('btn-close-modal');
    const btnCancel = document.getElementById('btn-cancel-modal');
    const leadSelect = document.getElementById('payment-lead');

    if(btnAdd) btnAdd.addEventListener('click', () => modal.classList.remove('hidden'));
    const closeModal = () => {
        modal.classList.add('hidden');
        formAdd.reset();
    };
    if(btnClose) btnClose.addEventListener('click', closeModal);
    if(btnCancel) btnCancel.addEventListener('click', closeModal);

    const loadLeadsForDropdown = async () => {
        const { data } = await supabase.from('leads').select('id, name');
        if(data && leadSelect) {
            data.forEach(l => {
                leadSelect.innerHTML += `<option value="${l.id}">${l.name}</option>`;
            });
        }
    };
    loadLeadsForDropdown();

    formAdd.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btnSubmit = document.getElementById('btn-submit-modal');
        btnSubmit.disabled = true;
        btnSubmit.innerText = 'Đang lưu...';

        try {
            const newPayment = {
                lead_id: document.getElementById('payment-lead').value,
                plan_name: document.getElementById('payment-plan').value,
                amount: document.getElementById('payment-amount').value,
                start_date: document.getElementById('payment-date').value,
                status: document.getElementById('payment-status').value
            };

            const { error } = await supabase.from('subscriptions').insert([newPayment]);
            if (error) throw error;
            
            closeModal();
            loadData();
        } catch (err) {
            alert('Lỗi tạo phiếu thu: ' + err.message);
        } finally {
            btnSubmit.disabled = false;
            btnSubmit.innerText = 'Lưu phiếu thu';
        }
    });

    loadData();
});
"""
    raw_html = raw_html[:start_idx] + new_script + raw_html[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(raw_html)

print("Payments module updated successfully.")
