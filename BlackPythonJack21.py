import random
import numpy
import time
import os

#juego de cartas de blackjack 21, version completa.
#el limite de cartas es 21, si pasa eso, el jugador pierde.
#siempre se reparte 2 cartas a cada jugador.

#el juego ya tiene configurado el limite de 21 puntos para jugar, en caso q lo supere
#el juego se perdera.
#tambien se agrego si tiene 21, sera black jack ganando quien tenga ese numero.

#cosas para agregar

#falta agregar poner los numeros el q tenga mayor ganara o el que tenga menos perdera.
#agregar sistema de apuestas y dinero
#LA FUNCION RENDIRSE en caso de que se rinda, el jugador si aposto, se le dara el 50% de su
# apuesta, en caso q crea que no vaya a ganar.
#/sistema de apuestas/ 
# sistemas de excepciones
# puntuaciones de ganar y perder, sistema monetario.}
#agregar que si al lanzar cartas es mayor a 20, te pregunte si estas seguro de esta decision
#agregar que si al lanzar cartas menor a 11, te pregunte si estas seguro de esta decision.
#arreglar error de la cantidad de cartas del enemigo, ya que una vez que inicia una nueva partida

#debe de tener 2 cartas siempre, despues se le debe sumar, cada vez que añada una y cuando
#gane o pierda, se reinicie y vuelva el contador a 2.

#decidi eliminar eso y solo contabilizar la cantidad de cartas que tiene la lista de cartas del
#enemigo del jugador (paso a eliminar lo agregado) use el comando LEN (CONTABILIZA LA CANTIDAD DE ELEMENTOS EN UNA LISTA(NO LO SUMA.))

#se ha añadido para perder, en caso de que el jugador se quede sin dinero o ganar en caso que la mesa no posea mas
#fondos...

#puntos de ganar y perder ya los agregue, falta añadirle sistema de dinero y apuesta.

#SISTEMA DE APUESTAS AGREGADO

#falta añadirle que al hacer BLACK JACK ganen o pierdan dinero.
#corregido bug de que si el jugador superaba los 21, se rompia el juego. 
#agregarle mas funciones y terminar la funcion *rendirse* (se obtiene la mitad de la apuesta).
#agregarle mas decoraciones al tablero y tiempos de pausa.

#quiza agregarle advertencias

#juego al 65% 

#reparado sistema de ganar y perder, antes podias ganar muy al azar o perder en cualquier momento
# le puse mejores condiciones para que el sistema no se maree cuando tenga resultados muy similares.

#por ejemplo si ambos jugadores superaban el 21, lo daba como ganador al jugador, ahora lo da como empate.

#HASTA AHORA el juego en parte esta terminado, las 4 funciones terminadas. quizas faltaria añadirle
# mas detalles como advertencias o si ambos superan los 21 puntos pierdan. aunque como el jugador es
# el primero en tomar una carta lo haria perder a el. de todas formas el juego es jugable. falta añadir
# un menu de presentacion y como jugar...

#---------------------------------------------------------

dinero = [250]
dineroCrupier = [1340]
partida = [1]
partidasGanadas = []
partidasPerdidas = []

#---------------------------------------------------------

def sumaTotal(lista):
	suma = 0
	for elem in lista:
		suma+=elem
	return suma

def blackjack():

	jugador = 0
	cartas = [2,3,4,5,6,7,8,9,10,11]
	jugadas = []
	apuesta = [0]

# baraja del jugador / carta random 1 y 2. 

	barajaJugador = []
	carta1Random = []
	carta2Random = []

# algoritmo carta random y repartirlo a la baraja jugador

	carta1Random = numpy.random.choice(cartas)
	carta2Random = numpy.random.choice(cartas)

	barajaJugador.append(carta1Random)
	barajaJugador.append(carta2Random)

# baraja del crupier / carta random 1 y 2.

	barajaCrupier = []
	baraja1Ramdom = []
	baraja2Ramdom = []

# algoritmo carta random y repartirlo a la baraja crupier

	baraja1Ramdom = numpy.random.choice(cartas)
	baraja2Ramdom = numpy.random.choice(cartas)

	barajaCrupier.append(baraja1Ramdom)
	barajaCrupier.append(baraja2Ramdom)

