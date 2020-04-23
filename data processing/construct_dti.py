import json
import csv
import codecs

json_data=open('test_dti.json',encoding='utf-8').read()
#2.json调用loads()方法将字符串数据转换成列表
data=json.loads(json_data)#data存取一行数据

csv_file=open('train_protein.csv')    #打开csv文件
csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
data_prot=[]    #创建列表准备接收csv各行数据
for one_line in csv_reader_lines:
    data_prot.append(one_line)    #将读取的csv分行数据按行存入列表‘data_prot’中

'''字典化'''
data_prot_dict = {}
for (i, item) in enumerate(data_prot):
    data_prot_dict[item[1]] = i

csv_file1=open('train_compound.csv')    #打开csv文件
csv_reader_lines1 = csv.reader(csv_file1)   #逐行读取csv文件
data_com=[]    #创建列表准备接收csv各行数据

for one_line1 in csv_reader_lines1:
    data_com.append(one_line1)    #将读取的csv分行数据按行存入列表‘data_prot’中

'''字典化'''
data_com_dict = {}
for (i, item) in enumerate(data_com):
    data_com_dict[item[1]] = i

result = []
inter = []
data_prot_len = len(data_prot)
data_com_len = len(data_com)
data_len = len(data)
find = 0
for k in range(data_len):
    #if k == :
    #    break
    if k % 10 == 0:
        print(k)
    '''for i in range(data_prot_len):
        for j in range(data_com_len):
            if data_prot[i][1]==data[k][0] and data_com[j][1]==data[k][1]:
                inter.append(data_com[j][0])
                inter.append(data_prot[i][0])
                inter.append(data[k][2])
                result.append(inter)
                find=1
                break
        if find==1:
            break
    '''
    i = data_prot_dict.get(data[k][0])
    j = data_com_dict.get(data[k][1])
    print(i)
    print(j)
    if i is not None and j is not None:
        result.append([data_com[j][0], data_prot[i][0], data[k][2]])
print(result)

file_csv = codecs.open('DTI_test.csv', 'w+', 'utf-8')
writer = csv.writer(file_csv)
for data in result:
    writer.writerow(data)
print("保存文件成功，处理结束")
