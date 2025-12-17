# print("Hola mundo")
# print("chau mundo")

#String - Cadenas de texto
estacion = "Estación Norte - Río Paraná"
contaminante = "eutrofización"

# print(estacion)

#Enteros / Int
muestras_tomadas = 10

#float / decimal
ph_agua = 7.5

#Boolean = Verdadero/ Falso
es_potable = True
supera_limite_legal = False

# print("muestras de: ", estacion)


caudal_rio_a = 5 #m3/s
caudal_rio_b = 12 #m3/s

#Suma 
caudal_total = caudal_rio_a + caudal_rio_b
# print("El caudal total es: ", caudal_total, "m3/s")

#Multiplicacion
distancia_km = 40
distancia_m = distancia_km * 1000
# print("La distancia en metros es", distancia_m)

#Division
manzanas_u = 10
partes = 2
total_partes_de_manzana = manzanas_u / partes
# print("El resultado es", total_partes_de_manzana)

#if / elif / else / Condicionales
ojos_de_pescado = 6

# if ojos_de_pescado == 2:
#     print("Es un pescado normal del RIo Parana")
# elif ojos_de_pescado == 3:
#     print("Es un pescado mutante de Springfield")
# else:
#     print("seguro que es un pescado?")

precio_fernet = 49999

if precio_fernet == 50000:
    print("esta bien")
elif precio_fernet > 50000:
    print("es muy caro")
else:
    print("es muy barato, compra ya!!!")


#And / or / Condicionales
auditor_en_puerta = False #llego el inspector
papeles_en_orden = False #Hicimos el reporte
tengo_cafe = False #cafe/ soborno

if auditor_en_puerta and papeles_en_orden:
    print("Todo bien, todo correcto")
elif auditor_en_puerta and not papeles_en_orden:
    if tengo_cafe:
        print("Plan b: invitale cafe mientras imprimimos los reportes")
    else:
        print("SALVENSE QUIEN PUEDA, activamos la alarma de incendio")
else:
    print("No hay auditor, seguir viendo memes")