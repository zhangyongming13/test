# https://www.nowcoder.com/practice/119bcca3befb405fbe58abe9c532eb29?tpId=37&tqId=21240&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，
# 并将最终输入结果输出到输出文件里面
if __name__ == '__main__':
    while True:
        try:
            coordinate = [0, 0]
            move_string = input()
            # 分割操作指令
            move_string_list = move_string.split(';')
            for signal_string in move_string_list:
                # 判断操作指令长度是否正确，以及第二位开始是否是数字
                if 1 < len(signal_string) <= 3:
                    for i in signal_string[1:]:
                        if i.isdigit():
                            pass
                        else:
                            break
                    # 判断是否以字母位开头
                    if signal_string[0].isalpha():
                        value = int(signal_string[1:])
                        if signal_string[0].upper() == 'A':
                            coordinate[0] -= value
                        elif signal_string[0].upper() == 'D':
                            coordinate[0] += value
                        elif signal_string[0].upper() == 'W':
                            coordinate[1] += value
                        elif signal_string[0].upper() == 'S':
                            coordinate[1] -= value
                    else:
                        break
                else:
                    break
            print(str(coordinate[0])+','+str(coordinate[1]))
        except:
            break
