import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data'

countries = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_countries.shp'
# points = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_populated_places.shp'
# disputed_areas = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_disputed_areas.shp'
new_points = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec2\cities_in_Palestine.shp'
new_disputed_areas = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Output\Rec2\disputed_areas_in_Palestine.shp'

# update_points = arcpy.UpdateCursor(points, ['SOV0NAME', 'ADM0NAME'])
# Update_disputed = arcpy.UpdateCursor(disputed_areas, ['SOVEREIGNT', 'ADMIN'])
update_new_points = arcpy.UpdateCursor(new_points, ['SOV0NAME', 'ADM0NAME'])
Update_new_disputed = arcpy.UpdateCursor(new_disputed_areas, ['SOVEREIGNT', 'ADMIN'])

# for y in update_points:
#     if y.getValue('ADM0NAME') == 'Israel':
#         y.setValue('SOV0NAME', 'Palestine')
#         update_points.updateRow(y)
#         print (y.getValue('SOV0NAME'))
# print '\n'

# for z in Update_disputed:
#     if z.getValue('SOVEREIGNT') == 'Israel':
#         z.setValue('SOVEREIGNT', 'Palestine')
#         Update_disputed.updateRow(z)
#         print (z.getValue('SOVEREIGNT'))
# print '\n'

for y in update_new_points:
    if y.getValue('SOV0NAME') == 'Israel':
        y.setValue('SOV0NAME', 'Palestine')
        update_new_points.updateRow(y)
        print (y.getValue('SOV0NAME'))
print '\n'


for z in Update_new_disputed:
    if z.getValue('SOVEREIGNT') == 'Israel':
        z.setValue('SOVEREIGNT', 'Palestine')
        Update_new_disputed.updateRow(z)
        print (z.getValue('SOVEREIGNT'))
