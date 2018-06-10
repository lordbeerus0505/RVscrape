import openpyxl


def database(posA,posB,x,y):
    file=openpyxl.load_workbook('results.xlsx')
    sheet=file.get_sheet_by_name('Scores')
    sheet[posA]=x
    sheet[posB]=y
    file.save('results.xlsx')



