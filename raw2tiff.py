import rawpy
import sys
import imageio


with rawpy.imread(sys.argv[1]+'.cr2') as raw:
    rgb = raw.postprocess()
imageio.imsave(str(sys.argv[1]+'.tiff') + '', rgb)