from SimpleCV import Image, Color
import copy

img = Image("peter1.png")

color_distance = img.colorDistance(Color.RED).invert() * 2.5

binarized = color_distance.binarize()

blobs = binarized.findBlobs( minsize=50, maxsize=500 )

#blobs.draw(width=2)

overlay = color_distance.dl()

print "blobs detected: ", len(blobs)

for blob in blobs:
    overlay.rectangle( blob.topLeftCorner(), (blob.width(), blob.height()), Color.RED, width = 2)

img.addDrawingLayer(overlay)
img.show()

