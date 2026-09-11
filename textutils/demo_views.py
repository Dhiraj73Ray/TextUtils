##  I Created this file for Practice - Dhiraj ##

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    # Match lowercase 'text' from the form
    text = request.POST.get('text', '')

    # Check the Checkbox values
    rempunc = request.POST.get('rempunc', 'off')
    capatalize = request.POST.get("capatalize", "off")
    rmnl = request.POST.get("rmnl", "off")
    rmsp = request.POST.get("rmsp", "off")
    count = request.POST.get("count", "off")

    operations = []

    # 1. Remove Punctuations
    if rempunc == "on":
        analyzed = ""
        punct = """.?”“‘,-—!'":;(){[]}…/~@#$%^&*_<>"""
        for char in text:
            if char not in punct:
                analyzed += char
        operations.append("Removed Punctuations")
        text = analyzed

    # 2. Capitalize
    if capatalize == "on":
        text = text.upper()
        operations.append("Changed to Upper Case")

    # 3. Remove New Lines
    if rmnl == "on":
        new = ""
        for char in text:
            if char != "\n" and char != "\r":
                new += char
        operations.append("Removed NewLines")
        text = new

    # 4. Remove Extra Spaces
    if rmsp == "on":
        new = ""
        for index, char in enumerate(text):
            if index + 1 < len(text):
                if not (text[index] == " " and text[index + 1] == " "):
                    new += char
            else:
                new += char
        operations.append("Removed Extra Spaces")
        text = new

    # 5. Count Characters (overrides output if selected)
    if count == "on":
        char_count = len(text)
        par = {
            "analyzed_text": f"Total characters: {char_count}",
            "ana": "Counted Characters"
        }
    else:
        par = {
            "analyzed_text": text,
            "ana": ", ".join(operations) if operations else "No Operation Selected"
        }

    return render(request, "analyze.html", par)