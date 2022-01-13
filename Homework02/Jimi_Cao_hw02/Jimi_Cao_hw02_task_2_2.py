# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:05:21 2021

@author: Jimi
"""

import spacy
import en_core_web_sm
import json

from spacy.matcher import Matcher
import sys

def birthplace_lexical(sent, nlp):
    birth = []
    
    pattern = [
                {'ORTH': 'born'},
                {'OP': '*'},
                {'ORTH': 'in'},
                {'OP': '*'},
                {'IS_TITLE': True,},
                {'IS_PUNCT': True,},
                {'IS_TITLE': True,},
                {'IS_PUNCT': True, 'OP': '?'},
                {'IS_TITLE': True, 'OP': '?'},
                {'IS_UPPER': True, 'OP': '?'},
               ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        match = matches[-1]
        span = sent[match[1]:match[2]] 
        
        isolate_pattern = [
                            {'IS_TITLE': True,},
                            {'IS_PUNCT': True, 'OP': '?'},
                            {'IS_TITLE': True, 'OP': '?'},
                            {'IS_PUNCT': True, 'OP': '?'},
                            {'IS_TITLE': True, 'OP': '?'},
                            {'IS_UPPER': True, 'OP': '?'},
                          ]
        
        isolate = Matcher(nlp.vocab)
        isolate.add('isolating', [isolate_pattern])
        
        sub_str_tok = nlp(span.text)
        name_match = isolate(sub_str_tok)
        
        n_match = name_match[-1]
        
        name = sub_str_tok[n_match[1]:n_match[2]]
    
        birth.append(' '.join(map(str,name)))
            
    return birth
    
def education_lexical(sent, nlp):
    edu = []
    
    pattern = [
                {'TEXT': {'REGEX': 'graduated|attended|enrolled'}},
                {'OP': '*'},
                {'TEXT': {'REGEX': 'School|College|University|Academy'}},
                {'TEXT': 'of', 'OP': '?'},
                {'IS_TITLE': True, 'OP': '*'},
                {'IS_PUNCT': True, 'OP': '*'},
                {'IS_TITLE': True, 'OP': '*'},
               ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern,])
    
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        match = matches[-1]
        span = sent[match[1]:match[2]] 
        isolate_pattern = [
                            {'IS_TITLE': True, 'OP': '+'},
                            {'IS_STOP': True, 'OP': '?'},
                            {'IS_TITLE': True, 'OP': '+'},
                          ]
        
        isolate = Matcher(nlp.vocab)
        isolate.add('isolating', [isolate_pattern])
        
        sub_str_tok = nlp(span.text)
        name_match = isolate(sub_str_tok)
        
        name = max([sub_str_tok[n_match[1]:n_match[2]] for n_match in name_match], key=len)
    
        edu.append(' '.join(map(str,name)))
    
    return edu

def parents_lexical(sent, nlp):
    parents = []
    
    pattern = [
                {'LOWER': {'REGEX': '^(son|daughter|born)$'}},
                # {'OP': '*'},
                {'ORTH': {'REGEX': 'of|to'}},
                {'OP': '*'},
                {'IS_TITLE': True, 'OP': '+'},
                {'OP': '*'},
                {'ORTH': 'and'},
                {'OP': '*'},
                {'IS_TITLE': True, 'OP': '+'},
                # {'IS_PUNCT': True,},
              ]
    pattern2 = [
                {'LOWER': {'REGEX': '^(mother|father|parent)$'}},
                {'ORTH': ',',},
                {'IS_TITLE': True, 'OP': '+'},
               ]
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern, pattern2])
    
    matches = matcher(nlp(str(sent)))
    
    if len(matches)>0:
        
        for match in matches:
            span = sent[match[1]:match[2]] 
            
        isolate_pattern = [
                            {'IS_TITLE': True},
                            {'IS_TITLE': True},
                          ]
        
        isolate = Matcher(nlp.vocab)
        isolate.add('isolating', [isolate_pattern])

        sub_str_tok = nlp(span.text)
        name_match = isolate(sub_str_tok)

        return [str(sub_str_tok[n_match[1]:n_match[2]]) for n_match in name_match]
    
    return parents

def awards_lexical(sent, nlp):
    awards = []
    
    pattern = [
                {'TEXT': {'REGEX': '^(nominated|nomination([s]?)|awarded|won)$'}},
                {'IS_STOP': True, 'OP': '*'},
                {'IS_TITLE': True, 'OP': '+'},
              ]
    pattern2 = [
                {'IS_TITLE': True, 'OP': '+'},
                {'TEXT': {'REGEX': '^(nomination|award)([s]?)$'}},
               ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern, pattern2])
    
    matches = matcher(nlp(str(sent)))
    
    if len(matches)>0:
        
        match = matches[-1]
        span = sent[match[1]:match[2]]
            
        isolate_pattern = [
                            {'IS_TITLE': True, 'OP': '+'},
                          ]
        
        isolate = Matcher(nlp.vocab)
        isolate.add('isolating', [isolate_pattern])

        sub_str_tok = nlp(span.text)
        name_match = isolate(sub_str_tok)
        
        award = max([sub_str_tok[n_match[1]:n_match[2]] for n_match in name_match], key=len)

        return [str(award)]
    
    return awards

def performances_lexical(sent, nlp):
    performances = []
    
    pattern = [
                {'IS_TITLE': True, 'OP': '+'},
                {'IS_STOP': True, 'OP': '*'},
                {'IS_TITLE': True, 'OP': '*'},
                {'TEXT': '('},
                {'LIKE_NUM': True},
                {'TEXT': ')'},
              ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    
    matches = matcher(nlp(str(sent)))
    
    if len(matches)>0:
        
        string_pos = {}
        for match in matches:
            if match[2] in string_pos.keys():
                if match[1] < string_pos[match[2]]:
                    string_pos[match[2]] = match[1]
            else:
                string_pos[match[2]] = match[1]
        
        for pos in string_pos:
            performances.append(str(sent[string_pos[pos]:pos-3]))
    
    return performances

def colleagues_lexical(sent, nlp):
    colleagues = []
    
    pattern = [
                {'LOWER': {'REGEX': '^(alongside|actor|actress|director|producer)'}},
                {'IS_STOP': True, 'OP': '*'},
                {'IS_TITLE': True, 'OP': '+'},
                {'IS_STOP': True, 'OP': '*'},
                {'IS_TITLE': True, 'OP': '*'},
              ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    
    matches = matcher(nlp(str(sent)))
    
    if len(matches)>0:
        
        match = matches[-1]
        span = sent[match[1]+1:match[2]]
            
        isolate_pattern = [
                            {'IS_TITLE': True},
                            {'IS_TITLE': True, 'OP': '+'},
                          ]
        
        isolate = Matcher(nlp.vocab)
        isolate.add('isolating', [isolate_pattern])

        sub_str_tok = nlp(span.text)
        name_match = isolate(sub_str_tok)
        
        if len(name_match) > 0:
            string_pos = {}
            for match in name_match:
                if match[1] in string_pos.keys():
                    if match[2] > string_pos[match[1]]:
                        string_pos[match[1]] = match[2]
                else:
                    string_pos[match[1]] = match[2]
            
            for pos in string_pos:
                colleagues.append(str(sub_str_tok[pos:string_pos[pos]]))
    
    return colleagues


def birthplace_syntatic(sent, nlp):
    birth = []
    pattern = [
                {'POS': 'VERB', 'ORTH': 'born'},
                {'OP': '*'},
                {'LOWER': 'in', 'POS': 'ADP'},
                {'OP': '*'},
                {'ENT_TYPE': 'GPE', 'OP': '+'},
              ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        match = matches[-1]
        span = sent[match[1]:match[2]] 
        birth.append(', '.join([str(ent) for ent in span.ents if ent.label_ == 'GPE']))
        
    return birth

def education_syntatic(sent, nlp):
    edu = []
    
    pattern = [
                {'POS': 'VERB', 'LEMMA': {'REGEX': 'graduate|attend|enroll'}},
                {'OP': '*'},
                {'ENT_TYPE': 'ORG', 'TEXT': {'REGEX': 'School|College|University|Academy'}},
              ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        match = matches[-1]
        span = sent[match[1]:match[2]] 
        edu.append(', '.join([str(ent) for ent in span.ents if ent.label_ == 'ORG']))
    
    return edu

def parents_syntatic(sent, nlp):
    parents = []
    
    pattern = [
                {'POS': 'NOUN', 'TEXT': {'REGEX': '^(son|daughter)$'}},
                {'LOWER': 'of', 'POS': 'ADP'},
                {'OP': '*'},
                {'ENT_TYPE': 'PERSON', 'OP': '+'},
              ]
    pattern2 = [
                {'POS': 'NOUN', 'LOWER': {'REGEX': '^(mother|father|parent)$'}},
                {'IS_PUNCT': True, 'OP': '?'},
                {'ENT_TYPE': 'PERSON', 'OP': '+'},
               ]
    pattern3 = [
                {'POS': 'VERB', 'LOWER': 'born'},
                {'LOWER': 'to', 'POS': 'ADP'},
                {'OP': '*'},
                {'ENT_TYPE': 'PERSON', 'OP': '+'},
               ]
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern, pattern2, pattern3])
    
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        match = matches[-1]
        span = sent[match[1]:match[2]] 
        parents.append(', '.join([str(ent) for ent in span.ents if ent.label_ == 'PERSON']))
    
    return parents

def awards_syntatic(sent, nlp):
    awards = []
    
    pattern = [
                {'POS': 'VERB', 'LEMMA': {'REGEX': '^(nominate|award|win)$'}},
                {'IS_STOP': True, 'OP': '*'},
                {'TAG': 'NNP', 'OP': '+'}
              ]
    pattern2 = [
                {'TAG': 'NNP', 'OP': '+'},
                {'POS': 'NOUN', 'LEMMA': {'REGEX': '^(nomination|award)$'}},
               ]
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern, pattern2])
    
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        match = matches[-1]
        span = sent[match[1]:match[2]] 
        awards.append(' '.join([str(w) for w in span if w.tag_ == 'NNP']))
    
    return awards

def performances_syntatic(sent, nlp):
    performances = []
    
    pattern = [
                {'IS_TITLE': True, 'OP': '+'},
                {'IS_STOP': True, 'OP': '*'},
                {'IS_TITLE': True, 'OP': '*'},
                {'TEXT': '('},
                {'LIKE_NUM': True},
                {'TEXT': ')'},
              ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        
        string_pos = {}
        for match in matches:
            if match[2] in string_pos.keys():
                if match[1] < string_pos[match[2]]:
                    string_pos[match[2]] = match[1]
            else:
                string_pos[match[2]] = match[1]
        
        for pos in string_pos:
            performances.append(str(sent[string_pos[pos]:pos-3]))
        
    return performances

def colleagues_syntatic(sent, nlp):
    colleagues = []
    
    pattern = [
                {'LOWER': {'REGEX': '^(along|actor|actress|director|producer|with|including|directed)'}},
                {'IS_STOP': True, 'OP': '*'},
                {'ENT_TYPE': 'PERSON', 'OP': '+'},
                {'IS_STOP': True, 'OP': '*'},
                {'ENT_TYPE': 'PERSON', 'OP': '*'},
              ]
    
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    matches = matcher(nlp(str(sent)))
    if len(matches)>0:
        match = matches[-1]
        span = sent[match[1]:match[2]]
        # print(span)
        
        colleagues.append(', '.join([str(ent) for ent in span.ents if ent.label_ == 'PERSON']))
    
    
    return colleagues


if len(sys.argv) < 4:
    print('Missing arguments')
    sys.exit()

in_file = sys.argv[1]
out_file = sys.argv[2]
try:
    syntactic = int(sys.argv[3])
except:
    print('3rd argument must be an int')
    sys.exit()

print(in_file, out_file, syntactic)

count = 0
data = []
nlp = en_core_web_sm.load()


with open(in_file, encoding='utf-8') as fp:
    for line in fp:
        
        line = line.strip()
        split = line.rfind(',')
        
        url = line[split+1:]
        bio = line[:split]
        
        data.append([bio, url])

json_list = []

for bio, act in data:
    
    count += 1
    
    birthplace = []
    education = []
    parents = []
    awards = []
    performances = []
    colleagues = []
    
    doc = nlp(bio)
    
    if syntactic:
        for sent in doc.sents:
            birthplace += birthplace_syntatic(sent, nlp)
            education += education_syntatic(sent, nlp)
            parents += parents_syntatic(sent, nlp)
            awards += awards_syntatic(sent, nlp)
            performances += performances_syntatic(sent, nlp)
            colleagues += colleagues_syntatic(sent, nlp)
            
    else: 
        for sent in doc.sents:
              
            birthplace += birthplace_lexical(sent, nlp)
            education += education_lexical(sent, nlp)
            parents += parents_lexical(sent, nlp)
            awards += awards_lexical(sent, nlp)
            performances += performances_lexical(sent, nlp)
            colleagues += colleagues_lexical(sent, nlp)
            
            
    print(count)
    
    
    final = {}
    final["url"] = act
    if birthplace:
        final['birthplace'] = birthplace[0]
    else:
        final['birthplace'] = []
    final['education'] = education
    final['parents'] = parents
    final['awards'] =  awards
    final['performances'] = performances
    final['colleagues'] = colleagues
    
    json_list.append(final)
    

if out_file.rfind('.jl') == -1:
    out_file += '.jl'


with open(out_file, 'w') as out:
    for entry in json_list:
        json.dump(entry, out)
        out.write('\n')

    