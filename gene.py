import numpy as np

def fitness(t,A,B,C,D):
    return A*(t**B)+C*np.cos(D*t)+np.random.normal(0,1,t.shape)

def gene2coef(gene):
    A = (np.sum(2**np.arange(10)*gene[0:10])-511)/100
    B = (np.sum(2**np.arange(10)*gene[10:20])-511)/100
    C = (np.sum(2**np.arange(10)*gene[20:30])-511)
    D = (np.sum(2**np.arange(10)*gene[30:40])-511)/100
    return A,B,C,D

T = np.random.random((1000,1))*100
b = fitness(T,0.6,1.2,100,0.4)

N = 10000
G = 10
survive_rate = 0.1
survive = round(N*survive_rate)
mutation_rate = 0.0001
mutation = round(N*40*mutation_rate)
pop = np.random.randint(0,2,(N,40))
fit = np.zeros((N,1))

"""
    print(fit.shape)
    print(fit[[2,3,4]])
"""

for generation in range(10):
    for i in range(N):
        A,B,C,D = gene2coef(pop[i,:])
        fit[i] = np.mean(abs(fitness(T,A,B,C,D)-b))
    sortf = np.argsort(fit[:,0])
    pop = pop[sortf,:]
    for i in range(survive,N):
        fid = np.random.randint(0,survive)
        mid = np.random.randint(0,survive)
        while(fid==mid):
            mid = np.random.randint(0,survive)
        mask = np.random.randint(0,2,(1,40))
        son = pop[mid,:]
        father = pop[fid,:]
        son[mask[0,:]==1] = father[mask[0,:]==1]
        pop[i,:] = son
    for i in range(mutation):
        m = np.random.randint(survive,N)
        n = np.random.randint(0,40)
        pop[m,n] = 1-pop[m,n]

for i in range(N):
    A,B,C,D = gene2coef(pop[i,:])
    fit[i] = np.mean(abs(fitness(T,A,B,C,D)-b))
sortf = np.argsort(fit[:,0])
pop = pop[sortf,:]

A,B,C,D = gene2coef(pop[0,:])
print(A,B,C,D)

        
        

