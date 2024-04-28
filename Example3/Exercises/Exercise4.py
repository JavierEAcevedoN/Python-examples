"""Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo."""
def m_c_d(num1, num2):
    if num2 == 0:
        return num1
    else:
        return m_c_d(num2, num1 % num2)

def m_c_m(num1, num2):
    return (num1 * num2) // m_c_d(num1, num2)

num1 = int(input("ingresa un 1° numero "))
num2 = int(input("ingresa un 2° numero "))

mcd = m_c_d(num1, num2)
print(f"el maximo comun divisor de {num1} y {num2} es {mcd}")

mcm = m_c_m(num1, num2)
print(f"el minimo comun multiplo de {num1} y {num2} es {mcm}")