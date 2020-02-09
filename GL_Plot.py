import pandas as pd
import numpy as np

filename = input("請將檔案拖曳至此>> ")
#filename = "../Data/gseq_01.xlsx"
print("開啟中...", end = '')
xlsxs = pd.ExcelFile(filename)
print(" 成功")
print("讀取到兩個欄位, %s, %s"%(xlsxs.sheet_names[0], xlsxs.sheet_names[1]))
print("正在讀取 ADJR .", end = "")
df = xlsxs.parse("ADJR")[1:]
print(".", end = '')


check_bool_np = np.array(df.drop(columns = df.columns[0]) > 1.98) #做判斷

check_dt = {}
names = list(df[df.columns[0]])
for i in range(len(names)): #然後轉換成字典去存布林值
    check_dt[names[i]] = check_bool_np[i]
print(". 成功",)

print("正在讀取 CONP.", end = "")
df = xlsxs.parse("CONP")[1:]

df = xlsxs.parse("CONP")[1:]
names = list(df[df.columns[0]])

weight_np = np.array(df.drop(columns = df.columns[0]))
print(".", end = '')

weight_dt = {}
for i in range(len(names)):
    weight_dt[names[i]] = weight_np[i]
print('. 成功')

print("正在讀取繪圖套件...", end = '')

from graphviz import Digraph
dot = Digraph(comment='The Round Table')

print(' 成功')

print("正在繪圖.", end = '')

for i in weight_dt.keys(): #新增全部的節點
    dot.node(i, i)

print(".", end = '')

for i in weight_dt.keys():
    for j in range(len(check_dt[i])):
        if check_dt[i][j]:
            #print(i, names[j])
            dot.edge(i, names[j], label = str(weight_dt[i][j]))
print(". 成功")

print("匯出檔案")
dot.render('round-table.gv', view=True) #匯出pdf檔案