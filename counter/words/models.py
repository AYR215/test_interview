import os

from django.db import models
from django.http import request


class Document(models.Model):
    file = models.FileField(upload_to='', null=True)
    name = models.CharField(max_length=155, null=True)

def handle_uploaded_file(self):
    count = 0
    wormcount = 0
    #with open(self.path(), 'w+') as destination:
    #    for chunk in self.chunks():
    #        destination.write(chunk)
    with open(f'media/{self.name}', 'r') as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
    text = text.lower()
    words = text.split()
    nonrep_words = list()

    for word in words:
        if word not in nonrep_words and word.isalpha():
            nonrep_words.append(word)
            count += 1
        else:
            pass
        if word in nonrep_words == "червяк":
            wormcount += 1
    return count, wormcount
