import os
from glob import glob
build_path = os.path.abspath("build") + "\\"

for file in glob("build/*.png"):
    print("removing old symlink", file)
    os.unlink(file)


def symlink(src, tgt):
    try:
        os.symlink(os.path.abspath(src), build_path + tgt)
    except WindowsError as e:
        if e.errno != 17:
            print(e.errno)
            raise e


iterator = 1


def link_folder(folder):
    global iterator
    for img in os.listdir(folder):
        print(folder, img, "->", str(iterator).zfill(4))
        symlink(f"{folder}/{img}", str(iterator).zfill(4) + ".png")
        iterator += 1


print("linking background")
symlink("res/bg.png", "0000.png")
print("linking clock")
link_folder("res/font/clock/ones")
link_folder("res/font/clock/tens")
print("linking date")
link_folder("res/font/date/months")
link_folder("res/font/date/weekdays")
link_folder("res/font/date/days")
print("linking battery bar")
link_folder("res/bars/battery")
print("linking step bar")
link_folder("res/bars/steps")
print("linking weather")
link_folder("res/font/weather")
print("linking status")
link_folder("res/font/status/off")
link_folder("res/font/status/on")
