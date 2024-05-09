matriz1 = [['💨','💨','💨','💨','💨','💨'],
       ['💨','💨','💨','💨','💨','💨'],
       ['💨','💨','💨','💨','💨','💨'],
       ['💨','💨','💨','💨','💨','💨'],
       ['💨','💨','💨','💨','💨','💨'],]
correcto = '🤪'
incorrecto= '☠️'
ls_preguntas = ['¿Que es Python? \n1. juego\n2. lenguaje de programacion\n3. marca de auto\n4. ninguna de las anteriores ', 
'¿ que es HTML?\n1. lenguaje de maquetacion\n2. marca de gaseosa\n3. navegador\n4. perro caliente ', ]
ls_respuesta = ['2', '1']

def fnt_PintarMatriz(): 
    for i in range(len(matriz1)):
        for J in range(len(matriz1[i])):
            print(matriz1[i][J], end='      ')
        print('\n\n')
        
sw = True
contador = 0

for i in range(len(matriz1)):
        for J in range(len(matriz1[i])):        
            import os
            os.system('cls')
            fnt_PintarMatriz()
            print()
            print(ls_preguntas[contador])
            r = input('-->')
            if r == ls_respuesta[contador]:
                matriz1[i][J] = correcto
            else:
                matriz1[i][J] = incorrecto
            contador += 1