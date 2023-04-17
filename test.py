import glymur, skimage.data, skimage.metrics, os, sys, rawpy
import time
'''
jp2file = glymur.data.nemo() # just a path to a JPEG 2000 file
jp2 = glymur.Jp2k(jp2file)
fullres = jp2[:]
print(fullres.shape)
thumbnail = jp2[::2, ::2]
print(thumbnail.shape)
print(jp2)

file = glymur.data.jpxfile() # just a path to a JPEG2000 file
j = glymur.Jp2k(file)
d0 = j[:] # first layer
j.layer = 3
d3 = j[:] # third layer

t0 = time.time(); data = jp2[:]; t1 = time.time()
print(t1 - t0)
glymur.set_option('lib.num_threads', 2)
t0 = time.time(); data = jp2[:]; t1 = time.time()
print(t1 - t0)

jp2 = glymur.Jp2k('test.jp2')
jp2[:] = skimage.data.astronaut()

jp2 = glymur.Jp2k('test.jp2', plt=True)
jp2[:] = skimage.data.astronaut()
c = jp2.get_codestream(header_only=False)
print(c.segment[6])
'''


cameraImg = skimage.io.imread('Kuvat/PNG/' + str(sys.argv[1]))
#cameraImg = rawpy.imread('Kuvat/' + str(sys.argv[1])).raw_image
#outImg = 'Kuvat/JP2/PSNR30/' + str(sys.argv[2]) + '.jp2'
outImg2 = 'Kuvat/JP2/PSNR40/' + str(sys.argv[2]) + 'PSNR.jp2'
#print(cameraImg)
#write images with different compression ratios for different layers
# quality layer 1: compress 20x
# quality layer 2: compress 10x
# quality layer 3: compress lossless
#out1 = glymur.Jp2k(outImg, data = cameraImg, cratios=[1])
# read the lossless layer
#jp2.layer = 2
#data = jp2[:]

#write images with different PSNR (or “quality”) for different layers, time result
#Testaa, miten ajojen määrä vaikuttaa nopeuteen (median of 7 jos eka ei ole erilainen)
t0 = time.time()
out2 = glymur.Jp2k(outImg2, data = cameraImg, psnr=[40])
t1 = time.time()

print('Time: ' + str(t1 - t0))

#Print picture properties
fullres = out2[:]
#filesizeNew = os.path.getsize("test3.jp2")
#print('Shape: ' + str(fullres.shape))
#print('File size: ' + str(filesizeNew))
'''
print('\n --- \nPicture information:')
print(out2)
'''

#Print signal to noise ratios
psnr = []
for layer in range(1):
    out2.layer = layer
    psnr.append(skimage.metrics.peak_signal_noise_ratio(cameraImg, out2[:]))
print(psnr)
