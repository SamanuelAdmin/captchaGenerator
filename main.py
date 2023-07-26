# As a result you will have a JSON file with value of a captcha and path to the photo

# configs
symbols = list('1234567890' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
available_fonts = ['arial.ttf', 'times.ttf', 'verdana.ttf']
image_size = (200, 50)
interference = 4000 # count of random dots
count_of_photos = 200


# -----------------------------------
offsets = [(20, 10), (45, 15), (70, 12), (95, 18), (120, 10), (145, 15)]

from PIL import Image, ImageDraw, ImageFont
import random


def getRandomColor(): return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generateCaptcha(index):
    captcha_text = ''.join(random.choices(symbols, k=6))
    
    font = ImageFont.truetype(random.choice(available_fonts), 30)

    img = Image.new('RGB', image_size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    for i in range(interference):
        draw.point(
                (random.randint(0, image_size[0]), random.randint(0, image_size[1])),
                fill=getRandomColor()
            )

    for i in range(6): draw.text(offsets[i], captcha_text[i], font=font, fill=(0, 0, 0))

    for i in range(interference):
        draw.point(
                (random.randint(0, image_size[0]), random.randint(0, image_size[1])),
                fill=getRandomColor()
            )

    img.save(f'captcha/c{index}.png')
    return captcha_text, f'captcha/c{index}.png'


open('captcha.json', 'w').write('')
fileToSave = open('captcha.json', 'a')
fileToSave.write('{')

for i in range(1, count_of_photos):
    text, path = generateCaptcha(i)
    fileToSave.write(f'"{text}": "{path}",')

fileToSave.write('}')
fileToSave.close()
