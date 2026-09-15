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
    lowercase = request.POST.get("lowercase", "off")
    title_case = request.POST.get("title_case", "off")
    sentence_case = request.POST.get("sentence_case", "off")
    remove_numbers = request.POST.get("remove_numbers", "off")
    reverse_text = request.POST.get("reverse_text", "off")
    reverse_lines = request.POST.get("reverse_lines", "off")
    remove_duplicates = request.POST.get("remove_duplicates", "off")
    sort_lines = request.POST.get("sort_lines", "off")
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

    # --- 2.1. Lowercase ---
    if lowercase == "on":
        text = text.lower()
        operations.append("Changed to Lower Case")

    # --- 2.2. Title Case ---
    if title_case == "on":
        # Python's .title() method capitalizes the first letter of each word
        text = text.title() 
        operations.append("Changed to Title Case")

    # --- 2.3. Sentence Case ---
    if sentence_case == "on":
        # 1. Lowercase everything first so we don't get weird casing
        # 2. Split text by sentence-ending punctuation (. ! ?)
        # 3. Capitalize the first letter of each split piece
        # 4. Join them back together
        import re
        text = text.lower()
        # This regex splits on ., !, or ? but keeps the punctuation attached
        sentences = re.split(r'(?<=[.!?])\s+', text)
        text = " ".join([s.capitalize() for s in sentences])
        operations.append("Changed to Sentence Case")

    # --- 2.4. Remove Numbers ---
    if remove_numbers == "on":
        # We loop through every character. If it is NOT a digit, we keep it.
        text = "".join(char for char in text if not char.isdigit())
        operations.append("Removed Numbers")

    # --- 2.5. Reverse Entire Text ---
    if reverse_text == "on":
        # Python's string slicing [start:stop:step]. 
        # Leaving start and stop blank means "everything".
        # Step -1 means "go backwards".
        text = text[::-1]
        operations.append("Reversed Entire Text")

    # --- 2.6. Reverse Line Order ---
    if reverse_lines == "on":
        # Split text into a list of lines
        lines = text.splitlines()
        # Reverse the list
        lines.reverse()
        # Join them back together with a newline character
        text = "\n".join(lines)
        operations.append("Reversed Line Order")

    # --- 2.7. Remove Duplicate Lines ---
    if remove_duplicates == "on":
        lines = text.splitlines()
        # dict.fromkeys() creates a dictionary where keys are the lines.
        # Dictionaries cannot have duplicate keys, and in Python 3.7+, 
        # dictionaries preserve insertion order. So this removes duplicates
        # while keeping the original order of the first occurrences.
        unique_lines = list(dict.fromkeys(lines))
        text = "\n".join(unique_lines)
        operations.append("Removed Duplicate Lines")

        # --- 2.8. Sort Lines ---
    sort_lines_switch = request.POST.get("sort_lines_switch", "off")
    
    if sort_lines_switch == "on":
        sort_lines = request.POST.get("sort_lines", "az")
        lines = text.splitlines()
        
        if sort_lines == "az":
            # THE FIX: key=str.lower ignores case during sorting
            lines.sort(key=str.lower) 
            operations.append("Sorted Lines A-Z")
        elif sort_lines == "za":
            # THE FIX: reverse=True and key=str.lower together
            lines.sort(key=str.lower, reverse=True)
            operations.append("Sorted Lines Z-A")
        elif sort_lines == "length":
            lines.sort(key=len)
            operations.append("Sorted Lines by Length")
            
        text = "\n".join(lines)

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