import arcpy
import re

arcpy.env.overwriteOutput = True

urban_area = arcpy.GetParameterAsText(0)
countries = arcpy.GetParameterAsText(1)
Area_sqkm = arcpy.GetParameterAsText(2)
outpath = arcpy.GetParameterAsText(3)

arcpy.MakeFeatureLayer_management(urban_area, "urban_layer")
mycur = arcpy.SearchCursor(urban_area, ['area_sqkm', 'FID'])
counter = 0
for i in mycur:
    if i.getValue('area_sqkm') > float(Area_sqkm):

        arcpy.MakeFeatureLayer_management(countries, 'countries_layer',
                                          """ "FID" = {} AND "CONTINENT" = 'Africa' """.format(i.getValue('FID')))

        with arcpy.da.SearchCursor('countries_layer', 'NAME') as search_cursor:
            for row in search_cursor:
                name = row[0]
                x = re.sub(r'[^a-zA-Z0-9/s]', '', name)

                arcpy.SelectLayerByLocation_management('urban_layer', 'WITHIN', 'countries_layer')
                arcpy.FeatureClassToFeatureClass_conversion('urban_layer', outpath, "UrbanAreas_in_{}_{}".format(x, i.getValue('FID')))

arcpy.AddMessage("Done!")
