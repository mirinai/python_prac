'''
import random
print("# random 모듈")

# random(): 0.0 <= x < 1.0 사이의 float을 리턴합니다.
print("- random():", random.random())

# uniform(min, max): 지정한 범위 사이의 float을 리턴합니다.
print("- uniform(10, 20):", random.uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴합니다.
# - randrange(max): 0부터 max 사이의 값을 리턴합니다.
# - randrange(min, max): min부터 max 사이의 값을 리턴합니다.
print("- randrange(10)", random.randrange(10))
print("- randrange(5, 10)", random.randrange(5 , 10))

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
val = [1, 2, 3, 4, 5]
print("random.shuffle(val) 실행 전 val=" , val)
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))
print("- shuffle(val):", random.shuffle(val))
print("random.shuffle(val) 실행 후 val=" , val)

# sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))
'''
from random import *

print("# random 모듈")

# random(): 0.0 <= x < 1.0 사이의 float을 리턴합니다.
print("- random():", random())

# uniform(min, max): 지정한 범위 사이의 float을 리턴합니다.
print("- uniform(10, 20):", uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴합니다.
# - randrange(max): 0부터 max 사이의 값을 리턴합니다.
# - randrange(min, max): min부터 max 사이의 값을 리턴합니다.
print("- randrange(10)", randrange(10))
print("- randrange(5, 10)", randrange(5 , 10))

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
print("- choice([1, 2, 3, 4, 5]):", choice([1, 2, 3, 4, 5]))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
val = [1, 2, 3, 4, 5]
print("random.shuffle(val) 실행 전 val=" , val)
print("- shuffle([1, 2, 3, 4, 5]):", shuffle([1, 2, 3, 4, 5]))
print("- shuffle(val):", shuffle(val))
print("random.shuffle(val) 실행 후 val=" , val)

# sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
print("- sample([1, 2, 3, 4, 5], k=2):", sample([1, 2, 3, 4, 5], k=2))