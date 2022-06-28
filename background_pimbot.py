import ctypes
import os
import random
import string

from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1920, 1080), color=(143, 143, 143))

fontsize = 30
font = ImageFont.truetype("arial.ttf", fontsize)

fontsize_pimmel = 80
font_pimmel = ImageFont.truetype("arial.ttf", fontsize_pimmel)

d = ImageDraw.Draw(img)

z1 = random.randint(0, 9)
z2 = random.randint(0, 9)
z3 = random.randint(0, 9)
z4 = random.randint(0, 9)
z5 = random.randint(0, 9)
z6 = random.randint(0, 9)
z7 = random.randint(0, 9)
z8 = random.randint(0, 9)
z9 = random.randint(0, 9)

t1 = random.choice(string.ascii_uppercase)
t2 = random.choice(string.ascii_uppercase)
t3 = random.choice(string.ascii_uppercase)
t4 = random.choice(string.ascii_uppercase)
t5 = random.choice(string.ascii_uppercase)
t6 = random.choice(string.ascii_uppercase)



d.text((400, 10), f'                                                                                                    ', font=font, fill=(255, 255, 0))
d.text((400, 30), f'                                                                                                    ', font=font, fill=(255, 255, 0))
d.text((400, 50), f'                                                                                                    ', font=font, fill=(255, 255, 0))
d.text((400, 70), f'                                            .^{z2}??{z1}!~:.                                               ', font=font, fill=(255, 255, 0))
d.text((400, 90), f'                                        .JBP{z3}{z4}B&Y5                                            ', font=font, fill=(255, 255, 0))
d.text((400, 110), f'                                        G#^    PB  :7@                                         ', font=font, fill=(255, 255, 0))
d.text((400, 130), f'                                       {z5}@!     GB    J@                                          ', font=font, fill=(255, 255, 0))
d.text((400, 150), f'                                       B{t1}       P#.      {t2}                                          ', font=font, fill=(255, 255, 0))
d.text((400, 170), f'                                      ^@?      J@:     &.                                         ', font=font, fill=(255, 255, 0))
d.text((400, 190), f'                                     ?@^       !P.     @^                                         ', font=font, fill=(255, 255, 0))
d.text((400, 210), f'                                      Y@^               @~                                         ', font=font, fill=(255, 255, 0))
d.text((400, 230), f'                                     Y@G{z6}?{z7}!~^!G~                                         ', font=font, fill=(255, 255, 0))
d.text((400, 250), f'                                     5&:^!!7JJYY55@                                         ', font=font, fill=(255, 255, 0))
d.text((400, 270), f'                                       B{t1}               !@~                                         ', font=font, fill=(255, 255, 0))
d.text((400, 290), f'                                      .&Y               {z8}@^                                         ', font=font, fill=(255, 255, 0))
d.text((400, 310), f'                                      ^@?               J@:                                         ', font=font, fill=(255, 255, 0))
d.text((400, 330), f'                                      !@!               J@:                                         ', font=font, fill=(255, 255, 0))
d.text((400, 350), f'                                      ?@^               Y&.                                         ', font=font, fill=(255, 255, 0))
d.text((400, 370), f'                                      Y&.                P#.                                         ', font=font, fill=(255, 255, 0))
d.text((400, 390), f'                                      {t3}#.                {t2}{t1}                                          ', font=font, fill=(255, 255, 0))
d.text((400, 410), f'                                      GB                 .&5                                          ', font=font, fill=(255, 255, 0))
d.text((400, 430), f'                                     .#P                  {z9}@~                                          ', font=font, fill=(255, 255, 0))
d.text((400, 450), f'                                     .&{z1}                  Y&.                                          ', font=font, fill=(255, 255, 0))
d.text((400, 470), f'                                     .&{z1}                  GB                                           ', font=font, fill=(255, 255, 0))
d.text((400, 490), f'                                     .&{z1}                 .&{z6}                                           ', font=font, fill=(255, 255, 0))
d.text((400, 510), f'                                     .&{z2}                 .&{z7}                                           ', font=font, fill=(255, 255, 0))
d.text((400, 530), f'                                     .&{z4}                 :@J                                           ', font=font, fill=(255, 255, 0))
d.text((400, 550), f'                          !JY{z8}{z8}{z8}{z8}{z8}Y        :@? .:^!7~:                                   ', font=font, fill=(255, 255, 0))
d.text((400, 570), f'                       :BB7~^::::^~!J  :@{t4}{z1}P55{t6}{t5}5PG                                ', font=font, fill=(255, 255, 0))
d.text((400, 590), f'                       5{t4}:             .G?               !~:. ~BB.                               ', font=font, fill=(255, 255, 0))
d.text((400, 610), f'                       GB                                          !@~                               ', font=font, fill=(255, 255, 0))
d.text((400, 630), f'                       P#.                                          ?@^                               ', font=font, fill=(255, 255, 0))
d.text((400, 650), f'                       7{t4}~                                         ~@Y                                ', font=font, fill=(255, 255, 0))
d.text((400, 670), f'                       .G#:                                       7@{t5}                                 ', font=font, fill=(255, 255, 0))
d.text((400, 690), f'                        .G{t5}                                    !@{t2}                                  ', font=font, fill=(255, 255, 0))
d.text((400, 710), f'                                                                                                    ', font=font, fill=(255, 255, 0))
d.text((400, 730), f'                                                                                                    ', font=font, fill=(255, 255, 0))
d.text((400, 750), f'                                                                                                    ', font=font, fill=(255, 255, 0))
d.text((400, 770), f'                                                                                                    ', font=font, fill=(255, 255, 0))
d.text((400, 820), f'           PIMMEL {z1}                                        ', font=font_pimmel, fill=(255, 255, 0))

try:
    if os.path.isfile(r'C:\pimmel\2pimmel.png'):
        os.remove(r'C:\pimmel\2pimmel.png')
        img.save(r'C:\pimmel\2pimmel.png')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\pimmel\2pimmel.png', 0)
    else:
        path = os.path.join("C:\pimmel")
        os.mkdir(path)
        img.save(r'C:\pimmel\2pimmel.png')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\pimmel\2pimmel.png', 0)

except Exception as e:
    print(e)











