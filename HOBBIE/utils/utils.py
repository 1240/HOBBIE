from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

__author__ = '1240'


def create_image(text, filename, W=250, H=70, fontsize=35):
    text = text.title()
    image = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("static//fonts//Xiomara-Script.ttf", fontsize)
    w, h = draw.textsize(text, font)
    draw.text(((W - w) / 2, (H - h) / 2), text, font=font, fill=(69, 200, 217, 225))
    filepath = 'temp/%s.png' % filename
    image.save(filepath, "PNG")
    return filepath