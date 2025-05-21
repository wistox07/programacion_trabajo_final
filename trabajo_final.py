def registrar_parte_diario(equipo, fecha, operador, combustible):
    tipo_equipo = ""
    while tipo_equipo not in ["Propio","Alquilado"]:
        tipo_input = input("Tipo de Equipo (Propio/Alquilado):").capitalize()
        if tipo_input == "Propio":
            tipo_equipo = "Propio"
        elif tipo_input == "Alquilado":
            tipo_equipo = "Alquilado"
        else : 
            print("Por favor , ingrese 'Propio' o 'Alquilado'.")


if __name__ == "__main__":
    registrar_parte_diario("EQUIPO","2025-01-01","","REGULAR")