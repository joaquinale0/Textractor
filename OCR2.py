from paddleocr import PaddleOCR

# Inicializa el OCR (sin 'paddle' delante)
# ocr = PaddleOCR(use_angle_cls=True, lang='es')
class OCR2:
    def __init__(self, ruta):
        self._ruta = ruta

    def extraer_texto(self):
        ocr = PaddleOCR(lang=['es', 'en'])
        img_path = self._ruta
        result = ocr.predict(img_path)  # Ya incluye 'cls' si lo configuraste en el constructor

        try:
            self.rec_texts = result[0]["rec_texts"]
            self.rec_scores = result[0]["rec_scores"]

            for idx, (text, score) in enumerate(zip(self.rec_texts, self.rec_scores)):
                print(f"{idx+1}. {text} (confianza: {score:.2f})")
        except FileNotFoundError as e:
            print(f"Error de PaddleOCR: No se encontró el archivo en la ruta: {e.filename}")
        except Exception as e:
            print(f"Otro error durante el OCR: {e}")
    
    def confianza_promedio (self):
        prom = 0
        for puntaje in self.rec_scores:
            prom += puntaje
        return prom/len(self.rec_scores)