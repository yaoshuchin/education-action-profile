# 董勳遠｜教育行動者個人誌

由兩份 PDF 資料整理而成的個人化靜態網站，將完整履歷轉譯為可閱讀、可分享的教育故事，並以代表性現場影像呈現教育行動。

## 專案結構

```text
.
├── index.html
├── photos.html          # 新版獨立照片牆
├── css/style.css
├── css/photos.css
├── js/app.js
├── js/photos.js
├── scripts/crop_photos.py
├── images/              # 由履歷 PDF 轉出的公開版代表頁面
└── README.md
```

## 本機預覽

直接用瀏覽器開啟 `index.html` 即可；若要使用較完整的本機伺服器，可在專案資料夾執行：

```bash
python -m http.server 8000
```

再開啟 <http://localhost:8000>。

## 內容與隱私

網站內容整理自「116 年校長甄試公務人員履歷表」與「115 年度大（非）臺中好人好事代表暨全國社會教育奉獻楷模選拔－得獎者名單」。公開版刻意不放入身分證號、住址、電話、電子郵件與家屬資料；部署前請再次確認影像與文字符合公開授權及當事人同意範圍。

## 後續維護

- 修改文字：直接編輯 `index.html`。
- 照片牆：開啟 `photos.html`，以分類按鈕瀏覽拆解後的單張照片。
- 修改視覺：集中調整 `css/style.css` 最上方的色彩與字體變數。
- 增加影像：放入 `images/`，再於 `index.html` 的 `.gallery-grid` 增加項目與分類標籤。
- 重新拆解照片：調整 `scripts/crop_photos.py` 的裁切座標後執行 `python scripts/crop_photos.py`。
- 部署：可直接使用 GitHub Pages、Netlify 或 Cloudflare Pages，這是一個不需要建置流程的靜態網站。
