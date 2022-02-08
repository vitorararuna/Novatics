from http.client import OK


def problema1(lista):
    sem_duplicatas = list(set(lista))
    ordem = sorted(sem_duplicatas)
    print(ordem)
    return(ordem)
problema1([1,7,44,55,89,76])

#auxilio para problema 2
def mini_tabelas(matriz):
    tabelas = [[],[],[],[],[],[],[],[],[]]
    for m in matriz:
        if m==matriz[0] or m==matriz[1] or m==matriz[2]:
            for index in range(9):
                if index <= 2:
                    tabelas[0].append(m[index])
                if index > 2 and index <= 5:
                    tabelas[1].append(m[index])
                if index > 5 and index <= 8:
                    tabelas[2].append(m[index])
        if m==matriz[3] or m==matriz[4] or m==matriz[5]:
            for index in range(9):
                if index <= 2:
                    tabelas[3].append(m[index])
                if index > 2 and index <= 5:
                    tabelas[4].append(m[index])
                if index > 5 and index <= 8:
                    tabelas[5].append(m[index])
        if m==matriz[6] or m==matriz[7] or m==matriz[8]:
            for index in range(9):
                if index <= 2:
                    tabelas[6].append(m[index])
                if index > 2 and index <= 5:
                    tabelas[7].append(m[index])
                if index > 5 and index <= 8:
                    tabelas[8].append(m[index]) 
    return tabelas

def problema2(matriz):
    #verificando duplicatas nas linhas:
    for m in matriz:
        m = [value for value in m if value != "."]
        sem_duplicatas = sorted(list(set(m)))
        if((sem_duplicatas) != sorted(m)): 
            print('false')
            return(False) 
    #verificando duplicatas nas colunas:
    trasnposta = []
    for c in range(9):
        t = [k[c] for k in matriz]
        trasnposta.append(t)
    for m in trasnposta:
        m = [value for value in m if value != "."]
        sem_duplicatas = sorted(list(set(m)))
        if(sem_duplicatas != sorted(m)): 
            print('false')
            return(False)
    #verificando duplicatas nas mini-tabelas:
    tabelas = mini_tabelas(matriz)
    for t in tabelas:
        t = [value for value in t if value != "."]
        sem_duplicatas = sorted(list(set(t)))
        if(sem_duplicatas != sorted(t)): 
            print('false')
            return(False)            
    print('true')
    return(True)

    
    
   


# (problema2(matriz))