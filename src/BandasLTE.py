from ConexionBD import miconexion
import json

def insertLTE(serie, path):
    lte_bands = {
        'bandEUTRA = (1)': '1',
        'bandEUTRA = (2)': '2',
        'bandEUTRA = (3)': '3',
        'bandEUTRA = (4)': '4',
        'bandEUTRA = (5)': '5',
        'bandEUTRA = (7)': '7',
        'bandEUTRA = (8)': '8',
        'bandEUTRA = (12)': '12',
        'bandEUTRA = (13)': '13',
        'bandEUTRA = (17)': '17',
        'bandEUTRA = (28)': '28',
        'bandEUTRA = (38)': '38',
        'bandEUTRA = (40)': '40',
        'bandEUTRA = (41)': '41',
        'bandEUTRA = (46)': '46',
        'bandEUTRA = (48)': '48',
        'bandEUTRA = (66)': '66',
        'bandEUTRA = (71)': '71'
    }

    lte_status = {band: 'Not supported' for band in lte_bands.values()}

    with open(path) as json_data:
        data = json.load(json_data)

    for x in data.get('Summary', []):
        if x.get('RAT Name') == 'LTE':
            try:
                for y in x.get('Bands', []):
                    if y in lte_bands:
                        lte_status[lte_bands[y]] = 'Activated'
            except Exception as e:
                pass

    connection = miconexion()
    cursor = connection.cursor()

    sql = ("INSERT INTO [dbo].[Bandas-LTE] "
           "([id_especificacion], [1], [2], [3], [4], [5], [7], [8], [12], [13], [17], [28], [38], [40], [41], [46], [48], [66], [71]) "
           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

    values = [str(serie)] + list(lte_status.values())

    cursor.execute(sql, values)
    connection.commit()
    connection.close()
