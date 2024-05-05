class Configuracoes:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.dia = 4
        self.mes = 6
        self.ano = 2024
    
    def get_full_date(self):
        return {
          "dia" : self.dia,
          "mes" : self.mes,
          "ano" : self.ano
        } 