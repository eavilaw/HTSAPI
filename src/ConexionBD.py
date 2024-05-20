import pyodbc

def miconexion ():
    try:
        connection=pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=MetricasAmx;UID=sa;PWD=Zfd2t7@82')
        return connection
        
    except Exception as ex:
        #return(ex)
        print('NOOK a la BD')

