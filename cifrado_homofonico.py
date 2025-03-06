import string
import random
cespeciales= ["¿", "¡", "ñ", "Ñ", "á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú", "ü", "Ü"]
specialc=list(string.punctuation) 

tabla= {'A': [28, 30, 25, 12, 46, 41, 63, 55, 14, 26],
 'B': [17],
 'C': [68, 31, 35, 2],
 'D': [72, 57, 54, 44, 81],
 'E': [40, 73, 39, 59, 11, 3, 43, 56, 89, 79],
 'F': [83],
 'G': [75],
 'H': [34],
 'I': [8, 69, 86, 27, 64, 88],
 'J': [32],
 'K': [13],
 'L': [33, 18, 49, 23],
 'M': [24, 70, 9],
 'N': [87, 6, 65, 22, 76, 1],
 'Ñ': [82],
 'O': [85, 20, 15, 45, 48, 19, 36, 16],
 'P': [21, 91],
 'Q': [74],
 'R': [29, 90, 84, 7, 50, 53],
 'S': [58, 60, 66, 47, 78, 62, 38],
 'T': [51, 67, 10, 52],
 'U': [4, 77, 37],
 'V': [80],
 'W': [42],
 'X': [71],
 'Y': [61],
 'Z': [5],
 ' ': [0]}


    
def preprocesamiento(string):
    for i in specialc:
        string = string.replace(i,"")
    return string

def homofonico(mensaje):
    cifrado=[]
    for i in mensaje:
        cifrado.append(format(random.sample(tabla[i],1)[0], '08b'))

    return cifrado

def main():
    m= str(input("Ingrese el texto a cifrar_"))
    m=preprocesamiento(m)
    m=m.upper()
    cifrado = homofonico(m)
    print("El texto cifrado es_",cifrado)

main()