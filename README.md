Geoprocessing Report Steps -

1 - Copy A4Landscape2.mxd to a registered folder with your ArcGIS Server\
\
2-  Copy Geoprocessing_Report.py to destinated folder\
\
3-  Open Geoprocessing_Report.py. Repath the mxd variable (mxd = arcpy.mapping.MapDocument(r"C:\Web_Print\A4 Landscape2.mxd") to where    you copied A4Landscape2.mxd\
\
4- Check the A4Landscape2.mxd. Make sure Data Driven Pages is set up correctly. Make sure that the Parcel_Select Layer's Definition Query is set up as well.\
\
5- Copy Geoprocessing_Report.tbx to a destinated folder. Open ArcCatolog.\
\
6- Under the Geoprocessing_Report.tbx, open up Create_Geoprocessing_Report Script Properties. Under Source, change the Script File Path to where you saved Geoprocessing_Report.py\
\
7- Test run the Create_Geoprocessing_Report Script. The script is designed to look for 13-digit Parcel Numbers. To change this, you will need to change the Parcel_Select layer's source in A4Landscape2.mxd. You will need to update the Data Driven Pages in the mxd and the Data Driven texts elements in the layout as well.\
\
8- Once you are satified with your results, publish this as a geoprocessing service.\
\
Any questions, feel free to contact me at 717-771-9870(ex.1724) or jsimora@ycpc.org


