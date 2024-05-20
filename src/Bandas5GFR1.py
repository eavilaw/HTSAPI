from ConexionBD import miconexion
import json

def insert5GFR1(serie, path):
    fr1_bands = {
        'bandNR = (1)': '[n1]',
        'bandNR = (7)': '[n7]',
        'bandNR = (40)': '[n40]',
        'bandNR = (66)': '[n66]',
        'bandNR = (71)':'[n71]',
        'bandNR = (78)':'[n78]'
    }

     

    fr1_status = {band: 'Not supported' for band in fr1_bands.values()}

    with open(path) as json_data:
        data = json.load(json_data)

    for x in data.get('5G NR', []):
        if x.get('RAT Name') == '5G NR':
            try:
                for y in x.get('Bands', []):
                    if y in fr1_bands:
                        fr1_status[fr1_bands[y]] = 'Activated'
            except:
                pass

    connection = miconexion()
    cursor = connection.cursor()

    sql = ("INSERT INTO [dbo].[Bandas-5G_FR1] "
           "([id_especificacion],[n1],[n7],[n40],[n66],[n71],[n78]) "
           "VALUES (?, ?, ?, ?, ?, ?, ?)")

    values = [str(serie)] + list(fr1_status.values())

    cursor.execute(sql, values)
    connection.commit()
    connection.close()