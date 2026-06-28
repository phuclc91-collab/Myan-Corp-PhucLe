import os
from bs4 import BeautifulSoup

file_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend/tasks.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Add btn-add-task ID
add_btn = soup.find(lambda tag: tag.name == "button" and "+ Tạo công việc mới" in tag.text)
if add_btn:
    add_btn['id'] = 'btn-add-task'

# 2. Add IDs to filter buttons
filters_container = soup.find(lambda tag: tag.name == "button" and "Tất cả" in tag.text).parent
if filters_container:
    btns = filters_container.find_all('button')
    if len(btns) >= 5:
        btns[0]['id'] = 'filter-all'
        btns[1]['id'] = 'filter-mine'
        btns[2]['id'] = 'filter-progress'
        btns[3]['id'] = 'filter-done'
        btns[4]['id'] = 'filter-overdue'

# 3. Clear static tasks
tasks_container = soup.find("div", class_="space-y-sm")
if tasks_container:
    tasks_container['id'] = 'task-list'
    tasks_container.clear()

# 4. Inject Modal HTML just before the scripts
modal_html = """
<!-- Create Task Modal -->
<div class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm transition-opacity" id="task-modal">
    <div class="bg-surface-container-lowest rounded-xl shadow-lg w-full max-w-md p-lg transform transition-all">
        <div class="flex justify-between items-center mb-md border-b border-outline-variant pb-sm">
            <h3 class="text-headline-sm font-bold text-on-surface">Thêm công việc mới</h3>
            <button class="text-outline hover:text-on-surface" id="btn-close-modal" type="button">
                <span class="material-symbols-outlined">close</span>
            </button>
        </div>
        <form class="space-y-md" id="form-add-task">
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Tên công việc *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="task-title" placeholder="VD: Gọi điện tư vấn" required="" type="text"/>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Khách hàng liên quan *</label>
                <select class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="task-lead" required="">
                    <option value="">-- Chọn khách hàng --</option>
                </select>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Hạn chót *</label>
                <input class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="task-due-date" required="" type="datetime-local"/>
            </div>
            <div>
                <label class="block text-label-md text-on-surface-variant mb-xs">Mức độ ưu tiên</label>
                <select class="w-full border border-outline-variant rounded-lg p-2 text-body-md focus:ring-2 focus:ring-primary/20" id="task-priority">
                    <option value="thap">Thấp</option>
                    <option value="trung_binh" selected>Trung bình</option>
                    <option value="cao">Cao</option>
                </select>
            </div>
            <div class="pt-md flex justify-end gap-sm">
                <button class="px-md py-2 border border-outline-variant rounded-lg text-on-surface hover:bg-surface-variant font-medium" id="btn-cancel-modal" type="button">Hủy</button>
                <button class="px-md py-2 bg-primary text-white rounded-lg hover:opacity-90 font-medium" id="btn-submit-modal" type="submit">Lưu công việc</button>
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

start_idx = raw_html.find("<script>\n        document.addEventListener('DOMContentLoaded', async () => {")
end_idx = raw_html.find("</script></body></html>")

if start_idx != -1 and end_idx != -1:
    new_script = """<script>
