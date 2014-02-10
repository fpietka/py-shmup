#!/usr/bin/python

# Include the PySFML extension
from PySFML import sf

# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "PySFML test")

# Create a graphical string to display
text = sf.String("Hello SFML")

# resources
Image = sf.Image()
if not Image.LoadFromFile("FAX-44_MkIII_b.png"):
    print "Error loading sprite"
    import sys
    sys.exit(1)
Image.CreateMaskFromColor(Image.GetPixel(0, 0))
Sprite = sf.Sprite(Image)
# get the sprite downsized
Sprite.Resize(Sprite.GetSize()[0] / 2, Sprite.GetSize()[1] / 2)

Image = sf.Image()
if not Image.LoadFromFile("water-blue-water-tile.jpg"):
    print "Error loading sprite"
    import sys
    sys.exit(1)
Sprite2 = sf.Sprite(Image)
# get the sprite downsized
Sprite2.Resize(Sprite2.GetSize()[0] / 4, Sprite2.GetSize()[1] / 4)

# Start the game loop
running = True
while running:
    event = sf.Event()
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False

    # Clear screen, draw the text, and update the window
    window.Clear()
    window.Draw(text)
    window.Draw(Sprite2)
    window.Draw(Sprite)
    window.Display()
