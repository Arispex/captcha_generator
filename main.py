from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def main(code: str):
    bg = Image.new("RGBA", (len(code) * 65, 100), "white")
    draw = ImageDraw.Draw(bg, "RGBA")

    for w in range(bg.width):
        for h in range(bg.height):
            draw.point((w, h), random_color())
    # bg.show()

    index = 0
    for i in code:
        code_bg = Image.new("RGBA", (70, 90), (0, 0, 0, 0))
        code_font = ImageFont.truetype(font="Alibaba-PuHuiTi-Regular.otf", size=70)
        code_draw = ImageDraw.Draw(code_bg, "RGBA")
        code_draw.text((10, 0), i, random_color(), font=code_font)
        # code_bg.show()
        code_bg = code_bg.rotate(random.randint(-30, 30))
        r, g, b, a = code_bg.split()
        bg.paste(code_bg, (index * 60, 0), mask=a)
        index += 1

    # bg = bg.filter(ImageFilter.EMBOSS)
    bg.show()


if __name__ == '__main__':
    main("NM4L")