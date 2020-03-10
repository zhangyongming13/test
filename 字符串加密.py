# 去重操作
def remove_dup(input_string):
    result = []
    for i in input_string:
        if i.upper() not in result:
            result.append(i.upper())
    return result


# 创建秘钥和剩下字母组成的list
def creat_key_value(keys):
    for i in range(65, 91):
        if chr(i) not in keys:
            keys.append(chr(i))
    return keys


if __name__ == '__main__':
    while True:
        try:
            keys = input()
            proclaimed_in_writing = input()
            keys = remove_dup(keys)
            keys = creat_key_value(keys)
            result = []
            for i in proclaimed_in_writing:
                # 利用减法来算出单个字符在keys里面的相对位置
                if i.isupper():
                    result.append(keys[ord(i) - 65])
                elif i.islower():
                    result.append(keys[ord(i) - 97].lower())
                else:
                    result.append(i)
            print(''.join(result))
        except Exception as e:
            break
