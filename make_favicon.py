from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO

# === Иконки в виде встроенных PNG (📚 и 🛠️) ===
# (Эти данные уже содержат base64-кодированные PNG, можно без интернета)
BOOK_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAADwAAAA8CAYAAAA6/NlyAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA"
    "B3RJTUUH5AEXDioCwE5mEAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAB10RVh0Q29tbWVudABDcmVh"
    "dGVkIHdpdGggR0lNUFeBDhcAAAECSURBVGje7ZoxDsIwDEV7EJb/0zFJHZswRslmjBBDxkZ6qYIB"
    "QlyT4s5cTxsOB1t6RZ+H7HOr2BplxkifA4DoFgK9BRWEMIfTjQoDHzgE9NxE+Pkm4Z1HqI8fElqG9"
    "Uq0pwEhqWQZyBhIpkNgDikJhrLqQQakVAE1okxQgFiSLoCUCe6ZUNn+snRrZFFogDptz5M7TyaGyc"
    "X6+XaeE/3b/NRxZHZVrQ8/8AAAAASUVORK5CYII="
)

TOOLS_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAADwAAAA8CAYAAAA6/NlyAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA"
    "B3RJTUUH5AEXDjMgI8s8PwAAAB10RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAFU"
    "SURBVGje7ZpLDoIwEEX/jD3//+RO0yBGpdx3IBvOwxUyiMGZkcZJ5Xly9sdOVocM2ygxfgqDAELIJ"
    "dJgHApqYZED4gCLuAURpTgk0xjAK7JPSGkQvI1PcBwMPa7kb0I9TCfKkQQrGqAA+k6b5U0jszkT6b"
    "tDco2sx5Aq1AjzXYyGyiojl01nV2dc3xQIJAjUqXwK4/koBr9i5QFyg4P2j6u6r3yQx3SJEUsJVKo"
    "xUURJpIfwh0IUcbYALfzwgpdTZZEvPV0kH0MLY3ZONxJrEifd18zyhhqEWLC0cF0IEZpV8q7pHynS"
    "D/ibynPDzOeNPfEX8COw2vwAZVGnIAAAAASUVORK5CYII="
)

# === Настройки иконки ===
size = (256, 256)
img = Image.new("RGBA", size, (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# --- Градиент ---
top_color = (30, 90, 255, 255)
bottom_color = (0, 40, 160, 255)
for y in range(size[1]):
    r = int(top_color[0] + (bottom_color[0] - top_color[0]) * (y / size[1]))
    g = int(top_color[1] + (bottom_color[1] - top_color[1]) * (y / size[1]))
    b = int(top_color[2] + (bottom_color[2] - top_color[2]) * (y / size[1]))
    draw.line([(0, y), (size[0], y)], fill=(r, g, b, 255))

# --- Скруглённые углы ---
corner_radius = 40
mask = Image.new("L", size, 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rounded_rectangle([0, 0, size[0], size[1]], corner_radius, fill=255)
img.putalpha(mask)

# --- Тень ---
shadow = Image.new("RGBA", (size[0] + 10, size[1] + 10), (0, 0, 0, 0))
shadow_draw = ImageDraw.Draw(shadow)
shadow_draw.rounded_rectangle([5, 5, size[0] + 5, size[1] + 5], corner_radius, fill=(0, 0, 0, 80))
shadow.alpha_composite(img, dest=(0, 0))
img = shadow

# --- Текст ---
font_main = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
draw = ImageDraw.Draw(img)
text_main = "TC"
text_w, text_h = draw.textbbox((0, 0), text_main, font=font_main)[2:]
main_position = ((img.width - text_w) // 2, (img.height - text_h) // 2 - 40)

# Тень и основной текст
draw.text((main_position[0] + 3, main_position[1] + 3), text_main, font=font_main, fill=(0, 0, 0, 100))
draw.text(main_position, text_main, font=font_main, fill=(255, 255, 255, 255))

# --- Иконки (📚 + 🛠️) ---
book_icon = Image.open(BytesIO(BOOK_PNG)).resize((50, 50), Image.LANCZOS)
tools_icon = Image.open(BytesIO(TOOLS_PNG)).resize((50, 50), Image.LANCZOS)

icons_y = main_position[1] + text_h + 10
icons_total_width = book_icon.width + tools_icon.width + 10
start_x = (img.width - icons_total_width) // 2

img.paste(book_icon, (start_x, icons_y), book_icon)
img.paste(tools_icon, (start_x + book_icon.width + 10, icons_y), tools_icon)

# --- Рамка ---
draw.rounded_rectangle([4, 4, img.width - 4, img.height - 4], corner_radius, outline=(255, 255, 255, 180), width=4)

# --- Сохраняем favicon ---
img.save("favicon.ico", sizes=[(64, 64), (48, 48), (32, 32), (16, 16)])
print("✅ Современный favicon создан: favicon.ico")
