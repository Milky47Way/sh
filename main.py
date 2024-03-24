from pygame import *

win_width = 700
win_height = 500
display.set_caption('Shooter')
window = display.set_mode((win_width, win_height))

img_back = 'b4731cf47a193ff46fa7ef82b637d7fa.jpg'
img_hero = '#png'

#mixer.init()
#mixer.music.load('space.ogg') #music
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')

background = transform.scale(image.load(img_back), (win_width, win_height))
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))
        display.update()
    time.delay(50)

#https://github.com/AnnaSepita/shooter_photo
