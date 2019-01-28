import json, os, uuid, collections, arcpy

arcpy.env.overwriteOutput = True

# Output to the scratch workspace
scratch = arcpy.env.scratchFolder
arcpy.AddMessage("  Scratch WS " + str(scratch))

#mxd = arcpy.mapping.MapDocument(arcpy.GetParameterAsText(0))
mxd = arcpy.mapping.MapDocument(r"C:\Web_Print\A4 Landscape2.mxd")

#Set Search Variable.
NameList = arcpy.GetParameterAsText(0)
#Example - Search by Parcel Number
#NameList = "42000GD008900"

#Set Output Names
output_name = str(NameList) + '.pdf'
OutputFile = os.path.join(arcpy.env.scratchFolder + '\\' + output_name)

# Loop thru Map Layers of mxd variable. If Layer is Parcel_Select, change definition query
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "Parcel Select":
        lyr.definitionQuery = "PIDN = '"+NameList+"'"

# Refresh mxd variable
mxd.dataDrivenPages.refresh()

# Data Driven variables
ddp = mxd.dataDrivenPages
indexLayer = ddp.indexLayer
arcpy.SelectLayerByAttribute_management(indexLayer, "NEW_SELECTION", "PIDN = '"+NameList+"'")

# Loop thru selected data driven pages. Will only be one data driven page.
for indexPage in ddp.selectedPages:
  ddp.currentPageID = indexPage
  # Export
  ddp.exportToPDF(OutputFile, "CURRENT")

del mxd

arcpy.SetParameterAsText(1, OutputFile)

arcpy.AddMessage("  Process Complete")