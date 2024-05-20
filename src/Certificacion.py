from ConexionBD import miconexion

import datetime

class Certificacion:
    
    def __init__(self,id_modelo,modelo_tecnico,modelo_comercial):
        self.id_modelo=id_modelo
        self.modelo_tecnico=modelo_tecnico
        self.modelo_comercial=modelo_comercial
        self.id_marca

####consultas#####
def getCertificacionAll():
    try:
        
        connection=miconexion()
        cursor=connection.cursor()
        cursor.execute("SELECT b.[nombre]"+
                            ",[año]"+
                            ",[serie]"+
                            ",c.[marca]"+
	                        ",c.[modelo_tecnico]"+
                            ",c.[modelo_comercial]"+
                            ",a.[alcance]"+
                            ",a.[version_sw]"+
                            ",a.[fecha_inicio_lab]"+
                            ",a.[fecha_final_lab]"+
	                        ",c.tipo_hw"+
                            ",d.marca"+
	                        ",d.modelo"+
                            ",a.[cat_lte_dl]"+
                            ",a.[cat_lte_ul]"+
                            ",a.[tier]"+
                        " FROM [MetricasAmx].[dbo].[Certificacion] as a,"+
	                        " [MetricasAmx].[dbo].[Lab] as b,"+
	                        " [MetricasAmx].[dbo].[Dispositivo] as c,"+
	                        " [MetricasAmx].[dbo].[Chipset] as d"+
                        " where  a.[id_lab]=b.[id_lab]"+
                        " and c.[id_dispositivo]=a.id_dispositivo"+
                        " and d.[id_chipset]=a.[id_chipset]")
        
        
        rows=cursor.fetchall()
        data = []
        #columns = [column[0] for column in cursor.description]
        #data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for row in rows:
            data.append({'LAB': row[0],'Fecha':row[1],'Serie':row[2],'Marca':row[3],'Modelo_Tecnico':row[4],'Modelo_Comercial':row[5],
                         'Alcance':row[6],'Version_SW':row[7],
                         'Fecha_Inicio_Lab':row[8],'Fecha_Final_Lab':row[9],'Tipo_HW':row[10],'Marca_Chipset':row[11],'Modelo_Chipset':row[12],
                         'CAT_LTE_DL':row[13],'CAT_LTE_UL':row[14],'TIER':row[15]
                         })

        if(len(data)==0):
            data=None
            print(data)
        return(data)
    except Exception as ex:
        return(ex)

