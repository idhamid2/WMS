# Following scriptis is used for mosaicing the WFS images after downloading from Open-Source

import os, glob
from osgeo import gdal
import time
from datetime import timedelta

# starting time to calculate how much total time it takes to finish the script
start_time = time.time()

# storing the images name 
all_images = ['WMS5000.tif', 'WMS10000.tif', 'WMS25000.tif', 'WMS50000.tif']
for i in range(4):
    image_path = 'C:/Users/hamida/PycharmProjects/WMS/image/all/*-' + all_images[i]
    filelist = glob.glob(image_path)
    image_build = gdal.BuildVRT("mergd.vrt", filelist)
    output_image_path = "C:/Users/hamida/PycharmProjects/WMS/image/Merge" + all_images[i]
    image_translate = gdal.Translate(output_image_path, image_build)
    image_build = None
   

# calculating the end time after saving all the data
elapsed_time_secs = time.time() - start_time

#displaying the total time
message = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
print(message)
