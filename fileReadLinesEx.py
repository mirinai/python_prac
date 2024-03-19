with open("info.txt","r") as file:
    for line in file:
        (name,weight,height)=line.strip().split(", ")#strip : 맨 앞이나 뒤에 공백이 있으면 지움
        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / ((int(height)/100)**2)
        result = ""
        if bmi >=25:
            result="과체중"
        elif bmi >=18.5:
            result ="정상체중"
        else:
            result="저체중"
        #출력
        print("\n".join(["이름 : {}","몸무게 : {}","키 : {}", "BMI : {}","결과 : {}"]).format(name,weight,height,bmi,result))
        #join() : 하나의 문자열로 뭉침 (\n + 뒤 문자열)
        
        print()


