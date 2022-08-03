from xmlrpc.server import SimpleXMLRPCServer
import os

# Se crea el servidor con la libreria xmlrpc.server
server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

# Se listan los productos
productos = {'camisa': ['camisa hombre', 'camisa mujer','camisa de cuadros', 'franela estampada'],
'short': ['short marron', 'short negro', 'short azul'], 'hogar': ['Cera','Esponja','Cubiertos']}

# Una función o proceso para devolver todos los productos
def listar_productos():
    return productos

# Una función o proceso para devolver todos los productos de una categoria
def listar_productos_categorias(categoria):
    if categoria in productos.keys():
        return productos.get(categoria)
    else:
        return "no hay productos en esta categoria"

# Se registran los procesos
server.register_function(listar_productos)

server.register_function(listar_productos_categorias)

if __name__ == '__main__':
    try:
        print('serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')