from ConexionBD import miconexion
import pandas as pd
import json

def insertget4glte(serie, path):
    with open(path) as json_data:
        data = json.load(json_data)

    supported_bands = {
        'Band 1 = fourLayers': 'LTEMIMOB1',
        'Band 2 = fourLayers': 'LTEMIMOB2',
        'Band 3 = fourLayers': 'LTEMIMOB3',
        'Band 4 = fourLayers': 'LTEMIMOB4',
        'Band 5 = fourLayers': 'LTEMIMOB5',
        'Band 7 = fourLayers': 'LTEMIMOB7',
        'Band 8 = fourLayers': 'LTEMIMOB8',
        'Band 12 = fourLayers': 'LTEMIMOB12',
        'Band 13 = fourLayers': 'LTEMIMOB13',
        'Band 17 = fourLayers': 'LTEMIMOB17',
        'Band 28 = fourLayers': 'LTEMIMOB28',
        'Band 38 = fourLayers': 'LTEMIMOB38',
        'Band 40 = fourLayers': 'LTEMIMOB40',
        'Band 41 = fourLayers': 'LTEMIMOB41',
        'Band 46 = fourLayers': 'LTEMIMOB46',
        'Band 48 = fourLayers': 'LTEMIMOB48',
        'Band 66 = fourLayers': 'LTEMIMOB66',
        'Band 71 = fourLayers': 'LTEMIMOB71'
    }

    supported_bands_status = {}
    for band in supported_bands.values():
        supported_bands_status[band] = 'Not supported'

    for ca in data['LTE CA']:
        for capability in ca['MIMO Capabilities DL']:
            if capability in supported_bands:
                supported_bands_status[supported_bands[capability]] = 'Activated'

    connection = miconexion()
    cursor = connection.cursor()

    sql = ("INSERT INTO [dbo].[4G_LTE-LTE_MIMO4X4]"
           " ([id_especificacion],[B1],[B2],[B3],[B4],[B5],[B7],[B8],[B12],[B13],[B17],[B28],[B38],[B40]"
           ",[B41],[B46],[B48],[B66],[B71])"
           " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

    cursor.execute(sql, (serie, ) + tuple(supported_bands_status.values()))
    connection.commit()
    connection.close()



def get4glte():
    try:
        
        connection=miconexion()
        cursor=connection.cursor()
        cursor.execute("SELECT   a.id_especificacion"+
                                 ",c.marca"+
	                            ",c.modelo_comercial"+
	                            ",c.modelo_tecnico"+
                                ",[1900(2)]"+
                                ",[1800(3)]"+
                                ",[850(5)]"+
                                ",[900(8)]"+
	                            ",d.[2100(I)]"+
	                            ",d.[1900(II)]"+
	                            ",d.[1700(IV)]"+
	                            ",d.[850(V)]"+
	                            ",e.[1]"+
	                            ",e.[2]"+
	                            ",e.[3]"+
	                            ",e.[4]"+
	                            ",e.[5]"+
	                            ",e.[7]"+
	                            ",e.[8]"+
	                            ",e.[12]"+
	                            ",e.[13]"+
	                            ",e.[17]"+
	                            ",e.[28]"+
	                            ",e.[38]"+
	                            ",e.[40]"+
	                            ",e.[41]"+
	                            ",e.[46]"+
	                            ",e.[48]"+
	                            ",e.[66]"+
	                            ",e.[71]"+
	                            ",f.n1"+
	                            ",f.n7"+
	                            ",f.n40"+
	                            ",f.n66"+
	                            ",f.n71"+
	                            ",f.n78"+
	                            ",g.n257"+
	                            ",g.n258"+
	                            ",g.n261"+
                        " FROM [MetricasAmx].[dbo].[Bandas-GSM] as a,"+
	                            " [dbo].[Certificacion] as b,"+
	                            " [dbo].[Dispositivo] as c,"+
	                            " [dbo].[Bandas-WCDMA] as d,"+
	                            " [dbo].[Bandas-LTE] as e,"+
	                            " [dbo].[Bandas-5G_FR1] as f,"+
	                            " [dbo].[Bandas-5G_FR2] as g"+
                            " where a.id_especificacion=b.serie"+
                                " and b.id_dispositivo=c.id_dispositivo"+
                                " and a.id_especificacion=d.id_especificacion"+
                                " and a.id_especificacion=e.id_especificacion"+
                                " and a.id_especificacion=f.id_especificacion"+
                                " and a.id_especificacion=g.id_especificacion")
        
        
        rows=cursor.fetchall()
        data = []
        #columns = [column[0] for column in cursor.description]
        #data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for row in rows:
            data.append({'Serie': row[0],'Marca':row[1],'Modelo_Tecnico':row[2],'Modelo_Comercial':row[3],'1900(2)':row[4],'1800(3)':row[5],
                         '850(5)':row[6],'900(8)':row[7],'2100(I)':row[8],'1900(II)':row[9],'1700(IV)':row[10],'850(V)':row[11],
                         '1':row[12],'2':row[13],'3':row[14],'4':row[15],'5':row[16],'7':row[17],
                         '8':row[18],'12':row[19],'13':row[20],'17':row[21],'28':row[22],'38':row[23],
                         '40':row[24],'41':row[25],'46':row[26],'48':row[27],'66':row[28],'71':row[29],
                         'n1':row[30],'n7':row[31],'n40':row[32],'n66':row[33],'n71':row[34],'n78':row[35],
                         'n257':row[36],'n258':row[37],'n261':row[38]
                         })

        if(len(data)==0):
            data=None
            print(data)
        connection.close()
        return(data)
    except Exception as ex:
        return(ex)

