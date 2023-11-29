# Reporte: Funciones Lambda en Python 

## Descripción de los Módulos

### `get_user_input()`
Este procedimiento habilita al usuario para introducir dos números y elegir la operación que desea realizar. Utiliza un conjunto `try/except` para controlar posibles errores si el usuario introduce caracteres en lugar de números. Luego, devuelve una tupla que contiene los valores ingresados por el usuario.

### Funciones lambda para operaciones matemáticas
Se definen funciones lambda (`sumar`, `restar`, `multiplicar`, `dividir`) para cada operación básica (+, -, *, /). Estas funciones son utilizadas en la función `ejecutar_operacion()`.

### `ejecutar_operacion(user_input, callback)`
Esta función lleva a cabo la operación elegida por el usuario. Se vale de un diccionario llamado `operations` que asigna los operadores a las funciones lambda correspondientes. Si la operación es reconocida como válida, procede a ejecutar la operación correspondiente; de lo contrario, informa que la operación ingresada no es válida.

### `main()`
El componente principal del programa mantiene un bucle continuo hasta que el usuario ingresa la palabra 'exit'. Durante cada iteración, solicita al usuario que ingrese números y operaciones a través de la función `get_user_input()`. A continuación, verifica si la operación es reconocida como válida y, en caso afirmativo, ejecuta la operación correspondiente utilizando la función `ejecutar_operacion()`.

## Funcionamiento y Ejemplos

El código interactúa con el usuario solicitando el ingreso de dos números y la selección de una operación matemática básica (+, -, *, /). Posteriormente, lleva a cabo la operación especificada por el usuario y muestra el resultado obtenido.

### Ejemplo de Uso:

```python
# Input del usuario: 7, 2, '+'
# Resultado esperado: 7 + 2 = 9
# Output del programa: "Resultado: 9.0"

# Input del usuario: 15, 5, '/'
# Resultado esperado: 15 / 5 = 3.0
# Output del programa: "Resultado: 3.0"

# Input del usuario: 'exit' (para salir del programa)
# Output del programa: Termina la ejecución del programa
