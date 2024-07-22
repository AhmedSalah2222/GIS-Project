import arcpy

arcpy.env.workspace = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data'
li = arcpy.ListFeatureClasses()
print (li)
