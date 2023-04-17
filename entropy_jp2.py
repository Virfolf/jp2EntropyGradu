import glymur, skimage.data, skimage.metrics, skimage.measure, skimage.io, os, sys
'''
This script reads a jp2 image and computes the chosen layer's entropy.
Args: filename
'''
img = glymur.Jp2k('Kuvat/jp2/PSNR40/'+ str(sys.argv[1]))
# read the lossless layer
img.layer = 0
data = img[:]
print(data)
print('\n --- \nPicture information:')
print(img)
print(str(sys.argv[1]) + " entropy:" + str(skimage.measure.shannon_entropy(data)))
