import operator

from django.http import HttpResponse
from django.shortcuts import render


# function performs action to url
def homepage(request):
    return render(request, 'home.html')


# function performs action to url
def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1

        else:
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',
                  {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sorted_words})


def about(request):
    return render(request, 'about.html')