document.addEventListener('DOMContentLoaded', async () => {
    const { data: { session } } = await supabase.auth.getSession();
    if (!session) {
        window.location.href = 'index.html';
        return;
    }
    const user = session.user;
    
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

    // --- TASKS LOGIC ---
    const taskList = document.getElementById('task-list');
    let currentFilter = 'all'; 

    const btnAdd = document.getElementById('btn-add-task');
    const modal = document.getElementById('task-modal');
    const formAdd = document.getElementById('form-add-task');
    const btnClose = document.getElementById('btn-close-modal');
    const btnCancel = document.getElementById('btn-cancel-modal');
    const leadSelect = document.getElementById('task-lead');

    // Init Modal
    if(btnAdd) btnAdd.addEventListener('click', () => modal.classList.remove('hidden'));
    const closeModal = () => {
        modal.classList.add('hidden');
        formAdd.reset();
    };
    if(btnClose) btnClose.addEventListener('click', closeModal);
    if(btnCancel) btnCancel.addEventListener('click', closeModal);

    const getInitials = (name) => {
        if(!name) return '??';
        const parts = name.trim().split(' ');
        if(parts.length >= 2) return (parts[0][0] + parts[parts.length-1][0]).toUpperCase();
        return name.substring(0,2).toUpperCase();
    };

    const formatDate = (isoString) => {
        const d = new Date(isoString);
        return d.toLocaleDateString('vi-VN') + ' ' + d.toLocaleTimeString('vi-VN', {hour: '2-digit', minute:'2-digit'});
    };

    // Load Leads for Dropdown
    const loadLeadsForDropdown = async () => {
        const { data } = await supabase.from('leads').select('id, name');
        if(data && leadSelect) {
            data.forEach(l => {
                leadSelect.innerHTML += `<option value="${l.id}">${l.name}</option>`;
            });
        }
    };
    loadLeadsForDropdown();

    const renderTask = (task) => {
        const isDone = task.status === 'da_xong';
        const isOverdue = new Date(task.due_date) < new Date() && !isDone;
        
        let priorityColor = 'bg-[#F1F5F9] text-[#64748B]';
        let priorityDot = 'bg-[#94A3B8]';
        let priorityText = 'Thấp';
        
        if (task.priority === 'cao') {
            priorityColor = 'bg-[#FEE2E2] text-[#F43F5E]';
            priorityDot = 'bg-[#F43F5E]';
            priorityText = 'Cao';
        } else if (task.priority === 'trung_binh') {
            priorityColor = 'bg-[#FEF9C3] text-[#A16207]';
            priorityDot = 'bg-[#FACC15]';
            priorityText = 'Trung bình';
        }

        const dateColor = isOverdue ? 'text-[#EF4444]' : 'text-[#64748B]';
        const dateIcon = isDone ? 'done_all' : (isOverdue ? 'event_busy' : 'calendar_today');
        const datePrefix = isDone ? 'Hoàn thành:' : (isOverdue ? 'Quá hạn:' : 'Hạn chót:');
        
        const checkCircleClass = isDone 
            ? 'border-primary bg-primary' 
            : (isOverdue ? 'border-error group-hover:border-error' : 'border-outline-variant group-hover:border-primary');
            
        const checkIcon = isDone ? '<span class="material-symbols-outlined text-white text-[16px]">check</span>' : '<div class="w-3 h-3 rounded-full bg-primary opacity-0 transition-opacity"></div>';
        
        return `
        <div class="bg-white border ${isOverdue && !isDone ? 'border-error/50 shadow-[0_0_10px_rgba(239,68,68,0.1)]' : 'border-[#E2E8F0]'} rounded-lg p-md flex items-center gap-md hover:shadow-sm transition-all group ${isDone ? 'opacity-70' : ''}">
            <div class="w-6 h-6 rounded-full border-2 flex items-center justify-center cursor-pointer ${checkCircleClass}" onclick="toggleTaskStatus('${task.id}', '${isDone ? 'chua_lam' : 'da_xong'}')">
                ${checkIcon}
            </div>
            <div class="flex-1 flex items-center justify-between">
                <div class="flex flex-col">
                    <div class="flex items-center gap-md mb-xs">
                        <span class="font-headline-sm text-headline-sm ${isDone ? 'text-on-surface-variant line-through' : 'text-on-surface'}">${task.title}</span>
                        <span class="px-sm py-0.5 bg-[#F1F5F9] text-[#64748B] font-label-sm text-label-sm rounded border border-[#E2E8F0]">${task.leads?.name || 'Không có khách hàng'}</span>
                    </div>
                    <div class="flex items-center gap-lg">
                        <div class="flex items-center gap-xs ${dateColor} font-body-sm text-body-sm">
                            <span class="material-symbols-outlined text-[14px]">${dateIcon}</span>
                            <span>${datePrefix} ${formatDate(task.due_date)}</span>
                        </div>
                        <div class="flex items-center gap-xs px-sm py-0.5 ${priorityColor} font-label-sm text-label-sm rounded-full">
                            <span class="w-1.5 h-1.5 rounded-full ${priorityDot}"></span>
                            <span>${priorityText}</span>
                        </div>
                    </div>
                </div>
                <div class="flex items-center gap-md">
                    <div class="w-8 h-8 rounded-full bg-surface-container border border-outline-variant flex justify-center items-center font-bold text-[10px] text-primary" title="${task.profiles?.full_name}">
                        ${getInitials(task.profiles?.full_name)}
                    </div>
                    <button class="material-symbols-outlined text-outline hover:text-primary">more_vert</button>
                </div>
            </div>
        </div>
        `;
    };

    const loadTasks = async () => {
        try {
            taskList.innerHTML = '<div class="text-center py-10 text-outline">Đang tải công việc...</div>';
            
            let query = supabase.from('tasks').select('*, leads(name), profiles(full_name)').order('due_date', { ascending: true });
            
            if (currentFilter === 'mine') {
                query = query.eq('assigned_to', user.id);
            } else if (currentFilter === 'progress') {
                query = query.in('status', ['chua_lam', 'dang_lam']);
            } else if (currentFilter === 'done') {
                query = query.eq('status', 'da_xong');
            } else if (currentFilter === 'overdue') {
                const now = new Date().toISOString();
                query = query.lt('due_date', now).neq('status', 'da_xong');
            }
            
            const { data, error } = await query;
            if (error) throw error;
            
            if (data.length === 0) {
                taskList.innerHTML = '<div class="text-center py-10 text-outline">Không có công việc nào.</div>';
                return;
            }
            
            taskList.innerHTML = data.map(t => renderTask(t)).join('');
            
        } catch (err) {
            console.error(err);
            taskList.innerHTML = '<div class="text-center py-10 text-error">Lỗi tải dữ liệu.</div>';
        }
    };

    window.toggleTaskStatus = async (taskId, newStatus) => {
        try {
            const { error } = await supabase.from('tasks').update({ status: newStatus }).eq('id', taskId);
            if(error) throw error;
            loadTasks();
        } catch(err) {
            alert('Lỗi cập nhật: ' + err.message);
        }
    };

    // Filters UI
    const filterIds = ['all', 'mine', 'progress', 'done', 'overdue'];
    filterIds.forEach(id => {
        const btn = document.getElementById(`filter-${id}`);
        if(btn) {
            btn.addEventListener('click', () => {
                // reset styling
                filterIds.forEach(fid => {
                    const b = document.getElementById(`filter-${fid}`);
                    if(b) {
                        b.className = "px-md py-sm text-on-surface-variant font-label-md text-label-md hover:bg-surface-container transition-colors rounded-lg";
                    }
                });
                // active styling
                btn.className = "px-md py-sm bg-primary-fixed-dim text-primary font-label-md text-label-md rounded-lg";
                currentFilter = id;
                loadTasks();
            });
        }
    });

    // Add Task
    formAdd.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btnSubmit = document.getElementById('btn-submit-modal');
        btnSubmit.disabled = true;
        btnSubmit.innerText = 'Đang lưu...';

        try {
            const newTask = {
                title: document.getElementById('task-title').value,
                lead_id: document.getElementById('task-lead').value,
                due_date: document.getElementById('task-due-date').value,
                priority: document.getElementById('task-priority').value,
                assigned_to: user.id,
                created_by: user.id,
                status: 'chua_lam'
            };

            const { error } = await supabase.from('tasks').insert([newTask]);
            if (error) throw error;
            
            closeModal();
            loadTasks();
        } catch (err) {
            alert('Lỗi tạo công việc: ' + err.message);
        } finally {
            btnSubmit.disabled = false;
            btnSubmit.innerText = 'Lưu công việc';
        }
    });

    loadTasks();
});
"""
    raw_html = raw_html[:start_idx] + new_script + raw_html[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(raw_html)

print("Tasks module updated successfully.")
