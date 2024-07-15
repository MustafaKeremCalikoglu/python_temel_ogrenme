#mustafa kerem çalıkoğlu 20120101059

eposta=input("eposta giriniz")

kontrol=True
if "@" in eposta:
    x=eposta.find("@")
    kontrol=True    
else:
    print("@ yazılmamış")
    kontrol=False

if kontrol:
    if " " not in eposta[0:x]:
        kontrol=True    

    else:
        print("@ kısmından önce boşluk var")
        kontrol=False

if kontrol:
    if "." in eposta[x+1:] :
        y=eposta[x+1:].find(".") + x + 1
        kontrol=True    

    else:
        print(". yok")
        kontrol=False

if kontrol:
    if  "com"  in  eposta[y+1:y+4]  or "edu" in eposta[y+1:y+4]:
        kontrol=True    

    else:
        print("com veya edu değil")
        kontrol=False
if kontrol:
    if "." in eposta[y+4:y+5]:
        kontrol=True    

    else:
        print("geçerli e posta")
        kontrol=False

if kontrol:
    if  "tr" in eposta[y+5:] :
        print("geçerli e posta")
    else:
        print("tr değil")                    

    