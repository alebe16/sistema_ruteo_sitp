# Sistema Inteligente de Ruteo para Transporte Masivo (SITP)

Este proyecto implementa un sistema inteligente de ruteo para el transporte masivo en ciudades, utilizando **sistemas basados en conocimiento** y **reglas lógicas** para la toma de decisiones inteligentes sobre rutas, transbordos y tiempos de viaje. El sistema está diseñado para optimizar los tiempos de traslado y mejorar la planificación de viajes en redes de transporte urbano.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Pruebas](#pruebas)
- [Tecnologías](#tecnologías)
- [Limitaciones y Mejoras Futuras](#limitaciones-y-mejoras-futuras)


## Descripción

El **Sistema Inteligente de Ruteo para Transporte Masivo** (SITP) utiliza un enfoque basado en reglas lógicas y sistemas basados en conocimiento para modelar las rutas, estaciones y conexiones dentro de la red de transporte. El sistema es capaz de encontrar rutas directas y con transbordos entre diferentes estaciones, estimar tiempos de viaje y ofrecer soluciones inteligentes para los usuarios.

### Conclusiones del Desarrollo

1. **Implementación de Sistemas Basados en Conocimiento:**
   - El proyecto ha demostrado la efectividad de los sistemas basados en conocimiento para resolver problemas complejos de transporte urbano. Utilizando una base de conocimiento estructurada (JSON/CSV), el sistema toma decisiones inteligentes que son comparables a soluciones comerciales.

2. **Ventajas del Enfoque de Reglas Lógicas:**
   - **Flexibilidad:** Las reglas lógicas permiten una fácil adaptación a cambios en la red de transporte.
   - **Transparencia:** La lógica de decisión es completamente explicable, a diferencia de modelos de "caja negra".
   - **Mantenibilidad:** Las reglas pueden ser actualizadas sin necesidad de modificar el código fuente.

3. **Retos Técnicos:**
   - La complejidad de los transbordos y la dependabilidad de los datos de entrada han sido desafíos técnicos importantes.
   - La escalabilidad es una preocupación para redes de transporte muy grandes.

4. **Logros del Prototipo:**
   - Implementación de búsqueda de rutas directas y con transbordos.
   - Estimación realista de tiempos de viaje.
   - Arquitectura modular que separa claramente la **base de conocimiento** (datos) y el **motor de inferencia** (lógica).

5. **Aprendizajes Clave:**
   - La estructuración adecuada del conocimiento es crucial.
   - Los sistemas basados en reglas son ideales en dominios con regulaciones explícitas y estructuras jerárquicas claras.
   - Python ha sido excelente para el prototipado rápido de sistemas inteligentes.

6. **Limitaciones y Mejoras Futuras:**
   - Incorporación de **datos en tiempo real** mediante APIs de transporte.
   - Optimización avanzada con algoritmos como **A* o Dijkstra**.
   - Desarrollo de una **interfaz gráfica** para visualización interactiva de rutas.
   - Incorporación de **aprendizaje automático** para predicciones de demanda y congestión.

7. **Impacto Potencial:**
   - Este sistema puede mejorar la movilidad urbana al reducir la incertidumbre en la planificación de viajes, optimizar los tiempos de traslado y democratizar el acceso a la información de transporte.

### Reflexión Final:
Este proyecto ha validado que, a pesar de ser un prototipo, el uso de **técnicas clásicas de inteligencia artificial (IA)** como los **sistemas basados en reglas** puede ser una solución eficaz para problemas complejos de transporte, subrayando la importancia de un enfoque riguroso en la ingeniería del conocimiento.

## Instalación

1. **Clona el repositorio:**

   git clone https://github.com/alebe16/sistema_ruteo_sitp.git

   cd sistema_ruteo_sitp

2. **Instala las dependencias:**

pip install -r requirements.txt

3.  **Uso**

Para usar el sistema de ruteo, simplemente ejecuta el archivo main.py:
python src/main.py

El sistema te permitirá ingresar una estación de origen y destino y te devolverá la mejor ruta, incluyendo las rutas directas y los transbordos si es necesario.

**Ejemplo de uso:**

Ingrese la estación de origen: "Suba Av Boyacá"
Ingrese la estación de destino: "Suba Calle 100"
Ruta recomendada: ["Suba Av Boyacá"]
Tiempo estimado: 15 minutos**

4. **Pruebas**
El proyecto incluye pruebas unitarias para verificar el correcto funcionamiento del sistema de ruteo. Las pruebas están en el directorio tests/ y puedes ejecutarlas con:

python -m unittest tests/test_ruteo.py

5. **Tecnologías**
- Lenguaje: Python 3.9+
- Librerías principales: pandas, networkx, unittest
- Estructura de datos: JSON, CSV (para la base de conocimiento)

6. **Limitaciones y Mejoras Futuras**

- Datos en tiempo real: La incorporación de APIs de transporte permitirá una actualización dinámica de las rutas.
- Optimización avanzada: Implementación de algoritmos más avanzados, como A* o Dijkstra, para encontrar rutas óptimas.
- Interfaz gráfica: Desarrollo de visualizaciones interactivas para facilitar la interacción del usuario.
- Integración de aprendizaje automático: Para predecir la demanda y congestión del sistema.

 
