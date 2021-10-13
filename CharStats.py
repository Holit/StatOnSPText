import sys
import csv

if(len(sys.argv) != 2):
    exit(-2)

filename = sys.argv[1]
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"#所有正常打印字符
strings = open(filename).read()#读取需要统计频数的文本

len = len(strings)

result = {}
for i in alphabet:
    counts = strings.count(i)
    i = '{0}'.format(i)
    result[i] = counts

res = sorted(result.items(), key=lambda item: item[1], reverse=True)
num = 0
print("Statistic file "+ filename+" ...")
print("Result sheet will be saved to "+filename+".analysis.csv\n")

for data in res:
    num += 1
    print("Char '" + data[0] + "' appeared "+ str(data[1]) + "times with percentage "+ str( 100 * data[1]/len) + "%")

print('\nRESULT')

for i in res:
    flag = str(i[0])
    print(flag[0], end="")

with open(filename+".analysis.csv", "w",encoding='utf-8',newline='') as csvfile:  # 打开文件

    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(["char","count"])
    #写入多行用writerows
    writer.writerows(res)