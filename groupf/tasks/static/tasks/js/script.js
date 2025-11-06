// groupf/tasks/static/tasks/js/script.js

document.addEventListener("DOMContentLoaded", function() {

    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.app-sidebar');
    const mainContent = document.querySelector('.main-content');
    
    // 要素が見つかった場合のみイベントリスナーを設定
    if (menuToggle && sidebar && mainContent) {
        menuToggle.addEventListener('click', () => {
            // サイドバーとメインコンテンツにクラスを付け外しして表示を切り替える
            sidebar.classList.toggle('is-open');
            mainContent.classList.toggle('sidebar-open');
        });
    }

});