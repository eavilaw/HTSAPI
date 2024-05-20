from ConexionBD import miconexion
import pandas as pd

def insertDispositivo(entrada):
    connection=miconexion()
    cursor=connection.cursor()
    cursor.execute("Select * from Dispositivo")
    rows=cursor.fetchall()
    df= pd.DataFrame(rows)
    valmarca=False
    valmodeloT=False
    valmodeloC=False
    iddispositivo=0
   
    for i in df.values:
        if entrada[0] == i[0][1]:
            valmarca=True # False
            
        
        if entrada[1] == i[0][2]:
            valmodeloT=True
            
        
        if entrada[2] == i[0][3]:
            valmodeloC=True
            
        
    sql="INSERT INTO [dbo].[Dispositivo]"+ " ([marca]"+",[modelo_tecnico]"+",[modelo_comercial]"+",[tipo_hw])"+" VALUES "+"("+"'"+entrada[0]+"',"+"'"+entrada[1]+"',"+"'"+entrada[2]+"',"+"'"+entrada[7]+"'"+")"
    if valmarca is False or valmodeloT is False or  valmodeloC is False:
        cursor.execute(sql)
        cursor.commit()
    
    cursor.execute("Select [id_dispositivo] from Dispositivo where [marca]="+"'"+entrada[0]+"'"+" and [modelo_tecnico]="+"'"+entrada[1]+"'"+" and [modelo_comercial]="+"'"+entrada[2]+"'")
    rows=cursor.fetchall()
    iddispositivo=rows[0][0]
    connection.close()
    return(iddispositivo)