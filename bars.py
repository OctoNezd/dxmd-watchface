from PIL import Image, ImageDraw
import os
import shutil
INNER_PADDING = 5
OUTER_PADDING = 2
HEIGHT = 36
WIDTH = 136 + OUTER_PADDING + 2
print("Width:", WIDTH)
print("X:", (152 - WIDTH)//2)
BAT_FILL_WIDTH = HEIGHT // 4
BAT_EMPTY_WIDTH = HEIGHT // 10
STEP_COUNT = 10


def generate_bar(path, fill_color, icon, icon_right):
    icon = Image.open(icon).convert("RGBA")
    extra_padding_left = 0 if icon_right else icon.width
    extra_padding_right = icon.width if icon_right else 0
    full_line = WIDTH-INNER_PADDING*2 - extra_padding_right
    for i in range(1, STEP_COUNT+1):
        with Image.new("RGBA", (WIDTH, HEIGHT), color=(0, 0, 0, 255)) as img:
            draw = ImageDraw.Draw(img)
            draw.rectangle(((OUTER_PADDING, OUTER_PADDING),
                            (WIDTH - OUTER_PADDING * 2, HEIGHT-OUTER_PADDING * 2)),
                           outline=(255, 255, 255, 160))
            draw.line(((INNER_PADDING + extra_padding_left, int(HEIGHT // 2)),
                       (full_line, int(HEIGHT // 2))), fill=(255, 255, 255, 159), width=BAT_EMPTY_WIDTH)
            fill_width = int((WIDTH-OUTER_PADDING * 2 - 3) * (i / STEP_COUNT))
            fill = Image.new("RGBA", (fill_width, HEIGHT-OUTER_PADDING*2-2),
                             color=(*fill_color, 120))
            draw_line = True
            if fill_width > WIDTH - INNER_PADDING - OUTER_PADDING - extra_padding_right:
                fill_width = WIDTH - INNER_PADDING * 2 - extra_padding_right
                draw_line = False
            img.paste(fill, (OUTER_PADDING + 1, OUTER_PADDING + 1), mask=fill)
            if fill_width >= 1 + extra_padding_left + INNER_PADDING + OUTER_PADDING or i == STEP_COUNT:
                overflow = fill_width + 1 > full_line
                if overflow:
                    fill_width = full_line
                else:
                    fill_width += 1
                draw.line(((INNER_PADDING + extra_padding_left, int(HEIGHT // 2)),
                           (fill_width, int(HEIGHT // 2))),
                          fill=fill_color, width=BAT_FILL_WIDTH)
                if draw_line and not overflow:
                    draw.line((
                        (fill_width+1,
                         0), (fill_width+1, HEIGHT)
                    ), fill=(255, 255, 255, 200), width=1)
            icon_position = WIDTH - icon.width - \
                OUTER_PADDING - INNER_PADDING if icon_right else OUTER_PADDING + 2
            img.paste(icon, (icon_position, (HEIGHT - icon.height) // 2),
                      mask=icon)
            alpha_mask = img.split()[-1]
            img_noalpha = Image.new("RGBA", img.size, (255, 255, 255, 255))
            img_noalpha.paste(img, mask=alpha_mask)
            img_noalpha.save(f"res/bars/{path}/{str(i).zfill(4)}.png")
