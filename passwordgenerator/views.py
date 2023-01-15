from django.shortcuts import render
from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def create_password(request):
    uppercaseLetters = ascii_uppercase
    lowercaseLetters = ascii_lowercase
    numbers = digits
    specialChars = punctuation

    pwChars = ""

    isUpper = True
    isUpper = True if request.POST.get("isUpper") == "on" else False
    isLower = True if request.POST.get("isLower") == "on" else False
    isDigits = True if request.POST.get("isDigits") == "on" else False
    isSpecialChars = True if request.POST.get(
        "isSpecialChars") == "on" else False

    if not isUpper and not isLower and not isDigits and not isSpecialChars:
        isUpper = True
        isLower = True
        isDigits = True
        isSpecialChars = True

    pwChars = uppercaseLetters if isUpper else ""
    pwChars = pwChars + (lowercaseLetters if isLower else "")
    pwChars = pwChars + (numbers if isDigits else "")
    pwChars = pwChars + (specialChars if isSpecialChars else "")

    # password length
    pwLength = 16 if request.POST.get('pwLength') == None or not (int(request.POST.get(
        'pwLength')) > 3 and int(request.POST.get('pwLength')) < 101) else int(request.POST.get('pwLength'))

    # generate a password string
    passwordGenerated = ''
    for i in range(pwLength):
        passwordGenerated += ''.join(choice(pwChars))

    print(passwordGenerated)

    # generate password meeting constraints
    while True:
        passwordGenerated = ''
        for i in range(pwLength):
            passwordGenerated += ''.join(choice(pwChars))

        if ((any(char in specialChars for char in passwordGenerated)) if isSpecialChars else True and (sum(char in numbers for char in passwordGenerated) >= 2) if isDigits else True):
            break

    context = {"generated_password": passwordGenerated, "pwLength": pwLength, "isUpper": isUpper,
               "isLower": isLower, "isDigits": isDigits, "isSpecialChars": isSpecialChars}

    print(context)
    return render(request, "pages/password-generator.html", context)
