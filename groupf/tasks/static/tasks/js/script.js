// groupf/tasks/static/tasks/js/script.js (プッシュ型レイアウト版)

document.addEventListener("DOMContentLoaded", function() {

    // ★★★ ヘッダーとメインコンテンツの要素を取得する処理を復活させます ★★★
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.app-sidebar');
    const header = document.querySelector('.app-header');
    const mainContent = document.querySelector('.main-content');
    
    if (!menuToggle || !sidebar || !header || !mainContent) {
        console.error('レイアウト用の要素が見つかりませんでした。');
        return;
    }

    // --- サイドバーを開閉する関数 ---
    function toggleSidebar() {
        sidebar.classList.toggle('is-open');
        
        // ★★★ ヘッダーとメインコンテンツにもクラスを付け外しします ★★★
        header.classList.toggle('sidebar-is-open');
        mainContent.classList.toggle('sidebar-is-open');

        // 背景のスクロール制御
        document.body.classList.toggle('body-noscroll');
    }

    // ハンバーガーメニューをクリックしたら開閉
    menuToggle.addEventListener('click', (event) => {
        event.stopPropagation();
        toggleSidebar();
    });

    // --- メニュー以外の場所をクリックした時に閉じる動作 ---
    document.addEventListener('click', function(event) {
        const isClickInsideSidebar = sidebar.contains(event.target);
        const isClickOnToggle = menuToggle.contains(event.target);

        if (sidebar.classList.contains('is-open') && !isClickInsideSidebar && !isClickOnToggle) {
            toggleSidebar();
        }
    });

});