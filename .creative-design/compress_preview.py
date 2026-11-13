import os
from PIL import Image

src_dir = r"C:\Users\Administrator\Desktop\我的知识库"
out_dir = r"C:\Users\Administrator\DoubaoWork\chats\2026-11-05\new-chat-2\ai-fashion-quote\assets\_preview"
os.makedirs(out_dir, exist_ok=True)

files = [
    "微信图片_20261105190511_4_65.jpg",
    "微信图片_20261105190531_5_65.jpg",
    "微信图片_20261105190549_6_65.jpg",
    "微信图片_20261105190552_7_65.jpg",
    "微信图片_20261105190555_8_65.jpg",
    "微信图片_20261105190557_9_65.jpg",
]

for f in files:
    p = os.path.join(src_dir, f)
    try:
        im = Image.open(p)
        w, h = im.size
        if w > 900:
            nh = int(h * 900 / w)
            im = im.resize((900, nh), Image.LANCZOS)
        out = os.path.join(out_dir, f)
        im.convert("RGB").save(out, "JPEG", quality=82)
        print(f, im.size, os.path.getsize(out))
    except Exception as e:
        print(f, "ERROR", e)
