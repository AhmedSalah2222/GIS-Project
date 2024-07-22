import arcpy

arcpy.env.overwriteOutput = True

countries = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_countries.shp'
airports = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_airports.shp'
outpath = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec4'

# arcpy.MakeFeatureLayer_management(countries, "countries_layer",)
# military_list = ['major and military', 'mid and military', 'military', 'military major', 'military mid']
# count = 0
#
#
# for i in military_list:
#     print (i)
#     count = count + 1
#     arcpy.MakeFeatureLayer_management(airports, "airports_layer", """ "TYPE" = '{}' """.format(i))
#     arcpy.SelectLayerByLocation_management("countries_layer", "INTERSECT", "airports_layer")
#     arcpy.FeatureClassToFeatureClass_conversion("countries_layer", outpath, "{}_{}_airport".format(count, i))
#     arcpy.SelectLayerByLocation_management("airports_layer", "INTERSECT", "countries_layer")

    # output_name = "{}_{}_airport".format(arcpy.ValidateTableName("countries"), arcpy.ValidateTableName(i))
    # arcpy.FeatureClassToFeatureClass_conversion("countries_layer", outpath, output_name)


arcpy.MakeFeatureLayer_management(countries, "countries_layer")

military_list = ['major and military', 'mid and military', 'military', 'military major', 'military mid']

for i in military_list:
    print i + ':-'
    arcpy.MakeFeatureLayer_management(airports, "airports_layer", """ "TYPE" = '{}' """.format(i))
    arcpy.SelectLayerByLocation_management("countries_layer", "INTERSECT", "airports_layer")
    arcpy.FeatureClassToFeatureClass_conversion("countries_layer", outpath, "{}_{}_airport".format("countries", i))

    countries_militarys = arcpy.SearchCursor("countries_layer", ['SOVEREIGNT'])
    for m in countries_militarys:
        print m.getValue('SOVEREIGNT')
    print '\n'

