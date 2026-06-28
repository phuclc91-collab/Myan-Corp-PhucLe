
const _supabaseUrl = 'https://wooyxavsxyqiutpxqatp.supabase.co';
const _supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indvb3l4YXZzeHlxaXV0cHhxYXRwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI1OTMwMDcsImV4cCI6MjA5ODE2OTAwN30.3ATEaYxPVMKN8ZR_iCwvL-980mE8uaF2CH59W1kvqUU';
window.supabase = window.supabase.createClient(_supabaseUrl, _supabaseKey);


// Global Auth Guard & Profile Fetcher
document.addEventListener('DOMContentLoaded', async () => {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const isPublicPage = currentPage === 'index.html' || currentPage === 'reset-password.html';

    const { data: { session }, error: sessionError } = await supabase.auth.getSession();
    
    // Auth Guard
    if (!isPublicPage && !session) {
        window.location.href = 'index.html';
        return;
    }

    if (session) {
        // Render Profile
        const nameEl = document.getElementById('header-user-name');
        const roleEl = document.getElementById('header-user-role');
        const avatarEl = document.getElementById('header-user-avatar');
        
        if (nameEl || roleEl) {
            const { data: profile } = await supabase.from('profiles').select('full_name, role').eq('id', session.user.id).single();
            if (profile) {
                if (nameEl) nameEl.innerText = profile.full_name || 'Người dùng';
                if (roleEl) {
                    const roleMap = { 'admin': 'Quản trị viên', 'manager': 'Trưởng nhóm', 'sales': 'NV Kinh doanh' };
                    roleEl.innerText = roleMap[profile.role] || profile.role;
                }
                if (avatarEl) {
                    // Create Initials
                    const name = profile.full_name || 'U';
                    const parts = name.trim().split(' ');
                    const initials = parts.length >= 2 ? (parts[0][0] + parts[parts.length-1][0]).toUpperCase() : name.substring(0,2).toUpperCase();
                    
                    // Replace img with div
                    const newAvatar = document.createElement('div');
                    newAvatar.className = 'w-10 h-10 rounded-full bg-primary flex items-center justify-center text-white font-bold text-label-md border-2 border-primary-fixed';
                    newAvatar.innerText = initials;
                    avatarEl.parentNode.replaceChild(newAvatar, avatarEl);
                }
            }
        }
        
        // Logout Event
        const btnLogout = document.getElementById('btn-logout');
        if (btnLogout) {
            btnLogout.addEventListener('click', async () => {
                await supabase.auth.signOut();
                window.location.href = 'index.html';
            });
        }
    }
});
