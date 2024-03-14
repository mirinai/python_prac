def selfCall():
    print("하",end="")
    selfCall()#스택이 쌓임, 스택 오버플로우 나기 전에 인터프리터가 끝냄
'''
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
'''
if __name__ == "__main__":

    selfCall()