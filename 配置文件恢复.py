if __name__ == '__main__':
    while True:
        try:
            input_command = str(input()).split(' ')
            if len(input_command) == 1:
                length = len(input_command[0])
                command_ = 'reset'
                if input_command[0] == command_[:length]:
                    print('reset what')
            elif len(input_command) == 2:
                length_1 = len(input_command[0])
                length_2 = len(input_command[-1])
                reset = 'reset'
                board = 'board'
                reboot = 'reboot'
                backplane = 'backplane'
                if input_command[0] == reset[:length_1]:
                    if input_command[-1] == board[:length_2]:
                        print('board fault')
                    else:
                        print('unkown command')
                elif input_command[0] == board[:length_1]:
                    add_ = 'add'
                    delet_ = 'delet'
                    if input_command[-1] == add_[:length_2]:
                        print('where to add')
                    elif input_command[-1] == delet_[:length_2]:
                        print('no board at all')
                    else:
                        print('unkown command')
                elif input_command[0] == reboot[:length_1]:
                    if input_command[-1] == backplane[:length_2]:
                        print('impossible')
                    else:
                        print('unkown command')
                elif input_command[0] == backplane[:length_1]:
                    abort_ = 'abort'
                    if input_command[-1] == abort_[:length_2]:
                        print('install first')
                    else:
                        print('unkown command')
                else:
                    print('unkown command')
            else:
                print('unkown command')
        except Exception as e:
            break
