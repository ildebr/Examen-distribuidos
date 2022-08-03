# saved as Server.py
import Pyro4

# Expose es un decorador para dar a conocer que este procedmiento puede ser accedido por un cliente

@Pyro4.expose
class Procedimientos(object):
    def saludo(self, nombre, apellido):
        return "Hola, {0} {1}. Bienvenida/o".format(nombre, apellido)
    def resta(self, a, b):
        return "{0} - {1} = {2}".format(a, b, int(a)-int(b))

daemon = Pyro4.Daemon()                # Crea un daemon de Pyro
ns = Pyro4.locateNS()                  # Encuentro el nombre del servidor
uri = daemon.register(Procedimientos)   # Registra los procedimientos como un objeto PYro
ns.register("rmi.procesos", uri)   # Registra el objeto con un nombre el servidor

print("El servidor está activo")
daemon.requestLoop()                   # Inicia el loop de eventos para esperar por llamadas al servidor