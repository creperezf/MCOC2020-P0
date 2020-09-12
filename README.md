# MCOC2020-P0

# Mi computador

 Marca/modelo: toshiba satellite radius P55W-B5162SM
* Tipo: Notebook
* Año adquisición: 2015
* Procesador:
  * Marca/Modelo: Intel Core i7-5550K
  * Velocidad Base: 2.40 GHz
  * Velocidad Máxima: 2.90 GHz
  * Numero de núcleos: 2 
  * Numero de hilos: 4
  * Arquitectura: x64_64
  * Set de instrucciones: Intel SSE4.1, Intel SSE4.2, Intel AVX2
* Tamaño de las cachés del procesador
  * L1d: 128KB
  * L1i: 128KB
  * L2: 512KB
  * L3: 4,0MB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 1600 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: INTEL(R) HD Graphics 5500
  * Memoria dedicada: 512 MB
  * Resolución: 1920 x 1080
* Disco: 
  * Marca: Toshiba
  * Tipo: HDD
  * Tamaño: 931,51GB
  * Particiones: 4
  * Sistema de archivos: NTFS, FAT32

* Dirección MAC de la tarjeta wifi:  00-FF-9A-74-4C-14 
* Dirección IP (Interna, del router): 192.168.1.21
* Dirección IP (Externa, del ISP): 190.217.205.101
* Proveedor internet: Telefonica del Sur

