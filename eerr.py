import pandas as pd
import spacy
import ssh_get_data
import numpy as np
import pprint
import math
from prettytable import PrettyTable
import analysis_utils

t = PrettyTable(['Original', 'Matched', 'Similarity'])

document = ssh_get_data.getDoc('EERR_67')

file = 'utils.xlsx'
xl = pd.ExcelFile(file)
df_1 = xl.parse('EERR')['value'].as_matrix()
df_2 = xl.parse('EERR')['value2'].as_matrix()

nlp = spacy.load('es')

eerr_data = []
for data in document[0]['data']:
    simil = []
    text = []
    name = data['name'].lower().strip()
    value = data['value']

    if (len(value) == 0):
        pass
    else:
        doc1 = nlp(name)
        for i in range (0, len(df_1)):
            doc2 = nlp(df_1[i].lower().strip())
            aux = doc1.similarity(doc2)
            if (df_2[i] != '--'):
                doc3 = nlp(df_2[i].lower().strip())
                aux_2 = doc1.similarity(doc3)
                if (aux_2 > aux):
                    simil.append(aux_2)
                    text.append(df_1[i])
                else:
                    simil.append(aux)
                    text.append(df_1[i])
            else:
                simil.append(aux)
                text.append(df_1[i])
        tmp = [text[simil.index(max(simil))], value]
        eerr_data.append(tmp)

        #print(name+" -> "+text[simil.index(max(simil))]+" "+str(max(simil)))
        t.add_row([name[:50], text[simil.index(max(simil))][:50], str(max(simil))[:5]])
f=open('log-'+document[0]['file_name']+'.txt', encoding='utf-8', mode='w')
f.write(t.get_string())
f.close()

analysis_utils.writeEERR(eerr_data)