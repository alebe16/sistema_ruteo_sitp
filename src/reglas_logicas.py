import json
import csv
from typing import List, Dict, Optional

class BaseConocimiento:
    def __init__(self):
        self.rutas = []
        self.estaciones = {}
        self.cargar_datos()
    
    def cargar_datos(self):
        # Cargar rutas desde JSON
        with open('data/rutas_sitp.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.rutas = data['rutas']
        
        # Cargar estaciones desde CSV
        with open('data/estaciones.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.estaciones[row['nombre']] = row
    
    def obtener_rutas_por_estacion(self, estacion: str) -> List[Dict]:
        return [ruta for ruta in self.rutas if estacion in ruta['estaciones']]
    
    def obtener_estaciones_conexion(self, estacion: str) -> List[str]:
        conexiones = []
        for ruta in self.rutas:
            if estacion in ruta.get('transbordos', []):
                conexiones.extend(ruta['estaciones'])
        return list(set(conexiones))
    
    def es_transbordo(self, estacion1: str, estacion2: str) -> bool:
        rutas_estacion1 = self.obtener_rutas_por_estacion(estacion1)
        rutas_estacion2 = self.obtener_rutas_por_estacion(estacion2)
        
        # Verificar si comparten alguna ruta
        for r1 in rutas_estacion1:
            for r2 in rutas_estacion2:
                if r1['nombre'] == r2['nombre']:
                    return False
        
        # Si no comparten rutas, es un transbordo
        return True
    