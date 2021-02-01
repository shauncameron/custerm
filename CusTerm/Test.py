import CusTerm

class MyCommand(CusTerm.Handling.Commands.Command):

    def __init__(self): 

        self.Alias = 'ALIAS'
        self.__POST = self.__FUNC

    def __FUNC(self, context):