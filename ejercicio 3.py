listanombre= []
listalargo= []
listatripulacion= []
listacantidadpasajeros= []
listageneral= []
class Starwars:
    def __init__(self, nombre, largo, tripulacion, cantidadpasajeros):
        self.nombre= nombre
        self.largo= largo
        self.tripulacion= tripulacion
        self.cantidadpasajeros= cantidadpasajeros
Halconmilenario= Starwars("Halconmilenario", 24865, 6, 873)
Estrelladelamuerte= Starwars("Estrelladelamuerte", 50765, 4, 4700)
Machupichu= Starwars("Machupichu", 17849, 5, 2876)
Lamuerte= Starwars("Lamuerte", 4566, 3, 743)
Atrapado= Starwars("Atrapado", 7654, 5, 973)
Calavera= Starwars("Calavera", 5078, 7, 470)
listacantidadpasajeros.append(Halconmilenario.cantidadpasajeros)
listacantidadpasajeros.append(Estrelladelamuerte.cantidadpasajeros)
listacantidadpasajeros.append(Machupichu.cantidadpasajeros)
listacantidadpasajeros.append(Lamuerte.cantidadpasajeros)
listacantidadpasajeros.append(Atrapado.cantidadpasajeros)
listacantidadpasajeros.append(Calavera.cantidadpasajeros)
listatripulacion.append(Halconmilenario.tripulacion)
listatripulacion.append(Estrelladelamuerte.tripulacion)
listatripulacion.append(Machupichu.tripulacion)
listatripulacion.append(Lamuerte.tripulacion)
listatripulacion.append(Atrapado.tripulacion)
listatripulacion.append(Calavera.tripulacion)
listalargo.append(Halconmilenario.largo)
listalargo.append(Estrelladelamuerte.largo)
listalargo.append(Machupichu.largo)
listalargo.append(Lamuerte.largo)
listalargo.append(Atrapado.largo)
listalargo.append(Calavera.largo)
listageneral.append(Halconmilenario)
listageneral.append(Estrelladelamuerte)
listageneral.append(Machupichu)
listageneral.append(Lamuerte)
listageneral.append(Atrapado)
listageneral.append(Calavera)

#Apartado 1
print("\nMostrando información Halcon Milenario: ")
print("\nLongitud: ",Halconmilenario.largo)
print("\nTripulacion: ",Halconmilenario.tripulacion)
print("\nCantidad de pasajeros: ",Halconmilenario.cantidadpasajeros)

print("\nMostrando información Estrella de la Muerte: ")
print("\nLongitud: ",Estrelladelamuerte.largo)
print("\nTripulacion: ",Estrelladelamuerte.tripulacion)
print("\nCantidad de pasajeros: ",Estrelladelamuerte.cantidadpasajeros)

#Apartado 2
listacantidadpasajeros.sort(reverse = True)
print(listacantidadpasajeros)
for i in range(5):
    print(listacantidadpasajeros[i])
print("Como podemos observar, las naves con mayor cantidad de pasajeros son, Estrella de la Muerte, Machupichu, Atrapado, Halcon Milenario y La Muerte")

#Apartado 3
listatripulacion.sort(reverse = True)
print(listatripulacion[0])
print("La nave con mayor tripulacion es Calavera")

#Apartado 4


#Apartado 5
listalargo.sort(reverse= True)
print("\nLa nave con mayor longitud es la Estrella de la Muerte con una longitud de : ",listalargo[-1])







