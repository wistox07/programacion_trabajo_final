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
    
    trabajos = []
    print("\n--- Trabajos Realizados ---")
    while True:
        hora = input("Hora (dejar en blanco para finalizar): ")
        if not hora:
            break
        trabajo = input("Trabajo Realizado: ")
        trabajos.append({"Hora": hora, "Trabajo": trabajo})

    observacion = input("\nObservación: ")
    vb_capataz = input("V.B. Capataz: ")
    vb_ing_residente = input("V.B. Ing. Residente: ")

def main():
    """Permite ingresar los datos del parte diario del martillo demoledor."""
    print("--- PARTE DIARIO MARTILLO DEMOLEDOR ---")
    equipo = input("Equipo: ")
    fecha = input("Fecha: ")
    operador = input("Operador: ")
    combustible = input("Combustible: ")
    registrar_parte_diario(equipo,fecha,operador,combustible)

if __name__ == "__main__":
    main()
