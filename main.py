EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2          #Definimos las variables que usaremos
number_of_layers = int(input("Introduce el número de capas que vas a preparar: "))
tiempo_transcurrido = int(input("¿Cúanto tiempo lleva en el horno?: "))

def bake_time_remaining(tiempo_transcurrido):
      return EXPECTED_BAKE_TIME - tiempo_transcurrido   #Creamos una función para calcular el tiempo de cocción restante y le decimos que nos lo devuelva


def preparation_time_in_minutes(number_of_layers):
      return number_of_layers * PREPARATION_TIME      #Creamos una función para calcular el tiempo que lleva preparar las capas y le decimos que nos lo devuelva
  

def elapsed_time_in_minutes(number_of_layers, tiempo_transcurrido):
  return preparation_time_in_minutes(number_of_layers) + EXPECTED_BAKE_TIME   #Creamos una última función que nos devuelva el tiempo de preparación


#Creamos una condición para que el código te diga los datos siempre que el tiempo en el horno sea menor al tiempo esperado
if tiempo_transcurrido<EXPECTED_BAKE_TIME:
#A continuación imprimimos los datos necesarios relacionados con el tiempo
  print(f"\nNecesitas {preparation_time_in_minutes(number_of_layers)} minutos para   prepararla")
  print(f"El tiempo de preparación total es de {elapsed_time_in_minutes(number_of_layers,tiempo_transcurrido)} minutos")
  print((f"Quedan {bake_time_remaining(tiempo_transcurrido)} minutos para sacarlo del horno\n"))

#Otra forma de poner lo de arriba
  print("El tiempo apróximado de cocción es de {} minutos, faltan {} minutos \nEl tiempo de   preparación es de {} minutos \nEl tiempo total estimado es de {} minutos".format(EXPECTED_BAKE_TIME, (EXPECTED_BAKE_TIME-tiempo_transcurrido),  (PREPARATION_TIME*number_of_layers), (EXPECTED_BAKE_TIME+(PREPARATION_TIME*number_of_layers))))
elif tiempo_transcurrido == EXPECTED_BAKE_TIME:
  print("¡Sácala del horno!")        #Si el tiempo es igual al tiempo esperado, que nos diga que vayamos a sacarla 
else:
  print("¡Se te ha quemado la comida!")      #Ponemos que si el tiempo dentro del horno es mayor al tiempo medio de cocción entonces se quema la lasagna