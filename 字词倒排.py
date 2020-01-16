# https://www.nowcoder.com/practice/81544a4989df4109b33c2d65037c5836?tpId=37&tqId=21254&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 对字符串中的所有单词进行倒排
import re


if __name__ == '__main__':
    while True:
        try:
            InputString = input()
            # 将不是字母的字符换成空格，方便后面匹配
            for i in InputString:
                if not i.isalpha():
                    InputString = InputString.replace(i, ' ')
            InputString = InputString.strip()
            zhang = re.split(r'[ ]+', InputString)
            zhang = zhang[::-1]
            print(' '.join(zhang))
        except:
            break
