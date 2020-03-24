import operator

from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def homepage(request):
    return render(request, 'homepage.html', {'one': 'see you'})


def count(request):
    textar = request.GET['textar']

    text = textar.split()

    worddictionary = {}

    for word in text:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'textar': textar, 'count': len(text), 'ttcount': sortedwords})

def about(request):
    return render(request, 'about.html')