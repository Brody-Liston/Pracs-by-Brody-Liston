usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']



def main():

    userinput = str(input(" Enter Username "))

    if userinput in usernames:
        print("Access Granted!")
    else:
        print("Access Denied!")

main()