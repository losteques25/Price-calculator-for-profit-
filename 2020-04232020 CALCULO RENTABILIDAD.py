   
y=float(input("El costo, incluyendo el IVA es de USD:     "))
r=float(input("¿Cuanto desea ganar en porcentaje , 20%, 30%, etc?:       "))
pcm=(y/(100-r))*100
print("El precio con una rentabilidad de",r," % es de $", round(pcm,2))    
