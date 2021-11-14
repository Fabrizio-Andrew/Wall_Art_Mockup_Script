import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
#import templates

templates = {
    1: {
        'name': 'exposed_brick',
        'slot_height': 1374,
        'slot_width': 1374,
        'position_left': 2063,
        'position_top': 400

    },
    2: {
        'name': 'bonded_leather'
    },
    3: {
        'name': 'exposed_brick'

    },
    4: {
        'name': 'gallery'

    },
    5: {
        'name': 'grey'

    },
    6: {
        'name': 'tan_leather'
    }
}
def add_shadow(temp, img_width, img_height, upper_pos, left_pos):
    shadow = Image.new('RGB', (img_width, img_height), 'grey')
    for i in range(10):
        shadow = shadow.filter(ImageFilter.BLUR)
    
    temp.paste(shadow, (left_pos - 20, upper_pos + 20))

    return temp


def draw(input_img, img_width, img_height, template, upper_pos, left_pos):
    """
    Draw Function
    ------------------ 
    Draws the mockup
    """
    temp = Image.open(f'templates/{template}.jpeg', 'r').convert('RGB') #Opens Template Image
    pasted = Image.open(f'input_images/{input_img}').convert("RGBA") #Opens Selected Image
    pasted=pasted.resize((img_width, int(pasted.size[1]*(img_width/pasted.size[0])))) #Resize image to width fit black area's width
    temp = add_shadow(temp, img_width, img_height, upper_pos, left_pos)
    temp.paste(pasted, (left_pos, upper_pos)) #Pastes image into template

    img_name = input_img.rsplit('.')[0]
    temp.save(f'outputs/{img_name}-{template}.jpg') #Saves output

print('Getting input files...')
inputlist = os.listdir('input_images')

for f in inputlist:
    print(f'Generating mockups for {f}')

    t = templates[1]
    draw(f, t['slot_width'], t['slot_height'], t['name'], t['position_top'], t['position_left'])

print('Complete')


# template = 5500 x 3354
# template mid = 2750 x 1677
# input = square 512 x 512

# insert = 1374 x 1374
# start 50% left and 100% up
# start = 2063/left and 600/top
