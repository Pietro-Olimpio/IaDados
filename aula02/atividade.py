#função

notas = [10, 4, 7.5, 9, 8]
print(max(notas)) # maior valor
print(min(notas)) # menor valor
print(sum(notas)) # soma 
print(len(notas)) # tamanho do array


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

notas = [n1, n2, n3, n4]

print("="*50)

print(f"A sua maior nota é {max(notas)}, a menor é {min(notas)}, a soma delas é {sum(notas)}, e vc tem {len(notas)} notas")

media = sum(notas) / len(notas)
print(f"Sua media é: {media}")

if media >6:
    print("Aprovado")
else:
    print("Reprovado")
