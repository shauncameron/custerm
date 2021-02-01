from Handling.Commands import Command as pCommand
from Builtin.Package import Package as pPackage

class CommandPackage(pPackage):

    def PUSH(self, Command):

        Command = Command().PACKAGE()

        self.__Database[f'{len(self.__Datanse)+1}'] = {'ALIAS': Command['ALIAS'], 'POST': Command['POST']}

@CommandPackage.PUSH
class Command(pCommand):

    def __init__(self): self.Alias = 'PING'

    def __POST(self, Terminal): Terminal.Output('PONG')