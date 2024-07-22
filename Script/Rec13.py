# import arcpy
#
# arcpy.env.overwriteOutput = True
#
# disputed_areas = arcpy.GetParameterAsText(0)
# count = 0
#
# Update_disputed = arcpy.UpdateCursor(disputed_areas, ['POP_YEAR', 'ECONOMY'])
#
# for z in Update_disputed:
#     if z.getValue('POP_YEAR') < 2014:
#         z.setValue('ECONOMY', "the data is updated")
#         Update_disputed.updateRow(z)
#
# arcpy.AddMessage('\n')
#
# arcpy.AddMessage("The data is updated")
#
# disputedAreas = arcpy.SearchCursor(disputed_areas, ['POP_YEAR', 'SOVEREIGNT'])
#
# for d in disputedAreas:
#     if d.getValue('POP_YEAR') < 2014:
#         count = count + 1
#         arcpy.AddMessage(d.getValue('SOVEREIGNT'))
#         arcpy.AddMessage(count)
# arcpy.AddMessage('totalcount:' + count)

import arcpy

arcpy.env.overwriteOutput = True

# disputed_areas = r'D:\4th Year Material\Second term\GIS\Project\GIS_Project\Data\ne_10m_admin_0_disputed_areas.shp'
disputed_areas = arcpy.GetParameterAsText(0)
count = 0

Update_disputed = arcpy.UpdateCursor(disputed_areas, ['POP_YEAR', 'ECONOMY', 'NAME_EN'])

arcpy.AddMessage('\n')
arcpy.AddMessage("The data is updated")
arcpy.AddMessage('\n')
for z in Update_disputed:
    if z.getValue('POP_YEAR') < 2014:
        z.setValue('ECONOMY', "the data is updated")
        count = count + 1
        Update_disputed.updateRow(z)
        arcpy.AddMessage('{} : {}'.format(z.getValue('NAME_EN'),z.getValue('ECONOMY')))
arcpy.AddMessage('\n')


total_count = arcpy.GetCount_management(disputed_areas)[0]
arcpy.AddMessage('Updated Areas {} out if {} Records '.format(count,total_count))
arcpy.AddMessage('\n')




# termDisputedAreas = arcpy.SearchCursor(term_disputed_areas, ['POP_YEAR', 'SOVEREIGNT'])

# for td in termDisputedAreas:
#     if td.getValue('POP_YEAR') < 2014:
#         count = count + 1
#         print td.getValue('SOVEREIGNT')
#         print count
#         print '\n'