# ------------------------------------------------------------
	
	while True:

		os.system("cls")
		
		try:
			if sumaTotal(barajaJugador) < 21 and sumaTotal(barajaCrupier) < 21 and sumaTotal(dinero) > 0 and sumaTotal(dineroCrupier) > 0:

				print("-------------------------")
				print("|     BLACK JACK 21     |")
				print("-------------------------")
				print(f"|     Partida(s): {sumaTotal(partida)}     |")
				print("-------------------------")
				print("|        CRUPIER        |")
				print("-------------------------")
				print(f"|Cart. en Mano Crupier: {len(barajaCrupier)}")
				print(f"|Dinero en mesa: ${sumaTotal(dineroCrupier) - sumaTotal(apuesta)}")
				print("-------------------------")
				print("+++++++++++++++++++++++++")
				print(f"+ APUESTA: ${sumaTotal(apuesta) + sumaTotal(apuesta)}           +")
				print("+++++++++++++++++++++++++")
				print("-------------------------")
				print("|        JUGADOR        |")
				print("-------------------------")
				print(f"|Dinero: ${sumaTotal(dinero) - sumaTotal(apuesta)}")
				print(f"|Mano Jugador: {barajaJugador}")
				print(f"|Suma Total: {sumaTotal(barajaJugador)}")
				print("--------------------------")
				print("| 1. TOMAR UNA CARTA")
				print("| 2. PLANTARSE")
				print("| 3. DOBLAR DINERO")
				print("| 4. RENDIRSE")
				print("--------------------------")
				print("5. SALIR")
				print("--------------------------")

				jugador = int(input("> "))

				if jugador == 1:

					os.system("cls")
					
					baraja3Random = numpy.random.choice(cartas)
					baraja4Ramdom = numpy.random.choice(cartas)

					barajaCrupier.append(baraja3Random)
					barajaJugador.append(baraja4Ramdom)

					print("Tomando carta de la baraja...")
					print("El crupier tambien toma una...")
					time.sleep(2)

				elif jugador == 2:

					os.system("cls")
					print("Decides plantarte...")
					
					if sumaTotal(barajaJugador) > sumaTotal(barajaCrupier):
						
						partidaJugada = 1
						partidaWon = 1
						partidasGanadas.append(partidaWon) 
						partida.append(partidaJugada)

						#--------------------------------------------------------
						#sistema de reparticion de ganancias... (GANA EL JUGADOR)

						ganar = sumaTotal(apuesta) + sumaTotal(dinero)
						perder = sumaTotal(dineroCrupier) - sumaTotal(apuesta)

						del dinero[0]
						del dineroCrupier[0]

						dinero.append(ganar)
						dineroCrupier.append(perder)
						#--------------------------------------------------------

						print("+++++++++++++++++++++")
						print("* JUGADOR GANA MANO +")
						print("+++++++++++++++++++++")
						print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
						print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
						time.sleep(3)
						blackjack()
						break

					elif sumaTotal(barajaJugador) < sumaTotal(barajaCrupier):
						
						partidaJugada = 1
						partidaLose = 1
						partidasPerdidas.append(partidaLose)
						partida.append(partidaJugada)

						#--------------------------------------------------------
						#sistema de reparticion de ganancias... (GANA EL CRUPIER)

						ganar = sumaTotal(apuesta) + sumaTotal(dineroCrupier)
						perder = sumaTotal(dinero) - sumaTotal(apuesta)

						del dinero[0]
						del dineroCrupier[0]

						dinero.append(perder)
						dineroCrupier.append(ganar)
						#--------------------------------------------------------

						print("+++++++++++++++++++++")
						print("+ LA MESA GANA MANO +")
						print("+++++++++++++++++++++")
						print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
						print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
						time.sleep(3)
						blackjack()
						break

					elif sumaTotal(barajaJugador) == sumaTotal(barajaCrupier):
						
						partidaJugada = 1
						partida.append(partidaJugada)

						print("+++++++++++++++++++++++++")
						print("+ EMPATE... NADIE GANA. +")
						print("+++++++++++++++++++++++++")
						print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
						print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
						print("+++++++++++++++++++++++++")
						print("----------------------------------------------")
						print("Se le devuelve el dinero a ambos jugadores...")
						print("----------------------------------------------")

						time.sleep(3)
						blackjack()
						break

				elif jugador == 3:

					os.system("cls")
					print("Ok apostemos...")
					time.sleep(1)

					#sistema de apuestas...

					if (sumaTotal(dinero) - sumaTotal(apuesta)) > 0:

						user3 = 0

						while True:

							try:

								os.system("cls")
								print("¿Cuanto dinero piensas apostar? ")
								print("(AÑADE EN NUMEROS...)")
								print(f"Tu dinero: {sumaTotal(dinero) - sumaTotal(apuesta)}")

								user3 = int(input("> "))

								if user3 < sumaTotal(dinero):

									apuestaAhora = sumaTotal(dinero) - user3

									apuesta.append(user3)

									print("+++++++++++++++++++++++")
									print(f"CANTIDAD AP. ${user3}")
									print("+++++++++++++++++++++++")
									print("El crupier tambien hace su apuesta...")

									time.sleep(2)
									break

								elif user3 == sumaTotal(dinero):

									apuestaAhora = sumaTotal(dinero) - user3

									apuesta.append(user3)

									print("+++++++++++++++++++++++")
									print(f"CANTIDAD AP. ${user3}")
									print("+++++++++++++++++++++++")
									print("El crupier tambien hace su apuesta...")

									time.sleep(2)
									break

								elif user3 > sumaTotal(dinero):

									print("ERROR: Lo lamento, estas poniendo mas dinero del que posees...")
									continue
							
							except:

								print("ERROR: Ponga solo numeros en la apuesta...")
								continue

					elif (sumaTotal(dinero) - sumaTotal(apuesta)) == 0:
						print("ERROR: no tienes mas dinero para apostar...")

				elif jugador == 4:

					os.system("cls")
					print("decides rendirte...")

					print("+++++++++++++++++++++++++++++++++++++++")
					print("+ NO OBTENDRAS NADA DE LO APOSTADO... +")
					print("+ SOLO LA MITAD...                    +")
					print("+++++++++++++++++++++++++++++++++++++++")

					time.sleep(1)
					blackjack()
					break

				elif jugador == 5:

					os.system("cls")
					print("Saliendo del juego.")

					print("++++++++++++++++++++++++++++")
					print(f"+ PARTIDAS JUGADAS: {sumaTotal(partida)}.")
					print(f"+ MANOS GANADAS: {sumaTotal(partidasGanadas)}")
					print(f"+ MANOS PERDIDAS: {sumaTotal(partidasPerdidas)}")
					print("++++++++++++++++++++++++++++")
					time.sleep(5)
					break			

				else:
					print("Numero ingresado incorrecto, ingrese los soportados por el programa.")
					continue

