# 모듈을 읽어 들입니다.
import os

# 기본 정보를 몇 개 출력해 봅시다.
print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].
os.mkdir("hello")
os.rmdir("hello")

# 파일을 생성하고 + 파일 이름을 변경합니다.
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거합니다.
#os.remove("new.txt")
os.unlink("new.txt")

# 시스템 명령어 실행
os.system("dir")
'''
현재 운영체제: nt
현재 폴더: E:\yse_python\python2\code\11thProject0312
현재 폴더 내부의 요소: ['11thFromMath', '11thModuleEx1', 'dkdkd.png', 'metropolis_hastings1.py', 'moduleInit', 'module_os.py', 'module_sys.py', 'plot.png', 'randomModuleEx.py']
 E 드라이브의 볼륨: 새 볼륨
 볼륨 일련 번호: 7844-35BB

 E:\yse_python\python2\code\11thProject0312 디렉터리

2024-03-12  오후 09:15    <DIR>          .
2024-03-12  오후 09:15    <DIR>          ..
2024-03-12  오후 07:44    <DIR>          11thFromMath
2024-03-12  오후 07:43    <DIR>          11thModuleEx1
2024-03-12  오후 09:12            34,094 dkdkd.png
2024-03-12  오후 09:12             1,179 metropolis_hastings1.py
2024-03-12  오후 08:09    <DIR>          moduleInit
2024-03-12  오후 09:15               652 module_os.py
2024-03-12  오후 09:14               992 module_sys.py
2024-03-12  오후 09:15                 5 new.txt
2024-03-12  오후 07:59            18,216 plot.png
2024-03-12  오후 08:53             2,389 randomModuleEx.py
               7개 파일              57,527 바이트
               5개 디렉터리  499,904,720,896 바이트 남음
'''