# -*- coding: utf-8 -*-
lines = []
with open("./红楼梦.txt","r+", encoding= 'utf-8') as f:
    for line in f.readlines():
        line = line.split("．")  #注意句号的书写
        #print(line)
        lines += line
    #print(lines)
    with open("./newrelation.txt", 'r+', encoding='utf-8') as f1:
        for l in f1.readlines():
                # print(l)
            l = l.replace('\n', '')
            list1 = l.split(',')
            #print(list1[0])
            for i in range(len(lines)):
                if list1[0] in lines[i] and list1[1] in lines[i]:
                    with open("sentence6.txt",'a+',encoding= 'utf-8') as f2:
                        f2.write(list1[0]+"#"+list1[1]+"#"+lines[i]+'\n')

