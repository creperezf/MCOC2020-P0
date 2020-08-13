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

