import pandas as pd
import openpyxl
from datetime import datetime
import os
from Certificacion import insertCertificacion
from Dispositivo import insertDispositivo
from Chipset import insertChipset
from ReadJson import jsonRead

#lee excel
now = datetime.now()
def ReadExcel():
    dexcel=os.getcwd()+'\\Excel\\'
    contenidoExcel = os.listdir(dexcel)
    df=pd.DataFrame()
    for f in contenidoExcel:
        try:
            print(dexcel+f)
            df= pd.read_excel(dexcel+f,sheet_name='Specifications', skiprows=[0,2,3],usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        except Exception as e:
            print(str(e))
            df=pd.DataFrame()
            pass
    
        Pdata=pd.DataFrame()
        Pdata=df
        if Pdata.size>0:
            try:
                Marca=Pdata['Brand'].values[0]
                ModeloTecnico=Pdata['Technical name'].values[0]
                ModeloComercial=Pdata['Commercial name'].values[0]
                Alcance='Regional'
                VersionSW=Pdata['SW Version'].values[0]
                FechaInicio=now.strftime('%d-%m-%Y')
                FechaTermino=now.strftime('%d-%m-%Y')
                TipoHW=Pdata['Device type'].values[0]
                CatLTEDL=Pdata['UE DL CAT'].values[0]
                CatLTEUL=Pdata['UE UL CAT'].values[0]
              
            except:
                Marca=f+" error"
                ModeloTecnico=f+" error"
                ModeloComercial=f+" error"
                Alcance='Regional'
                VersionSW=f
                FechaInicio=now.strftime('%d-%m-%Y')
                FechaTermino=now.strftime('%d-%m-%Y')
                TipoHW=f +" error"
                CatLTEDL=0
                CatLTEUL=0
                TIER=0
                MarcaChipset=f +" error"
                ModeloChipset=f+" error"
            try:
                if(CatLTEDL>=17):
                    TIER='Premium'
                elif(CatLTEDL>=11 and CatLTEDL<=16):
                    TIER='Hight'
                elif(CatLTEDL>=10 and CatLTEDL<=5):
                    TIER='Medium'
                elif(CatLTEDL<=4):
                    TIER='Low'
            except:
                TIER=0



            df= pd.read_excel(dexcel+'/'+f,sheet_name='Specifications', skiprows=[0,1,2],usecols=[36,37])
            Pdata=pd.DataFrame()
            Pdata=df
            try:
                MarcaChipset=Pdata['Brand'].values[0]
                ModeloChipset=Pdata['Model'].values[0]
            except:
                MarcaChipset=f+" error"
                ModeloChipset=f+ " error"
        else:
            Marca=f +" error"
            ModeloTecnico=f +" error"
            ModeloComercial=f +" error"
            Alcance='Regional'
            VersionSW=f +" error"
            FechaInicio=now.strftime('%d-%m-%Y')
            FechaTermino=now.strftime('%d-%m-%Y')
            TipoHW=f +" error"
            CatLTEDL=0
            CatLTEUL=0
            TIER=0
            MarcaChipset=f +" error"
            ModeloChipset=f+" error"
        salida= [Marca,ModeloTecnico,ModeloComercial,Alcance,VersionSW,FechaInicio,FechaTermino,TipoHW,MarcaChipset,ModeloChipset,CatLTEDL,CatLTEUL,TIER]
        dispositivo=insertDispositivo(salida)
        chipset=insertChipset(salida)
        id_certificacion =insertCertificacion(salida,dispositivo,chipset)
        jsonRead(id_certificacion,f)

ReadExcel()
