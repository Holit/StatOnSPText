根据密码学的明文推断中的统计学规律，一个英语文段中字母字频有一定的规律。因而对莎士比亚的七份作品做了基本的字频分析。

1. 脚本

   ```python
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
   ```

2. 示例数据（以hamlet_TXT_FolgerShakespeare.txt.analysis.csv为例）

   1. `csv`文件
      此分析文件包含了对整个个文段，即文件夹`/text`下的对应文章的字符个数分析结果。

   2. `.txt.output.txt`文件
      此文件格式如下

      ```
      Statistic file hamlet_TXT_FolgerShakespeare.txt ... 
      #从hamlet_TXT_FolgerShakespeare.txt统计字频
      Result sheet will be saved to hamlet_TXT_FolgerShakespeare.txt.analysis.csv
      #将此字频表存储到hamlet_TXT_FolgerShakespeare.txt.analysis.csv
      
      Char 	'e' appeared 	14843 times	(8.396026834704106%)
      #字符	   'e'出现了		14843次，频率为8.396026834704106%
      Char 	't' appeared 	10981 times	(6.211464708743905%)
      #...
      Char 	'8' appeared 	0 times	(0.0%)
      
      Sorting result:
      #按照出现先后排序
      etoasnhirldumywfcgpbTAIvEkHLONRMSWGPUBCDFKxYQqjzVZJ123450679X8
      ```

      

