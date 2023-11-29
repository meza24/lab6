
'''
Funcion que obtiene los numeros y la operacion a realizar por el usuario. 
'''
def get_user_input():
    # Se utiliza un try/except para evitar que el programa se caiga si el usuario ingresa un caracter en vez de un numero.
    try:
        num1 = float(input("Digite un numero (o un caracter para salir): ")) # Se utiliza float() para poder aceptar numeros decimales.
        num2 = float(input("Digite otro numero (o un caracter para salir): "))
        operation = input("Digite la operacion (+, -, *, /):  ") # Se utiliza input() para poder aceptar caracteres. 
        return num1, num2, operation # Se retorna una tupla con los valores ingresados por el usuario.
    
    # Si el usuario ingresa un caracter en vez de un numero, se imprime un mensaje de error y se vuelve a llamar la funcion.
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

# Se definen las funciones lambda para cada operacion.  
sumar = lambda x, y: x + y 
restar = lambda x, y: x - y
multiplicar = lambda x, y: x * y
dividir = lambda x, y: x / y if y != 0 else "No se puede dividir por cero"

# Funcion que ejecuta la operacion seleccionada por el usuario. 
def ejecutar_operacion(user_input, callback): # Se recibe la tupla con los valores ingresados por el usuario y la funcion lambda correspondiente a la operacion.
    num1, num2, operation = user_input
    operations = {'+': sumar, '-': restar, '*': multiplicar, '/': dividir}
    
    '''
    Esta condicion se utiliza para evitar que el programa se caiga si el usuario ingresa una operacion invalida. 
    '''
    if operation in operations:
        result = callback(num1, num2) #
    else:
        result = "Operacion invalida"
    
    print("Resultado:", result) #

# Funcion principal del programa.
def main():
    operations = {'+': sumar, '-': restar, '*': multiplicar, '/': dividir} # Se crea un diccionario con las operaciones y sus respectivas funciones lambda.
    
    '''
    Este ciclo se utiliza para que el programa se ejecute hasta que el usuario escriba 'exit'. Al final de cada iteracion se vuelve a llamar la 
    funcion get_user_input() para obtener los valores ingresados por el usuario. 
    '''
    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            break
        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("La operación ingresada no es válida. Por favor elija entre las operaciones matemáticas básicas (+, -, *, /) o escriba 'exit' para salir.salir")

if __name__ == "__main__":
    main()