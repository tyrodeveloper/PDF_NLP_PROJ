import PyPDF3
import re
# import io
import spacy
import pandas as pd
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
matcher1 = Matcher(nlp.vocab)
matcher2 = Matcher(nlp.vocab)
matcher3 = Matcher(nlp.vocab)

pdfFileObj = open('Assignment-1.pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
pageObj2 = pdfReader.getPage(2)

pages_text = pageObj.extractText()
pages_text2 = pageObj2.extractText()
# print(pages_text)
# for line in pages_text.split('\n'):
    #if re.match(r"^PDF", line):
    # print(line)
page_doc = re.sub('\n', ' ', pages_text)
page_doc2 = re.sub('\n', ' ', pages_text2)
page_doc=nlp(page_doc)
page_doc2=nlp(page_doc2)
# print(page_doc)
# for token in page_doc:
#     print(token.text)

# for ent in page_doc.ents:
#     print(ent.text)
def extarct_name(nlp_doc):

    pattern=  [{'ORTH': 'Title'},{'TEXT': {"REGEX": "\\w+"}},{'ORTH': "First"},{'ORTH': "name"},{'TEXT': {"REGEX": "\\w+"},'OP':'?'},{'ORTH': 'Surname'},{'TEXT': {"REGEX": "\\w+"}}]
    

    # pattern = [{'ORTH': 'Title'},{'TEXT': {"REGEX": "^(w+ ?)*$"}}]
    # ,{'TEXT': {"REGEX": "Mr "},'OP': '?'}]
    # ,{'ORTH': 'First name '},{'POS': 'PROPN', 'OP': '?'},{'ORTH': 'Surname '},{'POS': 'PROPN', 'OP': '?'}]
#     for label, pattern in patterns.items():
#         matcher1.add(label, None, pattern)

#     matches = matcher1(nlp_doc) 

#     for match in matches:
#   # match object returns a tuple with (id, startpos, endpos)
#         print(nlp_doc[match[1]:match[2]])
    
    
    
    matcher1.add('NAME', None, pattern)
    matches = matcher1(nlp_doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = nlp_doc[start:end]
        # print(span.text)
        return span.text


def extract_company_name(nlp_doc):
    pattern1=[{'ORTH': 'Company'},{'ORTH': 'name'},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}}]
    matcher2.add('Comapny Name', None, pattern1)
    matches = matcher2(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text

def extract_material(nlp_doc):
    # //Description of proposed materials and finishes:
    pattern2=[{'ORTH': 'Description'},{'ORTH': 'of'},{'ORTH': 'proposed'},{'ORTH': 'materials'},{'ORTH': 'and'},{'ORTH': 'finishes'},{'ORTH': ':'},{'TEXT': {"REGEX": "[a-zA-Z ]*"}},{'TEXT': {"REGEX": "[a-zA-Z ]*"}}]
    # pattern2=[{'ORTH': 'Description'},{'ORTH': 'of'},{'ORTH': 'proposed'},{'ORTH': 'materials'},{'ORTH': 'and'},{'ORTH': 'finishes'},{'ORTH': ':'},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}}]
    matcher3.add('Comapny Name', None, pattern2)
    matches = matcher3(nlp_doc)
    material=[]
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        material.append(span.text)
    return material

def extract_Address(nlp_doc):
    # //Description of proposed materials and finishes:
    pattern2=[{'ORTH': 'Description'},{'ORTH': 'of'},{'ORTH': 'proposed'},{'ORTH': 'materials'},{'ORTH': 'and'},{'ORTH': 'finishes'},{'ORTH': ':'},{'TEXT': {"REGEX": "[a-zA-Z ]*"}},{'TEXT': {"REGEX": "[a-zA-Z ]*"}}]
    # pattern2=[{'ORTH': 'Description'},{'ORTH': 'of'},{'ORTH': 'proposed'},{'ORTH': 'materials'},{'ORTH': 'and'},{'ORTH': 'finishes'},{'ORTH': ':'},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}},{'TEXT': {"REGEX": "\\w+"}}]
    matcher3.add('Comapny Name', None, pattern2)
    matches = matcher3(nlp_doc)
    material=[]
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        material.append(span.text)
    return material
 


name = extarct_name(page_doc)
a=['Title',"First name",'Surname']
for i in a :
    name = name.replace(i, '')

# .sub("First Name",'',name).sub("Surname",'',name)
company_name = extract_company_name(page_doc)
company_name=company_name.replace("Company name",'')
material_list = extract_material(page_doc2)
material_clean=[]
for i in material_list:
    temp=str(i).replace("Description of proposed materials and finishes: ",'')
    material_clean.append(temp)
print("name=",name)
print("Company name=",company_name)
print("materials :",material_clean)