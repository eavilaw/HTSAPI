from ConexionBD import miconexion
import json

def insertWCDMA(serie, path):
    wcdma_bands = {
        '2100': '2100(I)',
        '1900': '1900(II)',
        '1700': '1700(IV)',
        '850': '850(V)'
    }

    wcdma_status = {band: 'Not supported' for band in wcdma_bands.values()}

    with open(path) as json_data:
        data = json.load(json_data)

    for x in data.get('Summary', []):
        if x.get('RAT Name') == 'WCDMA':
            try:
                for y in x.get('Bands', []):
                    if y in wcdma_bands:
                        wcdma_status[wcdma_bands[y]] = 'Activated'
            except Exception as e:
                pass

    connection = miconexion()
    cursor = connection.cursor()

    sql = ("INSERT INTO [dbo].[Bandas-WCDMA] "
           "([id_especificacion], [2100(I)], [1900(II)], [1700(IV)], [850(V)]) "
           "VALUES (?, ?, ?, ?, ?)")

    values = [str(serie)] + list(wcdma_status.values())

    cursor.execute(sql, values)
    connection.commit()
    connection.close()