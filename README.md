
## Instrucciones Generales
- El archivo **debe** llamarse **Examen3.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación solo por **recursión** 
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**
- Recordar que en este caso por evaluar vectores o matrices **no se debe recortar**, solo el recorrido es por sus índices
- Pueden hacer uso **Try/Except, isinstance, type**
- Pueden hacer el uso de las funciones que se va creando durante el examen
- En todos los problemas aquí expuestos debe de validarse:
	-  de que los vectores acepten solo números enteros
	-  la matriz no debe ser nula
	-  deben ser homogéneas y del mismo largo
	-  los mensajes de error deben ser claros
- Cada pregunta vale 10 puntos:
 	- 1 punto comentarios
 	- 2 puntos validaciones
 	- 7 puntos resolución del problema
 - Usar el **IDLE de Python**, no usar **VSCode**


## numeroHermano(num)

Escriba un programa con sintaxis Python cuya función principal se llame **numeroHermano(num)**, que reciba como entrada un **número entero positivo** denominado num y que retorne si cumple (True) o no los requisitos (False) de número hermano. Un número hermano es un número natural y que posee al menos dos divisores primos (el 1 no es primo):

Ejemplos del comportamiento de la función:

```python
>>>numeroHermano(20) #(divisores propios: 2, 4, 5, 10)
True
>>> numeroHermano(8) #(divisores propios: 2,4)
False
>>> numeroHermano(-8)
"Error en la entrada, debe ser número positivo"
```

## esVectorOrdenado(vector, forma)

Escriba un programa con sintaxis Python cuya función principal se llame **esVectorOrdenado(vector, forma)**, que reciba como entradas un **vector** y una **forma**, este último será un string que especificará si el vector está ordenado en forma **ascendente o descendente**. Esta función retornará **True** si el vector corresponde al tipo de ordenamiento o **False** del caso contrario. No se puede usar su representación inversa o reversa del número

Los valores para **forma** son:  'asc' o 'desc'

```python
>>> esVectorOrdenado([23, 656, 5533, 8120], 'asc')
True
>>> esVectorOrdenado([15, 4, 0], 'desc')
True
>>> esVectorOrdenado([11, 45], 'desc')
False
```

## digitoMayoryMenor(lista)

Escriba un programa con sintaxis Python cuya función principal se llame **digitoMayoryMenor(lista)**, que reciba como entrada una **lista** con número **enteros**, y que retorne una lista de nuevos números que estará compuesto por los dígitos mayor y menor del número analizado.

```python
>>> digitoMayoryMenor([2300, 6756])
[30, 75]
>>> digitoMayoryMenor([2300, 6756, -99, 1001, 91823])
[30, 75, -99, 10, 91]

```

## numero polimax

Escriba una función llamada esPolimax(num) que reciba como entrada un número entero positivo num y determine si es un "Número Polimax". Un número es Polimax si, al dividirlo en dos mitades de igual longitud, ambas mitades tienen la misma cantidad de dígitos pares e impares. Si el número tiene una cantidad par de dígitos, y las dos mitades tienen la misma cantidad de dígitos pares e impares, la función debe retornar True; de lo contrario, debe retornar False.

```python
>>> esPolimax(123321)
True  # Mitades: 123 y 321 (1 par, 2 impares en cada mitad)
>>> esPolimax(1221)
False # Mitades: 12 y 21 (1 par, 1 impar en la primera mitad; 0 pares, 2 impares en la segunda mitad)
>>> esPolimax(123456)
False # Mitades: 123 y 456 (0 pares, 3 impares en la primera mitad; 3 pares, 0 impares en la segunda mitad)
>>> esPolimax(4444)
True  # Mitades: 44 y 44 (2 pares, 0 impares en cada mitad)
>>> esPolimax(123)
False # Cantidad impar de dígitos
```
