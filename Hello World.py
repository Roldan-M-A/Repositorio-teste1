print("Hello World")
frase = "Hello"
for letra in frase:
    if letra == "e":
        print("Tem a letra E")

print("""
Escreva uma palavra!
      
      """)
x = input("")
numero_de_letras_a = 0
x = x.lower()
for espaco in x:
    if espaco == "a":
        numero_de_letras_a += 1

print("Você escreveu " + str(numero_de_letras_a) + " letras A!") 
contagem = 0
for y in range(1,10):
    
    if y % 2 == 0:
        contagem += 1
        print(y)
        

print(f"Há {contagem} números pares")