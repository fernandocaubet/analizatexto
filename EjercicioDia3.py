texto = input("ingrese un texto: ").lower()
print('para un buen analisis ingrese 3 letras')
a = input('ingrese primera letra: ').lower()
b = input('ingrese segunda letra: ').lower()
c = input('ingrese tercera letra: ').lower()
print("***********************")
print("PRIMERO: ")
print("la letra "+ str(a) +" aparece >>> "+ str(texto.count(a))+ " veces")
print("la letra "+ str(b) +" aparece >>> "+ str(texto.count(b))+ " veces")
print("la letra "+ str(c) +" aparece >>> "+ str(texto.count(c))+ " veces")
textolista = texto.split()
print(f"SEGUNDO: hay un total de {str(len(texto.split()))} palabras en el texto")
print(f"TERCERO: la primera letra es >>> {texto[0]}  <<< y la ultima letra es >>> {texto[-1]} <<<")
textolista.reverse()
print("CUARTO: El texto invertido quedaria asi >>> "+" ".join(textolista))
dic ={True:"SI",False:"NO"}
print(f"QUINTO: La palabra'PYTHON' {dic["python" in textolista]} se encuentra en el texto")


