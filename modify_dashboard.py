import os
from bs4 import BeautifulSoup

file_path = "/Users/ryanle/Desktop/Ryan Le /AI/Agentic AI/Day-3/Homework-CRM-Thay_Hung/Myan_CRM_Prototype/crm-frontend/dashboard.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Add IDs to Metrics
h2s = soup.find_all("h2", class_=lambda x: x and "font-headline-lg" in x)
if len(h2s) >= 4:
    h2s[0]['id'] = 'metric-revenue'
    h2s[1]['id'] = 'metric-expected'
    h2s[2]['id'] = 'metric-new-customers'
    h2s[3]['id'] = 'metric-conversion'

# 2. Add ID to Funnel
funnel_h3 = soup.find(lambda tag: tag.name == "h3" and "Phễu bán hàng" in tag.text)
if funnel_h3:
    funnel_container = funnel_h3.find_next_sibling("div")
    if funnel_container:
        funnel_container['id'] = 'funnel-container'
        funnel_container.clear()

# 3. Add ID to Mini Table
table_h3 = soup.find(lambda tag: tag.name == "h3" and "Đợt thanh toán sắp đến hạn" in tag.text)
if table_h3:
    section = table_h3.find_parent("section")
    tbody = section.find("tbody")
    if tbody:
        tbody['id'] = 'mini-payment-table'
        tbody.clear()

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

