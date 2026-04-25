from PIL import Image
from pathlib import Path

SRC = Path("images")
MAX_WIDTH = 1600
QUALITY = 80

total_before = 0
total_after = 0

for img_path in sorted(SRC.glob("*.jpg")):
    before = img_path.stat().st_size
    total_before += before

    with Image.open(img_path) as im:
        im = im.convert("RGB")
        if im.width > MAX_WIDTH:
            ratio = MAX_WIDTH / im.width
            new_size = (MAX_WIDTH, int(im.height * ratio))
            im = im.resize(new_size, Image.LANCZOS)
        im.save(img_path, "JPEG", quality=QUALITY, optimize=True, progressive=True)

    after = img_path.stat().st_size
    total_after += after
    print(f"{img_path.name}: {before/1024:.0f}KB -> {after/1024:.0f}KB ({after/before*100:.0f}%)")

print(f"\nTOTAL: {total_before/1024/1024:.1f}MB -> {total_after/1024/1024:.1f}MB ({total_after/total_before*100:.0f}%)")
