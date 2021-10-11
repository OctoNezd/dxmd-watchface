import string
import font
import common
# CLOCK_FONT = "font/ProximaNovaT-Thin.ttf"
CLOCK_FONT = "font/AzeretMono-Thin.ttf"
HEIGHT = 141
HEIGHT_ACTUAL = 75
FONT_SIZE = font.determine_fontsize(
    stringset=string.digits, width=common.CLOCKBOX_W // 2, height=HEIGHT, font_path=CLOCK_FONT)
FULL_HEIGHT = (HEIGHT * 2 + common.CLOCKBOX_PADDING * 3)
if __name__ == "__main__":
    import shutil
    try:
        shutil.rmtree("res/font/clock")
    except FileNotFoundError:
        pass

    font.generate_fontset(string.digits, (common.CLOCKBOX_W // 2, HEIGHT),
                          "left", CLOCK_FONT,  FONT_SIZE, (255, 255, 255), "clock/ones")
    font.generate_fontset(range(6), (common.CLOCKBOX_W // 2, HEIGHT),
                          "right", CLOCK_FONT, FONT_SIZE, (255, 255, 255), "clock/tens")
    print("Center position for tens:",
          common.MIBAND_W // 2 - common.CLOCKBOX_W//2)
    print("Center position for ones:", (common.MIBAND_W) // 2)
    minutes_h = common.CLOCK_H_START + common.CLOCKBOX_H - \
        common.DATE_HEIGHT - HEIGHT_ACTUAL
    print("Minutes height:", minutes_h)
    hours_h = minutes_h - HEIGHT_ACTUAL - common.CLOCKBOX_PADDING
    print("Hours height:", hours_h)
