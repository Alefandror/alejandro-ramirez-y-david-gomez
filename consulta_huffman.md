# Informe: Árboles de Huffman

**Integrantes:**
* David Gomez - Código: [2252119]
* Alejandro Ramirez - Código: [2250930]

---

## 1. Introducción
[cite_start]El **Árbol de Huffman** es un algoritmo de compresión de datos sin pérdida desarrollado por David Huffman en 1952[cite: 36]. Se basa en un modelo de codificación de longitud variable, lo que significa que no todos los caracteres ocupan el mismo espacio en memoria.

## 2. Funcionamiento del Algoritmo
El objetivo es optimizar el almacenamiento asignando códigos binarios más cortos a los elementos que más se repiten. 

### Pasos para la construcción:
1. **Frecuencia:** Se identifica la cantidad de veces que aparece cada símbolo.
2. **Creación de Nodos:** Cada símbolo se convierte en un nodo hoja con su respectiva frecuencia.
3. **Unión de Mínimos:** Se toman los dos nodos con menor frecuencia y se crea un nodo padre cuya frecuencia es la suma de sus hijos.
4. **Finalización:** El proceso se repite hasta que queda un único nodo raíz.


## 3. Características y Propiedades
* **Código Prefijo:** Ningún código es prefijo de otro, lo que garantiza que la lectura de bits sea unívoca y no genere errores de interpretación.
* **Eficiencia:** Es el método más eficiente para comprimir datos cuando se conoce la probabilidad de aparición de cada símbolo.

## 4. Aplicaciones Prácticas
Este concepto es fundamental en la informática moderna y se utiliza en:
* **Compresión de imágenes:** Formatos como `JPEG`.
* **Archivos multimedia:** Formatos de audio como `MP3`.
* **Paquetes de datos:** Algoritmos como DEFLATE usados en archivos `.ZIP` o `.GZIP`.

## 5. Ejemplo de Código (Conceptual)
Aunque el algoritmo se puede implementar de varias formas, aquí se muestra una estructura lógica de cómo se vería un nodo en Python:

```python
class NodoHuffman:
    def __init__(self, char, freq):
        self.char = char      # El carácter
        self.freq = freq      # Su frecuencia
        self.izq = None       # Hijo izquierdo (0)
        self.der = None       # Hijo derecho (1)