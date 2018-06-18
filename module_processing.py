import analysis_utils
import threading

def separateGroups(document):
    ########################################
    ###         BALANCE IFRS             ###
    ########################################

    b1 = False
    b2 = False 
    b3 = False
    b4 = False
    b5 = False

    ac = []
    anc = []
    pc = []
    pnc = []
    pat = []

    data = document['data']
    count = 1
    for x in data:
        text = x['name'].lower().strip()
        value = x['value']
        if ('total' in text or ('estado' in text and 'consolidado' in text)):
            pass
        else:
            if (text == 'activo corriente' or text == 'activos corrientes'):
                b1 = True
                b2 = False
                b3 = False
                b4 = False
                b5 = False

            elif (text == 'activo no corriente' or text == 'activos no corrientes'):
                b1 = False
                b2 = True
                b3 = False
                b4 = False
                b5 = False

            elif (text == 'pasivo corriente' or text == 'pasivos corrientes'):
                b1 = False
                b2 = False
                b3 = True
                b4 = False
                b5 = False

            elif (text == 'pasivo no corriente' or text == 'pasivos no corrientes'):
                b1 = False
                b2 = False
                b3 = False
                b4 = True
                b5 = False

            elif (text == 'patrimonio' or text == 'patrimonios'):
                b1 = False
                b2 = False
                b3 = False
                b4 = False
                b5 = True

            else:
                if (b1):
                    aux = []
                    aux.append(text)
                    aux.append(value)
                    ac.append(aux)

                elif (b2):
                    aux = []
                    aux.append(text)
                    aux.append(value)
                    anc.append(aux)

                elif (b3):
                    aux = []
                    aux.append(text)
                    aux.append(value)
                    pc.append(aux)

                elif (b4):
                    aux = []
                    aux.append(text)
                    aux.append(value)
                    pnc.append(aux)

                elif (b5):
                    aux = []
                    aux.append(text)
                    aux.append(value)
                    pat.append(aux)

                else:
                    print('--ERROR--')
        count += 1

    return ac, anc, pc, pnc, pat

def fixList(document):
    EERR = []
    data = document['eerr']

    for x in data:
        aux = []
        text = x['name'].lower().strip()
        value = x['value']
        aux.append(text)
        aux.append(value)
        EERR.append(aux)
    
    return EERR
    
def runProcess(data, file_name, group):
    for x in data:
        analysis_utils.writeData(file_name, group, x)
    print('Thread '+str(group)+' -- FINISHED --')

def writeData(ac, anc, pc, pnc, pat, eerr, file_name, orig_file_name):
    try:
        analysis_utils.openWorkBook(file_name)

        thread1 = threading.Thread( target=runProcess, args=(ac, file_name, 0) )
        thread2 = threading.Thread( target=runProcess, args=(anc, file_name, 1) )
        thread3 = threading.Thread( target=runProcess, args=(pc, file_name, 2) )
        thread4 = threading.Thread( target=runProcess, args=(pnc, file_name, 3) )
        thread5 = threading.Thread( target=runProcess, args=(pat, file_name, 4) )
        thread6 = threading.Thread( target=runProcess, args=(eerr, file_name, 5) )

        thread1.setDaemon(True)
        thread2.setDaemon(True)
        thread3.setDaemon(True)
        thread4.setDaemon(True)
        thread5.setDaemon(True)
        thread6.setDaemon(True)

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        
        thread1.join()
        thread2.join()        
        thread3.join()
        thread4.join()     
        thread5.join()
        thread6.join()

    except:
        pass