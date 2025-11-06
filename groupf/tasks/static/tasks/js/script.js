// groupf/tasks/static/tasks/js/script.js (オーバーレイ方式の最終版)

document.addEventListener("DOMContentLoaded", function() {

    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.app-sidebar');
    const overlay = document.querySelector('#page-overlay'); // ★★★ オーバーレイ要素を取得

    if (!menuToggle || !sidebar || !overlay) {
        console.error('必要な要素が見つかりませんでした。');
        return;
    }

    // --- サイドバーを開く関数 ---
    function openSidebar() {
        sidebar.classList.add('is-open');
        overlay.classList.add('is-active'); // オーバーレイを表示
        document.body.classList.add('body-noscroll'); // 背景のスクロールを禁止
    }

    // --- サイドバーを閉じる関数 ---
    function closeSidebar() {
        sidebar.classList.remove('is-open');
        overlay.classList.remove('is-active'); // オーバーレイを非表示
        document.body.classList.remove('body-noscroll'); // 背景のスクロールを許可
    }

    // ハンバーガーメニューをクリックしたら開閉
    menuToggle.addEventListener('click', (event) => {
        event.stopPropagation(); // クリックイベントが親要素に伝播するのを防ぐ
        if (sidebar.classList.contains('is-open')) {
            closeSidebar();
        } else {
            openSidebar();
        }
    });

    // ★★★ オーバーレイをクリックしたら閉じる ★★★
    // これが「メニュー以外のところを押したら閉じる」機能になります
    overlay.addEventListener('click', () => {
        closeSidebar();
    });

});