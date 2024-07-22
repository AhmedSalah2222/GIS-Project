import arcpy
import re

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data'

countries = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_countries.shp'
urban_areas = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_urban_areas.shp'
outpath = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec9'

arcpy.MakeFeatureLayer_management(urban_areas, "urbanl")

mycur = arcpy.SearchCursor(urban_areas, ['area_sqkm', 'FID'])

for i in mycur:
    if i.getValue('area_sqkm') > 50:

        arcpy.MakeFeatureLayer_management(countries, 'citiesl',
                                          """ "FID" = {} AND "CONTINENT" = 'Africa' """.format(i.getValue('FID')))

        with arcpy.da.SearchCursor('citiesl', 'NAME') as cursor:
            for row in cursor:
                city_name = row[0]
                x = re.sub(r'[^a-zA-Z0-9/s]', '', city_name)
                output_name = 'UrbanAreas_in_{}_{}'.format(x, i.getValue('FID'))
                arcpy.SelectLayerByLocation_management('urbanl', 'WITHIN', 'citiesl')
                arcpy.FeatureClassToFeatureClass_conversion('urbanl', outpath, output_name)
