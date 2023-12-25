# 补全姓名
with open('./word/name.txt', 'r', encoding='utf-8') as f:
    L=[]
    for line in f.readlines():
        l = line.replace('\n', '').split('，')
        # print(l)
        l1=[]
        l1.append(l[0])
        # print(l[0])
        # print(l[1])
        l1.append(l[1])
        L.append(l1)
    # print(L)


with open('../KGQA/raw_data/result.txt', 'w', encoding='utf-8') as f1:#最终结果
    with open('./word/newresult.txt', 'r', encoding='utf-8') as f2:
        for line in f2.readlines():
            l = line.replace('\n', '').split(',')
            # print(l)
            for l2 in L:
                # print(l2)
                if l[0] == l2[1]:
                    l[0] = l2[0]
                    break
                    # print(l)
            for l2 in L:
                # print(l2)
                if l[1] == l2[1]:
                    l[1] = l2[0]
                    break
                    # print(l)
            f1.write(l[0] + ',' + l[1] + ',' + l[2] + '\n')
