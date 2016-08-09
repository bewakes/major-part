from openpyxl import load_workbook

wb2 = load_workbook('../../PUMS data districtwise/01 Census 2011 District Taplejung.xlsx')
print(wb2.get_sheet_names())
