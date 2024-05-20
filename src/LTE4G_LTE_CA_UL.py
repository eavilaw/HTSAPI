import json
from ConexionBD import miconexion

def insertLTECAUL(serie, path):
    with open(path) as json_data:
        data = json.load(json_data)

# Initialize a dictionary to store UL_CA flags
    supported_bands = {
        "CA_7A-28A": '[CA_7A-28A_UL]',
        "CA_3A-7A": '[CA_3A-7A_UL]',
        "CA_3A-28A": '[CA_3A-28A_UL]',
        "CA_7CL": '[7C_UL]',
        "CA_12A_66A": '[CA_12A-66A_UL]',
        "CA_5A_12A": '[CA_5A-12A_UL]',
        "CA_48C": '[CA_48C_UL]',
        "CA_48A_66A": '[CA_48A-66A_UL]',
        "CA_40C": '[CA_40C_UL]',
        "CA_3A_40A": '[CA_3A-40A_UL]',
        "CA_1A_3A": '[CA_1A-3A_UL]',
        "CA_4A_7A": '[CA_4A-7A_UL]',
        "CA_5A_7A": '[CA_5A-7A_UL]',
        "CA_4A_5A": '[CA_4A-5A_UL]',
        "CA_3C": '[CA_3C_UL]',
        "CA_2A_4A": '[CA_2A-4A_UL]',
        "CA_4A_28A": '[CA_4A-28A_UL]',
        "CA_LAA": '[LAA]'
    }
    supported_bands_status = {band: 'Not supported' for band in supported_bands.values()}

    for ca in data['LTE CA']:
        if ca['UL_CA'] in supported_bands:
            supported_bands_status[supported_bands[ca['UL_CA']]] = 'Activated'

    connection = miconexion()
    cursor = connection.cursor()

    sql = ("INSERT INTO [dbo].[4G_LTE-LTE_CA_UL]"
           " ([id_especificacion], " + ", ".join(supported_bands.values()) + ")"
           " VALUES (?, " + ", ".join(["?"] * len(supported_bands)) + ")")

    cursor.execute(sql, (serie, ) + tuple(supported_bands_status.values()))
    connection.commit()
    connection.close()