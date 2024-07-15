
try:
	sayi=int(input("bir sayı giriniz"))
	kare=sayi**2
	print(kare)
except:
	print("geçersiz sayi girdiniz")
	

try:
	sayi=int(input("bir sayı giriniz"))
	kare=sayi**2
	print(kare)
except ValueError:
	print("geçersiz giriş")

try:
	sayi1=int(input("bir sayı giriniz"))
	sayi2=int(input("bir sayı giriniz"))
	sonuc=sayi1/sayi2
	print(sonuc)
except ValueError:		
	print("geçersiz giriş")
except ZeroDivisionError:
	print("sayı 0 a bölünemez")

try:
	sayi1=int(input("bir sayı giriniz"))
	sayi2=int(input("bir sayı giriniz"))
	sonuc=sayi1/sayi2
	print(sonuc)
except (ValueError,ZeroDivisionError) as hata:		
	print("geçersiz giriş",hata)


try:
	dosya=open("tirendazakademi.txt","r")
except IOError:
	print("bir hata oldu")
finally:
	dosya.close








