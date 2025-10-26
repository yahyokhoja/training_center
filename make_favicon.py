from PIL import Image, ImageDraw, ImageFont

# Размер иконки
size = (64, 64)
background_color = (255, 255, 255, 0)  # прозрачный фон
text_main = "TC"
text_sub = "📚🛠️"  # Учёба + рабочий инструмент

# Создаем изображение
img = Image.new("RGBA", size, background_color)
draw = ImageDraw.Draw(img)

# Основной шрифт
font_main = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)

# Вычисляем позиции для центрирования
text_w, text_h = draw.textbbox((0,0), text_main, font=font_main)[2:]
sub_w, sub_h = draw.textbbox((0,0), text_sub, font=font_sub)[2:]

main_position = ((size[0] - text_w)//2, (size[1] - text_h - sub_h)//2)
sub_position = ((size[0] - sub_w)//2, main_position[1] + text_h)

# Рисуем текст
draw.text(main_position, text_main, font=font_main, fill=(0,0,0,255))
draw.text(sub_position, text_sub, font=font_sub, fill=(0,0,0,255))

# Сохраняем как favicon
img.save("favicon.ico")
print("Favicon создан: favicon.ico")
