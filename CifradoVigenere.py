A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

diccionario = {A[i]: i for i in range(len(A))}
def caesar(k,codigo):
    return (codigo+k)%len(A)

def codificar(frase):
    codigo=[]
    for i in frase:
        codigo.append(diccionario[i])
    return codigo

def main():
    frase=input("Ingrese la frase a cifrar:_")
    frase=frase.upper()
    k=str(input("Ingrese la llave:_")).upper()
    for i in k:
        if i not in A:
            print(f"El caracter {i} no está definido")
            return 0
    codigo=[]
    codigo_cifrado=[]
    cifrado=[]
    llave=[]
    
    llave = codificar(k)
    codigo = codificar(frase)
    j=0
    for i in  codigo:
        if j==len(llave):
            j=0
            codigo_cifrado.append(caesar(llave[j],i))
        else:
            codigo_cifrado.append(caesar(llave[j],i))
            j=+1
    
    for i in codigo_cifrado:
        cifrado.append(A[i])
    print(f"El cifrado es: {cifrado}")

main()
