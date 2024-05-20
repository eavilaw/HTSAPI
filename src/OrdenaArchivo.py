import os
import shutil
from src.ConexionBD import miconexion
from src.ReadExcel import ReadExcel

def ordenararchivo():
    djson=os.getcwd()+'//Json//'
    dexcel=os.getcwd()+'//Excel//'
    path= os.getcwd()+'//Files//'
    files = os.listdir(path)

    for f in files:
        
        nombre_archivo, extension = os.path.splitext(f)
        if(extension=='.xlsx'):
            shutil.move(path+f,dexcel+f )    
        elif(extension=='.json'):
            shutil.move(path+f,djson+f )
    ReadExcel()
