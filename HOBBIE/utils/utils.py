from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from room.models import HashTags

__author__ = '1240'


def create_image(text, filename, W=250, H=70, fontsize=45):
    text = text.title()
    image = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("static//fonts//anfisa_grotesk.ttf", fontsize)
    # font = ImageFont.truetype("..//static//fonts//anfisa_grotesk.ttf", fontsize)
    w, h = draw.textsize(text, font)
    draw.text(((W - w) / 2, (H - h) / 2), text, font=font, fill=(69, 200, 217, 225))
    # draw.text(((W - w) / 2, (H - h) / 2), text, font=font, fill=(255, 255, 255, 225))
    filepath = 'temp/%s.png' % filename
    # filepath = '%s.png' % filename
    image.save(filepath, "PNG")
    return filepath


# create_image("Along", "Along")


def fill_hash_tags_statistics(hash_tags):
    for hash_tag in hash_tags.split(','):
        try:
            hash_tag_object = HashTags.objects.get(hash_name=hash_tag)
        except:
            hash_tag_object = HashTags()
            hash_tag_object.hash_name = hash_tag
            hash_tag_object.count = 0
        hash_tag_object.count += 1
        hash_tag_object.save()