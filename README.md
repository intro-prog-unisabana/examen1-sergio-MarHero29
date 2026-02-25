[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/OLwFaIat)
# Examen 1

# Pregunta 1: Beca 
**Script:** `beca.py`

En esta pregunta, deberás crear una Calculadora de Becas. El objetivo de este programa es determinar si un promedio académico (PA), número de horas de servicio comunitario y puntaje en las Pruebas Saber Pro son suficientes para obtener la beca Andrés Bello de Excelencia Académica (ABEA).

## Parte I: Requisitos del Programa

1. El programa debe recibir como entrada estándar del usuario: `PA` (decimal), `horas` (entero), `Saber_Pro` (entero), `BI` (entero donde 0 significa "no" y 1 significa "sí"), siendo BI el Bachillerato Internacional.
2. El programa debe imprimir los datos ingresados de vuelta al usuario. A continuación se muestra un ejemplo del formato esperado.

### Entrada:
```
3.2
127
285
1
```

### Salida:
```
PA: 3.2
Horas: 127
Saber Pro: 285
BI: 1
```

**Pista:** Debes usar `input()` para recibir los valores. Ten en cuenta que **no hay un mensaje de texto como argumento**. El mensaje es un **argumento opcional** de la función `input()`, por lo que no es necesario incluirlo dentro de los paréntesis para que `input()` funcione.

## Parte II: Requisitos del Programa

> **Nota:** Comenta el `print` de la Parte I antes de comenzar la Parte II.

- Debes usar `input()` para recibir los valores. Ten en cuenta que no hay un mensaje de texto como argumento.
- El programa debe recibir la información del estudiante como entrada del usuario.
- El programa debe imprimir el valor booleano `True` si el estudiante recibirá la beca.
- El programa debe imprimir el valor booleano `False` si el estudiante no recibirá la beca.

> A continuación se presentan las reglas para determinar si se debe otorgar la beca ABEA:
> 1. Si el estudiante tiene un diploma del Bachillerato Internacional (BI), **debe** recibir la ABEA, ignorando las reglas siguientes.
> 2. Si el estudiante tiene un PA inferior a 3.5, **no puede** recibir la ABEA.
> 3. Si el estudiante tiene menos de 100 horas de servicio comunitario, **no puede** recibir la ABEA.
> 4. Si el estudiante tiene un puntaje en las Pruebas Saber Pro inferior a 260, **no puede** recibir la ABEA.

# Pregunta 2 - Encontrando la "s"

Eres un nuevo practicante en *MotoresCóndor* y tienes la tarea de encontrar, en un conjunto de 10 mensajes, cada vez que un empleado haya usado el carácter "s" en sus comunicaciones.

## Parte I
**Script:** `s_parte1.py`

Crea un programa que le pida al usuario ingresar el mensaje que desea analizar e imprima si ese mensaje contiene el carácter "s". Asegúrate de que detecte tanto mayúsculas como minúsculas.

Por ejemplo, asumiendo que el mensaje es: `Estoy bajo demasiada presión`
```plaintext
Ingresa tu mensaje:
True
```
Por ejemplo, asumiendo que el mensaje es: `Voy a la reunión`
```plaintext
Ingresa tu mensaje:
False
```

## Parte II
**Script:** `s_parte2.py`

Crea un programa que solicite 10 mensajes y al final muestre el número de mensajes que contenían el carácter "s".
***Asegúrate de que detecte tanto mayúsculas como minúsculas.***

Por ejemplo:
```plaintext
Ingresa tu mensaje:
True
Ingresa tu mensaje:
False
...
Ingresa tu mensaje:
True
3/10 mensajes contenían la letra "s"
```

# Pregunta 3: Sumas Únicas
**Script:** `sumas_unicas.py`

## Descripción

En este problema, se te da una lista de números. Tu tarea es determinar todas las posibles sumas **únicas** a partir de los números dados. Esto no incluye sumar un elemento consigo mismo.

Aquí hay dos ejemplos:

1. Si se da la lista `[0, 2, 4, 6]`, el programa debe imprimir `[2, 4, 6, 8, 10]`.
2. Si se da la lista `[-1, 2, 5, -3]`, el programa debe imprimir `[-4, -1, 1, 2, 4, 7]`.

## Requisitos del Programa

- La lista de números `nums` ya estará definida en el código como una variable.
- El programa debe recorrer todos los pares posibles de la lista y calcular su suma.
- El resultado debe ser una lista de sumas **sin duplicados**, y puede estar en cualquier orden.
- Al final, el programa debe imprimir la lista de sumas únicas.

## Notas
- Los números están restringidos a **valores enteros**.
- Asume que **cada elemento de la lista es único**, es decir, no hay valores repetidos.
- Asume que la **lista tiene 2 o más elementos**.

# Pregunta 4 - Cálculos de Ingeniería

## Tarea

En esta pregunta resolverás los siguientes **problemas independientes**, cada uno relacionado con ingeniería. El código de cada parte debe funcionar de forma independiente.

### Parte 1 - Temperatura válida
**Script:** `temp_valida.py`

Simula la recolección de lecturas de temperatura de un sistema mecánico.

- El programa debe **pedir continuamente** al usuario una temperatura en Fahrenheit hasta que ingrese un valor válido.
- ¿Qué es una temperatura válida?
  - Debe ser un número entero
  - Debe estar entre 55 y 100
```plaintext
Por favor ingresa la temperatura:
Entrada inválida, intenta de nuevo.
```
```plaintext
Por favor ingresa la temperatura:
Entrada válida.
```

**Ejemplo:**
```plaintext
Por favor ingresa la temperatura: #hola
Entrada inválida, intenta de nuevo.
Por favor ingresa la temperatura: #900
Entrada inválida, intenta de nuevo.
Por favor ingresa la temperatura: #76
Entrada válida.
```

### Parte 2 - Promedio de señales
**Script:** `promedio.py`

Se te dará una tupla `signals` con mediciones de voltaje (decimales) de un circuito. El programa debe calcular e imprimir el **voltaje promedio**.

- Asume que los valores serán correctos.

**Ejemplo:**
```plaintext
signals = (3.3, 5.0, 4.2, 3.8)
```
```plaintext
4.075
```

### Parte 3 - Registro de temperatura de material

**Script:** `registro_material.py`

Se te darán dos variables: una **temperatura (decimal)** llamada `temp` y un **nombre de material** llamado `material`. El programa debe imprimir un mensaje con el siguiente formato:

`"Temperatura registrada: X grados Celsius para el material: Y"`

**Ejemplo 1:**
```plaintext
temp = 1200
material = "Acero"
```
```plaintext
Temperatura registrada: 1200 grados Celsius para el material: Acero
```

**Ejemplo 2:**
```plaintext
temp = 850
material = "Aluminio"
```
```plaintext
Temperatura registrada: 850 grados Celsius para el material: Aluminio
```