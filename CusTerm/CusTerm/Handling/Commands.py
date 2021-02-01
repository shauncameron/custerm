class Command:

    def __repr__(self): return f"""<Custom Command Object>:A01[{self.Alias}],A02[{self.POST}]"""

    def __init__(self, Alias):

        self.Alias = Alias

    def __POST(self, context):

        x = 'PONG'
        
        return x

    def PACKAGE(self): 
        
        return {'ALIAS': self.Alias, 'POST': self.__POST}