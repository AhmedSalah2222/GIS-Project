import arcpy

arcpy.env.overwriteOutput = True

countries = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_countries.shp'
points = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_populated_places.shp'
outpath = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec8'

arcpy.MakeFeatureLayer_management(points, "points_layer")

arcpy.MakeFeatureLayer_management(countries, "country", """ "REGION_WB" = 'Middle East & North Africa' """)
arcpy.SelectLayerByLocation_management("points_layer", "WITHIN", "country")
arcpy.FeatureClassToFeatureClass_conversion("points_layer", outpath, "Arabic_countries")
