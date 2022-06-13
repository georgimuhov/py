
"""
 6l4br10n
"""
import ctypes

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

img.save('C:\Daten\pil_text.png')

ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\Daten\pil_text.png', 0)











