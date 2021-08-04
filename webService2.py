
#levantar el servicio en el puerto 8000
#   python webService2.py 8000
import requests,web


def obtData():   #consumo el servicio del WS1
    url='http://localhost:8080/autos'
    response=requests.get(url)
    response=response.json()
    return response
   
def obtPrecio():
    data=obtData()
    precios=[]
    for item in data:
        precios.append(item["precio"])
    return precios
    
def toTemplate(precio):
  
    if precio == "mayor":
        auto= mayor()
             
    elif precio == "menor":
        auto= menor()
             
    return auto
   

def mayor():
    data=obtData()
    pmax=max(obtPrecio())
    for auto in data :
        if pmax == auto["precio"] :
            return auto

def menor():
    data=obtData()
    pmin=min(obtPrecio())
    for auto in data :
        if pmin == auto["precio"] :
            return auto
    


urls = (
    '/consume(/.*)?', 'consume',
)

application = web.application(urls, globals())

class consume:
    auto={}
    codes = { 400 : '400 Bad Request',
            404 : '404 Not Found',
            405 : '405 Method Not Allowed',
            409 : '409 Conflict'
            }
    def GET (self,auto =None):
            
            return obtData()#retornamos la data consumida del WS1

    def POST (self,dato=None):
       
        if dato is not None:
            raise web.HTTPError(self.codes[404], data="Error: " +"no permitido"+"\n")

        input = web.input(precio=None) #input diccionario con los valores que envian el cliente
        if not input['precio']:
           raise web.HTTPError(self.codes[404], data="Error: " +"no señalo filtro"+"\n")
        
        self.auto=toTemplate(input['precio'])#devolvemos el auto que se solicita de precio mayor o menor
        
        return self.auto
        
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()