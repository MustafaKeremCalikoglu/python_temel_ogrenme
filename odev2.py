

eposta=input("eposta giriniz")

kontrol=True
if "@" in eposta:
    x=eposta.find("@")
    print("geçerli 1")
else:
    print("@ yazılmamış")
    kontrol=False

if kontrol:
    if " " not in eposta[0:x]:
        print("geçerli 2")
    else:
        print("@ kısmından önce boşluk var")
        kontrol=False

if kontrol:
    if "." in eposta[x+1:] :
        y=eposta[x+1:].find(".") + x + 1
        print("geçerli 3")    
    else:
        print(". yok")
        kontrol=False

if kontrol:
    if  "com"  in  eposta[y+1:y+4]  or "edu" in eposta[y+1:y+4]:
        print("geçerli 4")
    else:
        print("com veya edu değil")
        kontrol=False
if kontrol:
    if "." in eposta[y+4:y+5]:
        print("geçerli 5")
    elif "." not in eposta[y+4:y+5]:
        if  

if kontrol:
    if  "tr" in eposta[y+5:] :
        print("geçerli 7")
    else:
        print("tr değil")                    

    