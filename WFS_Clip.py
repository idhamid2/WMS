# Following scriptis is used for cliping the WFS images from Stadt Rhein-Sieg (Germany) boundary

import arcpy, os

# setting the workspace for arcpy
workspace = arcpy.env.workspace = r"Defining the Workspace"

# Geodatabase path 
gdb = r"Defining the Databse Path to store output images"

# checking if the database is already exist, delete it and creates a new one
if arcpy.Exists(gdb):
    arcpy.Delete_management(gdb)
    arcpy.AddMessage(arcpy.GetMessages())
    print('Database has been deleted')

if not os.path.exists(os.path.dirname(gdb)):
    os.mkdir(os.path.dirname(gdb))

arcpy.CreateFileGDB_management(os.path.dirname(gdb), os.path.basename(gdb))
arcpy.AddMessage(arcpy.GetMessages())
print('DB has been created')

# storing the all the merge images name 
all_images = ['MergeWMS5000.tif', 'MergeWMS10000.tif', 'MergeWMS25000.tif', 'MergeWMS50000.tif']
for i in range(4):
    input_raster = workspace +'\\'+ all_images[i]
    output_raster = gdb+ "\\"+ 'clip'+str(i)
    arcpy.management.Clip(all_images[i], "348456.383000001 5602403.623 407162.960000001 5645452.904",
                       output_raster, "\Rhein_Sieg_Kreis_Boundaries\Merge_Boundaries", "256", "ClippingGeometry", "MAINTAIN_EXTENT")
    print('Image has been clipped')

print('Clip process has been completed')