import ass
import os
import pandas as pd
import re
import numpy as np
import argparse
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from googletrans import Translator
translator = Translator(service_urls=['translate.google.co.in'])


def clean_text(string):
    string = re.sub(r"\{[^{}]*}","",string)
    return string
	
def jaccard(a, b):
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

parser = argparse.ArgumentParser("Subtitles Mapping")
parser.add_argument("--jp_dir", type=str, help="The common width and height for all images")
parser.add_argument("--en_dir", type=str, help="The common width and height for all images")
parser.add_argument("--anime_name", type=str, help="The name of the anime for naming the output files")
parser.add_argument("--threshold_score", type=float, default=0.1, help="The common width and height for all images")

args = parser.parse_args()


en_path = args.en_dir
jp_path = args.jp_dir
anime_name = args.anime_name

en_subs_list = os.listdir(en_path)
jp_subs_list = os.listdir(jp_path)

#check whether both directories have same number of files

assert len(en_subs_list) == len(jp_subs_list), "The number of files in both directories does not match"

print(f"Found {len(en_subs_list)} files")

for idx in range(len(en_subs_list)):

    try:
        with open(en_path+"\\"+en_subs_list[idx], encoding='utf_8_sig') as f:
            doc1 = ass.parse(f)
    
        with open(jp_path+"\\"+jp_subs_list[idx], encoding='utf_8_sig') as f:
            doc2 = ass.parse(f)
    except Exception as e:
        print(e)
        continue

    d1 = dict()
    d1['start'] = []
    d1['end'] = []
    d1['text'] = []

    d2 = dict()
    d2['start'] = []
    d2['end'] = []
    d2['text'] = []

    for i in doc1.events:
        d1['start'].append(i.start.total_seconds())
        d1['end'].append(i.end.total_seconds())
        d1['text'].append(i.text)
    
    for j in doc2.events:
        d2['start'].append(j.start.total_seconds())
        d2['end'].append(j.end.total_seconds())
        d2['text'].append(j.text)
    
    df1 = pd.DataFrame(d1).sort_values("start")
    df2 = pd.DataFrame(d2).sort_values("start")

    df1['text'] = df1['text'].apply(clean_text)

    df1 = df1[df1['text'] != ""]
    df1 = df1[df1['text'] != "ED"]
    df1 = df1[df1['text'] != "OP"]
    df2 = df2[df2['text'] != ""]

    df1.drop_duplicates(subset=['text'], inplace = True)
    df2.drop_duplicates(subset=['text'], inplace = True)

    df1.reset_index(inplace = True)
    df2.reset_index(inplace = True)

# google translation for jp subs

    translated_text = []
    for i, row in tqdm(df2.iterrows()):
        while True:
            try:
                translated = translator.translate(row['text'], dest = "en", src="ja")
                translated_text.append(translated.text)
            except Exception as e:
                continue
            break
    df2['translation'] = translated_text

# Creating a score matrix

    final_df = []
    previous_index = 0
    used_indices = []
    scores = np.zeros((len(df1), len(df2)))
    for i, row in df1.iterrows():
        en_tokenized = word_tokenize(row['text'].lower())
        for j, col in df2.iterrows():
            translated_tokenized = word_tokenize(col['translation'].lower())
            scores[i][j] = jaccard(en_tokenized, translated_tokenized)


    df_list = []
    slice_idx = 0
    for i in range(len(df1)):
        row = df1.loc[i]
        time_diff = abs(df2['start'] - row['start'])
        jp_nearest_time_indices = time_diff.sort_values()[:10].index
    
        max_idx = np.argmax(scores[i][jp_nearest_time_indices])
        jp_max_idx = jp_nearest_time_indices[max_idx]
        col = df2.loc[jp_max_idx]
        time_diff = abs(df1['start'] - col['start'])
        en_nearest_time_indices = time_diff.sort_values()[:10].index

        max_idx = np.argmax(scores[en_nearest_time_indices, jp_max_idx])
        en_max_idx = en_nearest_time_indices[max_idx]
        if en_max_idx == i:
            en_text = df1.loc[i].text
            jp_text = df2.loc[jp_max_idx].text
            translated_text = df2.loc[jp_max_idx].translation
            score = scores[en_max_idx][jp_max_idx]
            df_list.append([en_text, jp_text, translated_text, score])

    df = pd.DataFrame(df_list)
    df.to_csv("subs/"+anime_name+"-"+str(idx+1)+".csv", index = False)