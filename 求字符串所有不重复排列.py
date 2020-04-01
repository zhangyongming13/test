def permutation(input_string, start, input_list):
    if input_string == None or start < 0:
        return
    # 排到最后一个字符了，递归结束
    if start == len(input_string) - 1:
        input_list.append(''.join(input_string))
        return
    else:
        i = start
        while i < len(input_string):
            # 交换固定的第一个值
            input_string[i], input_string[start] = input_string[start], input_string[i]
            # 递归运算
            permutation(input_string, start + 1, input_list)
            # 交换回去，便于下一次固定
            input_string[start], input_string[i] = input_string[i], input_string[start]
            i += 1


while True:
    try:
        input_string = list(input())
        result = []
        permutation(input_string, 0, result)
        result = list(set(result))
        print(result)
        print(len(result))
    except Exception as e:
        print(e)
        break
