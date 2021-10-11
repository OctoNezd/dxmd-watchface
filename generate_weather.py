import icons
import generate_date
import font
import shutil
import common
try:
    shutil.rmtree("res/font/weather")
except FileNotFoundError:
    pass
WEATHER_ICONS = open("weather-icons.txt").read().strip().split("\n")
WEATHER_ICONS_SYMBOLS = ""
for item in WEATHER_ICONS:
    print("searching", item)
    WEATHER_ICONS_SYMBOLS += icons.get_icon(item)
WIDTH = font.determine_width(
    WEATHER_ICONS_SYMBOLS, icons.ICON_FONT, generate_date.FONT_SIZE)
print("Width:", WIDTH)
font.generate_fontset(WEATHER_ICONS_SYMBOLS, [
                      WIDTH, common.DATE_HEIGHT], "center", icons.ICON_FONT, generate_date.FONT_SIZE, common.ACCENT, "weather")
font.generate_symbol("-", common.DATE_HEIGHT,
                     generate_date.FONT, generate_date.FONT_SIZE, common.ACCENT, "weather")
font.generate_symbol("°", common.DATE_HEIGHT,
                     generate_date.FONT, generate_date.FONT_SIZE, common.ACCENT, "weather")
font.generate_symbol("/", common.DATE_HEIGHT,
                     generate_date.FONT, generate_date.FONT_SIZE, common.ACCENT, "weather")
