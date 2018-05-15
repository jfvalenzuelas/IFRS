from openpyxl import load_workbook
from openpyxl.styles import Alignment

global wb_cells

wb_cells = []

def fillCells():
    for i in range (3, 13):
        wb_cells.append('B'+str(i))
    for i in range (14, 24):
        wb_cells.append('B'+str(i))
    for i in range (26, 34):
        wb_cells.append('B'+str(i))
    for i in range (35, 42):
        wb_cells.append('B'+str(i))
    for i in range (44, 50):
        wb_cells.append('B'+str(i))
    for i in range (56, 59):
        wb_cells.append('B'+str(i))
    for i in range (60, 62):
        wb_cells.append('B'+str(i))
    for i in range (63, 71):
        wb_cells.append('B'+str(i))
    for i in range (72, 73):
        wb_cells.append('B'+str(i))

def cleanFormat(file_name):

    wb = load_workbook('reports/'+file_name)

    sheet = wb['IFRS']
    fillCells()
    
    for cell in wb_cells:
        currentCell = sheet[cell]
        currentCell.alignment = Alignment(horizontal='left')


