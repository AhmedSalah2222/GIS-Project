import os
from PIL import Image, ExifTags

img_folder = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Images'
img_contents = os.listdir(img_folder)

for image in img_contents:
    full_path = os.path.join(img_folder, image)

    pillow_img = Image.open(full_path)
    exif = {ExifTags.TAGS[k]: v for k, v in pillow_img._getexif().items() if k in ExifTags.TAGS}
    gps_all = {}

    print '\n'
    print exif
    print '\n'


    try:
        for key in exif['GPSInfo'].keys():
            print "This is the coded value {}".format(key)
            decoded_value = ExifTags.GPSTAGS.get(key)
            print "This is it's associated label {}".format(decoded_value)
            gps_all[decoded_value] = exif['GPSInfo'][key]

        print '\n'
        longitudeRef = gps_all.get('GPSLongitudeRef')
        longitude = gps_all.get('GPSLongitude')
        latitudeRef = gps_all.get('GPSLatitudeRef')
        latitude = gps_all.get('GPSLatitude')

        print longitudeRef, "       ", longitude
        print latitudeRef, "        ", latitude



    except:
        print "This image has no GPS Info in it {}".format(full_path)
        pass

    print '\n'
    print '\n'