import TPC7 as tpc
menu = (
    "\nEscolha uma das opções apresentadas\n"
    "1 - Ler a informação do ficheiro\n"
    "2 - Calcular a distribuição de alunos por curso\n"
    "3 - Calcular a média dos tpc's 1,2,3 e 4 e acrescentá-la numa coluna ao dataset)\n"
    "4 - Calcular a média por escalões e acrescentá-la numa coluna ao dataset)\n"
    "5 - Ler a informação do ficheiro com as colunas acrescentadas\n"
    "6 - Apresentar as distribuições em gráficos de barras\n"
    "7 - Apresentar as distribuições em gráficos de linhas\n"
    "8 - Apresentar as distribuições em tabelas\n"
    "0 - Sair do programa\n"
)
i = 10
alunos = tpc.ler()
while i != 0:
    print(menu)
    i = int(input("Qual a opção que quer escolhar?"))
    if i == 1:
        print(f"{'Informação do ficheiro':-^61}")
        print(f"|{'id':^5}|{'nome':^12}|{'curso':^12}|{'TPC1':^6}|{'TPC2':^6}|{'TPC3':^6}|{'TPC4':^6}|")
        for x in range(100):
            print(f"|{tpc.ler()[x][0]:^5}|{tpc.ler()[x][1][:10]:^12}|{tpc.ler()[x][2]:^12}|{tpc.ler()[x][3]:^6}|{tpc.ler()[x][4]:^6}|{tpc.ler()[x][5]:^6}|{tpc.ler()[x][6]:^6}|")

    elif i == 2:
        print(f"{'Distribuição de alunos por curso':^51}")
        print(tpc.alunos_curso(alunos))
        print(f"{'':-^51}")
        print(f"|{'LEI':^11}|{'ENGFIS':^12}|{'LCC':^11}|{'ENGBIOM':^12}|")
        lst = list(tpc.alunos_curso(alunos).values())
        print(f"|{lst[0]:^11}|{lst[1]:^12}|{lst[2]:^11}|{lst[3]:^12}|")
        
    
    elif i == 3:
        print(f"{'Média dos TPCs por alunos':-^50}")
        print(f"|{'Aluno':^40}|{'Média':^7}|")
        al = list(tpc.media(alunos).items())
        for x in range(100):
            print(f"|{al[x][0][:38]:^40}|{al[x][1]:^7}|")
        tpc.adicionar_coluna(tpc.listacomp(tpc.paralista(tpc.media(alunos))))
    
    elif i == 4:
        print(f"{'Escalão de cada aluno':-^52}")
        print(f"|{'Aluno':^40}|{'Escalão':^9}|")
        al = list(tpc.grau(tpc.ler()).items())
        for x in range(100):
            print(f"|{al[x][0][:38]:^40}|{al[x][1]:^9}|")
        tpc.addcolumn_1(tpc.listacomp(tpc.paralistag(tpc.grau(alunos))))

    elif i == 5:
        print(f"{'Informação do novo ficheiro':-^75}")
        print(f"|{'id':^5}|{'nome':^12}|{'curso':^12}|{'TPC1':^6}|{'TPC2':^6}|{'TPC3':^6}|{'TPC4':^6}|{'Média':6}|{'Grau':6}")
        for x in range(100):
            print(f"|{tpc.ler()[x][0]:^5}|{tpc.ler()[x][1][:10]:^12}|{tpc.ler()[x][2]:^12}|{tpc.ler()[x][3]:^6}|{tpc.ler()[x][4]:^6}|{tpc.ler()[x][5]:^6}|{tpc.ler()[x][6]:^6}|{tpc.ler()[x][7]:^6}|{tpc.ler()[x][8]:^6}|")

    elif i == 6:
        l = 4
        while l != 0:
            print("1 - Distribuição de alunos por curso\n"
        "2 - Distribuição de alunos por escalão\n"
        "3 - Distribuição da média de cada curso\n"
        "0 - Sair")
            l = int(input("Qual a distribuição que pretende ver?"))
            if l == 1:
                print("\nGráfico de barras:\n")
                print(tpc.distribuicaoP(tpc.alcurso(tpc.ler()), "Distribuição dos alunos por curso", "Curso", "Número de alunos"))
            if l == 2:
                print("\nGráfico de barras:\n")
                print(tpc.distribuicaoP(tpc.almedia(tpc.ler()), "Distribuição dos alunos por Escalão", "Escalões", "Número de alunos"))
            if l == 3:
                print("\nGráfico de barras:\n")
                print(tpc.distribuicaoP(tpc.mediacurso(tpc.ler()), "Distribuição da média por cada curso", "Curso", "Média"))
        if l == 0:
            print("Saiu da opção 6")
    
    elif i == 7:
        p = 4 
        while p != 0:
            print("1 - Distribuição de alunos por curso\n"
        "2 - Distribuição de alunos por escalão\n"
        "3 - Distribuição da média de cada curso\n"
        "0 - Sair")
            p = int(input("Qual a distribuição que pretende ver?"))
            if p == 1:
                print("\nGráfico de linha:\n")
                print(tpc.graf(tpc.alcurso(tpc.ler()), "Distribuição dos alunos por curso", "Curso", "Número de alunos"))
            if p == 2:
                print("\nGráfico de linha:\n")
                print(tpc.graf(tpc.almedia(tpc.ler()), "Distribuição dos alunos por Escalão", "Escalões", "Número de alunos"))
            if p == 3:
                print("\nGráfico de linha:\n")
                print(tpc.graf(tpc.mediacurso(tpc.ler()), "Distribuição da média por cada curso", "Curso", "Média"))
        if p == 0:
            print("Saiu da opção 6")
    
    elif i == 8:
        m = 5
        while m != 0:
            print("1 - Tabela de alunos por curso\n"
            "2 - Tabela de alunos por escalão\n"
            "3 - Tabela da média de cada curso\n"
            "0 - Sair")
            m = int(input("Qual a Tabela que pretende ver?"))
            if m == 1:
                print(f"{'Tabela de alunos por curso':_^105}")
                print(tpc.tabela3())
            if m == 2:
                print(f"{'Tabela de alunos por Escalão':_^96}")
                print(tpc.tabela2())
            if m == 3:
                print(f"{'Tabela da média de cada curso':_^96}")
                print(tpc.tabela2())

    elif i > 9:
        print("Opção inválida, escolha outra")

if i == 0:
    print(f"{'Saiu do programa':-^110}\n{'':-^110}")