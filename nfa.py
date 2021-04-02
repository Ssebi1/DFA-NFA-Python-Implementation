def read_data(file):
    global n,stari,m,t,s,nrf,fin,nrCuv,cuv,graph,stopState

    f = open(file,'r')
    n = int(f.readline()) #numar stari
    stari = [int(el) for el in f.readline().split()] #starile automatului


    graph = {el:{} for el in stari}
    stopState = max(stari) + 1
    graph[stopState] = {}
    m = int(f.readline()) #numar tranzitii
    for _ in range(m):
        x,y,z = f.readline().split()
        if z not in graph[int(x)]:
            graph[int(x)][z] = [y]
        else:
            graph[int(x)][z].append(y)
    for s in stari:
        for p in graph[s].keys():
            graph[s][p].append(str(stopState))


    s = int(f.readline()) #starea initiala
    nrf = int(f.readline()) #numar stari finale
    fin = [int(el) for el in f.readline().split()] #stari finale
    nrCuv = int(f.readline()) #numar cuvinte
    cuv = [] #cuvinte
    for _ in range(nrCuv):
        cuv.append(f.readline().strip())

    f.close()


def checkWord(initialWord,word,state,pos,path):
    global gPath
    for i in range(len(word)):
        if word[i] in graph[int(state)].keys():
            for t in graph[int(state)][word[i]]:
                if t != str(stopState):
                    state = t
                    path.append((t,word[i]))
                    if len(word)==1 and int(state) in fin and cuvDict[initialWord] == 0:
                        cuvDict[initialWord] = 1
                        gPath = path
                        return True
                    checkWord(initialWord,word[pos+1:],state,pos,path.copy())
                    path.pop()
            pos += 1
    return False

def print_data(file):
    g = open(file,'w')
    global cuvDict,gPath
    cuvDict= {c:0 for c in cuv}

    for c in cuv:
        gPath = []
        checkWord(c,c,s,0,[])
        if cuvDict[c] == 1:
            g.write('DA ')
            for el in gPath:
                g.write('(' + str(el[0])+','+str(el[1]) + ')' + ' ')
            g.write('\n')
        else:
            g.write('NU' + '\n')
    g.close()


read_data('date.in')
print_data('date.out')

