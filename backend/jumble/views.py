from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
import pandas as pd
import numpy as np
from django.http import JsonResponse
from collections import Counter
def index(request):
    if request.method == 'POST': 
        
        form = NameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["your_name"])
            main_df=pd.read_csv("../text_words");
            main_df=main_df.rename(columns={"name": "word"})
            alpha = 'a'
            test_list=[]
            diction={}
            for i in range(0, 26):
                test_list.append(alpha)
                alpha = chr(ord(alpha) + 1)
            cols = list(main_df.columns)[1:-1]
            temp_df = main_df[cols]
            txt = form.cleaned_data["your_name"]
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
            # return render(request,'thanks.html',{"match":match })
            return JsonResponse({"match":match })
    else:
        form = NameForm()
    return render(request,'index.html', {'form': form})

def thanks(request):
    return render(request,'thanks.html')
