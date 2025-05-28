import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np

class OCR:
    def __init__(self, ruta):
        self._ruta_imagen = ruta

    def realizar_ocr(ruta_imagen, idiomas=['es', 'en']):
        """
        Realiza OCR en una imagen usando EasyOCR
        
        Args:
            ruta_imagen (str): Ruta a la imagen para procesar
            idiomas (list): Lista de idiomas para reconocer (códigos de 2 letras)
        
        Returns:
            list: Lista de resultados de OCR
        """
        # Inicializar el lector OCR con los idiomas especificados
        print(f"Inicializando EasyOCR con idiomas: {idiomas}")
        reader = easyocr.Reader(idiomas, gpu=False)
        
        # Leer la imagen
        print(f"Leyendo imagen: {ruta_imagen}")
        imagen = cv2.imread(ruta_imagen)
        
        if imagen is None:
            print(f"Error: No se pudo cargar la imagen desde {ruta_imagen}")
            return []
        
        # Realizar OCR en la imagen
        print("Procesando OCR...")
        resultados = reader.readtext(imagen)
        
        return resultados

    def extraer_texto(resultados):
        """
        Extrae solo el texto de los resultados del OCR
        
        Args:
            resultados (list): Resultados del OCR
        
        Returns:
            list: Lista de textos detectados
        """
        return [texto for _, texto, _ in resultados]
    
    # def mostrar_resultados(imagen_path, resultados):
    #     """
    #     Muestra la imagen con cuadros delimitadores y texto detectado
        
    #     Args:
    #         imagen_path (str): Ruta a la imagen
    #         resultados (list): Resultados del OCR
    #     """
    #     # Leer la imagen con OpenCV
    #     imagen = cv2.imread(imagen_path)
        
    #     if imagen is None:
    #         print(f"Error: No se pudo cargar la imagen desde {imagen_path}")
    #         return
        
    #     # Convertir de BGR a RGB para matplotlib
    #     imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
    #     # Crear una figura
    #     plt.figure(figsize=(10, 10))
        
    #     # Dibujar cuadros delimitadores y texto
    #     for (bbox, texto, probabilidad) in resultados:
    #         # Obtener puntos del cuadro delimitador
    #         (tl, tr, br, bl) = bbox
    #         tl = (int(tl[0]), int(tl[1]))
    #         tr = (int(tr[0]), int(tr[1]))
    #         br = (int(br[0]), int(br[1]))
    #         bl = (int(bl[0]), int(bl[1]))
            
    #         # Dibujar el cuadro delimitador
    #         cv2.rectangle(imagen, tl, br, (0, 255, 0), 2)
            
    #         # Ajustar las coordenadas para el texto
    #         x = tl[0]
    #         y = tl[1] - 10 if tl[1] > 10 else tl[1] + 10
            
    #         # Convertir el texto para mostrar
    #         texto_mostrar = f"{texto} ({probabilidad:.2f})"
            
    #         # Colocar el texto sobre la imagen
    #         cv2.putText(imagen, texto_mostrar, (x, y),
    #                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    #     # Mostrar la imagen con las anotaciones
    #     plt.imshow(imagen)
    #     plt.axis('off')
    #     plt.title("Resultados OCR")
    #     plt.tight_layout()
    #     plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Ruta de la imagen (ajusta esto a tu imagen)
    # ruta_imagen = "./img/hola.png"
    # ruta_imagen = r"C:\Users\Joa7\Documents\Joa\Introduccion Software Libre\TP4 app\img\img_github_es.png"
    ruta_imagen = r"C:\Users\Joa7\Documents\Joa\Introduccion Software Libre\TP4 app\img\img_manuscrita_diagonal.jpg"
    
    # Realizar OCR
    ocr = OCR
    resultados = ocr.realizar_ocr(ruta_imagen, idiomas=['es', 'en'])
    
    # Mostrar resultados
    if resultados:
        print("\nResultados OCR:")
        for i, (bbox, texto, probabilidad) in enumerate(resultados, 1):
            print(f"{i}. Texto: '{texto}' (Confianza: {probabilidad:.2f})")
        
        # Extraer solo el texto
        textos = ocr.extraer_texto(resultados)
        print("\nTexto completo detectado:")
        print(" ".join(textos))
        
        # Visualizar resultados en la imagen
        # mostrar_resultados(ruta_imagen, resultados)
    else:
        print("No se detectó texto en la imagen.")