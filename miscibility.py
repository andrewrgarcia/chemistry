# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:59:40 2019

@author: garci
"""
import pandas

'CHANGE TO PATH WHERE CSV FILE IS KEPT'
path =r'C:\Users\garci\Dropbox (Personal)\scripts\chemistry\miscibility.csv'

df = pandas.read_csv(path)
print('MISCIBILITY STATUS RETRIEVAL FROM CHART*',\
      '\nAndrew Garcia 2019','\n*Chart values obtained from:',\
      'http://www.scharlab.com/tabla-reactivos-mezclabilidad.php')

def determine(i1,i2):
    i1= int(i1)
    i2=int(i2)
    
    name1 = df.iloc[i1][0]
    name2 = df.iloc[i2][0]
    
    
    str1 = name1 + ' and ' + name2 + ' are '
    
    if df[name1][i2] == 0 or df[name1][i2] == 1:
        display = str1+'miscible' if df[name1][i2] == 1 else str1+'immiscible' \
        if df[name1][i2] == 1 else None
    else:
        dft = df.transpose()
        display = str1+'miscible' if dft[i1][name2] == 1 else str1+'immiscible' \
        if dft[i1][name2] == 1 else None
    
    print()
    print(display)
    
print(df['Name'])      
i1=input('Choose first solvent (type index number): ')
i2=input('Choose second solvent (type index number): ')

determine(i1,i2)
