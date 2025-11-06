
document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.app-sidebar');
    const mainContent = document.querySelector('.main-content');

    if (!menuToggle || !sidebar || !mainContent) {
        console.error('必要な要素が見つかりませんでした。');
        return;
    }

    menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('is-open');
        mainContent.classList.toggle('sidebar-open');
    });

    document.addEventListener('click', function(event) {
        const isClickInsideSidebar = sidebar.contains(event.target);
        const isClickOnToggle = menuToggle.contains(event.target);

        if (sidebar.classList.contains('is-open') && !isClickInsideSidebar && !isClickOnToggle) {
            
            sidebar.classList.remove('is-open');
            mainContent.classList.remove('sidebar-open');
        }
    });

});