# coding=utf-8
#l el servicio se levanta por defecto puerto 8080
#   python webService1.py
import web
import json

urls = (
    '/autos(/.*)?', 'autos',
)

application = web.application(urls, globals()).wsgifunc()

class autos:
    autos= { 
            10: {"Auto1", "50000"},
            11: {"Auto2", "60000"},
            12: {"Auto3", "40000"},
            13: {"Auto4", "55000"},
            14: {"Auto5", "65000"},
            15: {"Auto6", "54000"},
            16: {"Auto7", "25000"},
            17: {"Auto8", "72000"},
            18: {"Auto9", "61000"},
            19: {"Auto10", "59000"} 
            }

    codes = { 400 : '400 Bad Request',
              404 : '404 Not Found',
              405 : '405 Method Not Allowed',
              409 : '409 Conflict'
              }
    def _init_(self):
        web.header('Content-Type', 'application/json', unique=True)

    def GET(self, auto=None):
        try:
            columns = [ 'codigo', 'nombre', 'precio' ]
            if auto is None:
                output = []
                for i,v in self.autos.items():
                    output.append(dict(zip(columns, [i] + list(v))))
            else:
                auto = int(auto[1:])
                
                if self.autos[auto] is None:
                    raise web.HTTPError(self.codes[404], data="Error: " +"no se encuentra el auto"+"\n")
                else:
                    output = []
                    output.append(dict(zip(columns, [auto] + list(self.autos[auto]))))

            return json.dumps(output, ensure_ascii=False)
        except Exception as e:
            msg, code = e.args if len(e.args)==2 else (e.args, 404)
            raise web.HTTPError(self.codes[code], data="Error: "+"no se encuentra el auto" +"\n")


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()