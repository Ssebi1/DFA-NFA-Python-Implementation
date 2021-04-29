def read_data(file):
    global n,stari,m,t,s,nrf,fin,nrCuv,cuv,graph,tranzitii

    f = open(file,'r')
    n = int(f.readline()) #numar stari
    stari = [el for el in f.readline().split()] #starile automatului


    graph = {el:{} for el in stari}
    tranzitii = []
    m = int(f.readline()) #numar tranzitii
    for _ in range(m):
        x,y,z = f.readline().split()
        tranzitii.append(z)
        if z not in graph[x]:
            graph[x][z] = [y]
        else:
            graph[x][z].append(y)
    tranzitii = set(tranzitii)
    tranzitii = list(tranzitii)

    s = int(f.readline()) #starea initiala
    nrf = int(f.readline()) #numar stari finale
    fin = [el for el in f.readline().split()] #stari finale

    f.close()


def convert():
    global dfa
    dfa = {}
    newStates = []

    dfa[stari[0]] = {}

    for t in graph[stari[0]]:
        new_state = '.'.join(graph[stari[0]][t])
        dfa['0'][t] = new_state
        if '.' in new_state:
            newStates.append(new_state)
            stari.append(new_state)

    while len(newStates)!=0:
        dfa[newStates[0]] = {}
        for _ in newStates[0].split('.'):
            for t in tranzitii:
                s = []
                for nr in newStates[0].split('.'):
                    if t in graph[nr]:
                        s += graph[nr][t]

                new_state = '.'.join(s)
                if '.' in new_state and new_state not in stari:
                    newStates.append(new_state)
                    stari.append(new_state)
                dfa[newStates[0]][t] = new_state
        newStates = newStates[1:]


def printDfa(file):
    g = open(file,'w')
    g.write('Numar stari:' + str(len(dfa.keys())) + '\n')
    g.write('Stari: ')
    for s in dfa.keys():
        g.write(str(s)+ ', ')
    g.write('\nTranzitii:\n')

    for s in dfa.keys():
        for t in dfa[s].keys():
            g.write(str(s) + ' ' + dfa[s][t]  + ' ' + str(t) + '\n')

    stariFinaleDfa = []
    for s in dfa.keys():
        for c in s.split('.'):
            if c in fin:
                stariFinaleDfa.append(s)

    g.write('Stari finale: ')
    for s in stariFinaleDfa:
        g.write(s + ', ')


read_data('date.in')
print(graph)
convert()
print(dfa)
printDfa('date.out')
