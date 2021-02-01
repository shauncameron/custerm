class Terminal: # Define the main Terminal class

    # Create method to represent terminal class object defining
    #   A01 - Amount of Commands
    #   A02 - Amount of Environment Variables
    def __repr__(self): return f"""<Custom Terminal Object>:A01[{len(self.Commands)}],A02[{len(self.Variables)}]"""
    

    # Create method to get possible options
    def __init__(self, options: dict):

        from CusTerm import Builtin.Commands.CommandPackage as bCommands

        self.__Database = {} # Define database as dictionary for later use

        self.Commands = bCommands.Package() # Assume that user will want to add cusotm commands and ready prebuilt commands
        self.Variables = bCommands.Package() # Assume that user will want to add custom variables and ready prebuilt variables

        self.__updateDatabse() # Update the databse with the new commands

    def __updateDatabse(self):

        for command in self.__Commands:

            self.__Database['Environment'][f'{command.Alias}'] = command.POST

        for variable in self.Variables:

            self.__Database['Environment'][f'{variable.Alias}'] = variable.POST

    def OUTPUT(self):

    def START():

