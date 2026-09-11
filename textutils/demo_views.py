##  I Created this file for Practice - Dhiraj ##

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # var = {"name":"Dhiraj", "age":22} # Includes variables in Templates
    return render(request, "index.html")


def analyze(request):
    # Get the Text
    text = request.POST.get('Text', 'default')

    # Check the Checkbox value
    rempunc = request.POST.get('rempunc', 'off')
    capatalize = request.POST.get("capatalize", "off")
    rmnl = request.POST.get("rmnl", "off")
    rmsp = request.POST.get("rmsp", "off")
    count = request.POST.get("count", "off")

    if rempunc != "on" and capatalize != "on" and rmnl != "on" and rmsp != "on" and count != "on":
        return HttpResponse("Please select at least one operation.")

    # Check which checkbox is "on"
    if rempunc == "on":
        analyzed = ""
        punct = """.?”“‘,-—!'":;(){[]}…/~@#$%^&\*_<>"""
        for i in text:
            if i not in punct:
                analyzed += i
        par = {"analyzed_text": analyzed, "ana": "Removed Punctuations"}
        text = analyzed

    if capatalize == "on":
        upper = text.upper()
        par = {"analyzed_text": upper, "ana": "Changed to Upper Case"}
        text = upper

    if rmnl == "on":
        new = ""
        for i in text:
            if i != "\n" and i != "\r":
                new += i
        par = {"analyzed_text": new, "ana": "Removed NewLines"}
        text = new

    if rmsp == "on":
        new = ""
        for index, i in enumerate(text):
            if index + 1 < len(text) and not (text[index] == " " and text[index + 1] == " "):
                new += i
        par = {"analyzed_text": new, "ana": "Removed Extra Spaces"}
        text = new

    if count == "on":
        char = len(text)
        par = {"analyzed_text": text, "ana": f"Total Characters: {char}"}

    return render(request, "analyze.html", par)

    
    

