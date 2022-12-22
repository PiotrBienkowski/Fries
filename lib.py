import random
import time
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from reportlab.graphics import renderPDF

global_width = 1
global_color = "black"
global_background_color = "white"
global_mode = "!DEBUG"

def draw_corner(x1, y1, x2, y2, right = False, color="", linecap = True, stroke_width = -1):
    ret = ""

    if linecap: 
        tmpLineCap = ""
    else:
        tmpLineCap = "stroke-linecap='round'"

    if stroke_width == -1:
        stroke_width = global_width

    tmp_right = 1
    if right:
        tmp_right = -1

    color = global_color
    radius = stroke_width
    ret += "<path d='M "
    ret += str(x1) + " " + str(y1) + " C "
    ret += str(x2 - tmp_right * radius * random.uniform(0.95, 1.2)) + " " + str(y1) + ", "
    ret += str(x2) + " " + str(y1 - radius * random.uniform(0.95, 1.2)) + ", " + str(x2) + " " + str(y2)
    ret += "' stroke-width='" + str(stroke_width) + "' stroke='" + color + "' " + tmpLineCap + " fill='transparent' />"

    return ret

def draw_point(x, y, color = "red", r = 1):
    ret = ""

    ret += "<circle cx='" + str(x) + "' cy='" + str(y) + "' r='" + str(r) +"' fill='" + color + "'/>"

    return ret

def draw_curve(x1, y1, x2, y2):
    ret = ""

    x_tmp = (x1 + x2) / 2 

    ret += "<path d='M " + str(x1) + " " + str(y1) + " C " + str(x_tmp) + " " + str(y1) + ", " + str(x_tmp) + " " + str(y1) + ", " + str(x2) + " " + str(y2) + "' stroke-width='" + str(global_width - 0.5) + "' stroke='" + global_color + "' fill='transparent' stroke-linecap='round'/>"

    return ret

def draw_Qcurve(x1, y1, x2, y2, x, y, width):
    ret = ""

    ret += "<path d='M " + str(x1) + " " + str(y1) + " Q " + str(x) + " " + str(y) + " " + str(x2) + " " + str(y2) + "' stroke='" + global_color + "' stroke-width='" + str(width) + "' fill='transparent' stroke-linecap='round'/>"
    
    return ret

def draw_eyeball(x1, y1, x2, y2, x_org):
    ret = ""

    tmp = x1 + (abs(x1 - x_org)) * random.uniform(1.2, 1.35)
    
    ret += "<path d='M " + str(x1) + " " + str(y1) + " C " + str(tmp) + " " + str(y1) + ", " + str(x1 + (abs(x1 - x_org)) * random.uniform(1.2, 1.35)) + " " + str(y2) + ", " + str(x2) + " " + str(y2) + "' stroke-width='" + str(global_width - 0.5) + "'  stroke-linecap='round' stroke='" + global_color + "' fill='transparent'/>"
    ret += draw_point(tmp - (abs(x1 - tmp)) * 0.44 * random.uniform(0.95, 1), (y1 + y2) / 2 + (abs(y1 - y2)) * random.uniform(-0.14, 0.14), global_color, global_width)

    return ret

def draw_eye(x1, y1, x2, y2):
    ret = ""

    tmp = max(y1, y2)
    y1 = min(y1, y2)
    y2 = tmp

    height = abs(y1 - y2)
    tmp_margin = height * random.uniform(0.1, 0.3)
    tmp_hor = height * random.uniform(0.55, 0.65)
    height_2 = height * random.uniform(0.47, 0.53)

    ret += "<path d='M " + str(x1) + " " + str(y1) + " C " + str(x1 - tmp_hor) + " " + str(y1 - tmp_margin) + ", " + str(x1 - tmp_hor) + " " + str(y2 + tmp_margin) + ", " + str(x2) + " " + str(y2) + "' stroke-width='" + str(global_width) +"'  stroke-linecap='round' stroke='" + global_color + "' fill='transparent'/>"
    ret += draw_eyeball(x1 - tmp_hor * 0.6, y1 + height * random.uniform(0.85, 1) / 2 - height_2 / 2, x1 - tmp_hor * 0.6, y1 + height * random.uniform(0.85, 1) / 2 + height_2 / 2, x1)

    return ret

def draw_line(x1, y1, x2, y2, linecap = True):
    ret = ""

    if linecap: 
        tmpLineCap = "stroke-linecap='square'"
    else:
        tmpLineCap = "stroke-linecap='round'"

    ret = "<line x1='" + str(int(x1)) + "' y1='" + str(int(y1)) + "' x2='"+ str(int(x2)) +"' y2='" + str(int(y2)) + "' stroke-width='" + str(global_width) + "' stroke='" + global_color + "' " + tmpLineCap + " />"
    return ret

