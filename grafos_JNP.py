# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:23:43 2023

@author: Judit Nieto Parla
    
"""

############################# APARTADO 1 ###################################

from pyspark import SparkContext
import sys

# El nodo mayor siempre lo pone a la derecha
def mapper(line):
    edge = line.split(',')
    n1 = edge[0]
    n2 = edge[1]
    if n1 < n2:
         return (n1,n2)
    elif n1 > n2:
         return (n2,n1)
    else:
        pass #n1 == n2
        
def mapper1(line):
    edge = line.split(',')
    n1 = edge[0]
    n2 = edge[1]
    return [(n1,n2), (n2,n1)]

def posibilidades(elem):
    result=[]
    for i in range(len(elem[1])):
        result.append(((elem[0],elem[1][i]),'exists'))
    num= len(result)
    for i in range(num-1):
        for j in range(i+1,num):  
            result.append(((result[i][0][1],result[j][0][1]),('pending',elem[0])))
    return result
 
def triciclo(lista):
    result=[]
    for i in range(len(lista)):
        if lista[i][1][0]=='pending':
            for j in range(i+1,len(lista)):
                if lista[j][1]=='exists' and lista[j][0]==lista[i][0]:
                    result.append((lista[i][1][1],lista[i][0][0],lista[i][0][1]))
    return result

def main(sc, filename):
    graph = sc.textFile(filename)
    
    graph=graph.flatMap(mapper)
    
    graph=graph.filter(lambda x: x[0]!=x[1])
    
    graph=graph.map(mapper1)
    
    graph=graph.distinct()
    
    graph=graph.groupByKey()
    
    graph=graph.map(lambda x: (x[0],tuple(sorted(x[1]))))
    
    graph=graph.flatMap(posibilidades)
    
    print(triciclo(graph.collect()))
    


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 {0} <file>".format(sys.argv[0]))
    else:
        with SparkContext() as sc:
            sc.setLogLevel("ERROR")
            main(sc, sys.argv[1])
            