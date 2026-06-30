#Calcule média Notas

primeiranota = float(input("Digite a primeira nota do aluno: "))
segundanota = float(input("Digite a segunda nota do aluno: "))
nota = primeiranota + segundanota 
media = (primeiranota + segundanota) / 2
if media >= 7: 
    print("Situação do Aluno: aprovado!")
elif media >= 5:
    print("Situação do Aluno: recuperação!")
else: 
    print("Situação do Aluno: reprovado!")
