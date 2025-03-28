from typing import List, Dict, Tuple, Optional
from src.reglas_logicas import BaseConocimiento

class SistemaRuteo:
    def __init__(self):
        self.base = BaseConocimiento()
    
    def encontrar_ruta(self, origen: str, destino: str) -> Tuple[List[Dict], int]:
        """
        Encuentra la mejor ruta entre origen y destino usando reglas lógicas
        
        Returns:
            Tuple con (lista de pasos, tiempo estimado en minutos)
        """
        # Verificar si están en la misma ruta
        ruta_directa = self._buscar_ruta_directa(origen, destino)
        if ruta_directa:
            return ruta_directa
        
        # Buscar con un transbordo
        ruta_transbordo = self._buscar_con_transbordo(origen, destino)
        if ruta_transbordo:
            return ruta_transbordo
        
        # Si no hay ruta directa ni con un transbordo
        return ([], 0)
    
    def _buscar_ruta_directa(self, origen: str, destino: str) -> Optional[Tuple[List[Dict], int]]:
        """Busca si hay una ruta que conecte origen y destino sin transbordos"""
        rutas_origen = self.base.obtener_rutas_por_estacion(origen)
        
        for ruta in rutas_origen:
            if destino in ruta['estaciones']:
                idx_origen = ruta['estaciones'].index(origen)
                idx_destino = ruta['estaciones'].index(destino)
                
                # Determinar dirección
                if idx_origen < idx_destino:
                    estaciones_ruta = ruta['estaciones'][idx_origen:idx_destino+1]
                else:
                    estaciones_ruta = ruta['estaciones'][idx_destino:idx_origen+1][::-1]
                
                tiempo = len(estaciones_ruta) * 3  # 3 minutos por estación
                
                return ([{
                    'ruta': ruta['nombre'],
                    'tipo': ruta['tipo'],
                    'estaciones': estaciones_ruta,
                    'transbordo': False
                }], tiempo)
        
        return None
    
    def _buscar_con_transbordo(self, origen: str, destino: str) -> Optional[Tuple[List[Dict], int]]:
        """Busca una ruta que requiera un transbordo"""
        rutas_origen = self.base.obtener_rutas_por_estacion(origen)
        rutas_destino = self.base.obtener_rutas_por_estacion(destino)
        
        for ruta_o in rutas_origen:
            for estacion in ruta_o['estaciones']:
                if estacion == origen:
                    continue
                
                # Verificar si esta estación tiene conexión a una ruta que lleve al destino
                for ruta_d in rutas_destino:
                    if estacion in ruta_d['estaciones']:
                        # Construir primera parte de la ruta (origen -> transbordo)
                        idx_origen = ruta_o['estaciones'].index(origen)
                        idx_transbordo_o = ruta_o['estaciones'].index(estacion)
                        
                        if idx_origen < idx_transbordo_o:
                            estaciones_ruta1 = ruta_o['estaciones'][idx_origen:idx_transbordo_o+1]
                        else:
                            estaciones_ruta1 = ruta_o['estaciones'][idx_transbordo_o:idx_origen+1][::-1]
                        
                        # Construir segunda parte de la ruta (transbordo -> destino)
                        idx_transbordo_d = ruta_d['estaciones'].index(estacion)
                        idx_destino = ruta_d['estaciones'].index(destino)
                        
                        if idx_transbordo_d < idx_destino:
                            estaciones_ruta2 = ruta_d['estaciones'][idx_transbordo_d:idx_destino+1]
                        else:
                            estaciones_ruta2 = ruta_d['estaciones'][idx_destino:idx_transbordo_d+1][::-1]
                        
                        # Calcular tiempo total
                        tiempo = (len(estaciones_ruta1) * 3 + 
                                 len(estaciones_ruta2) * 3 + 
                                10)  # 10 minutos para transbordo
                        
                        return ([{
                            'ruta': ruta_o['nombre'],
                            'tipo': ruta_o['tipo'],
                            'estaciones': estaciones_ruta1,
                            'transbordo': False
                        }, {
                            'ruta': ruta_d['nombre'],
                            'tipo': ruta_d['tipo'],
                            'estaciones': estaciones_ruta2,
                            'transbordo': True
                        }], tiempo)
        
        return None
    