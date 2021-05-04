# https://www.youtube.com/watch?v=0XaGAkY09Wc

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
    f.close()


def check_equivalent(s1,s2,mult):
    states1 = []
    states2 = []
    for el in graph[s1].keys():
        states1.append(el)
    for el in graph[s2].keys():
        states2.append(el)
    states1.sort()
    states2.sort()
    for i in range(len(states1)):
        if states1[i]!=states2[i]:
            return False

    valuesSet = set()
    for el in states1:
        if graph[s1][el] != graph[s2][el]:
            valuesSet.add(int(graph[s1][el]))
            valuesSet.add(int(graph[s2][el]))


    for el in valuesSet:
        if el not in mult:
            return False
    return True


def minify():
    equivalence = {}
    level = 0
    equivalence[level] = []
    equivalence[level].append(fin)
    equivalence[level].append([el for el in stari if el not in fin])
    level += 1

    while True:
        equivalence[level] = []
        for mult in equivalence[level-1]:
            if len(mult) == 1:
                equivalence[level].append(mult)
            else:
                new_set = set()
                for i in range(0,len(mult)-1):
                    for j in range(i+1,len(mult)):
                        if check_equivalent(mult[i],mult[j],mult):
                            new_set.add(mult[i])
                            new_set.add(mult[j])
                missing = set(mult) - new_set
                for el in missing:
                    equivalence[level].append([el])
                equivalence[level].append(list(new_set))
        if equivalence[level] == equivalence[level-1]:
            return equivalence[level]
        level += 1


def print_dfa(equivalence,file):
    g = open(file,'w')
    new_states = []
    for el in equivalence:
        new_states.append('.'.join(str(x) for x in el))
    new_states.sort()
    g.write('Numar stari: ' + str(len(new_states)) + '\n')
    g.write('Stari: ')
    for el in new_states:
        g.write(str(el) + ', ')
    g.write('\n')

    stare_initiala = ''
    for el in new_states:
        if str(s) in el.split('.'):
            stare_initiala = el
            break
    g.write('Stare initiala: ' + stare_initiala + '\n')

    map = {el:'' for el in stari}
    for el in new_states:
        for x in el.split('.'):
            map[int(x)] = el

    stari_finale = []
    for el in new_states:
        for x in fin:
            if str(x) in el.split('.'):
                stari_finale.append(el)
                break
    g.write('Stari finale: ')
    for el in stari_finale:
        g.write(str(el) + ', ')
    g.write('\n')

    new_graph = {state:{} for state in new_states}
    for state in new_graph.keys():
        for el in graph[int(state.split('.')[0])].keys():
            new_graph[state][el] = map[int(graph[int(state.split('.')[0])][el])]

    g.write('Tranzitii:' + '\n')
    for state in new_graph.keys():
        for el in new_graph[state].keys():
            g.write(state + ' ' + new_graph[state][el] + ' ' + el + '\n')
    # print(new_graph)


read_data('date-minimization.in')
print(graph)
equivalence = minify()
print_dfa(equivalence,'date.out')

