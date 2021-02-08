from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

def index(request):


    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def removepunc(request):
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')

    djtext=request.GET.get('text','default')
    #print(djtext)

    if removepunc == "on":
        # analyzed=djtext
        punctuations='''][;/.,,.,.,,[==--][?><'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            # get the text..
        params = {'purpose': 'removepunctuations', 'analyze': analyzed}
        return render(request, 'removepunc.html', params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to  upperCase', 'analyze': analyzed}
        return render(request, 'removepunc.html', params)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if djtext != '\n':
               analyzed= analyzed + char
        params = {'purpose': 'New Line Remover', 'analyze': analyzed}
        return render(request, 'removepunc.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for char in djtext:
            if " " in djtext:

                analyzed=analyzed+char.replace(" ","")
        params = {'purpose': 'Extra Space Remover', 'analyze': analyzed}
        return render(request, 'removepunc.html', params)

    else:
        return HttpResponse("Error")
def blog(request):
    s='''<a href="http://www.google.com">Google</a>'''
    return  HttpResponse(s)