#jugador pierde (funciona)

			elif sumaTotal(barajaJugador) > 21 and sumaTotal(barajaCrupier) < 21:
				
				partidaJugada = 1
				partidaLose = 1

				partidasPerdidas.append(partidaLose)
				partida.append(partidaJugada)

				#--------------------------------------------------------
				#sistema de reparticion de ganancias... (GANA EL CRUPIER)

				ganar = sumaTotal(apuesta) + sumaTotal(dineroCrupier)
				perder = sumaTotal(dinero) - sumaTotal(apuesta)

				del dinero[0]
				del dineroCrupier[0]

				dinero.append(perder)
				dineroCrupier.append(ganar)
				#--------------------------------------------------------
				os.system("cls")

				print("+++++++++++++++++++++")
				print("+ LA MESA GANA MANO +")
				print("+++++++++++++++++++++")
				print("EL JUGADOR SUPERO LOS 21 PUNTOS...")
				print("--------------------------")
				print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
				print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
				print("--------------------------")

				time.sleep(1)
				blackjack()
				break

#crupier pierde... (funciona)

			elif sumaTotal(barajaCrupier) > 21 and sumaTotal(barajaJugador) < 21:
				
				partidaJugada = 1
				partidaWon = 1

				partida.append(partidaJugada)
				partidasGanadas.append(partidaWon)

				#--------------------------------------------------------
				#sistema de reparticion de ganancias... (GANA EL JUGADOR)
				#funciona

				ganar = sumaTotal(apuesta) + sumaTotal(dinero)
				perder = sumaTotal(dineroCrupier) - sumaTotal(apuesta)

				del dinero[0]
				del dineroCrupier[0]

				dinero.append(ganar)
				dineroCrupier.append(perder)
				#--------------------------------------------------------
				os.system("cls")

				print("+++++++++++++++++++++")
				print("* JUGADOR GANA MANO +")
				print("+++++++++++++++++++++")
				print("EL CRUPIER SUPERA LOS 21 PUNTOS...")
				print("--------------------------")
				print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
				print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
				print("--------------------------")

				time.sleep(1)
				blackjack()
				break

