#flavio toro
#mi amado super input
def s_input(text):
    var = text
    text = input(var).lower().strip()
    while(text == ""):
        text = input("ingrese "+var).lower().strip()
    return text