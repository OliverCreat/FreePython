name = input("Qual seu nome? ")
birthYear = int(input("Qual o ano de nascimento? "))
newPatient = input("É um novo paciente? (S/N) ")
age = 2025 - birthYear


print(name, "tem ", age, " anos")
if (newPatient == "S" or newPatient == "s"):
    print(name, "é novo paciente")
else:
    print(name, "é paciente antigo")

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
x = int(num1) > int(num2)

print("O primeiro numero é maior que o segundo?", x)
