# https://www.nowcoder.com/practice/69ef2267aafd4d52b250a272fd27052c?tpId=37&tqId=21281&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
if __name__ == '__main__':
    while True:
        try:
            tmp = input()
            n = int(tmp.split(' ')[0])
            k = int(tmp.split(' ')[-1])
            li = input().strip().split(' ')
            li = list(map(int, li))
            #li.sort()
            li = sorted(li)
            print(' '.join(map(str, li[:k])))
        except Exception as e:
            #print(e)
            break
