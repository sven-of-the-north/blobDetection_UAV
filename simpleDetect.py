from SimpleCV import Image, Color
import os, sys, argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
ap.add_argument("-c", "--crop", default='store_false', action='store_true', help="save cropped blobs")
ap.add_argument("-s", "--show", default='store_false', action='store_true', help="show blobs on input image")
args = vars(ap.parse_args())

img = Image(args["image"])
crop = args["crop"]
show = args["show"]

if( crop == 'store_false' and show == 'store_false' ):
    print ( "warning: no crop/show mode specified" )
    sys.exit(2)
else:
    if not os.path.exists('croppedBlobs'):
        os.makedirs('croppedBlobs')

color_distance = img.colorDistance(Color.RED).invert() * 2.5
# we should consider using multiple color filters; using r/g/b or custom
# this /might/ improve accuracy

binarized = color_distance.binarize()

blobs = binarized.findBlobs( minsize=50, maxsize=500 )

#blobs.draw(width=2)

overlay = color_distance.dl()

#print "blobs detected: ", len(blobs)

counter = 1

for blob in blobs:
    overlay.rectangle( blob.topLeftCorner(), (blob.width(), blob.height()), Color.RED, width = 2)
    
    if( crop == True ):    
        croppedBlob = img.crop( blob )
        name = "croppedBlobs/blob" + str(counter) + ".png"
        croppedBlob.save(name)
        counter += 1

if( show == True ):
   img.addDrawingLayer(overlay)
   img.show()

