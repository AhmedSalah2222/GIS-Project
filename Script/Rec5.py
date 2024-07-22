import arcpy

arcpy.env.overwriteOutput = True

countries = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_countries.shp'
urban_areas = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_urban_areas.shp'
outpath = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec5'

arcpy.MakeFeatureLayer_management(urban_areas, "urban_areas_layer")
continents_list = ['Asia', 'Europe', 'North America']

for i in continents_list:
    arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "CONTINENT" = '{}' """.format(i))
    arcpy.SelectLayerByLocation_management("urban_areas_layer", "WITHIN", "countries_layer")
    arcpy.FeatureClassToFeatureClass_conversion("urban_areas_layer", outpath, "urban_areas_in_{}".format(i))

Sovereignt = arcpy.SearchCursor(countries, ['CONTINENT', 'SOVEREIGNT'])

for s in Sovereignt:
    if s.getValue('CONTINENT') == 'Asia':
        print s.getValue('SOVEREIGNT') + ' in ' + '(' + s.getValue('CONTINENT') + ')'

    elif s.getValue('CONTINENT') == 'Europe':
        print s.getValue('SOVEREIGNT') + ' in ' + '((' + s.getValue('CONTINENT') + '))'

    elif s.getValue('CONTINENT') == 'North America':
        print s.getValue('SOVEREIGNT') + ' in ' + '(((' + s.getValue('CONTINENT') + ')))'



