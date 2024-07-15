

# with open ("notlar.txt","a") as dosya:  #"a"  dosya içindekileri değiştirmez ekler 
  #  dosya.write("\nburak:100")
# with open ("notlar1.txt","w") as dosya:  # dosya ekledi
  #  dosya.write("\nburak:100")
 
# with open ("notlar.txt","a") as dosya:     # dosya içindekileri değiştirerek yazar
  #    dosya.write("calikoglu")

#with open ("notlar.txt","w") as dosya:   #dosyanın başına ekleme  
#  x=dosya.read()
#  dosya.seek(0)     # başa getirir
#  dosya.write("mustafa kerem\n"+x)


with open("notlar1.txt","r+") as dosya:
  veri=dosya.readlines()
  veri.insert(1,"ali 70\n")
  dosya.seek(0)
  dosya.writelines(veri)







 