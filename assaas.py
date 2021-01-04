# -*- coding : utf-8 -*-
from bs4 import *
basit_html = """
Başlık buraya>/title>
Paragraf 1Paragraf 2
"""
soup = BeautifulSoup(basit_html)

print (soup.html.head.title)
# ekrana "Başlık buraya" yazar.

print (len(soup('p')))
# 2 yazar. Belgedeki p tagı sayısı

print (soup('p', {"class": "hebele"}))
# [Paragraf 2] -> class="hebele" olan tagların listesi.

head = soup.html.head
print (head)
#Başlık buraya

head.next
#Başlık buraya
head.next.string
# u'Başlık buraya'

# tag'ın özelliklerine, tag sanki sözlükmüş gibi erişebiliyoruz.
soup.find('p',{"class" : "hebele"})["class"]
# u'hebele'

for i in soup.body:
    print (i)

# Paragraf 1
# Paragraf 2