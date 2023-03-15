def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('Bienvenido David')

'''
variable = "texto en la variable"
print(variable)
variable = 30
print('Hi, hello worl')
print(variable)


print("operaciones matematicas en python")

x=10
y=2

z=x+y

print(x)
print(y)
print('la suma de las variables es igual a ',z)

arg1 = 22
arg2 = 45
print(f'las variables que puedo mostrar juntas con el print f son variable 1 con valor  {arg1}  y variable 2 con valor {arg2}')


print('ejemplo de variables en memoria ')
print(x)
print(y)
print(z)
print('la variable x apunta a una direccion en memoria en la siguiebte posicion en memoria ',id(x))
print('la variable y apunta a una direccion en memoria en la siguiebte posicion en memoria ',id(y))
print('la variable z apunta a una direccion en memoria en la siguiebte posicion en memoria ',id(z))


texto = 'Este texto lo estamos almacenando en la variable '
print(texto)
print(type(texto))

num = 2345
print(num)
print(type(num))

num = 2345,234
print(num)
print(type(num))

num = 2345.234
print(num)
print(type(num))


num = True
print(num)
print(type(num))


miGrupoFavorito = 'estopa '+'fania all stars'
print("mi grupo favorito es : "+ miGrupoFavorito)

print("ejemplos de parseo en python")

num1 = "23"
num2 = "32"
print(num1 + num2)
print(int(num1) + int(num2))


print('Variables tipo bools')
mi_var = False
print(mi_var)
mi_var = 2 > 1
print(mi_var)

print('Condicionales')

mi_var = 2 > 1

if mi_var:
    print("el resultado fue verdadero")
else:
    print("el resultado fue falso")

print('\n')
print("pedir datos por consola")

resultado = int(input('Como estuvo su dia de 1 a 10??'))
print('de 1 a 10 mi dia tuvo una calificacion de ',resultado)


libro = input('Digite el nombre del ultimo libro que leyó')
autor = input('Digite el nombre del autor de ese libro')

print(f'el libro {libro} fue escrito por el autor {autor}')


print('\n')


operandoA = 3
operandoB = 2

suma = operandoA + operandoB
resta = operandoA - operandoB
multiplicacion = operandoA * operandoB
division = operandoA / operandoB
division2 = operandoA // operandoB
exponente =  operandoA ** operandoB
print(f'el resultado de la suma es {suma}'
      f'\n el resultado de la resta {resta}'
      f'\n el resultado de la multiplicacion es {multiplicacion}'
      f'\n el resultado de la division es {division}'
      f'\n el resultado de la division entera es  {division2}'
      f'\n el resultado de la potencia es {exponente}')



#pedir por teclado el alto y el ancho y vamos a sacar el area y el perimetro de un rectangulo


alto = int(input('proporcionar el alto'))
ancho = int(input('proporcionar el ancho'))

area = alto * ancho
perimetro = (alto + ancho ) * 2


print(f'el area es {area}'
      f'\n el perimetro es {perimetro}')



num = 10
print(num)

num *=1
print(num)
num *=10
print(num)
num *=100
print(num)


num = 10
print(num)

num +=1
print(num)
num +=10
print(num)
num +=100
print(num)


num = 10
print(num)

num -=1
print(num)
num -=10
print(num)
num -=100
print(num)



a = 4
b = 2

result = a==b
print(f'A es igual a B ==:{result}')



result = a!=b
print(f'A es igual a B ==:{result}')


result = a>=b
print(f'A es mayor o igual a B ==:{result}')



#pedir por teclado la edad de una perosna, si es igual o mayoa 18 años mostrar que es mayo de edad y mostrar la edad ,
# si es menor muestre un mensaje que no puede entrar al motel porque tien tanytos años


edad = int(input('Digite la edad'))
tope = 18
if edad >= 18:
    print(f"como ya tienes {edad} años , puedes ingresar al establecimiento ")
else:
    print(f"lamentablemente como  tienes {edad} años , No puedes ingresar al establecimiento, regresa cuando tengas cedula ")


'''
a = True
b = False

result = a and b
print(f'resultado and {result}')

result = a or b
print(f'resultado or  {result}')

result = not a
print(f'resultado negado de a   {result}')



#valor que sea emtero , una valor minimo y lo quemamos , valor maximo lo quemamos en 20 y luego que tengamos los numero ingresados y comparamos si el valor ingresado esta en el rango

num = int(input('Digite el numero '))

min = 10
max = 20

if num >= min and num <= max:
    print(f"el numero {num} se encuentra en el rango entre {min} y {max}")
else:
    print(f"el numero {num} NO se encuentra en el rango entre {min} y {max}")



vacaciones = True
diaDescanso = False

if vacaciones or diaDescanso:
    print('amigo puede asistir al concierto ')
else:
    print('trabaje amigo ')


edad = int(input('Digite la edad'))
veinte  = edad >= 20 and edad < 30
treinta  = edad >= 30 and edad < 40

if edad >= 20 and edad  <= 29:
    print(f"se encuentra en el rango de 20 años {veinte}")
else:
    print(f"se encuentra en el rango de 30 años {treinta}")


