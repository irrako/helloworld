def  palindromeRearranging ( inputString ):

	lista  =  lista ( inputString )
	largo  =  len ( lista )

	# Compruebe si hay al menos un número par para cada palabra, excepto una excepción: las palabras con un número impar de letras
	lista  =  ordenado ( lista )
	err  =  0
	elem  =  1
	#print (lista)
	para  i  en  rango ( largo - 1 ):
		# Bucle desde el segundo elemento. El segundo tiene que ser igual al primero. si no da un error,
		#print ('Índice de letras:', i, 'Letra:', lista [i], 'elem:', elem)
		#print ('prev:', lista [i-1])
		#print ('Siguiente:', lista [i + 1])
		
		si  lista [ i ] == lista [ i + 1 ]:
			# Es el mismo elemento
			elem  =  elem  +  1
			si  i ==  largo - 2 :
				si  elem % 2  ! =  0 :
					#print ("El error era:", err)
					err  =  err  +  1
					#print ("Ahora error:", err)
					si  err  ==  2 :
						volver  falso

		más :
			# Si es un elemento nuevo
			#print ("Cambiamos! La letra se repitió:", elem)
			si  elem % 2  ! =  0 :
				#print ("El error era:", err)
				err  =  err  +  1
			elem  =  1
			si  i  ==  largo - 2 :
				err  =  err  +  1
			#print ("Ahora error:", err)
			si  err  ==  2 :
				volver  falso
			#print ("¡Incorrecto!")
	volver  verdadero