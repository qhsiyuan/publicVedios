import os
os.chdir(os.path.dirname(__file__))

import pickle

stepstr = 'href=\"/video/'

with open('web.txt', 'r', encoding='utf-8') as f:

    for webstring in f.readlines():
        webstring = webstring.strip('\n')       #去除文本中的换行符

    f.close
print(webstring.count(stepstr))

webnumpath = '../dat/webnum_zzl.pkl'
vedindx = []
stastr = 0
num = 1

while stastr < len(webstring) and num == 1:
    
    tempstr = ''
    tempnum = 0
    indx = webstring.find(stepstr, stastr, len(webstring)-1) + len(stepstr)

    if webstring.find(stepstr, stastr, len(webstring)-1) < 0:
        num = 0
        break

    while webstring[indx] >= '0' and webstring[indx] <= '9' and num == 1:
        # print('yes')
        tempstr = tempstr + webstring[indx]
        indx  = indx + 1
    stastr = indx

    if len(tempstr) > 0:
        vedindx.append(tempstr)
        print(len(vedindx))
    
with open(webnumpath,'wb') as f:
    pickle.dump(vedindx, f)
    f.close()

with open(webnumpath, 'rb') as f:
    data = pickle.load(f)
    f.close()

print(len(data))
print(data)
