
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


# In[2]:


try: f = open("./setting_for_program.txt", mode = "r")
except FileNotFoundError:
        pyautogui.alert(text='please put "setting_for_program.txt"\nat the path "'+ path+'"\nIf you finish, please click OK.', title='Alart!', button='OK')
        f = open("./_/setting_for_program.txt", mode = "r")

if not os.path.isdir(path + '/' +DateTime):
    os.mkdir(path + '/' +DateTime)
print("The Output file will storage at: " + path + '\\' +DateTime)
path = path + '\\' +DateTime


# In[3]:


temp = f.readlines()
f.close()


# In[4]:


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


# In[5]:


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


# In[6]:


temp = input("請輸入欲處理的csv位置，如空白則為預設值>> ")
if temp == "" or '.csv' not in temp:
    print('使用預設值')
else:
    print('使用輸入值')
    temp = temp.replace('"',"")
    filename = temp


# In[7]:


file = open(filename)
df = pd.read_csv(file)


# In[8]:


temp = input("請輸入你要處理幾個欄位(數字)，如空白則為預設值>> ")
if temp == "":
    print('使用預設值')
else:
    print('使用輸入值')
    temp = temp.replace('"',"")
    amount = int(temp)


# In[9]:


#指定Fixation
#排除交接時的空白
MoveType = df['Eye movement type']
tempBool= np.array(MoveType) == 'Fixation'
temp = df.columns[-amount]
Temp = df[temp]
Temp = Temp.fillna(87)
tempBool_2 = np.array(Temp) != 87
df2 = df[tempBool & tempBool_2]


# In[10]:


#移除其他不必要的欄位
columns = df2.columns
columns = list(columns)
amount = int(amount)
dropped = list(columns[:-amount])
dropped = np.delete(np.array(dropped), dropped.index('Recording name'))
df3 = df2.drop(axis = 1, columns= dropped)


# In[11]:


#將Recording Name 縮短，加入Out欄位
name = "<>".join(list(df3["Recording name"]))
name = name.replace("Recording","")
name = name.split("<>")
df3['Recording name'] = name


# In[12]:


sumofThem = np.delete(np.array(df3), 0, axis = 1).sum(axis = 1)
Out_ready = (sumofThem == 0) + 0
df3["Out"] = Out_ready


# In[13]:


#df3.to_csv(r'./test.csv',index=False,sep=',')


# In[14]:


DfArray = np.array(df3.drop(columns="Recording name"))


# In[15]:


Df2Array = np.array(df3['Recording name'])


# In[16]:


Total_pass = []
Total_pass_out = []
temp = 0
x,y = DfArray.shape
for i in range(x):
    for j in range(y):
        #print(DfArray[i,j])
        if DfArray[i,j] == 1.0:
            if j == 8:
                temp = 14
            else:
                temp = j
    if i<=x-2:
        if Df2Array[i] != Df2Array[i+1]:
            Total_pass_out.append(chr(temp+65) + ';')
        else:Total_pass_out.append(chr(temp+65))
    else:
        Total_pass_out.append(chr(temp+65) + ';')
    Total_pass.append(chr(temp+65))


# In[17]:


df4 = pd.DataFrame(df3["Recording name"])
df4['AOI'] = Total_pass_out


# In[18]:


path


# In[19]:


len(Total_pass)


# In[20]:


df4.to_csv(path+ "\\" + Total_Pass_csv_file_name +".csv",index=False,sep=',')


# In[21]:


#過濾重複的
Total_pass = np.array(Total_pass)
Total_1 = []
Temp_bool = []
for i in range(len(Total_pass)):
    if i == 0:
        Total_1.append(Total_pass[i])
        Temp_bool.append(True)
        continue
    elif Df2Array[i] != Df2Array[i-1]:
        Total_1.append(Total_pass[i])
        Temp_bool.append(True)
    elif Total_pass[i] != Total_1[-1]:
        Total_1.append(Total_pass[i])
        Temp_bool.append(True)
    else:
        Temp_bool.append(False)
    


# In[22]:


df5 = df4[Temp_bool]
temp =df5.columns
total_1_origin = df5['AOI']
df55 = np.array(df5)
x,y = df55.shape
for i in range(x):
    if i==x-1:
        df55[i,1] += ';'
    elif df55[i,0] != df55[i+1,0]:
        df55[i,1] += ';'
df55 = pd.DataFrame(data = df55, columns= temp)


# In[23]:


df55.to_csv(path + "\\" + Total_1_csv_file_name + ".csv",index=False,sep=',')


# In[32]:


first_pass = []
second_pass = []
name = np.array(df5["Recording name"])
name_history = 0
history = []
history_2 = []
Temp_bool = []
Temp_bool_2 = []
second_pass_2 = []
for i in range(len(Total_1)):
    if name[i] != name_history:
        history = []
        history_2 = []
        name_history = name[i]
        
    if Total_1[i] not in history:
        if i <= len(Total_1)-2:
            if name_history == name[i+1]:
                temp = Total_1[i]+" "+ Total_1[i+1] + ";"
                first_pass.append(temp)
                Temp_bool.append(True)
                Temp_bool_2.append(False)
            else:
                Temp_bool.append(False)
                Temp_bool_2.append(False)
        else:
            Temp_bool.append(False)
            Temp_bool_2.append(False)
        history.append(Total_1[i])
    elif i <= len(Total_1)-2:
        if Total_1[i] in history and Total_1[i] not in history_2 and name_history == name[i+1]:
            Temp_bool.append(False)
            Temp_bool_2.append(True)
            history_2.append(Total_1[i])
            temp = Total_1[i-1]+" "+ Total_1[i] + ";"
            second_pass.append(temp)
            temp = Total_1[i]+" "+ Total_1[i+1] + ";"
            second_pass_2.append(temp)
        else:
            Temp_bool.append(False)
            Temp_bool_2.append(False)
    else:
        Temp_bool.append(False)
        Temp_bool_2.append(False)


# In[33]:


len(Total_1)


# In[34]:


len(name)


# In[35]:


#儲存 first_pass
df6 = df5[Temp_bool].drop(columns="AOI")
df6["AOI"] = first_pass
df6.to_csv(path + "\\" + First_Pass_csv_file_name + ".csv",index=False,sep=',')


# In[36]:


#儲存 second_pass
df7 = df5[Temp_bool_2]
df7["From"] = second_pass
df7["To"] = second_pass_2
df7 = df7.drop(columns="AOI")
df7.to_csv(path + "/" + Second_Pass_csv_file_name + ".csv",index=False,sep=',')


# In[37]:


print("程式已經完成\nThe process is finish.")
print("\nThe Output file is storage at: " + path + "\ \n")
print("本程式由陳怡升製作")
print("This program is made by Isheng Chen.")
print("謝謝你的使用 Thanks for using.")
#input("謝謝你的使用，請按enter結束本程式\nThanks for using, please press Enter to close this program.")

