# 董勳遠｜教育行動者個人誌

由兩份 PDF 資料整理而成的個人化靜態網站，將完整履歷轉譯為可閱讀、可分享的教育故事，並以代表性現場影像呈現教育行動。

## 專案結構

```text
.
├── index.html
├── record.html          # 68 頁資料整理後的完整教育履歷檔案
├── photos.html          # 新版獨立照片牆
├── share.html           # 短網址與主要／備用 QR Code
├── css/style.css
├── css/photos.css
├── css/share.css
├── js/app.js
├── js/photos.js
├── js/share.js
├── scripts/crop_photos.py
├── scripts/generate_qr.py
├── images/              # 公開版代表頁面與裁切後的教育現場照片
│   └── photos/           # sport / international / care / school / profile
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
- 完整內容：開啟 `record.html`，可查閱學歷、資格、行政歷練、研習、教育行動、獎項與治校承諾。
- 個人網站首頁已改為重新整理後的個人品牌結構，不直接呈現原始 PDF 頁面。
- 閱讀設定：首頁右上方可切換文字「中／大／特大」與「淺／深／綠／藍」背景，選擇會保存在瀏覽器。
- 照片牆：開啟 `photos.html`，以分類按鈕瀏覽拆解後的單張照片。
- 分享頁：開啟 `share.html`，取得短網址 `https://is.gd/5AKOTT`、主要 QR 與 GitHub Pages 備用 QR。
- 修改視覺：集中調整 `css/style.css` 最上方的色彩與字體變數。
- 增加影像：放入 `images/`，再於 `index.html` 的 `.gallery-grid` 增加項目與分類標籤。
- 重新拆解照片：調整 `scripts/crop_photos.py` 的裁切座標後執行 `python scripts/crop_photos.py`。
- 個人照片：`images/photos/profile-*.jpg` 是從高解析度頁面獨立裁切的董勳遠人物／團隊照片；首頁、完整檔案、照片牆與分享頁均以圖說對應教育脈絡。
- 影像原則：網站使用獨立裁切照片，不直接公開 PDF 頁面；若替換照片，請同步更新 `alt` 文字與圖說，並確認公開授權。
- 重新產生 QR：調整 `scripts/generate_qr.py` 的網址後執行 `python scripts/generate_qr.py`。
- 部署：可直接使用 GitHub Pages、Netlify 或 Cloudflare Pages，這是一個不需要建置流程的靜態網站。
