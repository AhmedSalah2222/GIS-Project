import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data'

countries = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_countries.shp'
points = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_populated_places.shp'
disputed_areas = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_disputed_areas.shp'
outpath = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec2'

arcpy.MakeFeatureLayer_management(points, "points_layer")
arcpy.MakeFeatureLayer_management(disputed_areas, "disputed_areas_layer")

arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "NAME"='Palestine' """)

arcpy.SelectLayerByLocation_management("points_layer", "WITHIN", "countries_layer")
arcpy.FeatureClassToFeatureClass_conversion("points_layer", outpath, "cities_in_Palestine")

arcpy.SelectLayerByLocation_management("disputed_areas_layer", "WITHIN", "countries_layer")
arcpy.FeatureClassToFeatureClass_conversion("disputed_areas_layer", outpath, "disputed_areas_in_Palestine")

createdCities = arcpy.SearchCursor(points, ['NAME', 'ADM0NAME'])
disputedAreas = arcpy.SearchCursor(disputed_areas, ['NAME', 'ADMIN'])

for c in createdCities:
    if c.getValue('ADM0NAME') == 'Palestine':
        print c.getValue('NAME')

print '\n'

for d in disputedAreas:
    if d.getValue('ADMIN') == 'Palestine':
        print d.getValue('NAME')
