from ConexionBD import miconexion
import pandas as pd

def insertChipset(entrada):
    connection=miconexion()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM [MetricasAmx].[dbo].[Chipset]")
    rows=cursor.fetchall()
    df= pd.DataFrame(rows)
    valmarca=False
    valmodelo=False
    idchipset=0

    for i in df.values:
        if entrada[8]  == i[0][1]:
            valmarca=True 
        if entrada[9] == i[0][2]:
            valmodelo=True

    
    if valmarca is False or valmodelo is False:
        cursor.execute("INSERT INTO [dbo].[Chipset]"+
           " ([marca]"+
           ",[modelo])"+
         " VALUES "+
           "("+"'"+str(entrada[8])+"',"+
           "'"+str(entrada[9])+"')")
        cursor.commit()
    sql="SELECT * FROM [MetricasAmx].[dbo].[Chipset] where [marca]="+"'"+entrada[8]+"'"+" and [modelo]="+"'"+str(entrada[9])+"'"
    cursor.execute(sql)
    rows=cursor.fetchall()
    idchipset=rows[0][0]
    connection.close()
    return(idchipset)