# grafos

Los grafos están definidos como listas de aristas.

1. Los 3-ciclos muestran una relación estrecha entre 3 entidades (vértices),
    cada uno de los vértices está relacionado con los otros dos
    
    Ejemplo:
        {(B,B),(B,A),(C,A),(A,B),(A,D),(B,C),(F,A),(F,D)}
        
        Está formado por dos 3-ciclos:
            
            {(A,B,C),(D,A,F)}
            
    Se puede suponer que el grafo de partida, es decir, la lista de aristas
    que lo representa, está simplificada. Es decir, no tiene repeticiones, ni 
    aristas de un nodo a sí mismo. Una vez resuelto el problema con esta
    restricción, no es difícil pasar al caso general.
    
    Primero construimos la lista de adyacencias considerando nodos posteriores
    
        A  [B,C,D,F]
        B  [C]
        C  []
        D  [F]
        F  []
        
    Si suponemos que tenemos la lista de adyacencias de un nodo, por ejemplo,
    el nodo A, entonces a este nodo le podemos asociar la lista:
        
        [((A,B), exists), 
         ((A,C), exists),
         ((A,D), exists),
         ((A,F), exists),
         ((B,C) , (pending, A))
         ((B,D) , (pending, A))
         ((B,F) , (pending, A))
         ((C,D) , (pending, A))
         ((C,F) , (pending, A))
         ((D,F) , (pending, A))]
        
2. Datos en múltiples ficheros
    Suponemos que la lista de las aristas no están en un único fichero, sino 
    en muchos.
    Escribir un programa que calcule los 3-ciclos de un grafo que se encuentra
    definido en múltiples ficheros de entrado.
    
3. 3-ciclos locales
    Supongamos que los datos del grafo se encuentran repartidos en múltiples
    ficheros. Queremos calcular los 3-ciclos, pero sólamente aquellos que sean
    locales a cada uno de los ficheros.
    Escribir un programa que calcule independientemente los 3-ciclos de cada
    uno de los ficheros de entrada.
