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
        document = getDocument(doc_id)
        #print ('\n')
        #pprint.pprint(document)
        #print ('\n')
        a, b, c, d, e = module_processing.separateGroups(document[0])
        f = module_processing.fixList(document[0])

        #Second
        file_name = document[0]['title']+'.xlsx'
        analysis_utils.copy_rename('/var/www/html/scrapper/IFRS/ifrs-template.xlsx', file_name)

        #Third
        module_processing.writeData(a, b, c, d, e, f, file_name, document[0]['file_name'])
        analysis_utils.writeCell(file_name)

        #Fourth
        client = pymongo.MongoClient('localhost', 27654)
        db = client['scrapper']
        coll = db.IFRS

        coll.update_one({'_id': ObjectId(doc_id)}, {'$set': {'processed': 1}})
        
        return 1
    except:
        return 0

if __name__ == '__main__':
    print('--HOLI :) --')
    run(os.sys.argv[1])