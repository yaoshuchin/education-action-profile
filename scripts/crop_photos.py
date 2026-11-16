"""將履歷 PDF 轉出的版面圖裁切成可獨立使用的照片素材。

座標以 images/page-*.jpg 的 910 x 1287 版本為基準，之後若重新輸出 PDF，
只要更新這份裁切清單即可重建 images/photos/。
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "images"
HIGH_RES_SOURCE = SOURCE / "source-hi"
OUTPUT = SOURCE / "photos"

# (來源頁碼, 檔名, left, top, right, bottom, 分類, 標題)
CROPS = [
    (19, "sport-01", 36, 175, 292, 430, "sport", "第一次勇奪全國冠軍"),
    (19, "sport-02", 295, 173, 570, 350, "sport", "冠軍隊伍的高峰時刻"),
    (19, "sport-03", 584, 158, 866, 424, "sport", "學生獻獎與冠軍獎盃"),
    (19, "sport-04", 42, 445, 458, 720, "sport", "超刻苦的訓練"),
    (19, "sport-05", 464, 438, 870, 735, "sport", "第六次國內冠軍"),
    (20, "international-01", 68, 135, 465, 436, "international", "國家隊訓練現場"),
    (20, "international-02", 493, 130, 866, 450, "international", "主席特頒最佳國際獎"),
    (20, "international-03", 57, 450, 524, 805, "international", "美國 16 歲組冠軍"),
    (20, "international-04", 48, 820, 554, 1112, "international", "與加拿大隊賽後合照"),
    (20, "international-05", 585, 458, 864, 654, "international", "迪士尼與米老鼠"),
    (21, "australia-01", 39, 120, 449, 441, "international", "澳洲國際錦標賽開幕"),
    (21, "australia-02", 459, 125, 864, 444, "international", "雪梨大橋與團隊"),
    (21, "australia-03", 46, 465, 486, 763, "international", "澳洲 C 組冠軍"),
    (21, "australia-04", 496, 466, 853, 762, "international", "參訪雪梨歌劇院"),
    (25, "care-01", 43, 138, 450, 365, "care", "為植物人募款募發票"),
    (25, "care-02", 451, 138, 868, 377, "care", "品格教育課堂"),
    (25, "care-03", 308, 315, 598, 548, "care", "學生志工團隊"),
    (25, "care-04", 303, 675, 594, 1010, "care", "為獨居老人送棉被"),
    (28, "filial-01", 42, 142, 315, 390, "care", "孝道文化活動"),
    (28, "filial-02", 316, 142, 637, 390, "care", "感恩與品格教育"),
    (28, "filial-03", 646, 136, 867, 400, "care", "親師生共同參與"),
    (54, "eco-01", 48, 143, 447, 417, "school", "生態校園夥伴計畫"),
    (54, "eco-02", 451, 143, 864, 417, "school", "環境教育現場"),
    (54, "eco-03", 50, 425, 450, 680, "school", "全國決賽成果"),
]


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for page, name, left, top, right, bottom, _category, _title in CROPS:
        # Prefer 220 DPI exports for sharper website images; fall back to the
        # earlier 110 DPI previews when a source page is not available.
        source = HIGH_RES_SOURCE / f"page-{page}.jpg"
        scale = 2 if source.exists() else 1
        if not source.exists():
            source = SOURCE / f"page-{page}.jpg"
        with Image.open(source) as image:
            box = (left * scale, top * scale, right * scale, bottom * scale)
            image.crop(box).save(OUTPUT / f"{name}.jpg", quality=94, optimize=True)
    print(f"created {len(CROPS)} individual photos in {OUTPUT}")


if __name__ == "__main__":
    main()
