f = open("live.txt","rt")#쓰기용으로 열기
text = ""
line = 1
while True:
    row = f.readline()#한줄씩 읽어오기
    if not row:
        break
    text+=str(line) +":"+row
    line+=1
f.close()
#print("{}".format(text).split("\n"))
print(text)
#1:삶이 그대를 속일지라도
#2:        슬퍼하거나 노하지 말라!
#3:우울한 날들을 견디면
#4:        믿으라, 기쁨의 날이 오리니