#jugador gana 

			elif sumaTotal(barajaJugador) == 21 and sumaTotal(barajaCrupier) < 21:

				partidaJugada = 1
				partidaWon = 1

				partida.append(partidaJugada)
				partidasGanadas.append(partidaWon)

				#--------------------------------------------------------
				#sistema de reparticion de ganancias... (GANA EL JUGADOR)

				ganar = sumaTotal(apuesta) + sumaTotal(dinero)
				perder = sumaTotal(dineroCrupier) - sumaTotal(apuesta)

				del dinero[0]
				del dineroCrupier[0]

				dinero.append(ganar)
				dineroCrupier.append(perder)
				#--------------------------------------------------------
				os.system("cls")

				print("----------------------------------")
				print("BLACK JACK 21. ¡¡EL JUGADOR GANA!!")
				print("----------------------------------")
				print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
				print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
				print("----------------------------------")

				time.sleep(1)
				blackjack()
				break

#crupier gana

			elif sumaTotal(barajaCrupier) == 21 and sumaTotal(barajaJugador) < 21:
				
				partidaJugada = 1
				partidaLose = 1

				partidasPerdidas.append(partidaLose)
				partida.append(partidaJugada)

				#--------------------------------------------------------
				#sistema de reparticion de ganancias... (GANA EL CRUPIER)

				ganar = sumaTotal(apuesta) + sumaTotal(dineroCrupier)
				perder = sumaTotal(dinero) - sumaTotal(apuesta)

				del dinero[0]
				del dineroCrupier[0]

				dinero.append(perder)
				dineroCrupier.append(ganar)
				#--------------------------------------------------------
				os.system("cls")

				print("----------------------------------")
				print("BLACK JACK 21. ¡¡LA MESA GANA!!")
				print("----------------------------------")
				print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
				print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
				print("----------------------------------")

				time.sleep(1)
				blackjack()
				break

			elif sumaTotal(barajaJugador) > 21 and sumaTotal(barajaCrupier) > 21:

				partidaJugada = 1
				partida.append(partidaJugada)

				print("+++++++++++++++++++++++++++")
				print("+ AMBAS MANOS SUPERAN 21. +")
				print("+++++++++++++++++++++++++++")
				print(f"TOTAL MANO JUGADOR: {sumaTotal(barajaJugador)}")
				print(f"TOTAL MANO CRUPIER: {sumaTotal(barajaCrupier)}")
				print("+++++++++++++++++++++++++")
				print("----------------------------------------------")
				print("Se le devuelve el dinero a ambos jugadores...")
				print("----------------------------------------------")

				time.sleep(2)
				blackjack()
				break

#jugador pierde o termina partida por falta de fondos.

			elif sumaTotal(dinero) <= 0:

				os.system("cls")

				print("Lo lamento, te has quedado sin dinero...")
				print("//////////////")
				print("// PIERDES. //")
				print("//////////////")

				print("++++++++++++++++++++++++++++")
				print(f"+ PARTIDAS JUGADAS: {sumaTotal(partida)}.")
				print(f"+ MANOS GANADAS: {sumaTotal(partidasGanadas)}")
				print(f"+ MANOS PERDIDAS: {sumaTotal(partidasPerdidas)}")
				print("++++++++++++++++++++++++++++")

				time.sleep(5)
				break

