import bars
import os
import shutil
try:
    shutil.rmtree("res/bars")
except FileNotFoundError:
    pass
os.makedirs("res/bars/battery")
os.makedirs("res/bars/steps")
bars.generate_bar("battery", (0, 210, 255),
                  "res/battery_icon.png", False)
bars.generate_bar("steps", (128, 255, 178), "res/health_icon.png", True)
