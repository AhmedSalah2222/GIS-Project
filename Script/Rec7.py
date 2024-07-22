import arcpy

arcpy.env.overwriteOutput = True

airports = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_airports.shp'

mycur = arcpy.SearchCursor(airports, ['name', 'location', 'wikipedia'])
for i in mycur:
    adj = i.getValue('name').encode('ascii', 'ignore').decode('ascii')
    if i.getValue('location') == "ramp":
        print("NAME : {}".format(adj))
        print("Location :{}".format(i.getValue('location')))
        print("wiki  : {}".format(i.getValue('wikipedia'))) + "\n"
