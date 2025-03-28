from src.sistema_ruteo import SistemaRuteo

def mostrar_ruta(pasos: list, tiempo: int):
    print("\n--- Ruta Encontrada ---")
    for i, paso in enumerate(pasos, 1):
        print(f"\nPaso {i}: Tomar ruta {paso['ruta']} ({paso['tipo']})")
        print(f"Estaciones: {' → '.join(paso['estaciones'])}")
        if paso.get('transbordo', False):
            print("¡Realizar transbordo aquí!")
    print(f"\nTiempo estimado: {tiempo} minutos")

def main():
    sistema = SistemaRuteo()
    
    print("Sistema de Ruteo Inteligente SITP Bogotá")
    print("---------------------------------------")
    
    origen = input("Ingrese estación de origen: ")
    destino = input("Ingrese estación de destino: ")
    
    pasos, tiempo = sistema.encontrar_ruta(origen, destino)
    
    if pasos:
        mostrar_ruta(pasos, tiempo)
    else:
        print("No se encontró una ruta entre las estaciones especificadas.")

if __name__ == "__main__":
    main()
    