# 4. Replace Script block via string manipulation
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

    const formatCurrency = (val) => new Intl.NumberFormat('vi-VN').format(val || 0);

    const loadDashboard = async () => {
        try {
            // Fetch necessary data
            const [
                { data: subscriptions },
                { data: leads },
                { data: stages }
            ] = await Promise.all([
                supabase.from('subscriptions').select('*'),
                supabase.from('leads').select('*').eq('is_deleted', false),
                supabase.from('pipeline_stages').select('*').order('order', {ascending: true})
            ]);

            // 1. Metric: Doanh thu thực tế (Completed subscriptions)
            const actualRevenue = (subscriptions || []).filter(s => s.status === 'completed').reduce((sum, s) => sum + parseFloat(s.amount || 0), 0);
            const mRev = document.getElementById('metric-revenue');
            if(mRev) mRev.innerHTML = `${formatCurrency(actualRevenue)} <span class="text-body-md font-medium">VND</span>`;

            // 2. Metric: Doanh thu dự kiến
            let expectedRevenue = 0;
            const stageMap = {};
            if (stages) {
                stages.forEach(st => stageMap[st.id] = st);
            }
            if (leads) {
                leads.forEach(l => {
                    if (l.stage_id && stageMap[l.stage_id]) {
                        const prob = stageMap[l.stage_id].probability || 0;
                        const val = parseFloat(l.expected_value || 0);
                        expectedRevenue += val * (prob / 100);
                    }
                });
            }
            const mExp = document.getElementById('metric-expected');
            if(mExp) mExp.innerHTML = `${formatCurrency(expectedRevenue)} <span class="text-body-md font-medium">VND</span>`;

            // 3. Metric: Khách hàng mới
            const totalLeads = leads ? leads.length : 0;
            const mNew = document.getElementById('metric-new-customers');
            if(mNew) mNew.innerHTML = `+${totalLeads}`;

            // 4. Metric: Tỷ lệ chuyển đổi
            // Assume the last stage in stages is the success stage
            let conversionRate = 0;
            if (stages && stages.length > 0 && totalLeads > 0) {
                const lastStage = stages[stages.length - 1];
                const successCount = leads.filter(l => l.stage_id === lastStage.id).length;
                conversionRate = (successCount / totalLeads) * 100;
            }
            const mConv = document.getElementById('metric-conversion');
            if(mConv) mConv.innerHTML = `${conversionRate.toFixed(1)}%`;

            // 5. Funnel Chart
            const funnelContainer = document.getElementById('funnel-container');
            if (funnelContainer && stages) {
                let html = '';
                // Count leads per stage
                const stageCounts = stages.map(st => {
                    return {
                        ...st,
                        count: leads.filter(l => l.stage_id === st.id).length
                    };
                });
                
                // For a funnel, max width is 100% (or the max count)
                const maxCount = Math.max(...stageCounts.map(s => s.count), 1); // prevent division by zero

                const colors = [
                    'bg-primary',
                    'bg-primary/85',
                    'bg-primary/70',
                    'bg-primary/55',
                    'bg-tertiary-container'
                ];

                stageCounts.forEach((st, idx) => {
                    const widthPct = (st.count / maxCount) * 100;
                    // minimum width to show text
                    const displayWidth = Math.max(widthPct, 20); 
                    const margin = (100 - displayWidth) / 2;
                    const color = colors[Math.min(idx, colors.length - 1)];

                    html += `
                    <div class="flex items-center gap-md">
                        <div style="margin-left: ${margin}%; width: ${displayWidth}%;" class="${color} h-10 rounded-lg flex items-center justify-between px-md text-white font-bold text-body-sm transition-all duration-500">
                            <span class="truncate pr-2">${st.name}</span>
                            <span>${st.count}</span>
                        </div>
                        <span class="w-12 text-label-sm text-on-surface-variant">${widthPct.toFixed(0)}%</span>
                    </div>
                    `;
                });
                funnelContainer.innerHTML = html;
            }

            // 6. Mini Table
            const tbody = document.getElementById('mini-payment-table');
            if (tbody) {
                // get 5 latest pending/overdue payments
                const { data: upcoming, error: upErr } = await supabase
                    .from('subscriptions')
                    .select('*, leads(name)')
                    .in('status', ['active', 'past_due'])
                    .order('start_date', { ascending: true })
                    .limit(5);
                
                if (upcoming && upcoming.length > 0) {
                    tbody.innerHTML = upcoming.map(p => {
                        const isOverdue = p.status === 'past_due';
                        const badgeClass = isOverdue ? 'bg-[#FEE2E2] text-[#EF4444]' : 'bg-[#FEF3C7] text-[#D97706]';
                        const dotClass = isOverdue ? 'bg-[#EF4444]' : 'bg-[#F59E0B]';
                        const statusText = isOverdue ? 'Quá hạn' : 'Đang chờ';
                        
                        return `
                        <tr class="hover:bg-surface-container-lowest transition-colors group">
                            <td class="px-lg py-md">
                                <div class="flex items-center gap-md">
                                    <div class="w-8 h-8 rounded bg-secondary-fixed/50 flex items-center justify-center font-bold text-secondary text-xs">KH</div>
                                    <div>
                                        <p class="text-body-md font-bold text-on-background">${p.leads?.name || 'Vô danh'}</p>
                                        <p class="text-[11px] text-on-surface-variant">${p.plan_name}</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-lg py-md text-body-md font-bold text-on-background">${formatCurrency(p.amount)} VND</td>
                            <td class="px-lg py-md text-body-md text-on-surface-variant">${new Date(p.start_date).toLocaleDateString('vi-VN')}</td>
                            <td class="px-lg py-md">
                                <span class="inline-flex items-center px-sm py-1 rounded-full ${badgeClass} text-[11px] font-bold">
                                    <span class="w-1.5 h-1.5 rounded-full ${dotClass} mr-1.5"></span>
                                    ${statusText}
                                </span>
                            </td>
                            <td class="px-lg py-md text-right">
                                <button class="p-xs hover:bg-surface-container rounded transition-colors text-on-surface-variant">
                                    <span class="material-symbols-outlined">more_horiz</span>
                                </button>
                            </td>
                        </tr>
                        `;
                    }).join('');
                } else {
                    tbody.innerHTML = '<tr><td colspan="5" class="text-center py-5 text-outline">Không có khoản thu sắp tới.</td></tr>';
                }
            }
        } catch(err) {
            console.error('Error loading dashboard:', err);
        }
    };

    loadDashboard();
});
"""
    raw_html = raw_html[:start_idx] + new_script + raw_html[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(raw_html)

print("Dashboard module updated successfully.")
