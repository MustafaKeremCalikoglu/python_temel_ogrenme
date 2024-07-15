i=1
while i<=5:
	print("MUSTAFA KEREM ÇALIKOĞLU")
	i=i+1

gizlikelime="mustafa"
tahmin=""
j=1
t=2
while tahmin!=gizlikelime and j<=3:
	
	tahmin=input("tahmin ediniz:  ")
	if tahmin==gizlikelime:
		print("helal bildin") 
	else:
		
		print("bilemedin  "+str(t)+" hakkın kaldı")	
		j=j+1	
		t=t-1
