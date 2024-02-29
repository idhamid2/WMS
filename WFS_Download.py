# Following scriptis used for downlaoding the WFS images for Stadt Rhein-Sieg (Germany) at different scales from Open-Source

from owslib.wms import WebMapService
from datetime import timedelta
import time

# starting time to calculate how much total time it takes to finish the script.
start_time = time.time()

# links to Open-data WFS at different scales
dtm_wms_links = ['https://www.wms.nrw.de/geobasis/wms_nw_abk', ' https://www.wms.nrw.de/geobasis/wms_nw_dtk',
                'https://www.wms.nrw.de/geobasis/wms_nw_dtk25', 'https://www.wms.nrw.de/geobasis/wms_nw_dtk50']

# layer-name in WFS data for every scale
wms_layer_name = ['nw_abk_col','nw_dtk_col','nw_dtk25_col', 'nw_dtk50_col']

# extent properties of rhein-Seig boundary
startLong = 348456.3830000013113022
startLat = 5602403.6229999996721745
endLong = 407162.9600000008940697
endLat = 5645452.9039999991655350

imageNumber = 1
wms_layer_name_counter = 0

# setting the coordinates of image
imageStartLong = startLong
imageStartLat = startLat
imageEndLong = startLong
imageEndLat = startLat

# making connection and saving the image from WMS data
for dtm_wms_link in dtm_wms_links:
    if wms_layer_name_counter == 0:
        image_name = 'WMS5000.tif'
    elif wms_layer_name_counter == 1:
        image_name = 'WMS10000.tif'
    elif wms_layer_name_counter == 2:
        image_name = 'WMS25000.tif'
    else:
        image_name = 'WMS50000.tif'
    wms = WebMapService(dtm_wms_link, version="1.3.0")

    # for every image there is a change 750 latitude and 750 longitude
    while (imageEndLat <= endLat):
        imageEndLat += 750
        while (imageEndLong <= endLong):
            imageEndLong += 750
            img = wms.getmap(
                layers=[wms_layer_name[wms_layer_name_counter]],
                size=[1000, 800],
                srs="EPSG:25832",
                bbox=[imageStartLong, imageStartLat, imageEndLong, imageEndLat],
                format="image/tiff")

            save_fp = 'image/all/'  + str(imageNumber) +'-' +image_name
            with open(save_fp, 'wb') as out:
                out.write(img.read())

            imageNumber += 1
            imageStartLong = imageEndLong
            imageEndLong += 750

        imageStartLong = startLong
        imageEndLong = startLong
        imageStartLat = imageEndLat
        imageEndLat += 750

    wms_layer_name_counter+=1
    imageNumber = 1
    imageStartLong = startLong
    imageStartLat = startLat
    imageEndLong = startLong
    imageEndLat = startLat

# calculating the end time after saving all the data
elapsed_time_secs = time.time() - start_time

#displaying the total time
message = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
print(message)
