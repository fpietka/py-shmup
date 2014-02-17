#!/usr/bin/python

from __future__ import division

# Include the PySFML extension
import sfml as sf

import math

# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "PySFML test")
window.vertical_synchronization = True

# resources
try:
    Image = sf.Image.from_file("FAX-44_MkIII_b.png")
except IOError:
    print "Error loading sprite"
    import sys
    sys.exit(1)
Image.create_mask_from_color(Image[0, 0])
Texture = sf.Texture.from_image(Image)
Sprite = sf.Sprite(Texture)
# get the sprite downsized
Sprite.scale((0.5, 0.5))
Sprite.move((400 - (Image.width / 2), 300 - (Image.height / 2)))

try:
    Image = sf.Image.from_file("water-blue-water-tile.jpg")
except IOError:
    print "Error loading background"
    import sys
    sys.exit(1)
Texture = sf.Texture.from_image(Image)
Texture.repeated
# Prepare background
Background = sf.Sprite(Texture)
# get the background downsized
Background.scale((0.25, 0.25))

b_width = Image.width / 4
b_height = Image.height / 4

def ceil(value):
    return int(math.ceil(value))

speed = 1
sprite_speed = 5

step = 0

# Start the game loop
while window.is_open:
    for event in window.events:
        # window closed or escape key pressed: exit
        if type(event) is sf.CloseEvent:
            window.close()
    window.clear()

    for x in range(0, ceil(window.width / b_width)):
        for y in range(0, ceil(window.height / b_height) + int(b_height)):
            Background.position = x * b_width, y * b_height - step - b_height
            window.draw(Background)

    if step <= - b_height:
        step = 0
    else:
        step -= speed

    if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
        Sprite.move((- sprite_speed, 0));
    if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
        Sprite.move((sprite_speed, 0));
    if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
        Sprite.move((0, - sprite_speed));
    if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
        Sprite.move((0, sprite_speed));

    window.draw(Sprite)
    window.display()
