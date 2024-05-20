from ConexionBD import miconexion
import json

def insert5GFR2(serie, path):
    fr2_bands = {
        'bandNR = (257)': '[n257]',
        'bandNR = (258)': '[n258]',
        'bandNR = (261)': '[n261]'
    }

     

    fr2_status = {band: 'Not supported' for band in fr2_bands.values()}

    with open(path) as json_data:
        data = json.load(json_data)

    for x in data.get('5G NR', []):
        if x.get('RAT Name') == '5G NR':
            try:
                for y in x.get('Bands', []):
                    if y in fr2_bands:
                        fr2_status[fr2_bands[y]] = 'Activated'
            except:
                pass

    connection = miconexion()
    cursor = connection.cursor()

    sql = ("INSERT INTO [dbo].[Bandas-5G_FR2] "
           "([id_especificacion],[n257],[n258],[n261]) "
           "VALUES (?, ?, ?, ?)")

    values = [str(serie)] + list(fr2_status.values())

    cursor.execute(sql, values)
    connection.commit()
    connection.close()