arquivo = open("Adresses3.txt",'r')
ler= arquivo.readline()
print(ler)
for i in ler:
    tal=i.replace("\n","")
    tal2="0b".join(tal)
    tal3=print(tal2)