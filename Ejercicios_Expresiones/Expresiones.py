import re
opcion = 0
while (opcion != 11):
    print("____________________Ejercicios con expresiones regulares_____________________\n"          
                "1-Todas las palabras que tengan una longitud de 7 o más letras\n"
                 +"2-Expresiones que NO finalicen con una vocal\n"
                 +"3-Las palabras que inicien con “M” donde la segunda letra no sea vocal\n"
                 +"4-Expresiones encerradas entre comillas\n"
                 +"5-Ip’s\n"
                 +"6-Horas\n"
                 +"7-Telefonos\n"
                 +"8-Correo electronicos\n"
                 +"9-URL´S\n"
                 +"10-Codigo postal\n"
                +"11-Salir")

    opcion = int(input("Seleccione un ejercicio: "))

    if (opcion == 1):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]{7,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("La lista de palabras con 7 o mas letras es: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 2):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z0-9]+[^aeiou][ \t\n\r\f\v]"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("La lista de expresiones que NO finalizan con vocal es: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 3):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex = "M[^aeiou][a-zA-Z]{1,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("La lista de palabras que incian con M y la segunda letra no es vocal es: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 4):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex = "(\".*?\"|\'.*?\')"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("La lista de palabras entre comillas es: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 5):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("Las direcciones ips encontradas son: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 6):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex ="(?:[01]\d|2[0-3]):[0-5]\d"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("Las horas encontradas en el texto son: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 7):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex ="\d[0-9]{7,10}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("Los telefonos encontrados en el texto son: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 8):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex ="[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("Los correos encontrados en el texto son: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 9 ):
        filename = "ejemplo.txt"
        textfile = open(filename, "r")
        regex = "https?:\/\/[\w\-]+\.[\w\-]+[#?]?.*"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print("Las URL´S encontrados en el texto son: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 10):
        filename = "ejemplo.txt"
        textfile = open(filename, "r",)
        regex ="^(\d{5}$)"
        reg = re.compile(regex,flags=re.MULTILINE)
        for line in textfile:
            lista = reg.findall(line)
            print("Los codigos postales encontrados en el texto son: ")
            print(lista)
            print("La expresion regular del ejercicio es: " + regex)
        textfile.close()

    elif (opcion == 11):
        print("Programa hecho por Henry Froylan Chuc Tec")
        break




