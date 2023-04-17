import glymur, skimage.data, skimage.metrics, skimage.measure, skimage.io, os, sys
'''
This script reads a PNG image and computes the entropy.
Args: filename
'''
img = skimage.io.imread('Kuvat/PNG/'+ str(sys.argv[1]))
#print(cameraImg)
print(str(sys.argv[1]) + " entropy:" + str(skimage.measure.shannon_entropy(img, base=2)))
