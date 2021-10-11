import cssutils
from tqdm import tqdm
ICON_FONT = "node_modules/@mdi/font/fonts/materialdesignicons-webfont.ttf"

mdi = list(cssutils.parseFile(
    "node_modules/@mdi/font/css/materialdesignicons.css"))
ICONS = {}
for rule in tqdm(mdi):
    if rule.type == rule.STYLE_RULE and rule.selectorText.endswith("::before"):
        ICONS[rule.selectorText] = rule.style.content.strip('"')


def get_icon(icon_name):
    selector = f".mdi-{icon_name}::before"
    return ICONS[selector]
