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

    wb = load_workbook('/var/www/html/scrapper/public/reports/'+file_name)

    sheet = wb['IFRS']

def copy_rename(new_file_name):
        dst_dir= '/var/www/html/scrapper/public/reports/'
        src_file = '/var/www/html/scrapper/IFRS/ifrs-template.xlsx'
        shutil.copy(src_file, dst_dir)
        
        dst_file = '/var/www/html/scrapper/public/reports/ifrs-template.xlsx'
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
                value = tools.formatNumber(value)
            except ValueError:
                value = tools.formatNumber(value)

        if (target_cell.value == None):
            target_cell.value = value
        else:
            aux = float(("{0:.2f}".format(target_cell.value)))
            target_cell.value = value + aux
        
    wb.save('/var/www/html/scrapper/public/reports/'+file_name)
    wb.close()

def ignoreAccount(text):
    text = text.strip().lower()
    if (('ganancia bruta' in text) or ('atrib' in text and ('propiet' in text or 'particip' in text) and 'control' in text) or 
       ('total' in text) or ('antes' in text and 'mpuesto' in text)):
        return True
    else:
        return False

def writeData(file_name, group, data):
    aux = []

    if (ignoreAccount(data[0])):
        print('IGNORED ==> '+data[0])
    else:
        # here we get the file's cell's name to write the value
        target_cell = tools.matchCell(group, data[0])
        #We load the sheet's cell
        target_cell = sheet[target_cell]

        aux.append(target_cell)
        aux.append(data[1])

        #logdata = data[0]+' | '+str(data[1])+' | '+str(group)+' | '+str(aux_target)

        saveContent(aux)


        #return target_cell
        #writeCell(target_cell, data[1], wb, file_name)
                    
        #wb.save('reports/'+file_name)