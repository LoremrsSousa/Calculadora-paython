from calculadora import Calculadora

num1 = float(input("Adicione o primeiro numero: "))
num2 = float(input("Adicione o segundo numero: "))
operacao = int(input("1 - somar: \n 2 - dividir: \n 3 - multiplicar: \n 4 - subtrair: "))



CalculadoraObj = Calculadora(num1, num2)

if operacao == 1:
    resultado = CalculadoraObj.somar()
elif operacao == 2:
    resultado = CalculadoraObj.dividir
elif operacao == 3:
    resultado = CalculadoraObj.multiplicar
elif operacao == 4:
     resultado = CalculadoraObj.subtrair

print(str(resultado))


   
