import glymur, skimage.data, skimage.metrics, skimage.measure, skimage.io, os, sys, rawpy
'''
This script reads a CR2 image and computes the chosen layer's entropy.
Args: filename
'''
img = rawpy.imread('Kuvat/'+ str(sys.argv[1]))
data = img.raw_image
print(data)
print(str(sys.argv[1]) + " entropy:" + str(skimage.measure.shannon_entropy(data)))
