import arcpy
import re

airports = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_airports.shp'
field_list = arcpy.ListFields(airports)
list = []

for x in field_list:
    if x.type == 'String':
        list.append(x.name)
    else:
        print "this is not a String, it's {}".format(x.type)

for field in list:
    with arcpy.da.UpdateCursor(airports, [field, 'name_en']) as empty_string:
        for e in empty_string:
            if e[0] == ' ':
                x = re.sub(r'[^a-zA-Z0-9/s]', '', e[1])
                e[0] = x
                empty_string.updateRow(e)
                # print "value updated to {}".format(e[0])
