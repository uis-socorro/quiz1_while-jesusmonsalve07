"Programa para saber en cuantos meses pedro y pablo pueden hacer su negocio xD "

print("""------------------------------------""")
print("""----------capital intereses---------""")
print("""------------------------------------""")

#input

c1 = int(input("Digite el capital a invertir"))
c2 = int(input("Digite el segundo capital a invertir"))
c3 = int(input("Digite el capital necesario para el negocio"))
n = 0

#processing 

while (c1+c2) < c3:
 c1 = c1 +(c1 *0.03)
 c2 = c2 +(c1 * 0.04)
 n = n + 1

#output

print("Los meses que necesitan inc¿vertir para hacer el negocio es ", str(n)) 
