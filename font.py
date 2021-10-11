from PIL import Image, ImageDraw, ImageFont
import os


def determine_width(stringset, font_path, font_size):
    width = 0
    font = ImageFont.truetype(font_path, font_size)
    for item in stringset:
        w, _ = font.getsize(str(item))
        if w > width:
            width = w
    print("Width for", stringset, ":", width)
    return width


def determine_fontsize(stringset, width, height, font_path):
    font_size = 999
    for letter in stringset:
        letter = str(letter)
        for i in reversed(range(0, font_size+1)):
            font = ImageFont.truetype(font_path, i)
            w, h = font.getsize(letter)
            if w <= width and h <= height:
                print("Size", i, "fits for character", letter)
                font_size = i
                break
    return font_size


def generate_fontset(stringset, size, align, font, font_size, color, path):
    os.makedirs(f"res/font/{path}", exist_ok=True)

    print("Selected font size:", font_size)
    print("Generating font text")
    font = ImageFont.truetype(font, font_size)
    for i, letter in enumerate(stringset):
        letter = str(letter)
        img = Image.new("RGBA", size, color=(255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        w, h = font.getsize(letter)
        if align == "center":
            w = (size[0] - w) // 2
        elif align == "right":
            w = (size[0] - w)
        elif align == "left":
            w = 0
        h = size[1] - h
        draw.text((w, 0), letter, font=font, fill=color)
        img.save(f"res/font/{path}/{str(i).zfill(4)}.png")


def generate_symbol(symbol, height, font, font_size, color, path):
    font = ImageFont.truetype(font, font_size)
    width, _ = font.getsize(symbol)
    img = Image.new("RGBA", [width, height], (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), symbol, font=font, fill=color)
    idx = len(os.listdir(f"res/font/{path}"))
    img.save(f"res/font/{path}/{idx}.png")
