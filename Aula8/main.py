from cachorro import Cachorro
from gato import Gato
from passaro import Passaro

# Criando objetos e utilizando métodos
cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mia", 2, "Branco")
passaro = Passaro("Piu-Piu", 1, "Canario")

cachorro.emitir_som()
gato.emitir_som()
passaro.emitir_som()
