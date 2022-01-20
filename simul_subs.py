#!/usr/bin/env python
# coding: utf-8

import ass
import codecs
import sys
import os
import pandas as pd
import datetime
import argparse
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from googletrans import Translator
from langdetect import detect
translator = Translator(service_urls=['translate.google.co.in'])
import re


def clean_text(string):
    string = string.replace("）",")").replace("（","(")
    string = re.sub(r"\{[^{}]*}","",string)
    string = re.sub(r"\([^)]*\)","",string).replace("\\N", " ")
    string = string.strip()
    if len(string) and string[0] == ")":
        string = string[1:].strip()
    return string

def jaccard(a, b):
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


parser = argparse.ArgumentParser("Subtitles Mapping")
parser.add_argument("--dir", type=str, help="The common width and height for all images")
parser.add_argument("--anime_name", type=str, help="The name of the anime for naming the output files")
parser.add_argument("--threshold_score", type=float, default=0.1, help="The common width and height for all images")
parser.add_argument("--start", type=int, default=0, help="The episode number where the program ended on the previous run")

args = parser.parse_args()
anime_name = args.anime_name
start = args.start

en_path = args.dir
en_subs_list = os.listdir(en_path)

print(f"Found {len(en_subs_list)} files")

for idx in range(start,len(en_subs_list)):

    d1 = dict()
    d1['start'] = []
    d1['end'] = []
    d1['text'] = []

    d2 = dict()
    d2['start'] = []
    d2['end'] = []
    d2['text'] = []

    extension = en_subs_list[idx].split(".")[-1]

    if extension == 'ass':
        try:
            with open(en_path+"\\"+en_subs_list[idx], encoding='utf_8_sig') as f:
                doc1 = ass.parse(f)
        except UnicodeError as e:
            with open(en_path+"\\"+en_subs_list[idx], encoding='utf16') as f:
                doc1 = ass.parse(f)
        except Exception as e:
            continue
    
        for i in doc1.events:
            try:
                if detect(i.text) == "en":
                    d1['start'].append(i.start.total_seconds())
                    d1['end'].append(i.end.total_seconds())
                    d1['text'].append(i.text)
        
                elif detect(i.text) == "ja":
                    d2['start'].append(i.start.total_seconds())
                    d2['end'].append(i.end.total_seconds())
                    d2['text'].append(i.text)
            except:
                continue

    elif extension == 'srt':
        try:
            with open(en_path+"\\"+en_subs_list[idx], encoding='utf_8_sig') as f:
                doc2 = srt.parse(f.read())
        except UnicodeError as e:
            with open(en_path+"\\"+en_subs_list[idx], encoding='utf16') as f:
                doc2 = srt.parse(f.read())
        except Exception as e:
            continue

        for i in doc1:
            try:
                if detect(i.text) == "en":
                    d1['start'].append(i.start.total_seconds())
                    d1['end'].append(i.end.total_seconds())
                    d1['text'].append(i.text)
        
                elif detect(i.text) == "ja":
                    d2['start'].append(i.start.total_seconds())
                    d2['end'].append(i.end.total_seconds())
                    d2['text'].append(i.text)
            except:
                continue
    
    df1 = pd.DataFrame(d1).sort_values("start")
    df1['text'] = df1['text'].apply(clean_text)
    df1 = df1[df1['text'] != ""]
    df1 = df1.drop_duplicates(subset=['text'])

    df2 = pd.DataFrame(d2).sort_values("start")
    df2['text'] = df2['text'].apply(clean_text)
    df2 = df2[df2['text'] != ""]
    df2 = df2.drop_duplicates(subset=['text'])

    translated_text = []
    for i, row in tqdm(df2.iterrows()):
        while True:
            if row['text'].strip() == '':
                translated_text.append("")
                break
            try:
                translated = translator.translate(row['text'], dest = "en", src="ja")
                translated_text.append(translated.text)
            except Exception as e:
                continue
            break
    df2['translation'] = translated_text

    df_list = []
    for i, row in df1.iterrows():
        time_diff = abs(df2['start'] - row['start'])
        time_diff = time_diff.sort_values()
        en_tokenized = word_tokenize(row['text'].lower())
        try:
            nearest_idxs = time_diff[time_diff < 2].index
            if len(nearest_idxs) > 1:
                scores = []
                for n_idx in nearest_idxs:
                    translated_text = df2.loc[n_idx].translated
                    translated_tokenized = word_tokenize(translated_text.lower())
                    score = jaccard(en_tokenized, translated_tokenized)
                    scores.append(score)
                max_idx = scores.index(max(score))
                nearest_idx = nearest_idxs[max_idx]
            else:
                nearest_idx = nearest_idxs[0]
            
            jp_text = df2.loc[nearest_idx].text
            en_text = row['text']
            translated_text = df2.loc[nearest_idx].translation
        
            translated_tokenized = word_tokenize(translated_text.lower())
            score = jaccard(en_tokenized, translated_tokenized)
        
            df_list.append([en_text, jp_text, translated_text, score, nearest_idx])
        except Exception as e:
            continue

    df = pd.DataFrame(df_list)
    df.columns = ["en_text", "jp_text", "translated_text", "score", "index"]

    # Merging sentences with same index
    merged_df_list = []
    dup_indices = []
    for i, row in df.iterrows():
        if i in dup_indices:
            continue
        index = row['index']
        dup_idx = df.index[df['index'] == index]
        if len(dup_idx) == 2:
            en_text = df.loc[dup_idx[0]].en_text + " " + df.loc[dup_idx[1]].en_text.lower()
            jp_text = df.loc[dup_idx[0]].jp_text
            translated_text = df.loc[dup_idx[0]].translated_text
            dup_indices.append(dup_idx[1])
        
            en_tokenized = word_tokenize(en_text.lower())
            translated_tokenized = word_tokenize(translated_text.lower())
            score = jaccard(en_tokenized, translated_tokenized)
            merged_df_list.append([en_text, jp_text, translated_text, score])
        else:
            merged_df_list.append([row[0], row[1], row[2], row[3]])

    merged_df = pd.DataFrame(merged_df_list)
    merged_df.columns = ["en_text", "jp_text", "google_translated", "score"]
    merged_df.to_csv("subs/"+anime_name+"-"+str(idx+1)+".csv", index = False)