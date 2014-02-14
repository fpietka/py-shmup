#!/usr/bin/python

# Include the PySFML extension
import sfml as sf

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
Background = sf.Sprite(Texture)
# get the background downsized
Background.scale((0.25, 0.25))


# Start the game loop
while window.is_open:
    for event in window.events:
        # window closed or escape key pressed: exit
        if type(event) is sf.CloseEvent:
            window.close()
    # Clear screen, draw the text, and update the window
    window.clear()

    for x in range(0, window.width / (Image.width / 4) +1):
        for y in range(0, window.height / (Image.height / 4) +1):
            Background.position = x * (Image.width /4), y * (Image.height /4)
            window.draw(Background)

    window.draw(Sprite)
    window.display()
