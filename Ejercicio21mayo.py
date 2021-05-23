#Saludemos al usuario no hay que ser mala onda :p
print ("\nWelcome to this VAT price calculator, \nmade by Jorge Eduardo\n")

#Tomamos el valor porcentuado del IVA y dividimos entre 100 para poderlo multiplicar con el producto.
iva = int(input("Let's start by knowing the VAT percentage "))
print ("The VAT rate is " + str(iva))
iva = (iva / 100)

#Tomamos valor del producto.
priceProduct = int(input("Please enter the value of the product "))
print ("The value of the product is " + str(priceProduct), "\n")

#Hacemos la operacion y la guardamos en la variable "totalVAT" para luego poderla mostrar al usuario.
totalVAT = int(priceProduct * iva)
print ("The total VAT is: " + str(totalVAT))

#Mostramos el valor añadido del IVA al sumar el precio del producto y el IVA.
totalPrice = int(totalVAT + priceProduct)
print("The added value of VAT to your product is: " + str(totalPrice), "\n\nThank you for using this calculator.")