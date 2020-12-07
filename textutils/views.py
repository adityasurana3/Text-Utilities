#User Created
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    djtext=print(request.POST.get('text','default'))
    # print(djtext)
    return render(request,'index.html')
    # return HttpResponse("Hello")
# def removepunc(request):
#     return HttpResponse("This remove punctutation marl")
# def capfirst(request):
#     return HttpResponse("This capitalized letter")
# def newlineremove(request):
#     return HttpResponse("Removes line")
# def spaceremove(request):
#     return HttpResponse("Remove Space")
# def charcount(request):
#     return HttpResponse("Count Character")
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
    if (removepunc == "on") and (fullcaps == 'on'):
        analyzed=""
        for char in djtext:
            if (char not in punctuations) and (char in djtext):
                analyzed=analyzed+char.upper()
        param ={'purpose':'Remove Punctuation and Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',param)
    elif removepunc == "on":
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        param ={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',param)
    elif fullcaps == 'on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        param = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)  
    elif newlineremover=='on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed+char
        param = {'purpose': 'Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', param)            
    else:
        return HttpResponse("Error")
