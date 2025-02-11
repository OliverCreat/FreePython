#Desafio Saudação
name = input("Digite seu nome: ")
print("Olá, ", name, "! Seja bem vindo(a)")

#Desafio Soma
num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
print("A soma dos números é: ", int(num1) + int(num2))

#Encontrar o maior número
# Solicita a entrada de uma lista de números separados por vírgula
entrada = input("Digite uma lista de números separados por vírgula: ")

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split(",")

# Converte cada item da lista para float, removendo espaços em branco
numeros = [float(num.strip()) for num in numeros_str]

# Encontra o maior número da lista usando a função max()
maior_numero = max(numeros)

# Exibe o maior número encontrado
print("O maior número é:", maior_numero)


#Desafio Números pares de 1 a 20
for numero in range(2, 21, 2):
    print(numero)