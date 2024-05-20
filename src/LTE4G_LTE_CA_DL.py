import json
from ConexionBD import miconexion

def insertLTECADL(serie, path):
    with open(path) as json_data:
        data = json.load(json_data)

    supported_bands = {
        'CA_4A-28A': '[CA_4A-28A_DL]',
        'CA_2A-4A': '[CA_2A-4A_DL]',
        'CA_2A-4A-28A': '[CA_2A-4A_28A_DL]',
        'CA_7A-28A': '[CA_7A-28A_DL]',
        'CA_3A-7A-28A': '[CA_3A-7A-28_DL]',
        'CA_3A-7A': '[CA_3A-7A_DL]',
        'CA_3A-28A': '[CA_3A-28A_DL]',
        'CA_1A-3A-7A': '[CA_1A-3A-7A_DL]',
        'CA_1A-3A-7A-28A': '[CA_1A-3A-7A-28A_DL]',
        'CA_1A-7A-28A': '[CA_1A-7A-28A_DL]',
        'CA_1A-3A': '[CA_1A-3A_DL]',
        'CA_4C': '[CA_4C_DL]',
        'CA_3A-40A': '[CA_3A-40A_DL]',
        'CA_2A-7A': '[CA_2A-7A_DL]',
        'CA_2A-28A': '[CA_2A-28A_DL]',
        'CA_7A-7A': '[CA_7A-7A_DL]',
        'CA_2A-7A-7A': '[CA_2A-7A-7A_DL]',
        'CA_7C': '[CA_7C_DL]',
        'CA_2A-7C': '[CA_2A-7C_DL]',
        'CA_7C-28A': '[CA_7C-28A_DL]',
        'CA_1A-3C': '[CA_1A-3C_DL]',
        'CA_4A-7C': '[CA_4A-7C_DL]',
        'CA_2C': '[CA_2C_DL]',
        'CA_4A-7A': '[CA_4A-7A_DL]',
        'CA_4A-5A': '[CA_4A-5A_DL]',
        'CA_28C': '[CA_28C_DL]',
        'CA_7A-28A-38A': '[CA_7A-28A-38A_DL]',
        'CA_2A-7A-28A': '[CA_2A-7A-28A_DL]',
        'CA_2A-7C-28A': '[CA_2A-7C-28A_DL]',
        'CA_66A-66A': '[CA_66A-66A_DL]',
        'CA_12A-66A-66A': '[CA_12A-66A-66A_DL]',
        'CA_12A-66A': '[CA_12A-66A_DL]',
        'CA_5A-41A': '[CA_5A-41A_DL]',
        'CA_5A-12A-66A': '[CA_5A-12A-66A_DL]',
        'CA_41A-48A': '[CA_41A-48A_DL]',
        'CA_48C-66A-66A': '[CA_48C-66A-66A_DL]',
        'CA_5A-48D-66A-66A': '[CA_5A-48D-66A-66A_DL]',
        'CA_48C-48D': '[CA_48C-48D_DL]',
        'CA_48E': '[CA_48E_DL]'
    }

    supported_bands_status = {band: 'Not supported' for band in supported_bands.values()}

    for ca in data['LTE CA']:
        if ca['DL_CA'] in supported_bands:
            supported_bands_status[supported_bands[ca['DL_CA']]] = 'Activated'

    connection = miconexion()
    cursor = connection.cursor()

    sql = ("INSERT INTO [dbo].[4G_LTE-LTE_CA_DL]"
           " ([id_especificacion], " + ", ".join(supported_bands.values()) + ")"
           " VALUES (?, " + ", ".join(["?"] * len(supported_bands)) + ")")

    cursor.execute(sql, (serie, ) + tuple(supported_bands_status.values()))
    connection.commit()
    connection.close()