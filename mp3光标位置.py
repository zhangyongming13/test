# https://www.nowcoder.com/practice/eaf5b886bd6645dd9cfb5406f3753e15?tpId=37&tqId=21287&tPage=4&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
if __name__ == '__main__':
    while True:
        try:
            number = int(input())
            commands = str(input())
            if number <= 4:
                head, tail, index = 1, number, 1
                for command in commands:
                    if command == 'U':
                        if index == 1:
                            index = number
                        else:
                            index -= 1
                    elif command == 'D':
                        if index == number:
                            index = 1
                        else:
                            index += 1
            else:
                head, tail, index = 1, 4, 1
                for command in commands:
                    if command == 'U':
                        if index == 1:
                            index = number
                            tail = number
                            head = number - 3
                        else:
                            index -= 1
                            if index < head:
                                head = index
                                tail = head + 3
                    else:
                        if index == number:
                            index = 1
                            head = 1
                            tail = 4
                        else:
                            index += 1
                            if index > tail:
                                tail = index
                                head = tail - 3
            for i in range(head, tail + 1):
                print(i, end=' ')
            print()
            print(index)
        except Exception as e:
            break
