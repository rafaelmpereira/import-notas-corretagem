from tika import parser

def main(path):
    #path = "/Nova Pasta/"
    #path = "C:/Users/rafae/Downloads/"
    #arq = input("Digite o nome do arquivo: ")

    arq = path

    file_data = parser.from_file(arq)
    info = []

    f = open("notas.csv", "a") # append

    text = file_data["content"]
    linha = text.split("\n")

    # removendo linhas vazias
    for i in linha:
        if i == "":
            linha.remove("")

    # buscando nr nota
    for j in range(len(linha)):
        x = linha[j].find("Nr. nota")
        if x != -1:
            info.append(linha[j+1])

    # buscando data
    for k in range(len(linha)):
        x = linha[k].find("Data")
        if x != -1:
            info.append(linha[k+1])

    # bypassando tx corretagem
    info.append("0,00")

    # buscando tx liquidacao
    for l in range(len(linha)):
        x = linha[l].find("Taxa de liq")
        if x != -1:
            i = linha[l].split(" ")
            j = i[0].strip("Taxa")
            info.append(j)

    # buscando tx emol
    for m in range(len(linha)):
        x = linha[m].find("Emol")
        if x != -1:
            i = linha[m].split(" ")
            j = i[0].strip("Emolumentos")
            info.append(j)

    # buscando IRPF
    for n in range(len(linha)):
        x = linha[n].find("I.R.R.F")
        if x != -1:
            i = linha[n].split(" ")
            j = i[0].strip("I.R.R.F")
            info.append(j)

    # buscando ativo, operacao, qtd e valor
    for o in range(len(linha)):
        x = linha[o].find("1-BOVESPA")
        if x != -1:
            i = linha[o].split(" ")
            i.pop(0)
            i.pop(1)
            i.pop()
            i.pop()
            for lm in range(i.count("")):
                i.remove("")
            i.insert(1,"%s %s %s"%(i[1],i[2],i[3]))
            for l in range(2):
                i.pop(2)

            #print(i)
            info.append(i[1]) # ativo
            info.append(i[0]) # operacao
            info.append(i[-2]) # qtd
            info.append(i[-1]) # valor
            
            if i[-3] == "#":
                info.append("Neg.Direta")
            elif i[-3] == "D":
                info.append("Day trade")
            else:
                info.append("Normal")
            #print(info)
            #print(i)

            f.write("\n")
            for i in info:
                f.write(";"+i)
            #print(info)
            for c in range(5):
                info.pop()
    f.close()
    print("Finalizado.")

#main("C:/Users/rafae/Desktop/python/Nova Pasta/NotaNegociacao_1484493_20200420 (2).pdf")





