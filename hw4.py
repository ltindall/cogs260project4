
# coding: utf-8

# # COGS 260 
# # Assignment 4
# 
# ## Author: Lucas Tindall

# ### Tinyshakespeare dataset

# In[58]:


import matplotlib.pyplot as plt

files = ['shakespeare_1layer.txt','tinyshakespeare_rnn_output.txt','tinyshakespeare_console.txt','shakespeare_100seq.txt','shakespeare_rnn160.txt']

x_all = []
y_all = []
for name in files: 
    with open(name) as f:
        mylist = f.read().splitlines() 
        x = []
        y = []
        for a in mylist: 
            l = a.split(' ')

            if len(l) == 12: 
                x.append(l[6])
                y.append(l[11])
        x_all.append(x)
        y_all.append(y)


plt.figure(figsize=(10,7))
plt.plot(y_all[4],'m', label='2 layers, seq_len=50, hidden=160, LSTM')
plt.plot(y_all[0],'b', label='1 layer, seq_len=50, hidden=128, LSTM')
plt.plot(y_all[1],'r', label='2 layers, seq_len=50, hidden=128, RNN')
plt.plot(y_all[2],'g', label='2 layers, seq_len=50, hidden=128, LSTM')
plt.plot(y_all[3],'y', label='2 layers, seq_len=100, hidden=128, LSTM')

plt.legend(loc='upper center', shadow=True)
plt.title('RNN trained on tinyshakespeare data')
plt.ylabel('loss')
plt.xlabel('iterations')
plt.ylim([1,3])
plt.show()






# ### Nottingham Music Database

# In[63]:

files = ['music_1layer.txt','music_rnn_output.txt','music_regular.txt','music_100seq_output.txt','music_rnn192.txt']


x_all = []
y_all = []
for name in files: 
    with open(name) as f:
        mylist = f.read().splitlines() 
        x = []
        y = []
        for a in mylist: 
            l = a.split(' ')
            if len(l) == 12: 
                x.append(l[6])
                y.append(l[11])
        x_all.append(x)
        y_all.append(y)

plt.figure(figsize=(10,7))
plt.plot(y_all[4],'m', label='2 layers, seq_len=50, hidden=192, LSTM')
plt.plot(y_all[0],'b', label='1 layer, seq_len=50, hidden=128, LSTM')
plt.plot(y_all[1],'r', label='2 layers, seq_len=50, hidden=128, RNN')
plt.plot(y_all[2],'g', label='2 layers, seq_len=50, hidden=128, LSTM')
plt.plot(y_all[3],'y', label='2 layers, seq_len=100, hidden=128, LSTM')
plt.legend(loc='upper center', shadow=True)
plt.title('RNN trained on Nottingham Music Database')
plt.ylabel('loss')
plt.xlabel('iterations')
plt.ylim([0,3])
plt.show()





