import fontforge
import os
import psMat

# Путь к каталогу с SVG-файлами
svg_dir = "./src"
# Имя выходного шрифта
output_font = "output_font.ttf"

# Создайте новый шрифт
font = fontforge.font()

# Переберите все SVG-файлы в каталоге
for filename in os.listdir(svg_dir):
    if filename.endswith(".svg"):
        # Извлеките имя файла без расширения для использования в качестве кодовой точки
        glyph_name = os.path.splitext(filename)[0]

        # Предполагаем, что имена файлов имеют формат 'uXXXX', где XXXX - это шестнадцатеричный код
        glyph_unicode = int(glyph_name[1:], 16)  # Например, 'uF624' -> 0xF624

        # Создайте новый символ в шрифте
        glyph = font.createChar(glyph_unicode, glyph_name)

        # Импортируйте SVG-файл в символ
        glyph.importOutlines(os.path.join(svg_dir, filename))

        # Получите размеры контура
        bbox = glyph.boundingBox()
        glyph_width = bbox[2] - bbox[0]
        glyph_height = bbox[3] - bbox[1]

        # Рассчитайте смещения для выравнивания по центру
        offset_x = (glyph.width - glyph_width) / 2 - bbox[0]
        offset_y = (font.ascent - glyph_height) / 2 - bbox[1]

        # Примените смещения для центрирования
        glyph.transform(psMat.translate(offset_x, offset_y))

# Сохраните шрифт в формате TTF
font.generate(output_font)
