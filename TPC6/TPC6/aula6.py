#Modelo:[(nome, desc, periodo, duracao, _id)]

import csv
import matplotlib.pyplot as plt


def lerObras():   
    file = open("obras.csv", encoding = "UTF8")   # file = open("../datasets/obras.csv") quando o nosso ficheiro está numa pasta diferente
    file.readline()    #Permite passar uma linha à frente
    obras = csv.reader(file, delimiter = ";")
    lista = []

    for line in obras:
        lista.append((line))
    return lista


def contarObras():
    file = open("obras.csv", encoding = "UTF8")   
    file.readline()    
    obras = csv.reader(file, delimiter = ";")
    lista1 = []
    for i in obras:
        lista1.append(i)
    return len(lista1)


def imprimeObras():
    file = open("obras.csv", encoding = "UTF8")   
    file.readline()    
    obras = csv.reader(file, delimiter = ";")
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor:':15} |")
    for nome, desc, ano, _, comp, *_ in obras:
        print(f"| {nome[:20:20]} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")


def alfabeticamente():                                  # def titAno(obras):
    file = open("obras.csv", encoding = "UTF8")         #   lista = []
    file.readline()                                     #   for nome, _, ano, *in obras:
    obras = csv.reader(file, delimiter = ";" )          #       lista.append((nome, ano))
    listaOrdAlf = []                                    #   lista.sort(key = ordem)
    for line in obras:                                  #   return lista
        tuplo = (line[0], line[2])
        listaOrdAlf.append(tuplo)
    return sorted(listaOrdAlf)


def crescentemente():
    file = open("obras.csv", encoding = "UTF8")
    file.readline()     
    obras = csv.reader(file, delimiter = ";" )
    lista = []
    for nome, desc, ano, _, comp, *_ in obras:
        lista.append((nome, ano))
        lista.sort(key = lambda tuplo: tuplo[1])
    return lista


def compositores():
    file = open("obras.csv", encoding = "UTF8")
    file.readline()
    obras = csv.reader(file, delimiter = ";" )
    listaCompositores = []
    for line in obras:
        listaCompositores.append(line[4])
    return sorted(listaCompositores)


def disPeriodo():
    file = open("obras.csv", encoding = "UTF8")
    file.readline()
    obras = csv.reader(file, delimiter = ";")
    dicPeriodo = {}
    for line in obras:
        if line[3] in dicPeriodo:
            dicPeriodo[line[3]] = dicPeriodo[line[3]] + 1
        else:
            dicPeriodo[line[3]] = 1
    return dicPeriodo


def disAno():
    file = open("obras.csv", encoding = "UTF8")
    file.readline()
    obras = csv.reader(file, delimiter = ";")
    dicAno = {}
    for line in obras:
        if line[2] in dicAno:
            dicAno[line[2]] = dicAno[line[2]] + 1
        else:
            dicAno[line[2]] = 1
    return dicAno


def disCompositor():
    file = open("obras.csv", encoding = "UTF8")
    file.readline()
    obras = csv.reader(file, delimiter = ";")
    dicCompositor = {}
    for line in obras:
        if line[4] in dicCompositor:
            dicCompositor[line[4]] = dicCompositor[line[4]] + 1
        else:
            dicCompositor[line[4]] = 1
    return dicCompositor



def grafico(obras):
    file = open("obras.csv", encoding = "UTF8")
    file.readline()
    obras = csv.reader(file, delimiter = ";")
    plt.figure(figsize=(28,12))
    plt.bar(obras.keys(), obras.values(), color="purple")
    plt.xticks([x for x in range(0, len(obras.keys()))], obras.keys(), rotation= "vertical")
    plt.show()
    



def inversao():
    file = open("obras.csv", encoding = "UTF8")
    file.readline()
    obras = csv.reader(file, delimiter = ";")
    listaCompositores = []
    listaTitulos = []
    for line in obras:
        listaCompositores.append(line[4])
        listaTitulos.append(line[0])
        resultado = [list(zip(listaCompositores, listaTitulos))]
    return resultado










    


    



    

    




    

    





    