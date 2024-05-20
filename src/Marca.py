from src.ConexionBD import miconexion
import json

class Marca():
    def __init__(self,id_marca,marca):
        self.marca=marca
        self.id_marca=id_marca

def getMarca():
    try:
        connection=miconexion()
        cursor=connection.cursor()
        cursor.execute("Select * from Marca")
        rows=cursor.fetchall()
        data = []
        #columns = [column[0] for column in cursor.description]
        #data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        print("sacando resultado de la tabla")
        for row in rows:
            data.append({'id': row[0], 'marca':row[1]})
        
        #print("OK")
        #json_data = json.dumps({'Marcas':data})
        return(data)
    except Exception as ex:
        return(ex)

def getallModeloMarca():
    try:
        connection=miconexion()
        cursor=connection.cursor()
        cursor.execute("select a.marca,b.modelo_tecnico,b.modelo_comercial from [dbo].[Marca] as a,[dbo].[Modelo] as b where a.id_marca=b.id_marca;")
        rows=cursor.fetchall()
        data = []
        #columns = [column[0] for column in cursor.description]
        #data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for row in rows:
            data.append({'marca': row[0], 'modelo_tecnico':row[1], 'modelo_comercial':row[2]})
        #print(rows)
        #print("OK")
        #json_data = json.dumps(data)
        connection.close()
        return(data)
    except Exception as ex:
        return(ex)


