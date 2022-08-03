from xmlrpc.client import ServerProxy

# Se crea un proxy para establecer una comunicación con el servidor
proxy = ServerProxy('http://localhost:3000')

if __name__ == '__main__':
    # Se llaman los procedimientos
    print(proxy.listar_productos())
    print(proxy.listar_productos_categorias('camisa'))


