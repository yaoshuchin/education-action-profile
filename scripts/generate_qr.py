"""Generate local QR assets for the share page."""
from pathlib import Path
import qrcode

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "images"

QR_TARGETS = {
    "qr-primary.png": "https://is.gd/5AKOTT",
    "qr-backup.png": "https://yaoshuchin.github.io/education-action-profile/",
}

for filename, url in QR_TARGETS.items():
    qr = qrcode.QRCode(version=None, box_size=12, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="#152d3b", back_color="white").save(OUTPUT / filename)
    print(f"created {filename} -> {url}")
