"""
Views for the TextUtils Django app.

Handles:
- Homepage rendering (index)
- Text analysis and transformation (analyze)
"""

from django.shortcuts import render


# Characters stripped by the "Remove Punctuation" operation
PUNCTUATION_CHARS = """.?”“‘,-—!'":;(){[]}…/~@#$%^&*_<>"""


def index(request):
    """Render the homepage with the analysis form."""
    return render(request, "index.html")


def analyze(request):
    """
    Process the submitted text and apply selected operations in sequence.

    Operations run in this fixed order:
        1. Remove punctuation
        2. Convert to uppercase
        3. Remove new lines
        4. Remove extra spaces

    If 'count' is selected, it overrides the final output with a character count.
    """
    # --- Get user input ---
    text = request.POST.get("text", "")

    # --- Get checkbox states (default "off" if unchecked) ---
    rempunc = request.POST.get("rempunc", "off")
    capitalize = request.POST.get("capitalize", "off")
    rmnl = request.POST.get("rmnl", "off")
    rmsp = request.POST.get("rmsp", "off")
    count = request.POST.get("count", "off")

    operations = []

    # --- 1. Remove Punctuations ---
    if rempunc == "on":
        text = "".join(char for char in text if char not in PUNCTUATION_CHARS)
        operations.append("Removed Punctuations")

    # --- 2. Capitalize ---
    if capitalize == "on":
        text = text.upper()
        operations.append("Changed to Upper Case")

    # --- 3. Remove New Lines ---
    if rmnl == "on":
        text = text.replace("\n", "").replace("\r", "")
        operations.append("Removed NewLines")

    # --- 4. Remove Extra Spaces ---
    if rmsp == "on":
        # Collapse any run of whitespace into a single space
        text = " ".join(text.split())
        operations.append("Removed Extra Spaces")

    # --- 5. Count Characters (overrides output if selected) ---
    if count == "on":
        char_count = len(text)
        context = {
            "analyzed_text": f"Total characters: {char_count}",
            "ana": "Counted Characters",
        }
    else:
        context = {
            "analyzed_text": text,
            "ana": ", ".join(operations) if operations else "No Operation Selected",
        }

    return render(request, "analyze.html", context)