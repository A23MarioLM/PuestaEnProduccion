#test_fibo.py

#############
###parte 2###
#############
# Importamos libreria unittest
import unittest

#############
###parte 1###
#############

# Función de Fibonacci que devuelve solo el número en la posición indicada
def fibonacci_numero_en_posicion(posicion):
    # Variables de inicio de los números
    numero1, numero2 = 0, 1
    
    # Bucle for para iteración numérica
    for _ in range(posicion - 1):
        # Actualizamos los valores de numero1 y numero2 para la siguiente iteración
        numero1, numero2 = numero2, numero1 + numero2

    # Devolvemos el valor de numero1, que es el número en la posición indicada 
    #print(numero1)
    return numero1

#fibonacci_numero_en_posicion(5)

#############
###parte 3###
#############
# Clase de prueba que hereda de unittest.TestCase
class TestFibonacci(unittest.TestCase):

    # Función de prueba para la quinta posición de la serie
    def test_quinta_posicion(self):
        # Calculamos el número en la quinta posición utilizando tu implementación de Fibonacci
        result = fibonacci_numero_en_posicion(5)
        # Verificamos si el resultado es igual al número esperado para la quinta posición
        self.assertEqual(result, 3, "La quinta posición debe ser 3 en la secuencia de Fibonacci.")

#############
###parte 4###
#############
# Verificamos si este archivo se ejecuta directamente y ejecutamos las pruebas
if __name__ == '__main__':
    unittest.main()

