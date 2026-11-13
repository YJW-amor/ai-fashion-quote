# -*- coding: utf-8 -*-
"""生成初始视图为制作页的临时验证副本（仅用于布局截图验证，非交付产物）。"""
from pathlib import Path

base = Path(r"C:\Users\Administrator\DoubaoWork\chats\2026-11-05\new-chat-2\ai-fashion-quote")
src = base / "AI模特图小程序原型.html"
out = base / "_shots" / "check-make.html"

t = src.read_text(encoding="utf-8")
t = t.replace('class="view on" id="v-home"', 'class="view" id="v-home"')
t = t.replace('class="view" id="v-make"', 'class="view on" id="v-make"')
t = t.replace('showView("home");', 'showView("make");')
out.write_text(t, encoding="utf-8")
print("written", len(t))
