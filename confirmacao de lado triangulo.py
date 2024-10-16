# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = input("Defina o tamanho do lado 1 do triangulo")
lado2 = input("Defina o tamanho do lado 2 do triangulo")
lado3 = input("Defina o tamanho do lado 3 do triangulo")

if lado1 == lado2 : #No equilatero não teve muita magia, foi mais a ideia de ser tudo igual, então é uma comparaçãodireta
    if lado2 == lado3:
        print("Seu triangulo é equilatero")

if lado1 != lado2: #Aqui como foram apenas duas confimações, fiz elas da maneira mais pratica possivel, fazendo a comparação direta
    if lado1 ==lado3:
        print ("Seu triangulo pe isoceles")
if lado2 != lado3:
    if lado2 == lado1:
        print ("Seu triangulo pe isoceles")

if lado1 != lado2: #logica direta... Se fora um lado diferente do outro, logo é escaleno
    if lado1 != lado3:
        print ("Seu triangulo pe escaleno")

#ASS: CrazyOreo/Pedro Macegosa