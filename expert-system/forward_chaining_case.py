def bool_converter(option):
    if option.lower() == 'y':
        return True
    elif option.lower() == 'n':
        return False
    else:
        raise Exception('Error.. Tolong pilih y atau n!')

# Input
knalpot_king = bool_converter(input("Apakah knalpotnya berisik? [y/n] "))
kecepatan_135Cc = bool_converter(input("Apakah motornya sangat cepat? [y/n] "))
motor_metic = bool_converter(input("Apakah motornya tinggal gas aja? [y/n] "))
kecepatan_125Cc = bool_converter(input("Apakah motornya sering dibawa sunmori? [y/n] "))
motor_gigi = bool_converter(input("Apakah motornya menggunakan transisi manual? [y/n] "))
motor_kebun = bool_converter(input("Apakah motornya sering dilihat dikebun? [y/n] "))
   
if knalpot_king and kecepatan_135Cc:
    print("\nItu adalah rx-king")
elif motor_metic and kecepatan_125Cc:
    print("\nItu adalah scoopy")
elif motor_gigi and motor_kebun:
    print("\nItu adalah supra x")
else:
    print("\nTidak ditemukan!")