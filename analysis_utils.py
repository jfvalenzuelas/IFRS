import os
from openpyxl import load_workbook
import shutil
import tools
import threading
import log_utils

global wb
global sheet

global_lock = threading.Lock()
file_contents = []

def saveContent(data):
    
    global_lock.acquire()
    file_contents.append(data)
    global_lock.release()

def openWorkBook(file_name):
    global wb
    global sheet

    wb = load_workbook('/var/www/html/scrapper/IFRS/reports/'+file_name)

    sheet = wb['IFRS']

def copy_rename(old_file_name, new_file_name):
        src_dir= '/var/www/html/scrapper/IFRS/'
        dst_dir= os.path.join(os.curdir , "reports")
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy(src_file,dst_dir)
        
        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)

def writeCell(file_name):

    for data_tuple in file_contents:
        target_cell = data_tuple[0]
        value = data_tuple[1]

        if (len(value.strip()) == 1 or len(value.strip()) == 0 or 
            value.strip() == '-' or value.strip() == ''):
            value = float(0)
        else:
            try:
                value = value.replace('.', '', 3)
                value = float(value)
                value = float("{0:.2f}".format(value))
            except ValueError:
                value = value.replace('.', '', 3)
                value = float(value)
                value = float("{0:.2f}".format(value))

        if (target_cell.value == None):
            target_cell.value = value
        else:
            aux = float(("{0:.2f}".format(target_cell.value)))
            target_cell.value = value + aux
        
    wb.save('/var/www/html/scrapper/IFRS/reports/'+file_name)
    wb.close()

def writeData(file_name, group, data):
    aux = []

    if (data[0].lower().strip() == 'ganancia bruta' or 
    ('utilidad' in data[0].lower().strip() and 'ejercicio' in data[0].lower().strip()) or 
    ('ganancia' in data[0].lower().strip() and 'antes de impuesto' in data[0].lower().strip())):
        pass
    else:
        #log_utils.write('Writing:\nGroup --> '+str(group)+', Text --> '+data[0])
        # here we get the file's cell's name to write the value
        target_cell = tools.matchCell(group, data[0])
        #return target_cell
        #We load the sheet's cell
        target_cell = sheet[target_cell]

        aux.append(target_cell)
        aux.append(data[1])

        saveContent(aux)

        #return target_cell
        #writeCell(target_cell, data[1], wb, file_name)
                    
        #wb.save('reports/'+file_name)