def draw_mouth(x1, y1, width, mouth_position):
    ret = ""

    tmp_width = width * random.uniform(0.18, 0.28)
    ret += draw_curve(x1, y1, x1 - tmp_width, y1 - mouth_position * random.uniform(-0.08, 0.3))

    return ret

def draw_hair(start_x, start_y, width, max_height):
    ret = ""

    random_range_l = 0.3
    random_range_r = 1.3

    random_range_l_h = 0.7
    random_range_r_h = 1.1

    tmp_strokre_width = global_width * random.uniform(0.7, 0.9)

    number_of_hairs = int((width * 0.8) / tmp_strokre_width * ((2.2 * random.uniform(0.75, 1))/ 3))
    space_between_hairs = width * 0.8 - number_of_hairs * tmp_strokre_width
    average_space = space_between_hairs / (number_of_hairs - 2)

    tmp_order = []
    for i in range(number_of_hairs):
        tmp_order.append(i)
    tmp_order.remove(0)
    tmp_order.remove(number_of_hairs - 1)

    rands = []
    rands.append(random.uniform(-0.5, 0.5)) 
    rands.append(-1)

    tmp_x = start_x + width * 0.1
    tmp_end_x = tmp_x + width * rands[0]
    tmp_end_y = start_y + max_height * rands[1]

    ret += draw_Qcurve(tmp_x, start_y, tmp_end_x, tmp_end_y, tmp_x, tmp_end_y, tmp_strokre_width)

    tmp_tmp = random.uniform(0, 1)
    if tmp_tmp < 0.5:
        tmp_tmp = -0.5
    else: 
        tmp_tmp = 1

    tmp_x = start_x + width * 0.1 + (number_of_hairs - 1) * average_space + (number_of_hairs - 1) * tmp_strokre_width
    tmp_end_x = tmp_x + width * rands[0] * random.uniform(random_range_l, random_range_r) * tmp_tmp
    tmp_end_y = start_y + max_height * rands[1] * random.uniform(random_range_l_h, random_range_r_h)

    ret += draw_Qcurve(tmp_x, start_y, tmp_end_x, tmp_end_y, tmp_x, tmp_end_y, tmp_strokre_width)

    while(len(tmp_order) > 0):
        tmp_tmp = random.uniform(0, 1)
        if tmp_tmp < 0.5:
            tmp_tmp = -0.5
        else: 
            tmp_tmp = 1

        tmp_idx = random.randint(0, len(tmp_order) - 1)
        idx = tmp_order[tmp_idx]
        tmp_order.remove(idx)

        tmp_x = start_x + width * 0.1 + idx * average_space + idx * tmp_strokre_width
        tmp_end_x = tmp_x + width * rands[0] * random.uniform(random_range_l, random_range_r) * tmp_tmp
        tmp_end_y = start_y + max_height * rands[1] * random.uniform(random_range_l_h, random_range_r_h)

        ret += draw_Qcurve(tmp_x, start_y, tmp_end_x, tmp_end_y, tmp_x, tmp_end_y, tmp_strokre_width)

    return ret

def draw_legs(x, y, width, legs_height):
    ret = ""

    tmp_position = width * random.uniform(0.25, 0.3)
    new_start_x = x + (width / 2) - tmp_position
    random_knee_x = random.uniform(-0.2, 0.2)
    random_bottom_x = random.uniform(-0.005, 0.005)
    knee_x = new_start_x - width * random_knee_x
    knee_y = y + legs_height * random.uniform(0.45, 0.55)
    legs_stroke_width = global_width

    ret += draw_Qcurve(new_start_x, y, new_start_x * (1 + random_bottom_x), y + legs_height, knee_x, knee_y, legs_stroke_width)

    new_start_x = x + (width / 2) + tmp_position
    knee_x = new_start_x + width * random_knee_x

    ret += draw_Qcurve(new_start_x, y, new_start_x * (1 - random_bottom_x * random.uniform(0.95, 1)), y + legs_height, knee_x, knee_y, legs_stroke_width)

    return ret

