import arcpy

arcpy.env.overwriteOutput = True

countries = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_countries.shp'
disputed_areas = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_disputed_areas.shp'
outpath = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec6'

arcpy.MakeFeatureLayer_management(disputed_areas, "disputed_areas_layer")
disputed_areas_list = ['-99', '1. High income: OECD', '2. High income: nonOECD', '3. Upper middle income']
count = 0

for i in disputed_areas_list:
    arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "INCOME_GRP" = '{}' """.format(i))
    arcpy.SelectLayerByLocation_management("disputed_areas_layer", "WITHIN", "countries_layer")
    arcpy.FeatureClassToFeatureClass_conversion("disputed_areas_layer", outpath,
                                                "disputed_areas_in_{}".format(count))
    count = count + 1


disputedAreas_Income = arcpy.SearchCursor(disputed_areas, ['NAME', 'INCOME_GRP'])

for d in disputedAreas_Income:
    if d.getValue('INCOME_GRP') == '-99':
        print d.getValue('NAME') + ' ( INCOME_GRP = -99 ) '
    elif d.getValue('INCOME_GRP') == '1. High income: OECD':
        print d.getValue('NAME') + ' (( INCOME_GRP = 1. High income: OECD )) '
    elif d.getValue('INCOME_GRP') == '2. High income: nonOECD':
        print d.getValue('NAME') + ' ((( INCOME_GRP = 2. High income: nonOECD ))) '
    elif d.getValue('INCOME_GRP') == '3. Upper middle income':
        print d.getValue('NAME') + ' (((( INCOME_GRP = 3. Upper middle income )))) '

