import lib
import random
import subprocess
import time

global_name = "!!tapeta" + str(random.randint(1, 2137))

SET_WALLPAPER_OSASCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "{}"
end tell
END"""


def init(width, height):
    size = 256
    ret = ""
    last_y = 0

    tmp = random.randint(0, 6 * 10)

    cnt = 0
    for i in range(height // size):
        last_x = 0
        for j in range(width // size):
            if cnt == tmp:
                lib.set_variables("#ff8400", "#151515")
            ret += lib.generate(size, size, last_x, last_y)
            if cnt == tmp:
                lib.set_variables("white", "#151515")
            cnt += 1
            last_x += size
        last_y += size
    lib.svg_init(2 * size, size, global_name, ret, width, height)


def set_wallpaper_2():
    full_image_path = "/Users/piotrbienkowski/Documents/IT/fryta/" + global_name + ".png"
    print("done")
    subprocess.Popen(SET_WALLPAPER_OSASCRIPT.format(full_image_path), shell=True)
    time.sleep(1)

lib.set_variables("white", "#151515")
init(2560, 1600)
lib.svgToPng(global_name)


set_wallpaper_2()