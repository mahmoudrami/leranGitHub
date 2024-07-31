import os

# print(os.getcwd())
# print(os.path.abspath(__file__))

path = os.path.dirname(os.path.abspath(__file__))
print(path)

fileName = input('ادخل اسم الملق الذي تريد النسخ منه : ')
fileWithoutNumber = input('ادخل اسم الملف الذي تريد النسخ اليه : ')



mainFile = open(r""+ path + "\\" + fileName +".txt")
copiedFile = open(r""+ path + "\\"+ fileWithoutNumber +".txt", "w")

statedNUmber = int(input('enter the count of stated number: '))

for x in mainFile:
    # print(x)
    copiedFile.write(x[statedNUmber:])

print('end')