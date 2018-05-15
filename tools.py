import spacy
import pandas as pd
import clean_utils

global file
global xl
global df1
global df2
global df3
global df4
global df5
global df6

file = 'utils.xlsx'
xl = pd.ExcelFile(file)

df1 = xl.parse('ActivosCorrientes')
df2 = xl.parse('ActivosNoCorrientes')
df3 = xl.parse('PasivosCorrientes')
df4 = xl.parse('PasivosNoCorrientes')
df5 = xl.parse('Patrimonio')
df6 = xl.parse('EERR')

def evaluate(df, header, text):
    sim = []
    text = clean_utils.correctText(text)
    
    nlp = spacy.load('es')
    doc1 = nlp(text)
    for element in df:
        doc2 = nlp(element.lower().strip())
        sim.append(doc1.similarity(doc2))
        if (doc1.similarity(doc2) == 1.0):
            break
    return max(sim)

def matchCell(group, text):

    if( group == 0):
        group = []
        value = []
        for x in df1:
            dataframe = df1[x].dropna(how='all')
            group.append(x)
            tmp = evaluate(dataframe, x, text)
            value.append(tmp)
            if (tmp == 1.0):
                break
        return group[value.index(max(value))]

    elif( group == 1):
        group = []
        value = []
        for x in df2:
            dataframe = df2[x].dropna(how='all')
            group.append(x)
            tmp = evaluate(dataframe, x, text)
            value.append(tmp)
            if (tmp == 1.0):
                break
        return group[value.index(max(value))]
    
    elif( group == 2):
        group = []
        value = []
        for x in df3:
            dataframe = df3[x].dropna(how='all')
            group.append(x)
            tmp = evaluate(dataframe, x, text)
            value.append(tmp)
            if (tmp == 1.0):
                break
        return group[value.index(max(value))]
    
    elif( group == 3):
        group = []
        value = []
        for x in df4:
            dataframe = df4[x].dropna(how='all')
            group.append(x)
            tmp = evaluate(dataframe, x, text)
            value.append(tmp)
            if (tmp == 1.0):
                break
        return group[value.index(max(value))]
    
    elif( group == 4):
        group = []
        value = []
        for x in df5:
            dataframe = df5[x].dropna(how='all')
            group.append(x)
            tmp = evaluate(dataframe, x, text)
            value.append(tmp)
            if (tmp == 1.0):
                break
        return group[value.index(max(value))]

    elif( group == 5):
        group = []
        value = []
        for x in df6:
            dataframe = df6[x].dropna(how='all')
            group.append(x)
            tmp = evaluate(dataframe, x, text)
            value.append(tmp)
            if (tmp == 1.0):
                break
        return group[value.index(max(value))]