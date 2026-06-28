import os
from bs4 import BeautifulSoup

file_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend/pipeline.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Add SortableJS
if not soup.find(src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"):
    script_tag = soup.new_tag("script", src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js")
    soup.head.append(script_tag)

# 2. Add ID to Total Pipeline Value
total_val_p = soup.find(lambda tag: tag.name == "p" and "4.500.000.000 VND" in tag.text)
if total_val_p:
    total_val_p['id'] = 'total-pipeline-value'

# 3. Empty the kanban board container and give it an ID
kanban_container = soup.find("div", class_=lambda x: x and "kanban-scroll" in x)
if kanban_container:
    kanban_container['id'] = 'kanban-board'
    kanban_container.clear()

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

# 4. Replace Script block via string manipulation
with open(file_path, "r", encoding="utf-8") as f:
    raw_html = f.read()

start_idx = raw_html.find("<script>\n        // Simple micro-interaction for cards")
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

    // --- KANBAN LOGIC ---
    const board = document.getElementById('kanban-board');
    const totalPipelineValueEl = document.getElementById('total-pipeline-value');
    
    // Format tiền
    const formatCurrency = (val) => new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(val || 0);

    // Get Initials
    const getInitials = (name) => {
        if(!name) return '??';
        const parts = name.trim().split(' ');
        if(parts.length >= 2) return (parts[0][0] + parts[parts.length-1][0]).toUpperCase();
        return name.substring(0,2).toUpperCase();
    };
    
    // Determine Priority color based on value
    const getPriorityHtml = (value) => {
        if (value >= 500000000) {
            return `<span class="bg-error-container text-on-error-container text-[10px] font-bold px-2 py-0.5 rounded uppercase">Cao</span>`;
        } else if (value >= 100000000) {
            return `<span class="bg-secondary-container text-on-secondary-container text-[10px] font-bold px-2 py-0.5 rounded uppercase">Trung bình</span>`;
        }
        return `<span class="bg-primary-fixed text-on-primary-fixed text-[10px] font-bold px-2 py-0.5 rounded uppercase">Thấp</span>`;
    };

    const loadBoard = async () => {
        try {
            board.innerHTML = '<div class="w-full text-center py-10 text-outline">Đang tải bảng Kanban...</div>';
            
            // 1. Fetch Stages
            const { data: stages, error: stageErr } = await supabase.from('pipeline_stages').select('*').order('order', { ascending: true });
            if(stageErr) throw stageErr;
            
            // 2. Fetch Leads
            const { data: leads, error: leadErr } = await supabase.from('leads').select('*, profiles!leads_assigned_to_fkey(full_name)').eq('is_deleted', false);
            if(leadErr) throw leadErr;
            
            board.innerHTML = '';
            let totalPipelineValue = 0;
            
            // Render columns
            stages.forEach(stage => {
                // Determine leads for this stage
                let stageLeads = leads.filter(l => l.stage_id === stage.id);
                // If it's the first stage, also include leads with no stage_id
                if (stage.order === 1) {
                    stageLeads = stageLeads.concat(leads.filter(l => !l.stage_id));
                }
                
                const stageValue = stageLeads.reduce((sum, l) => sum + Number(l.expected_value || 0), 0);
                totalPipelineValue += stageValue;
                
                const colHTML = `
                <div class="flex-shrink-0 w-80">
                    <div class="flex justify-between items-center mb-md px-sm">
                        <h3 class="font-headline-sm text-headline-sm text-on-surface flex items-center gap-sm">
                            ${stage.name}
                            <span class="bg-surface-container-highest text-on-surface-variant text-[11px] px-2 py-0.5 rounded-full" id="count-${stage.id}">${stageLeads.length}</span>
                        </h3>
                        <p class="font-label-md text-secondary" id="value-${stage.id}">${formatCurrency(stageValue)}</p>
                    </div>
                    <div class="space-y-md min-h-[500px] p-sm rounded-xl border-2 border-dashed border-outline-variant/30 kanban-column-body bg-surface-container-lowest" data-stage-id="${stage.id}">
                        ${stageLeads.map(lead => `
                        <!-- Card -->
                        <div class="bg-white border border-outline-variant p-md rounded-[6px] hover:shadow-md transition-shadow cursor-pointer kanban-card" data-lead-id="${lead.id}" data-value="${lead.expected_value || 0}">
                            <div class="flex justify-between items-start mb-sm">
                                <h4 class="font-headline-sm text-on-primary-container font-semibold">${lead.name}</h4>
                                ${getPriorityHtml(lead.expected_value)}
                            </div>
                            <p class="text-headline-sm font-bold text-primary-container mb-md">${formatCurrency(lead.expected_value)}</p>
                            <div class="flex items-center justify-between mt-auto">
                                <div class="flex items-center gap-sm">
                                    <div class="w-6 h-6 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-[10px]">${getInitials(lead.profiles?.full_name)}</div>
                                    <span class="text-body-sm text-on-surface-variant">${lead.profiles?.full_name || 'Chưa giao'}</span>
                                </div>
                                <span class="material-symbols-outlined text-outline text-lg">more_horiz</span>
                            </div>
                        </div>
                        `).join('')}
                    </div>
                </div>
                `;
                board.insertAdjacentHTML('beforeend', colHTML);
            });
            
            if (totalPipelineValueEl) totalPipelineValueEl.innerText = formatCurrency(totalPipelineValue);
            
            // 3. Initialize SortableJS
            document.querySelectorAll('.kanban-column-body').forEach(container => {
                new Sortable(container, {
                    group: 'pipeline',
                    animation: 150,
                    ghostClass: 'opacity-50',
                    onEnd: async function (evt) {
                        const itemEl = evt.item;  // dragged HTMLElement
                        const toContainer = evt.to;    // target list
                        const fromContainer = evt.from;
                        
                        if(toContainer === fromContainer) return;
                        
                        const leadId = itemEl.getAttribute('data-lead-id');
                        const newStageId = toContainer.getAttribute('data-stage-id');
                        
                        // Optimistic UI updates could go here (updating the count/values of headers)
                        recalculateColumns();
                        
                        // Update DB
                        try {
                            const { error } = await supabase.from('leads').update({ stage_id: newStageId }).eq('id', leadId);
                            if(error) throw error;
                        } catch(err) {
                            console.error('Update stage failed:', err);
                            alert('Lỗi khi chuyển trạng thái: ' + err.message);
                            // Fallback reload if fail
                            loadBoard();
                        }
                    },
                });
            });
            
        } catch(err) {
            console.error(err);
            board.innerHTML = '<div class="w-full text-center py-10 text-error">Lỗi tải dữ liệu Kanban.</div>';
        }
    };
    
    // Function to recalculate headers locally after a drop
    const recalculateColumns = () => {
        let totalVal = 0;
        document.querySelectorAll('.kanban-column-body').forEach(col => {
            const stageId = col.getAttribute('data-stage-id');
            const cards = col.querySelectorAll('.kanban-card');
            
            let colValue = 0;
            cards.forEach(card => {
                colValue += parseFloat(card.getAttribute('data-value')) || 0;
            });
            totalVal += colValue;
            
            const countEl = document.getElementById(`count-${stageId}`);
            const valEl = document.getElementById(`value-${stageId}`);
            if(countEl) countEl.innerText = cards.length;
            if(valEl) valEl.innerText = formatCurrency(colValue);
        });
        
        if(totalPipelineValueEl) totalPipelineValueEl.innerText = formatCurrency(totalVal);
    };

    loadBoard();
});
"""
    raw_html = raw_html[:start_idx] + new_script + raw_html[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(raw_html)

print("Pipeline module updated successfully.")
