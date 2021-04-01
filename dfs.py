def read_data(file):
    global n,stari,m,t,s,nrf,fin,nrCuv,cuv,graph

    f = open(file,'r')
    n = int(f.readline()) #numar stari
    stari = [int(el) for el in f.readline().split()] #starile automatului
    graph = {el:{} for el in stari}
    m = int(f.readline()) #numar tranzitii
    for _ in range(m):
        x,y,z = f.readline().split()
        graph[int(x)][z]=y

    s = int(f.readline()) #starea initiala
    nrf = int(f.readline()) #numar stari finale
    fin = [int(el) for el in f.readline().split()] #stari finale
    nrCuv = int(f.readline()) #numar cuvinte
    cuv = [] #cuvinte
    for _ in range(nrCuv):
        cuv.append(f.readline().strip())
    f.close()


def checkWord(word):
    state = s
    for c in word:
        state = graph[int(state)][c]
    if int(state) in fin:
        return True
    return False


def print_data(file):
    g = open(file,'w')
    for c in cuv:
        if checkWord(c):
            g.write('DA'+'\n')
        else:
            g.write('NU'+'\n')
    g.close()



read_data('date.in')
print_data('date.out')

