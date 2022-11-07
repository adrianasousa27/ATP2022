import csv
import matplotlib.pyplot as plt

# ler a informação do ficheiro
def ler():
    file = open("alunos.csv", encoding="utf8")
    file.readline()
    csv_file = csv.reader(file, delimiter=",")
    lista = []
    for line in csv_file:
        lista.append(tuple(line))
    return lista

def countalunos():
    lst = list(ler())
    return len(lst)

#distribuição de alunos por curso:
def alunos_curso(alunos):
    dicionario_curso = {}
    for _,_,curso, *_ in alunos:
        if curso in dicionario_curso.keys():
            dicionario_curso[curso] = dicionario_curso[curso] + 1
        else:
            dicionario_curso[curso] = 1
    return dicionario_curso

#média de cada aluno  [(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4)]
def media(alunos):
    lsta_media = []
    for _, nome, _, tpc1,tpc2,tpc3,tpc4, *_ in alunos:
        media = (int(tpc1)+int(tpc2)+int(tpc3)+int(tpc4))/4
        lsta_media.append((nome, media))
    dici = dict(lsta_media)
    return dici

def distribuicaoP(alunos, titulo, abcissa, ordenada): 
    plt.figure()
    plt.bar(alunos.keys(), alunos.values(), color="green")
    plt.xticks([x for x in range(0, len(alunos.keys()))], alunos.keys(), rotation= "vertical")
    plt.ylabel(ordenada, rotation= 'vertical')
    plt.xlabel(abcissa)
    plt.title(titulo)
    plt.show()

# Transformar o dicionário das médias numa lista
def paralista(al):
    l=[]
    l.append("Médias")
    alu = list(al.items())
    for i in alu:
        l.append(i[1])
    return l

# Transformar a lista de tuplos numa lista de escalões
def paralistag(al):
    l=[]
    l.append("Grau")
    alu = list(al.items())
    for i in alu:
        l.append(i[1])
    return l

# Meter os dados numa lista de linhas
def listadelinhas():
    data = []
    with open("alunos.csv", "r", encoding="utf8") as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    f.close()
    return data
# Adicionar uma das listas anteriores criadas ao dataset
def listacomp(lst): 
    data = listadelinhas()
    for i in range(len(lst)):
        data[i].append(lst[i])
    return data
# Adicionar_coluna(listacomp(media(alunos)))    
def adicionar_coluna(data): 
    with open("alunos.csv", "w", encoding= "utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    f.close()

# Distribuição dos alunos por escalão
def almedia(alunos):
    dic_escalao = {"[1,4.99] - E":0, "[5,8.99] - D":0, "[9,12.99] - C":0, "[13,16.99] - B":0, "[17,20] - A":0,}
    for _,_,_,_, _, _, _, media, *_ in alunos:
        med = float(media) 
        if med < 5:
            dic_escalao["[1,4.99] - E"] = dic_escalao["[1,4.99] - E"] + 1
        elif med < 9:
            dic_escalao["[5,8.99] - D"] = dic_escalao["[5,8.99] - D"] + 1
        elif med < 13:
            dic_escalao["[9,12.99] - C"] = dic_escalao["[9,12.99] - C"] + 1
        elif med < 17:
            dic_escalao["[13,16.99] - B"] = dic_escalao["[13,16.99] - B"] + 1
        elif med < 21:
            dic_escalao["[17,20] - A"] = dic_escalao["[17,20] - A"] + 1
    return dic_escalao

# Escalão correspondente a cada aluno
def escalao(alunos):
    lista_escalao= []
    med = list(media(alunos).items())
    for x in range (100):
        if med[x][1] < 5:
            lista_escalao.append((ler()[x][1], "E"))
        elif float(med[x][1]) < 9:
            lista_escalao.append((ler()[x][1], "D"))
        elif float(med[x][1]) < 13:
            lista_escalao.append((ler()[x][1], "C"))
        elif float(med[x][1]) < 17:
            lista_escalao.append((ler()[x][1], "B"))
        elif float(med[x][1]) < 21:
            lista_escalao.append((ler()[x][1], "A"))
    dicio = dict(lista_escalao)
    return dicio

# Média dos alunos por curso
def mediacurso(alunos):
    lst1 = []
    for _, _, curso, tpc1,tpc2,tpc3,tpc4, *_ in alunos:
        media = (int(tpc1)+int(tpc2)+int(tpc3)+int(tpc4))/4
        lst1.append((curso, media))
        a = [n for (eb, n) in lst1 if eb == "ENGBIOM"]
        b = [n for (eb, n) in lst1 if eb == "ENGFIS"]
        c = [n for (eb, n) in lst1 if eb == "LEI"]
        d = [n for (eb, n) in lst1 if eb == "LCC"]
        med_eb = sum(a)/25
        med_ef = sum(b)/32
        med_lei = sum(c)/23
        med_lcc = sum(d)/20
    dici = dict([("ENGBIOM", round(med_eb, 2)), ("ENGFIS", round(med_ef, 2)), ("LEI", round(med_lei, 2)), ("LCC", round(med_lcc, 2))])
    return dici

def graf(dist, titulo, abcissa, ordenada):
    x = list(dist.keys())
    y = list(dist.values())
    plt.xlabel(abcissa)
    plt.ylabel(ordenada, rotation= 'vertical')
    plt.plot(x,y,color= "blue")
    plt.title(titulo)
    plt.show()

#Tabela de médias por curso
def tabela1(): 
    print(f"{'':19} {'':_^85}")
    print(f"{'':20}|{'ENGBIOM':^20}|{'ENGFIS':^20}|{'LEI':^20}|{'LCC':^20}|")
    print(f"{'':_^105}")
    print(f"|{'Média:':^19}|{list(mediacurso(ler()).values())[0]:^20}|{list(mediacurso(ler()).values())[1]:^20}|{list(mediacurso(ler()).values())[2]:^20}|{list(mediacurso(ler()).values())[3]:^20}|")
    print(f"{'':_^105}")

#Tabela de medias por escalão
def tabela2(): #graus
    print(f"{'':14} {'':_^81}")
    print(f"{'':15}|{'A':^15}|{'B':^15}|{'C':^15}|{'D':^15}|{'E':^15}|")
    print(f"{'':_^96}")
    print(f"|{'Alunos:':^14}|{list(almedia(ler()).values())[4]:^15}|{list(almedia(ler()).values())[3]:^15}|{list(almedia(ler()).values())[2]:^15}|{list(almedia(ler()).values())[1]:^15}|{list(almedia(ler()).values())[0]:^15}|")
    print(f"{'':_^96}")

#Tabela de alunos por curso
def tabela3():
    print(f"{'':19} {'':_^85}")
    print(f"{'':20}|{'ENGBIOM':^20}|{'ENGFIS':^20}|{'LEI':^20}|{'LCC':^20}|")
    print(f"{'':_^105}")
    print(f"|{'Alunos:':^19}|{list(alcurso(ler()).values())[0]:^20}|{list(alcurso(ler()).values())[1]:^20}|{list(alcurso(ler()).values())[2]:^20}|{list(alcurso(ler()).values())[3]:^20}|")
    print(f"{'':_^105}")
