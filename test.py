if __name__ == '__main__':
    while True:
        try:
            coordinate = [0, 0]
            move_string = input()
            move_string_list = move_string.split(';')
            for signal_string in move_string_list:
                if len(signal_string) == 3:
                    if signal_string[0].isalpha():
                        if signal_string[1].isdigit() and signal_string[2].isdigit():
                            value = int(signal_string[1]) * 10 + int(signal_string[2])
                            if signal_string[0].upper() == 'A':
                                coordinate[0] -= value
                            if signal_string[0].upper() == 'D':
                                coordinate[0] += value
                            if signal_string[0].upper() == 'W':
                                coordinate[1] += value
                            if signal_string[0].upper() == 'S':
                                coordinate[1] -= value
            print(str(coordinate[0])+','+str(coordinate[1]))
        except:
            break