#jugador gana o se deja la mesa sin dinero.

			elif sumaTotal(dineroCrupier) <= 0:

				os.system("cls")
				
				print("La mesa se ha quedado sin fondos...")

				print("//////////////////////")
				print("/ FIN DE LA PARTIDA. /")
				print("//////////////////////")

				print("++++++++++++++++++++++++++++")
				print(f"+ PARTIDAS JUGADAS: {sumaTotal(partida)}.")
				print(f"+ MANOS GANADAS: {sumaTotal(partidasGanadas)}")
				print(f"+ MANOS PERDIDAS: {sumaTotal(partidasPerdidas)}")
				print("++++++++++++++++++++++++++++")
				
				time.sleep(5)
				break

		except:
			os.system("cls")
			print("Comando ingresado incorrecto, ingrese otro.")
			continue

def howto():

	os.system("cls")
	
	while True:
		try:

			good = 0

			print("Para explicar, es sencillo.")
			print("""-------------------------------------------------------------------------
Para ganar una mano: 
- requieres que la suma de tu baraja, llegue a los 21 puntos(BLACKJACK).
- que el enemigo o crupier tenga menos puntaje que tu, sin que tu hayas pasado
los 21 puntos.
- que el crupier llegue a mas de 21 puntos. 

Para perder una mano:
- Que el crupier tenga 21 puntos(BLACKJACK).
- que el jugador tenga menos puntaje en su baraja que el crupier, sin que este supere
los 21 puntos requeridos para ganar.
- que el jugador tenga MAS 21 puntos.
-------------------------------------------------------------------------""")
			print("""-------------------------------------------------------------------------
EL JUEGO POSEE 4 FUNCIONES:

1_ TOMAR UNA CARTA: toma una carta... en caso de que llegues a mas de 21, perderas o 
en caso de que el crupier tome una, tambien perdera.
2_ PLANTARSE: te plantas con la suma de tu baraja actual, si tienes mas que el crupier, ganas.
si no, pierdes.
3_ DOBLAR DINERO: te llevara a un menu, donde apostaras todo el dinero que quieras, aunque si
superas tu monto actual, no te dejara apostarlo.
4_ RENDIRSE: reiniciara la partida.
		-------------------------------------------------------------------------""")

			print("// PRESIONE 1 PARA SALIR. //")
			good = int(input("> "))

			if good == 1:

				os.system("cls")
				
				print("De acuerdo, vayamos al menu...")
				main()
				break

			else:
				print("Agregue 1 para salir de este menu.")
				continue

		except:
			print("Agregue el numero 1 para salir...")
			continue

def main():

	menu = 0

	while True:

		try:
			print("""
      _____           _____
  ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           `Yd
8(              "              )8
I8                             8I
 Yb,                         ,dP
  "8a,                     ,a8"
    "8a,                 ,a8"
      "Yba             adP"
        `Y8a         a8P'
          `88,     ,88'
            "8b   d8"  BLACK JACK 21
             "8b d8"   By Jeff McWill.
              `888'
                "
				""")
			print("-------------------")
			print("1. JUGAR")
			print("2. ¿COMO JUGAR?")
			print("3. SALIR")
			print("-------------------")

			menu = int(input("> "))

			if menu == 1: 
				
				print("Ok, empezemos a jugar...")
				time.sleep(1)
				print("Mezclando cartas...")
				time.sleep(1)
				print("Repartiendo...")
				blackjack()
				break

			elif menu == 2:

				print("Ok, te explicare como jugar...")
				howto()
				break

			elif menu == 3:

				print("Ok, hasta luego...")
				time.sleep(1)
				break

			else:

				print("ERROR: Numeros que ingresaste no estan soportados por el programa.")
				continue

		except:

			print("ERROR: comandos ingresados no soportados por el programa.")
			continue

if __name__ == "__main__":
	main()
	#blackjack()