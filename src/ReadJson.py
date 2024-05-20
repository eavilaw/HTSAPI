import pandas as pd
import json
import os
from BandasGSM import insertGSM
from BandasWCDMA import insertWCDMA
from BandasLTE import insertLTE
from Bandas5GFR1 import insert5GFR1
from Bandas5GFR2 import insert5GFR2
from lteMimo4x4 import insertget4glte
from LTE4G_LTE_CA_DL import insertLTECADL
from LTE4G_LTE_CA_UL import insertLTECAUL

def jsonRead(serie,namefile):
    djson=os.getcwd()+'\\Json\\'
    contenidoJson = os.listdir(djson)
    
    for f in contenidoJson:
        jsonfile=f.split(".")
        nameexcel=namefile.split(".")
        if(jsonfile[0]==nameexcel[0]):
            insertGSM(serie,djson+f)
            insertWCDMA(serie,djson+f)
            insertLTE(serie,djson+f)
            insert5GFR1(serie,djson+f)
            insert5GFR2(serie,djson+f)
            insertget4glte(serie,djson+f)
            insertLTECADL(serie,djson+f)
            insertLTECAUL(serie,djson+f)