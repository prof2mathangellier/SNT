def conversion_ms_kmh(vitesse_en_ms):
    vitesse_en_km_h = vitesse_en_ms * 3600 / 1000 # 3600 secondes pour 1 heure et 1000 mètres pour 1 kilomètre
    return vitesse_en_km_h # la fonction 'retourne' la réponse

def farenheit_celcus(temperature_f):
    temperature_c = temperature_f*1.8 + 32
    return temperature_c
    

vitesse1 = float(input('entrer une vitesse en m/s : '))
vitesse2 = conversion_ms_kmh(vitesse1)
print('une vitesse de ',vitesse1,' en m/s correspond à une vitesse de ',vitesse2,' en km/h')
