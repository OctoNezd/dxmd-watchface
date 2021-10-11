import icons
import common
from PIL import Image, ImageDraw, ImageFont
import font
import shutil
import os
PATH = "res/font/status"
try:
    shutil.rmtree(PATH)
except FileNotFoundError:
    pass
os.makedirs(PATH)
os.makedirs(PATH + "/on")
os.makedirs(PATH + "/off")
ICONS_ON = ["bluetooth", "lock", "minus-circle"]
ICONS_OFF = ["bluetooth-off", "lock-open", "watch-vibrate"]
font_size = font.determine_fontsize(
    [icons.get_icon(icon) for icon in ICONS_ON + ICONS_OFF], 18, 18, icons.ICON_FONT)
font.generate_fontset([icons.get_icon(icon) for icon in ICONS_ON], [
                      18, 18], "center", icons.ICON_FONT, font_size, common.ACCENT, "status/on")
font.generate_fontset([icons.get_icon(icon) for icon in ICONS_OFF], [
                      18, 18], "center", icons.ICON_FONT, font_size, (255, 255, 255), "status/off")
