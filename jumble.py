import pandas as pd
import numpy as np
main_df=pd.read_csv("text_words");
main_df=main_df.rename(columns={"name": "word"})

alpha = 'a'
test_list=[]
diction={}
for i in range(0, 26):
    test_list.append(alpha)
    alpha = chr(ord(alpha) + 1)


cols = list(main_df.columns)[1:-1]
temp_df = main_df[cols]


print("Enter the shuffled words")
txt = input()
diction={}
ind=0
for i in test_list:
    diction[i]=txt.count(i)
data = pd.DataFrame.from_dict(diction, orient='index').T
match = []
for index,row in temp_df.iterrows():
    x=row
    if(np.array_equal(data.values[0],row.values)):
        ind = index
        match.append(main_df.iloc[ind].word)
print("The possible words are")
print(match)
