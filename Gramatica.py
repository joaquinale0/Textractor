import language_tool_python

class Gramatica:
    def __init__(self, texto="", idioma='es'):
        self.texto = texto
        self.herramienta = language_tool_python.LanguageTool(language=idioma)
        self.corregido = ""

    def cambiar_texto(self, texto):
        self.texto = texto

    def corregir(self):
        self.matches = self.herramienta.check(self.texto)
        self.corregido = language_tool_python.utils.correct(self.texto, self.matches)
    
    def get_texto(self):
        return self.texto
    
    def get_texto_corregido(self):
        return self.corregido

# if __name__ == "__main__":
#     texto = "No te rindas, que la vida es eso, continwar el viagje, sovans sf nbod 00N- Ba"
#     g = Gramatica(texto)
#     g.corregir()
#     print(f"corregido {g.get_texto_corregido()}")