def draw_body(width, height, start_x, start_y, legs_height, hairs_max_height, step = 2137):
    ret = ""

    tmp_height_top_round = height * random.uniform(0.15, 0.25)
    tmp_height_bottom_round = height * random.uniform(0.15, 0.4)
    tmp_width_round = width * random.uniform(0.25, 0.5)
    eye_height = height * random.uniform(0.20, 0.25)
        
    if step == 0: 
        return ret

    ret += "<!-- START OF THE BODY -->"
    # left top corner
    ret += draw_corner(start_x + tmp_width_round, start_y, start_x, start_y + tmp_height_top_round)
    
    # right top corner
    ret += draw_corner(start_x + width - tmp_width_round, start_y, start_x + width, start_y + tmp_height_top_round, True, global_color, False)
    
    # top line
    ret += draw_line(start_x + tmp_width_round, start_y, start_x + width - tmp_width_round, start_y)
    
    # left line
    ret += draw_line(start_x, start_y + tmp_height_top_round, start_x, start_y + height - tmp_height_bottom_round)
    
    # left bottom corner
    ret += draw_corner(start_x + tmp_width_round, start_y + height, start_x, start_y + height - tmp_height_bottom_round)
    
    # right bottom corner
    ret += draw_corner(start_x + width - tmp_width_round, start_y + height, start_x + width, start_y + height - tmp_height_bottom_round, True, global_color, False)

    # bottom line
    ret += draw_line(start_x + tmp_width_round, start_y + height, start_x + width - tmp_width_round, start_y + height)

    # right line
    ret += draw_line(start_x + width, start_y + tmp_height_top_round + eye_height, start_x + width, start_y + height - tmp_height_bottom_round * 0.98, False)

    ret += "<!-- INFO -->"
    ret += "<!-- Fryta copyright © -->"
    ret += "<!-- END OF INFO -->"


    ret += "<!-- END OF THE BODY -->"

    if step == 1: 
        return ret

    ret += "<!-- START OF THE EYES -->"
    # eye
    ret += draw_eye(start_x + width, start_y + tmp_height_top_round, start_x + width, start_y + tmp_height_top_round + eye_height)
    ret += "<!-- END OF THE EYES -->"

    if step == 2: 
        return ret

    ret += "<!-- START OF THE MOUTH -->"
    mouth_position = height * random.uniform(0.14, 0.25)

    ret += draw_mouth(start_x + width, start_y + height - mouth_position, width, mouth_position)
    ret += "<!-- END OF THE MOUTH -->"

    if step == 3: 
        return ret

    ret += "<!-- START OF THE LEGS -->"
    ret += draw_legs(start_x, start_y + height, width, legs_height)
    ret += "<!-- END OF THE LEGS -->"
    
    if step == 4: 
        return ret
    
    ret += "<!-- START OF THE HAND -->"
    tmp_hand_y = random.uniform(start_y + tmp_height_top_round, start_y + tmp_height_top_round + (eye_height / 4) * 2)
    tmp_hand_x = start_x + width / 3 

    tmp_hand_y_2 = start_y + height - mouth_position - height * random.uniform(0.1, 0.2)
    tmp_hand_x_2 = start_x + width / 3 * 2
    
    ret += draw_Qcurve(tmp_hand_x, tmp_hand_y, tmp_hand_x_2, tmp_hand_y_2, tmp_hand_x, tmp_hand_y_2, global_width - 0.5)
    ret += "<!-- END OF THE HAND -->"

    if step == 5:
        return ret

    ret += "<!-- START OF THE HAIR -->"
    if hairs_max_height != 0:
        ret += draw_hair(start_x, start_y, width, hairs_max_height)
    ret += "<!-- END OF THE HAIR -->"

    return ret

def svgToPng(name):
    tmp = svg2rlg(name + '.svg')
    renderPM.drawToFile(tmp, name + '.png', fmt='PNG')

def svgToPdf(name):
    tmp = svg2rlg(name + '.svg')
    renderPDF.drawToFile(tmp, name + '.pdf')

def generate(width, height, sta_x = 0, sta_y = 0):

    tmp_width = int((width * (23/114)) * random.uniform(0.70, 1.2))
    tmp_height = int((height * (62.7/114)) * random.uniform(0.90, 1.1))
    hair_max_height = int(tmp_height * random.uniform(0.12, 0.17))
    legs_height = int(tmp_height * random.uniform(0.12, 0.20))

    global global_width 
    global_width = width * (2 / 154)

    tmp_bald = random.uniform(0, 1)
    if tmp_bald < 0.03:
        hair_max_height = 0

    start_y = sta_y + int((height - (tmp_height + legs_height + hair_max_height)) / 2) + hair_max_height
    start_x = sta_x + int((width) / 2 - tmp_width / 2)

    return draw_body(tmp_width, tmp_height, start_x, start_y, legs_height, hair_max_height)
    
def generate_name():
    ret = ""
    
    ret += "fryta_" + str(time.time()).replace('.', '_')
    
    return ret

def set_variables(color = global_color, background_color = global_background_color):
    global global_color
    global_color = color
    
    global global_background_color
    global_background_color = background_color
    

def set_background(width, height):
    ret = ""

    if global_background_color != "white":
        ret += "<rect width='" + str(width) + "' height='" + str(height) + "' style='fill:" + str(global_background_color) + " '/>"
    
    return ret

def svg_init(width, height, name, content, width_s, height_s):
    start_line = "<svg width='" + str(width_s) + "' height='" + str(height_s) + "' xmlns='http://www.w3.org/2000/svg' style=''>" 
    end_line = "</svg>"

    f = open(str(name) + ".svg", "w")
    f.write(start_line)
    f.write(set_background(width_s, height_s))
    f.write(content)
    f.write(end_line)
    f.close()