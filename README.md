# 📌 MDSS2

Este proyecto implementa un sistema de gestión de lotes de materia prima y producción para una cooperativa de productores de olivo. Se ha desarrollado en **Python**, aplicando patrones de diseño para garantizar una arquitectura modular, flexible y escalable.

## 🏗️ Estructura del Proyecto

📁 src
- analyzer.py    # Implementa el patrón Visitor para analizar los lotes
- exporter.py    # Define el patrón Strategy para exportación de reportes
- main.py    # Script principal de ejecución
- producer.py    # Define la clase Productor
- product.py    # Define la clase ProductoFinal
- production.py    # Define la clase LoteProduccion y su relación con lotes y productos
- quality.py    # Implementa el patrón Strategy para evaluación de calidad
- rawbatch.py    # Define la clase LoteMateriaPrima y su gestión de estados
- state.py    # Implementa el patrón State + Template Method para los estados del lote


## 🎯 Patrones de Diseño Aplicados

### 🕵️ Visitor (Analizadores de Imágenes)
- La clase `LoteMateriaPrima` implementa el metodo `accept()`, permitiendo que visitantes externos procesen su información.
- `AnalizadorVisitor` es una interfaz que define la estructura de los analizadores de imágenes.
- `AnalizadorMadurezVisitor` y `AnalizadorDefectosVisitor` implementan la lógica de análisis, devolviendo los resultados según el tipo de producto (aceite u oliva de mesa).

### 🔄 State + Template Method (Gestión de Estados)
- `EstadoLote` es una clase abstracta que define un **metodo plantilla** `registrar_transicion()`, asegurando que todas las transiciones sean registradas de forma uniforme.
- `Ingresado`, `EnAnalisis`, `Analizado` y `EnProduccion` extienden `EstadoLote`, definiendo el comportamiento específico de cada estado.
- `LoteMateriaPrima` mantiene una referencia a su estado actual y delega sus acciones al objeto `estado`, permitiendo transiciones dinámicas.

### 📤 Strategy (Exportación de Reportes)
- `ExportStrategy` define una interfaz para los distintos metodos de exportación.
- La clase `ExportJSONStrategy` implementa la exportación en JSON, garantizando la separación entre la lógica del negocio y el formato de salida.
- `LoteProduccion` recibe una estrategia de exportación en su método `exportar_reporte()`, permitiendo modificar el formato sin afectar su lógica interna.

### 🏆 Strategy (Evaluación de Calidad)
- `CalidadStrategy` define la interfaz para la evaluación de calidad de los productos finales.
- Las clases `CalidadAceiteVirgenExtra`, `CalidadAceiteVirgen` y `CalidadAceiteDeOrujo` evalúan la calidad del aceite en función de sus atributos.
- `ProductoFinal` asigna su calidad utilizando una de estas estrategias.

## ✅ Beneficios de la Implementación

- 🏗 **Código modular:** Cada componente tiene una única responsabilidad, lo que facilita el mantenimiento.
- 📈 **Escalabilidad:** Se pueden agregar nuevos estados, estrategias o analizadores sin afectar el código existente.
- 🔌 **Extensibilidad:** El sistema permite incluir nuevas estrategias de exportación, tipos de productos o evaluaciones de calidad sin modificar la lógica central.
- 🛠 **Separación de responsabilidades:** El uso de patrones de diseño permite que cada módulo sea independiente y reutilizable.
