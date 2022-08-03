import Pyro4, sys, gc
proxy = Pyro4.Proxy("PYRONAME:rmi.procesos")    # use name server object lookup uri shortcut

print(gc.get_count())
print(sys.getrefcount(proxy))

name, apellido = input("¿Cual es tu nombre y tu apellido? (ingresalos en una misma linea separados por un solo espacio)").split(' ')
print(proxy.saludo(name, apellido))

a,b = input("Ingresa 2 valores 'a', 'b' separados por un espacio para restarlos ").split(' ')
print(proxy.resta(a,b))

# se borra la variable que almacena proxy
del proxy
# Obtenemos la cantidad de objetos en memoria teniendo una clasificación por generaciones
print(gc.get_count())
# Corremos un proceso de limpieza y nos deshacemos de una gran cantidad de objetos
print(gc.collect())
# Volvemos a obtener la cantidad de objetos en memoria
print(gc.get_count())
# El colector de basura de python es eficiente y una vez borrado la variable tambien elimina la referencia por lo cual la siguiente linea
# devuelve error ya que tampoco no hay otros apuntadores locales que creen un ciclo de referencia
print(sys.getrefcount(proxy))

