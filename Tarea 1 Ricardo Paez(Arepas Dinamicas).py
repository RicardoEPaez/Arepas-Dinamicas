#Este programa calcula la masa resultante, el numero de arepas
#de una receta de masa de arepas de acuerdo a la harina 
#utilizar que indique al usuario

#receta original harina pan
# 2 x tazas de harina
# 2.5 x tazas de agua
# 1 x cucharita de sal


numero_de_taza_harina = float(input('Indica el numero de tazas de harina al utilizar: '))
cantidad_taza_agua = numero_de_taza_harina * 2.5 / 2
cantidad_cucharita_sal = numero_de_taza_harina * 0.5


#calculamos la masa resultante y la cantidad de arepas 
# una taza de harina pesa 150 gr
# 1 cucharita de sal pesa 8 gr
# 1 taza de agua pesa 250 gr
masa_final_arepas = (numero_de_taza_harina * 150)+ (cantidad_cucharita_sal * 8) + (cantidad_taza_agua * 250)
cantidad_arepas = numero_de_taza_harina * 5 

print("Cantidad de ingredientes: ")
print("----------------------------------------")
print("Tazas de harina: ", numero_de_taza_harina)
print("Tazas de agua: ", cantidad_taza_agua)
print("Cucharitas de sal: ", cantidad_cucharita_sal)
print("----------------------------------------")
print("La cantidad de masa resultante es de " , masa_final_arepas, "gr.")
print("Con el numero de taza de harina", numero_de_taza_harina, "La cantidad de arepas es de" , cantidad_arepas)