# Desempeño MATMUL
 
 ![image](https://user-images.githubusercontent.com/69158551/89689590-b59e3e80-d8d2-11ea-89e7-a76008cb0457.png)

  * Comentarios:
 
    * ¿Como difiere del gráfico del profesor/ayudante?
      * difiere bastante en los tiempos empleados en la ejecución de mi programa. tardando considerablemente más el mio.
    * ¿A qué se pueden deber las diferencias?
      * Esta diferencia se puede deber a la diferencia de procesador y a la cantidad de memoria ram que tienen los computadores.
    * El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
      * El gráfico con el tiempo utilizado para resolución de las matrices no es lineal debido a que cuando el proceso se estaba realizando el pc estaba al mismo tiempo realizondo otras acciones, haciendo que la memoria ram no este dedicada 100% en la solución de las matrices.
    * ¿Qué versión de python está usando?
      * python 3.8
    * ¿Qué versión de numpy está usando?
      * versión 1.18.5
    * Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
      * En la gráfica se puede ver que en un punto llega a mas del 100% de su capacidad por lo que debería usar 2 procesadores.
 
![WhatsApp Image 2020-08-07 at 20 25 58](https://user-images.githubusercontent.com/69158551/89698201-efc90980-d8ed-11ea-899e-514e7952712c.jpeg)
      
# Desempeño mimatmul

![grafica2 mimatmul](https://user-images.githubusercontent.com/69158551/89828612-453c2b00-db27-11ea-9cfb-0dd6fc7377cf.png)
  * Como se puede ver en la gráfica solo se realizó hasta la matriz de 1000x1000, dado que se demoraba bastante en obtener los resultados. Esto se debe a que mi función trabaja en un nivel mucho mas elevado que el matmul, el cual trabaja a un nivel inferior, optimizando el proceso, permitiendo tiempos bastante mas bajos.
  
# Desempeño inversa de matriz A:
  * El rendimiento de la matriz inversa de A en half, no se pudo sacar al igual que la de longdouble, dando como error:  
    * TypeError: array type float16 is unsupported in linalg  
    * TypeError: array type float64 is unsupported in linalg 

![image](https://user-images.githubusercontent.com/69158551/90090683-a95f1a80-dcf2-11ea-9e4d-09310c35f9b6.png)

![image](https://user-images.githubusercontent.com/69158551/90090693-aebc6500-dcf2-11ea-9151-513f6bb2402e.png)

# Entrega 5

![grafica_Ax=B](https://user-images.githubusercontent.com/69158551/90441997-e4bd6880-e0a7-11ea-9c13-28efb409c62e.png)


# Entrega 6 (solvers de scipy):
![imagen entrega 6](https://user-images.githubusercontent.com/69158551/90440977-20efc980-e0a6-11ea-93e7-5e32ab5dc7cb.png)
  * En la gráfica se puede ver claramente que los mejores desempeños los tienen los solvers de scipy siendo el con el mejor desempeño el solver con la función pos overwrite_a=True.
  y el con el peor desempeño es hacer la inversa para solucionar el problema. Esto se debe a que esta función es la orden mas directa de todas las demás, ya que usa un lennguaje de programación de bajo nivel para realizar la orden, realizandola de una forma mas directa.
  Además el primer solver de scipy es el que tiene un mejor desempeño en un comienzo a matrices inferios a 100x100, como se ve en la curva naranja. Pero pasado el valor N=100 comienza a caer con respecto a los otros 4 solvers de scipy.

# Entrega 7
  * Gráficos:
    * Matriz llena SOLVE: ![grafico_llena_SOLVE](https://user-images.githubusercontent.com/69158551/90947122-63e0d280-e401-11ea-845a-fb5c81a918ef.png)
    * Matriz llena MATMUL: ![grafico_llena_MATMUL](https://user-images.githubusercontent.com/69158551/90947125-68a58680-e401-11ea-8b4c-b9452b6298d8.png)
    * Matriz llena INVERSA: ![grafica_llena_INVERSA](https://user-images.githubusercontent.com/69158551/90947128-6c390d80-e401-11ea-8b94-af8ccf7b3f8a.png)
    * Matriz llena SOLVE: ![grafica_dispersa_SOLVE](https://user-images.githubusercontent.com/69158551/90947133-72c78500-e401-11ea-84d7-ed075794ecfd.png)
    * Matriz llena MATMUL: ![grafica_dispersa MATMUL](https://user-images.githubusercontent.com/69158551/90947138-765b0c00-e401-11ea-8696-80c4ca41d22f.png)
    * Matriz llena INVERSA: ![grafica_dispersa_INVERSA](https://user-images.githubusercontent.com/69158551/90947140-7955fc80-e401-11ea-94d1-2e744c1ff8f4.png)
 
 * Matrices laplacianas: (https://github.com/creperezf/MCOC2020-P0/blob/master/entrega%207/matrices_laplace.py)
 
 * Preguntas:
 
   *1. La diferencia que hay entre las matrices llenas y dispersas es que en los tres casos que se utilizaron las dispersas el proceso se optimizó con respecto a la de las matrices llenas ya que el entrega mas información al computador haciendo que la realizacion del cálculp de matrices tenga tiempos sean inferiores.
   
   *2. El comportamiento asintótico en la mayoria de los casos fue para la recta O(N) que se ve en amarillo y tambien para la recta O(N$^2$) que se ve en verde, pero a medida que va creciendo el N, la recta se va alejando de la curva de los tiempos obtenidos.
   
   *3. A medida que aumenta el tamaño de la matriz los tiempos aumentan exponencialmente con ella, y todas los puntos de las iteraciones se van pareciendo mas.
   
   *4. Las corridas para matrices mas bajas son menos estables teniendo puntos completamente distintos, pero a medida que aumentan las matrices los puntos se van estabilizando quedando casi exactos en los tiempos.
   
 
#Entrega Final
  * comentarios:
    En esta entrega los cambios realizados fueron bastante grandes, ya que no logré alcanzar a realizar la entrega 6 cuando tuve que haberlo reaalizado.
    Los resultados obtenidos son bastante cercanos a los reales pero aun así se alejan en varios km de lo que se quiere obtener. Para mejorarlo habría que emplear la mayor cantidad de correcciones posibles. J4,J5,J6,J7...J10 y hasta donde se pueda llegar.
 
    





  
