

def pegaTag(objeto):
    index=0
    for i in cache:
        for j in i:
            if objeto[:14] == j[:14]:
                return index
        else:
            index+=1
    return -1
def calculaBloco():
    tal=""
    for i in range(0,4):
        tal=str(tal).join(" ").join(str(bin(i)))
    return tal
tamanho_limite=16
tam_tag=14
cache = []
for t in range(0,16):
    cache.append([])
index2=0
indexCache=0
hits=0
arq= open("Adresses3.txt",'r')
entradas = arq.readlines()
for entrada in entradas:

    if pegaTag(entrada)!=-1:
        hits+=1


    else:
        if indexCache< tamanho_limite:
            cache[indexCache] = [entrada,"00 ","01 ","10 ","11"]
            indexCache+=1

        else:

            cache[index2]=[entrada,"00 ","01 ","10 ","11"]
            index2+=1
            if index2>=tamanho_limite:
                index2=0
        indexAux = 0
        print("\n")
        print("CACHE")
        print("    tag            | dado")
        for tagg in cache:
            if len(str(hex(indexAux))) > 3:
                print(str(hex(indexAux)) + " " + tagg[0][:14] + " | " + tagg[1] + tagg[2]+tagg[3]+tagg[4])
            else:
                try:
                    print(str(hex(indexAux)) + "  " + tagg[0][:14] + " | " + tagg[1] + tagg[2]+tagg[3]+tagg[4])
                except Exception:
                    pass
            indexAux += 1
print("\n")
print('CACHE FINAL')
print("    tag            | dado")
indexAux=0
for tagg in cache:
        print(str(hex(indexAux))+" "+tagg[0][:14]+" | "+tagg[1]+tagg[2]+tagg[3]+tagg[4])
        indexAux +=1
print("\n\n"+"Quantidade total: "+str(hits)+" hits")
print(str(hits*100/288.0)[:5]+"%")
print("\n\n"+"Quantidade total: "+str(288-hits)+" miss")
print(str((288-hits)*100/288.0)[:5]+"%")

print("\n\n\n############################################################################\n\n\n")
exit()

def pegaTag(objeto):
    index=0
    for i in cache:
        for j in i:
            if objeto[:15] == j[:15]:
                return index
        else:
            index+=1
    return -1
tamanho_limite=32
tam_tag=15
cache = []
for t in range(0,32):
    cache.append([])
index2=0
indexCache=0
hits=0
arq= open("Adresses3.txt",'r')
entradas = arq.readlines()
for entrada in entradas:

    if pegaTag(entrada)!=-1:
        hits+=1


    else:
        if indexCache< tamanho_limite:
            cache[indexCache] = [entrada,"  0 ","1"]
            indexCache+=1

        else:

            cache[index2]=[entrada,"  0 ","1"]
            index2+=1
            if index2>=tamanho_limite:
                index2=0
    indexAux = 0
    print("\n")
    print("CACHE")
    print("     tag            |  dado")
    for tagg in cache:
        if len(str(hex(indexAux))) > 3:
            print(str(hex(indexAux)) + " " + tagg[0][:14] + " | " + tagg[1] + tagg[2])
        else:
            try:
                print(str(hex(indexAux)) + "  " + tagg[0][:14] + " | " + tagg[1] + tagg[2])
            except Exception:
                pass
        indexAux += 1
print("\n")
print('CACHE FINAL')
print("     tag            |  dado")
indexAux=0
for tagg in cache:
    if len(str(hex(indexAux)))>3:
        print(str(hex(indexAux)) + " " + tagg[0][:14] + " | " + tagg[1] + tagg[2])
    else:
        print(str(hex(indexAux)) + "  " + tagg[0][:14] + " | " + tagg[1] + tagg[2])

    indexAux+=1
print("\n\n"+"Quantidade total: "+str(hits)+" hits")
print(str(hits*100/288.0)[:5]+"%")
print("\n\n"+"Quantidade total: "+str(288-hits)+" miss")
print(str((288-hits)*100/288.0)[:5]+"%")











