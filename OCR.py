import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np
from paddleocr import PaddleOCR

nombre_archivo = "daotos.txt"

class OCR:
    def __init__(self, ruta, idiomas):
        self.ruta_imagen = ruta     
        self.habilitado = False     # si la ruta de imagen es valida modificas esta variable con la funcion habilitar_OCR()
        self.texto = []             # lista del textos de la imagen procesada el ocr
        self.confianza = []         # lista del números de la confianza de cada elemento en la variable self.texto
        self.nueva = True           # tiene la funcion de negar la funcion de realizar ocr si ya lo habias ejecutado conla misma imagen
        self.idiomas = idiomas      
        # self.gpu = gpu

    def habilitar_OCR(self):
        # Intento de abrir el archivo usando Python directamente
        try:
            with open(self.ruta_imagen, 'rb') as f:
                self.habilitado = True
                self.nueva = True
                print("El archivo se abrió correctamente usando Python.")
        except FileNotFoundError as e:
            self.habilitado = False
            print(f"Error al abrir el archivo con Python: {e}")
        except Exception as e:
            self.habilitado = False
            print(f"Otro error al abrir el archivo con Python: {e}")

    def cambiar_imagen(self, ruta):
        if ruta != self.ruta_imagen:
            self.ruta_imagen = ruta
            self.habilitar_OCR()
    
    def realizar_ocr(self):
        pass

    def texto_completo(self):
        """
        Extrae solo el texto de los resultados del OCR
        
        Args:
            resultados (list): Resultados del OCR
        
        Returns:
            list: Lista de textos detectados
        """
        texto = [texto for texto in self.texto]
        return " ".join(texto)
    
    def confianza_promedio (self):
        prom = 0
        if(len(self.confianza) != 0):
            for puntaje in self.confianza:
                prom += puntaje
            return prom/len(self.confianza)
        else:
            print("Error tamaño de la lista es 0")
            return 0

    def agregar_en_archivo (self):
        pass

class Easy(OCR):
    def __init__(self, ruta, idiomas=['es', 'en']):
        super().__init__(ruta, idiomas)

    def realizar_ocr(self):
        try:
            if self.habilitado and self.nueva: 

                # modificamos nueva para que no vuelva a utilizar recursos si el proceso ya se hizo una vez con la misma imagen
                self.nueva = False

                """
                Realiza OCR en una imagen usando EasyOCR
                
                Args:
                    ruta_imagen (str): Ruta a la imagen para procesar
                    idiomas (list): Lista de idiomas para reconocer (códigos de 2 letras)
                
                Returns:
                    list: Lista de resultados de OCR
                """
                # Inicializar el lector OCR con los idiomas especificados
                print(f"Inicializando EasyOCR con idiomas: {self.idiomas}")
                reader = easyocr.Reader(self.idiomas)
                
                # Leer la imagen
                print(f"Leyendo imagen: {self.ruta_imagen}")
                imagen = cv2.imread(self.ruta_imagen)
                
                if imagen is None:
                    print(f"Error: No se pudo cargar la imagen desde {self.ruta_imagen}")
                
                # Realizar OCR en la imagen
                print("Procesando OCR...")
                resultados = reader.readtext(imagen)
                
                if resultados:
                    print("\nResultados OCR:")
                    for i, (bbox, texto, confianza) in enumerate(resultados, 1):
                        self.texto.append(texto)
                        self.confianza.append(confianza)

                            #         with open(nombre_archivo, 'w+') as archivo:
                            # contenido = archivo.read()
                            # print("Contenido leído del archivo:")
                            # print(contenido)

        except FileNotFoundError as e:
            print(f"Error de PaddleOCR: No se encontró el archivo en la ruta: {e.filename}")
        except Exception as e:
            print(f"Otro error durante el OCR: {e}")

    # def agregar_en_archivo (self):
    #     try:
    #         with open(nombre_archivo, 'w+') as archivo:
    #             contenido = archivo.read()
    #             print("Contenido leído del archivo:")
    #             print(contenido)
    #     except:
    #         print("error al abrir el arhivo")

class Paddle(OCR):
    def __init__(self, ruta, idiomas=['es', 'en']):
        super().__init__(ruta, idiomas)

    def realizar_ocr(self):
        try:
            if self.habilitado and self.nueva: 
                # modificamos nueva para que no vuelva a utilizar recursos si el proceso ya se hizo una vez con la misma imagen
                self.nueva = False
                ocr = PaddleOCR(lang=self.idiomas)
                result = ocr.predict(self.ruta_imagen)  

                self.texto = result[0]["rec_texts"]
                self.confianza = result[0]["rec_scores"]

                # for idx, (text, score) in enumerate(zip(self.rec_texts, self.rec_scores)):
                #     print(f"{idx+1}. {text} (confianza: {score:.2f})")
        except FileNotFoundError as e:
            print(f"Error de PaddleOCR: No se encontró el archivo en la ruta: {e.filename}")
        except Exception as e:
            print(f"Otro error durante el OCR: {e}")
    


# if __name__ == "__main__":
#     # ruta_imagen = r"C:\Users\Joa7\Documents\Joa\Introduccion Software Libre\TP4 app\img\img_github_en.png"
#     ruta_imagen = r"C:\Users\Joa7\Documents\Joa\Introduccion Software Libre\TP4 app\img\RD-002-2025-EXA-UNSa_250529_093933_1.jpg"

#     # ocr = Easy(ruta_imagen)
#     ocr = Paddle(ruta_imagen)

#     ocr.habilitar_OCR()
#     resultados = ocr.realizar_ocr()
#     # print(f"resultados:\n{resultados}")
#     print(f"textos:\n{ocr.texto}")
#     print(f"confianza:\n{ocr.confianza}")

#     textos = ocr.texto_completo()
#     print(f"extraer texto:\n {textos}")

#     print(f"prom {ocr.confianza_promedio()}")


