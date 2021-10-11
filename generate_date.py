import font
import calendar
import common
import shutil
try:
    shutil.rmtree("res/font/date")
except FileNotFoundError:
    pass
DAYS = list(range(0, 10))
WEEKDAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
MONTHS = [i.upper() for i in calendar.month_abbr[1:]]
FONT = "font/AzeretMono-Light.ttf"
FONT_SIZE = font.determine_fontsize(
    DAYS + WEEKDAYS + MONTHS, 9999999, common.DATE_HEIGHT, FONT)
if __name__ == "__main__":
    for item, pos in [("DAYS", "center"), ("WEEKDAYS", "right"), ("MONTHS", "left")]:
        font.generate_fontset(locals()[item], (font.determine_width(
            locals()[item], FONT, FONT_SIZE), common.DATE_HEIGHT), pos, FONT,
            FONT_SIZE, common.ACCENT, f"date/{item.lower()}")
    day_pos = (common.MIBAND_W -
               font.determine_width(range(1, 32), FONT, FONT_SIZE)) // 2
    print("Day position:", day_pos)
    print("day width:", font.determine_width(range(1, 32), FONT, FONT_SIZE))
    wd_pos = day_pos - \
        font.determine_width(WEEKDAYS, FONT, FONT_SIZE) - \
        common.CLOCKBOX_PADDING
    print("Weekday pos:", wd_pos)
    month_pos = (common.MIBAND_W +
                 font.determine_width(range(1, 32), FONT, FONT_SIZE)) // 2 + common.CLOCKBOX_PADDING
    print("Month pos:", month_pos)
    print("Height:", common.CLOCK_H_START +
          common.CLOCKBOX_PADDING)
