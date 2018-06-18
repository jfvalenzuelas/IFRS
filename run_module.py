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
        #First
        client = pymongo.MongoClient('localhost', 27654)
        db = client['scrapper']
        coll = db.IFRS
        coll.update_one({'_id': ObjectId(doc_id)}, {'$set': {'processed': 2}})
        document = getDocument(doc_id)
        #print ('\n')
        #pprint.pprint(document)
        #print ('\n')
        a, b, c, d, e = module_processing.separateGroups(document[0])
        f = module_processing.fixList(document[0])
        print(a)
        print('\n')
        print(b)
        print('\n')
        print(c)
        print('\n')
        print(d)
        print('\n')
        print(e)
        print('\n')
        print(f)
        print('\n')
        print('--1 CHECK--')

        #Second
        file_name = doc_id+'.xlsx'
        analysis_utils.copy_rename(file_name)
        print('--2 CHECK--')

        #Third
        module_processing.writeData(a, b, c, d, e, f, file_name, document[0]['file_name'])
        analysis_utils.writeCell(file_name)
        print('--3 CHECK--')

        #Fourth
        coll.update_one({'_id': ObjectId(doc_id)}, {'$set': {'processed': 1}})
        print('--4 CHECK--')

        #analysis_utils.writeLog(doc_id)
        client.close()
        print('--L I S T O :) --')
        return 1
    except Exception as e:
        print ('--E R R O R :( --')
        print('Message:\n'+repr(e))
        coll.update_one({'_id': ObjectId(doc_id)}, {'$set': {'processed': 0}})
        return 0

if __name__ == '__main__':
    #print('--HOLI :) --')
    run(os.sys.argv[1])