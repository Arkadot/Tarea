'''Con la intención de hacer la web más social se han creado múltiples aplicaciones o sitios en Internet que
permiten compartir información y establecer comunicación entre grupos de personas, estos sitios
son denominados REDES SOCIALES. Una empresa de publicidad cuyo lema es “las empresas que invierten
en publicidad, son las empresas que permanecen en la mente de las personas”, quiere evaluar la posibilidad de
colocar publicidad en alguna de las tres redes sociales que considera de mayor uso o más
comunes. Para ello se realiza una encuesta a un conjunto W de personas a quienes se les solicita
suministren la siguiente información: 
NOMBRE, GÉNERO, EDAD Y RED SOCIAL MÁS UTILIZADA
Desarrolle un programa que procese la información, almacenada en un archivo de nombre REDES.TXT y
genere dos archivos de nombre USAREDSOCIAL.TXT y NOLASENCUESTADAS.TXT, con los nombres de los
usuarios que usan alguna de las tres redes sociales consideradas en el estudio o los que no usan
ninguna de las redes sociales consideradas en el
estudio respectivamente, además...
determine e imprima por pantalla:
✓ Cantidad de personas que utilizan cada uno de las tres principales redes sociales
considerados en la encuesta
✓ Porcentaje de personas que utilizan alguna de las tres principales redes sociales
considerados en la encuesta
✓ Nombre y edad del primer usuario procesado que usa hi5
✓ En cuál de las tres redes sociales sería más rentable invertir en publicidad.
Consideraciones:
o El género se tomará como 1 =Femenino y 2 = Másculino
o Los valores para tipo de red social más utilizada son 1 =Facebook, 2 =Myspace, 3=Hi5 y
4=Ninguno u otro
o Mientras más usuarios usen una red social, esta se considera más rentable para hacer
publicidad
Actividades a Desarrollar:
1. Identifique los datos de entrada y salida, colocándolos en esta tabla con el tipo de
dato
'''







#Codigo del programa ejecutable de la actividad de manejo de archivos

#declarando algunas variables y contadores

salto = 1

facebook = 0

myspace = 0

hi5 = 0

a = 0

#lectura del archivo ".txt"



arch = open('redes.txt','r')

#Abriendo archivos en los que se imprimira la informacion


usared = open('usaredsocial.txt','w')

nousared = open('nolasencuestadas.txt','w')


#Leyendo archivos linea a linea

linea = arch.readlines()

#creando una variable que asuma el valor de las personas en la lista

w = int(linea[0])

#utilizando el ciclo for para realizar w cantidad de veces las operaciones que pide el problema para cada individuo

for i in range(w):

    #Creando lista que separa cada uno de los elementos de cada linea

    lista = linea[salto].split(",")

    #guardando datos
    
    nombre = str(lista[0])
    
    genero = str(lista[1])
    
    edad = int(lista[2])
    
    red = int(lista[3])


    #Imprimiendo en el archivo de texto los nombres de los que no utilizan redes sociales

    if red == 4:

        nousared.write(str(nombre) + '\n')

    #Imprimiendo en el archivo de texto los nombres de las personas que si utilizan redes sociales    

    else:

        usared.write(str(nombre) + '\n')

        #contando la cantidad de personas que utilizan facebook, myspace o hi5


        if red == 1:

            facebook += 1
            
        elif red == 2:

            myspace += 1

        else:

            hi5 += 1

            #ejecutando una instruccion que unicamente se ejecutara una vez dentro del ciclo
            if a == 0:

                nombre_primera = nombre

                edad_primera = edad

                a = 1
    #Salto a la siguiente linea
    salto += 1

#calculando porcentaje de personas que utilizan redes sociales

porcentaje = (facebook + myspace + hi5)*100/w


porcentaje = round(porcentaje, 2)

#imprimiendo resultados de las preguntas en pantalla

print("La Cantidad de personas que utilizan Facebook es de: ",facebook)

print(" ")

print("La Cantidad de personas que utilizan MySpace es de: ",myspace)

print(" ")

print("La Cantidad de personas que utilizan hi5 es de: ",hi5)

print(" ")

print("La primera persona que aparece en la lista que utiliza hi5 se llama: ",nombre_primera," y tiene ",edad_primera, " años")

print(" ")      

print("El porcentaje de personas encuestadas que utilizan redes sociales es de: ",porcentaje, "%")
      
print(" ")

#determinando la red social mas utilizada

if facebook > myspace and facebook > hi5:

    print("La red social mas utilizada es Facebook")

elif myspace > facebook and myspace > hi5:

    print("La red social mas utilizada es Myspace")

else:
    print("La red social mas utilizada es hi5")


#cerrando archivos



arch.close()

usared.close()

nousared.close()

    
    





















