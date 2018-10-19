"""
Copyright (c) 2018 Daniel J. Swearson

"""

# Run this script in RevitPythonShell; user must create a project parameter in Revit titled "CUSTOM_PARAM".
# CUSTOM_PARAM should be created as instance parameter, category set to sheet and type set to text.

__author__= 'Daniel J. Swearson'
__doc__ = 'Updates custom_param project parameter for all sheets in model.'

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction

doc = __revit__.ActiveUIDocument.Document

sheets_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets) \
												.WhereElementIsNotElementType().ToElements()
												
t = Transaction(doc, "Update Sheet Parameters")
t.Start()

for sheet in sheets_collector:
	custom_param = sheet.LookupParameter("CUSTOM_PARAM")
	if custom_param:
		custom_param.Set("Example Value")
		
t.Commit()
__window__.Close()
