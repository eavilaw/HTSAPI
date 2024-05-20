from src.ConexionBD import miconexion
import json
class Modelo:
    
    def __init__(self,id_modelo,modelo_tecnico,modelo_comercial):
        self.id_modelo=id_modelo
        self.modelo_tecnico=modelo_tecnico
        self.modelo_comercial=modelo_comercial
        self.id_marca

####consultas#####
def getModelo(id_marca):
    try:
        connection=miconexion()
        cursor=connection.cursor()
        cursor.execute("Select * from Modelo where id_marca="+"'"+id_marca+"'")
        rows=cursor.fetchall()
        data = []
        #columns = [column[0] for column in cursor.description]
        #data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for row in rows:
            data.append({'id': row[0], 'modelo':row[2]})
        #print(rows)
        #print("OK")
        #json_data = json.dumps(data)
        connection.close()
        return(data)
    except Exception as ex:
        return(ex)


