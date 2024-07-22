import os

img_folder = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Images'
img_contents = os.listdir(img_folder)

for image in img_contents:
    print image
    full_path = os.path.join(img_folder,image)
    print full_path
    print '\n'
