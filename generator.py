import lib

global_mode = "!DEBUG"

def init(size_v = -1):
    if global_mode == "DEBUG":
        size = 200
    else:
        if size_v != -1:
            size = int(size_v)
        else:
            size = int(input())

    if size < 40 and not global_mode == "DEBUG":
        print("The size is too small. Minimum size is 110.")
    else:
        name = ""
        if global_mode == "DEBUG":
            name = "fryta"
        else:
            name = lib.generate_name()
        
        lib.svg_init(2 * size, size, name, lib.generate(size, size) + lib.generate(size, size, size))
        lib.svgToPdf(name)
        lib.svgToPng(name)

lib.set_variables()
init()