from OCR import *
import multiprocessing as mp
from multiprocessing import Process
from Gramatica import Gramatica
import time

comienzo = time.time()

def iniciar_easy(ruta_imagen, extracto, porcentaje):
    ocr = Easy(ruta_imagen)
    ocr.habilitar_OCR()
    resultados = ocr.realizar_ocr()
    print(f"textos:\n{ocr.texto}")
    print(f"confianza:\n{ocr.confianza}")

    textos = ocr.texto_completo()
    extracto.append({'easy': textos})
    porcentaje.append({'easy': ocr.confianza_promedio()})

def iniciar_paddle(ruta_imagen, extracto, porcentaje):
    ocr = Paddle(ruta_imagen)
    ocr.habilitar_OCR()
    resultados = ocr.realizar_ocr()
    print(f"textos:\n{ocr.texto}")
    print(f"confianza:\n{ocr.confianza}")

    textos = ocr.texto_completo()
    extracto.append({'paddle': textos})
    porcentaje.append({'paddle': ocr.confianza_promedio()})

if __name__ == '__main__':

    # mejora la graatica y correcciones del texto
    gramatica = Gramatica()

    # ruta_imagen = r"C:\Users\Joa7\Documents\Joa\Introduccion Software Libre\TP4 app\img\RD-002-2025-EXA-UNSa_250529_093933_1.jpg"
    ruta_imagen = r"C:\Users\Joa7\Documents\Joa\Introduccion Software Libre\TP4 app\img\img_manuscrita_diagonal.jpg"
    # ruta_imagen = r"C:\Users\Joa7\Documents\Joa\Introduccion Software Libre\TP4 app\img\img_cartilla.jpg"


    with mp.Manager() as manager:
        extracto = manager.list()
        porcentaje = manager.list()

        easy = Process(target=iniciar_easy, args=(ruta_imagen, extracto, porcentaje))
        paddle = Process(target=iniciar_paddle, args=(ruta_imagen, extracto, porcentaje))

        easy.start()
        paddle.start()

        easy.join()
        paddle.join()

        print(f"\nporcentaje lista: {list(porcentaje)}")

        # Extraer los valores
        # Aquí se está extrayendo el valor de confianza del OCR Easy de la lista porcentaje.
        easy_conf = next((v['easy'] for v in porcentaje if 'easy' in v), None)
        paddle_conf = next((v['paddle'] for v in porcentaje if 'paddle' in v), None)

        easy_extr = next((v['easy'] for v in extracto if 'easy' in v), None)
        paddle_extr = next((v['paddle'] for v in extracto if 'paddle' in v), None)

        # Asegura que se encontraron ambos valores de confianza antes de compararlos.
        if easy_conf is not None and paddle_conf is not None:
            if easy_conf > paddle_conf:
                print(f"Ganó Easy con {easy_conf}")
                print(f"texto:\n {easy_extr}")
                
                gramatica.cambiar_texto(easy_extr)
                gramatica.corregir()
                print(f"corregido:\n {gramatica.get_texto_corregido()}")
                
            else:
                print(f"Ganó Paddle con {paddle_conf}")
                print(f"texto:\n {paddle_extr}")
                
                gramatica.cambiar_texto(paddle_extr)
                gramatica.corregir()
                print(f"corregido:\n {gramatica.get_texto_corregido()}")
        else:
            print("No se pudo obtener la confianza de ambos OCR.")

        fin = time.time()
        print(f"duracion = {fin - comienzo:.2f} segundos")