# 通过词频统计人物关系
a = {}
result = {}
with open('./text3.txt', 'w', encoding='utf-8') as f1:
    with open('./text1.txt', 'r', encoding='utf-8') as f2:
        for line in f2.readlines():
            l = line.replace('\n', '')
            if l not in a.keys():
                a[l] = 1
            else:
                a[l] += 1
        # print(a)

        for k, v in a.items():
            c, *b = k.split(',')
            b[0] = c + ',' + b[0]
            if b[0] not in result.keys():
                result[b[0]] = [b[1],v]
            else:
                if v > result[b[0]][1]:
                    result[b[0]] = [b[1], v]
        # print(result)

        for k, v in result.items():
            f1.write(k + ',' + v[0] + '\n')