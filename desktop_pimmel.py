'''
"""
 6l4br10n @ qxz2uyl
"""

from tkinter import *
import tkinter as tk
import ctypes
from PIL import ImageGrab, ImageDraw, Image

app = Tk()
app.geometry("400x400")
app.title("Desktop Pimmel Bot v0.1")
app.eval('tk::PlaceWindow . center')


def xy(event):
    global x, y
    x, y = event.x, event.y


def draw(event):
    global x, y
    canvas.create_line((x, y, event.x, event.y), fill='red')
    # canvas.create_text(100, 20, fill='red', font=("Arial", "30", "bold"),
    #                   text="PIMMEL")
    x, y = event.x, event.y
#########################################
width = 400
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)


# Tkinter create a canvas to draw on
canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", draw)
canvas.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
canvas.create_line([0, center, width, center], fill='green')

# do the PIL image/draw (in memory) drawings
draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
def save_widget_as_image[]
filename = "C:\my_drawing.jpg"
image1.save(filename)

# save as desktopWallpaper
# ctypes.windll.user32.SystemParametersInfoW(20, 0, "absolute path", 0)

schaltf1 = tk.Button(app, text="Aktion durchführen", command=save_widget_as_image)
schaltf1.pack()

app.mainloop()

'''
import ctypes
import os
import sys

from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1920, 1080), color=(143, 143, 143))

fontsize = 30
font = ImageFont.truetype("arial.ttf", fontsize)

fontsize_pimmel = 80
font_pimmel = ImageFont.truetype("arial.ttf", fontsize_pimmel)

d = ImageDraw.Draw(img)
d.text((400, 10), "                                                                                                    ", font=font, fill=(255, 255, 0))
d.text((400, 30), "                                                                                                    ", font=font, fill=(255, 255, 0))
d.text((400, 50), "                                                                                                    ", font=font, fill=(255, 255, 0))
d.text((400, 70), "                                           .^7??7!~:.                                               ", font=font, fill=(255, 255, 0))
d.text((400, 90), "                                       .JBPJ77B&Y5                                            ", font=font, fill=(255, 255, 0))
d.text((400, 110), "                                         G#^    PB  :7@                                         ", font=font, fill=(255, 255, 0))
d.text((400, 130), "                                        7@!     GB     J@~                                          ", font=font, fill=(255, 255, 0))
d.text((400, 150), "                                       BB      P#.      B                                          ", font=font, fill=(255, 255, 0))
d.text((400, 170), "                                      ^@?      J@:     &.                                         ", font=font, fill=(255, 255, 0))
d.text((400, 190), "                                     ?@^       !P.     @^                                         ", font=font, fill=(255, 255, 0))
d.text((400, 210), "                                      Y@^               @~                                         ", font=font, fill=(255, 255, 0))
d.text((400, 230), "                                     Y@G5?7!~^!G~                                         ", font=font, fill=(255, 255, 0))
d.text((400, 250), "                                     5&:^!!7JJYY55@                                         ", font=font, fill=(255, 255, 0))
d.text((400, 270), "                                       BB               !@~                                         ", font=font, fill=(255, 255, 0))
d.text((400, 290), "                                      .&Y               7@^                                         ", font=font, fill=(255, 255, 0))
d.text((400, 310), "                                      ^@?               J@:                                         ", font=font, fill=(255, 255, 0))
d.text((400, 330), "                                      !@!               J@:                                         ", font=font, fill=(255, 255, 0))
d.text((400, 350), "                                      ?@^               Y&.                                         ", font=font, fill=(255, 255, 0))
d.text((400, 370), "                                      Y&.                P#.                                         ", font=font, fill=(255, 255, 0))
d.text((400, 390), "                                      P#.                GB                                          ", font=font, fill=(255, 255, 0))
d.text((400, 410), "                                      GB                 .&5                                          ", font=font, fill=(255, 255, 0))
d.text((400, 430), "                                     .#P                  7@~                                          ", font=font, fill=(255, 255, 0))
d.text((400, 450), "                                     .&5                  Y&.                                          ", font=font, fill=(255, 255, 0))
d.text((400, 470), "                                     .&5                  GB                                           ", font=font, fill=(255, 255, 0))
d.text((400, 490), "                                     .&5                 .&5                                           ", font=font, fill=(255, 255, 0))
d.text((400, 510), "                                     .&5                 .&5                                           ", font=font, fill=(255, 255, 0))
d.text((400, 530), "                                     .&5                 :@J                                           ", font=font, fill=(255, 255, 0))
d.text((400, 550), "                         !JY555555Y   :@? .:^!7~:                                   ", font=font, fill=(255, 255, 0))
d.text((400, 570), "                       :BB7~^::::^~!J  :@B5P55JJ5PG                                ", font=font, fill=(255, 255, 0))
d.text((400, 590), "                       5@:            .G?                !~:. ~BB.                               ", font=font, fill=(255, 255, 0))
d.text((400, 610), "                       GB                                          !@~                               ", font=font, fill=(255, 255, 0))
d.text((400, 630), "                       P#.                                          ?@^                               ", font=font, fill=(255, 255, 0))
d.text((400, 650), "                       7@~                                         ~@Y                                ", font=font, fill=(255, 255, 0))
d.text((400, 670), "                       .G#:                                       7@J                                 ", font=font, fill=(255, 255, 0))
d.text((400, 690), "                        .GP                                    !@J                                  ", font=font, fill=(255, 255, 0))
d.text((400, 710), "                                                                                                    ", font=font, fill=(255, 255, 0))
d.text((400, 730), "                                                                                                    ", font=font, fill=(255, 255, 0))
d.text((400, 750), "                                                                                                    ", font=font, fill=(255, 255, 0))
d.text((400, 820), "           PIMMEL                                        ", font=font_pimmel, fill=(255, 255, 0))

try:
    if os.path.isdir("C:\pimmel"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\pimmel\pimmel.jpg', 0)
    else:
        path = os.path.join("C:\pimmel")
        os.mkdir(path)
        img.save('C:\pimmel\pimmel.jpg')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\pimmel\pimmel.jpg', 0)
except Exception as e:
    print(e)











