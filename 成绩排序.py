# https://www.nowcoder.com/practice/8e400fd9905747e4acc2aeed7240978b?tpId=37&tqId=21291&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
# 都按先录入排列在前的规则处理
class StudentScore(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


if __name__ == '__main__':
    while True:
        try:
            number = int(input())
            flag = int(input())
            student_list = []
            if flag == 0 or flag == 1:
                for _ in range(number):
                    tmp = input().split(' ')
                    name = str(tmp[0])
                    score = int(tmp[-1])
                    student_score = StudentScore(name, score)
                    student_list.append(student_score)
                if flag == 1:
                    student_list.sort(key=lambda x:x.score)
                else:
                    student_list.sort(key=lambda x:x.score, reverse=True)
                for i in student_list:
                    print(str(i.name) + ' ' + str(i.score))
            else:
                continue
        except Exception as e:
            break
