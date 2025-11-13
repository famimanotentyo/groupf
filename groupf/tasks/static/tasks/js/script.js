document.addEventListener("DOMContentLoaded", function() {
    // 固定サイドバーレイアウトのため、開閉用のスクリプトは不要になります。
});

document.addEventListener('DOMContentLoaded', function () {
    // すべての「・・・」ボタンに対してイベントリスナーを設定
    document.querySelectorAll('.action-btn').forEach(button => {
        button.addEventListener('click', function (event) {
            // 親要素の a タグへのクリックイベント伝播を止め、ページ遷移を防ぐ
            event.preventDefault();
            event.stopPropagation();

            // クリックされたボタンの隣にあるメニュー要素を取得
            const menu = this.nextElementSibling;
            
            // 現在表示されている他のメニューをすべて閉じる
            // これにより、複数のメニューが同時に開くのを防ぐ
            document.querySelectorAll('.action-menu.show').forEach(openMenu => {
                if (openMenu !== menu) {
                    openMenu.classList.remove('show');
                }
            });

            // クリックされたボタンに対応するメニューの表示/非表示を切り替える
            menu.classList.toggle('show');
        });
    });

    // ページ上のどこかをクリックしたときに、開いているメニューを閉じる
    document.addEventListener('click', function (event) {
        // クリックされた要素がアクションメニューの領域内でなければ
        if (!event.target.closest('.col-actions')) {
            // 表示されているすべてのメニューを閉じる
            document.querySelectorAll('.action-menu.show').forEach(openMenu => {
                openMenu.classList.remove('show');
            });
        }
    });
});