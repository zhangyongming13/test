# https://www.nowcoder.com/practice/e8480ed7501640709354db1cc4ffd42a?tpId=37&tqId=21286&tPage=4&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）是序列中G和C两个字母的总的出现次数除以总的字母数目（也就是序列长度）
# 在基因工程中，这个比例非常重要。因为高的GC-Ratio可能是基因的起始点。
# 给定一个很长的DNA序列，以及要求的最小子序列长度，研究人员经常会需要在其中找出GC-Ratio最高的子序列。


def get_gc_ratio(input_string, length):
    GC = input_string.count('G') + input_string.count('C')
    return GC / length


if __name__ == '__main__':
    while True:
        try:
            input_string = list(input())
            length = int(input())
            if len(input_string) < length:
                continue
            elif len(input_string) == length:
                print(''.join(input_string))
            else:
                i = 0
                # 记录GC比例最高的段的开头
                result_index = 0
                GC_Ratio = 0
                while i + length <= len(input_string):
                    zhang = input_string[i:i+length]
                    tmp = get_gc_ratio(input_string[i:i+length], length)
                    if GC_Ratio < tmp:
                        result_index = i
                        GC_Ratio = tmp
                    i += 1
                print(''.join(input_string[result_index:result_index+length]))
        except Exception as e:
            break