def getCertificacion(id_marca, id_modelo):
    try:
        
        connection=miconexion()
        cursor=connection.cursor()
        if(id_marca==0 and id_modelo==0):
            cursor.execute("select "+
	                    "c.lab,"+
	                    "c.fecha,"+
	                    "c.id_certificacion,"+
	                    "m.marca,"+
                        "mo.modelo_tecnico,"+
	                    "mo.modelo_comercial,"+
	                    "c.version_sw,"+
	                    "c.fecha_ini,"+
	                    "c.fecha_fin,"+
	                    "t.tipo_hw,"+
	                    "mc.marca_chipsaet,"+
	                    "ch.nombre_chipset,"+
	                    "c.cat_lte_dl,"+
	                    "c.cat_lte_dl,"+
	                    "c.tier"+
                        " from Certificacion as c,"+
	                        " Marca as m,"+
	                        " Modelo as mo,"+
	                        " Tipo_hardware as t,"+
	                        " Marca_chipset as mc,"+
	                        " Chipset as ch"+
                        " where"+
	                        " m.id_marca=mo.id_marca"+
                            " and mo.id_modelo=c.id_modelo"+
                            " and c.id_tipo_hw=t.id_tipo_hw"+
                            " and ch.id_chipset=c.id_chipset"+
                            " and ch.id_marca_chipset=mc.id_marca_chipset")
        
        elif(id_marca>=1 and id_modelo>=1):
            sql="select"+" c.lab,"+" c.fecha,"+" c.id_certificacion,"+" m.marca,"+"mo.modelo_tecnico,"+" mo.modelo_comercial,"+" c.version_sw,"+" c.fecha_ini,"+" c.fecha_fin,"+" t.tipo_hw,"+" mc.marca_chipsaet,"+" ch.nombre_chipset,"+" c.cat_lte_dl,"+" c.cat_lte_dl,"+" c.tier"+" from Certificacion as c,"+" Marca as m,"+" Modelo as mo,"+" Tipo_hardware as t,"+" Marca_chipset as mc,"+" Chipset as ch"+" where"+" m.id_marca=mo.id_marca and mo.id_modelo=c.id_modelo and c.id_tipo_hw=t.id_tipo_hw"+" and ch.id_chipset=c.id_chipset"+" and ch.id_marca_chipset=mc.id_marca_chipset and mo.id_marca="+str(id_marca)+" and mo.id_modelo="+str(id_modelo)
            print(sql)
            cursor.execute(sql)
        elif(id_marca>=1 and id_modelo==0):
            sql="select"+" c.lab,"+" c.fecha,"+" c.id_certificacion,"+" m.marca,"+"mo.modelo_tecnico,"+" mo.modelo_comercial,"+" c.version_sw,"+" c.fecha_ini,"+" c.fecha_fin,"+" t.tipo_hw,"+" mc.marca_chipsaet,"+" ch.nombre_chipset,"+" c.cat_lte_dl,"+" c.cat_lte_dl,"+" c.tier"+" from Certificacion as c,"+" Marca as m,"+" Modelo as mo,"+" Tipo_hardware as t,"+" Marca_chipset as mc,"+" Chipset as ch"+" where"+" m.id_marca=mo.id_marca and mo.id_modelo=c.id_modelo and c.id_tipo_hw=t.id_tipo_hw"+" and ch.id_chipset=c.id_chipset"+" and ch.id_marca_chipset=mc.id_marca_chipset and mo.id_marca="+str(id_marca)
            print(sql)
            cursor.execute(sql)
        rows=cursor.fetchall()
        data = []
        #columns = [column[0] for column in cursor.description]
        #data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for row in rows:
            data.append({'LAB': row[0],'Fecha':row[1],'Serie':row[2],'Marca':row[3],'Modelo_Tecnico':row[4],'Modelo_Comercial':row[5],
                         'Modelo_Comercial':row[6],'Version_SW':row[7],'Fecha_Inicio_Lab':row[8],'Fecha_Final_Lab':row[9],
                         'Tipo_HW':row[10],'Marca_Chipset':row[11],'Modelo_Chipset':row[12],
                         'CAT_LTE_DL':row[13],'CAT_LTE_UL':row[14],'TIER':row[15]
                         })

        if(len(data)==0):
            data=None
            print(data)
        return(data)
    except Exception as ex:
        return(ex)
    
def insertCertificacion(entrada,dispositivo,chipset):
    connection=miconexion()
    cursor=connection.cursor()
    
    print(dispositivo)
    print(chipset)
    ano=datetime.datetime.now().year
    fecha_inicio = datetime.datetime.now().strftime('%Y-%m-%d')
    fecha_fin = datetime.datetime.now().strftime('%Y-%m-%d')
    sql = ("INSERT INTO [dbo].[Certificacion] "
       "([id_lab], [año], [id_dispositivo], [alcance], [version_sw], "
       "[fecha_inicio_lab], [fecha_final_lab], [id_chipset], "
       "[cat_lte_dl], [cat_lte_ul], [tier]) "
       "VALUES "
       "("+"'"+str(1)+"',"+"'"+str(ano)+"',"+"'"+str(dispositivo)+"',"+"'"+str(entrada[3])+"',"+"'"+str(entrada[4])+"',"+"'"+fecha_inicio+"',"
       +"'"+fecha_fin+"',"+"'"+str(chipset)+"',"+"'"+str(entrada[10])+"',"+"'"+str(entrada[11])+"',"+"'"+str(entrada[12])+"'"+")")
    
    
    cursor.execute(sql)
    cursor.commit()
    cursor.execute("SELECT MAX([serie]) AS valor_maximo FROM Certificacion")
    rows=cursor.fetchall()
    connection.close()
    return(rows[0][0])

