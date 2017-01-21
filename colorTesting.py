from SimpleCV import Image, Color

img = Image('targets.png')

#distance = img.colorDistance(Color.GREEN).invert() * 1.5 
#edges = distance.edges()
binarized = img.invert().binarize()

#distance.show()
#edges.show()
binarized.show()
