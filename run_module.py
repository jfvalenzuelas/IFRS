import module_processing
import analysis_utils
import pymongo
import os
import pprint
from bson.objectid import ObjectId

def getDocument(id):
    client = pymongo.MongoClient('localhost', 27654)
    #print('CLIENTE: SUCCESS')
    db = client['scrapper']
    #print('BD: SUCCESS')
    coll = db.IFRS
    #print('COLLECTION: SUCESS')

    cursor = coll.find({'_id':ObjectId(id)})
    return cursor

def run(doc_id):
    try:
        print('ID TO LOG')
        with open('/var/www/html/scrapper/public/logs/log.txt', 'w') as log_file:
            log_file.write(doc_id)
            log_file.write('\n')
            log_file.close()
        print('ID WRITTEN')
        #First
        document = getDocument(doc_id)
        #print ('\n')
        #pprint.pprint(document)
        #print ('\n')
        a, b, c, d, e = module_processing.separateGroups(document[0])
        f = module_processing.fixList(document[0])
        print('--1 CHECK--')

        #Second
        file_name = document[0]['title']+'.xlsx'
        file_name2 = doc_id+'.xlsx'
        analysis_utils.copy_rename(file_name2)
        print('--2 CHECK--')

        #Third
        module_processing.writeData(a, b, c, d, e, f, file_name2, document[0]['file_name'])
        analysis_utils.writeCell(file_name2)
        print('--3 CHECK--')

        #Fourth
        client = pymongo.MongoClient('localhost', 27654)
        db = client['scrapper']
        coll = db.IFRS

        coll.update_one({'_id': ObjectId(doc_id)}, {'$set': {'processed': 1}})
        print('--4 CHECK--')

        print('--L I S T O :) --')
        return 1
    except Exception as e:
        print ('--E R R O R :( --')
        print('Message:\n'+repr(e))
        return 0

if __name__ == '__main__':
    #print('--HOLI :) --')
    run(os.sys.argv[1])