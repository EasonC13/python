
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime
import os
pd.options.mode.chained_assignment = None  # default='warn'
ISOTIMEFORMAT = '%Y%m%d_%H%M%S'
DateTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
path = os.path.abspath('.')


# In[3]:


try: f = open("./setting_for_program.txt", mode = "r")
except FileNotFoundError:
        pyautogui.alert(text='please put "setting_for_program.txt"\nat the path "'+ path+'"\nIf you finish, please click OK.', title='Alart!', button='OK')
        f = open("./_/setting_for_program.txt", mode = "r")
        
        
#print("The Output file will storage at: " + path + '\\' +DateTime)
path = path + '\\' +DateTime


# In[4]:


temp = f.readlines()
f.close()


# In[5]:


locate = [0]*6
for i in range(len(temp)):
    if "the_csv's_path = " in temp[i]:
        locate[0] = i
    elif "amount_of_target = " in temp[i]:
        locate[1] = i
    elif "Total_Pass_csv_file_name = " in temp[i]:
        locate[2] = i
    elif "Total_1_csv_file_name = " in temp[i]:
        locate[3] = i
    elif "First_Pass_csv_file_name = " in temp[i]:
        locate[4] = i
    elif "Second_Pass_csv_file_name = " in temp[i]:
        locate[5] = i
filename = temp[locate[0]]
filename = filename.replace("the_csv's_path = ","").replace("\n","")
amount = temp[locate[1]]
amount = amount.replace("amount_of_target = ","").replace("\n","")
amount = int(amount)
Total_Pass_csv_file_name = temp[locate[2]]
Total_Pass_csv_file_name = Total_Pass_csv_file_name.replace("Total_Pass_csv_file_name = ","").replace("\n","")
Total_1_csv_file_name = temp[locate[3]]
Total_1_csv_file_name = Total_1_csv_file_name.replace("Total_1_csv_file_name = ","").replace("\n","")
First_Pass_csv_file_name = temp[locate[4]]
First_Pass_csv_file_name = First_Pass_csv_file_name.replace("First_Pass_csv_file_name = ","").replace("\n","")
Second_Pass_csv_file_name = temp[locate[5]]
Second_Pass_csv_file_name = Second_Pass_csv_file_name.replace("Second_Pass_csv_file_name = ","").replace("\n","")


# In[24]:


locate = input("請輸入欲處理的資料夾>> ")
if locate == "":
    print("使用預設值")
    locate = "C:/Users/user/Documents/G_eye_movement/20190715_142046/"
else: 
    print("使用輸入值")
    locate = locate.replace('"',"")
    locate = locate + "/"


# In[19]:


filename = locate + Total_1_csv_file_name + ".csv"


# In[45]:


file = open(filename)
df = pd.read_csv(file)


# In[116]:


name = input("請輸入輸出檔案前輟名稱(如空白將使用預設值)>> ")
if name == "":
    name = "select"


# In[46]:


N = df["Recording name"]


# In[27]:


history = []
for i in N:
    if i not in history:
        history.append(i)


# In[128]:


print ("你能輸入得值從'" + str(history[0]) + "' 到 '" + str(history[-1]) + "' (本輸入僅供參考，請以實際需求為準)")
print("輸入格式為 'A B C...'，不同數字中間要有一個空格相隔")
temp = input("請輸入欲選取的編號")


# In[68]:


numbers = np.array(temp.split(" "))


# In[71]:


numbers = numbers.astype(int)


# In[72]:


N = np.array(N)


# In[112]:


temp = []

for i in numbers:
    temp.append(N == i)
temp = np.array(temp)
temp = temp.sum(axis=0) == 1


# In[117]:


df2 = df[temp]
df2.to_csv(locate + name + "_"+ Total_1_csv_file_name + ".csv",index=False,sep=',')


# In[118]:


filename = locate + Total_Pass_csv_file_name + ".csv"
file = open(filename)
df = pd.read_csv(file)


# In[122]:


N = df["Recording name"]
N = np.array(N)
temp = []

for i in numbers:
    temp.append(N == i)
temp = np.array(temp)
temp = temp.sum(axis=0) == 1
df2 = df[temp]
df2.to_csv(locate + name + "_"+ Total_Pass_csv_file_name + ".csv",index=False,sep=',')


# In[123]:


filename = locate + First_Pass_csv_file_name + ".csv"
file = open(filename)
df = pd.read_csv(file)


# In[124]:


N = df["Recording name"]
N = np.array(N)
temp = []

for i in numbers:
    temp.append(N == i)
temp = np.array(temp)
temp = temp.sum(axis=0) == 1
df2 = df[temp]
df2.to_csv(locate + name + "_"+ First_Pass_csv_file_name + ".csv",index=False,sep=',')


# In[125]:


filename = locate + Second_Pass_csv_file_name + ".csv"
file = open(filename)
df = pd.read_csv(file)


# In[126]:


N = df["Recording name"]
N = np.array(N)
temp = []

for i in numbers:
    temp.append(N == i)
temp = np.array(temp)
temp = temp.sum(axis=0) == 1
df2 = df[temp]
df2.to_csv(locate + name + "_"+ Second_Pass_csv_file_name + ".csv",index=False,sep=',')


# In[127]:


print("程式已經完成\nThe process is finish.")
#print("\nThe Output file is storage at: " + path + "\ \n")
print("本程式由陳怡升製作")
print("This program is made by Isheng Chen.")
print("謝謝你的使用  Thanks for using.")
#input("謝謝你的使用，請按enter結束本程式\nThanks for using, please press Enter to close this program.")

