import os
BannerStart="""




 ▄▄▄▄▄▄                        ▄▄▄   ▄▄     ██     ▄▄       
 ██▀▀▀▀█▄                      ███   ██     ▀▀     ██       
 ██    ██  ▀██  ███            ██▀█  ██   ████     ██ ▄██▀  
 ██████▀    ██▄ ██             ██ ██ ██     ██     ██▄██    
 ██          ████▀             ██  █▄██     ██     ██▀██▄   
 ██           ███              ██   ███  ▄▄▄██▄▄▄  ██  ▀█▄  
 ▀▀           ██               ▀▀   ▀▀▀  ▀▀▀▀▀▀▀▀  ▀▀   ▀▀▀ 
            ███   

	 ▄▄▄▄▄▄▄▄     ██                     ▄▄ 
	 ██▀▀▀▀▀▀     ▀▀                     ██ 
	 ██         ████     ██▄████▄   ▄███▄██ 
	 ███████      ██     ██▀   ██  ██▀  ▀██ 
	 ██           ██     ██    ██  ██    ██ 
	 ██        ▄▄▄██▄▄▄  ██    ██  ▀██▄▄███ 
	 ▀▀        ▀▀▀▀▀▀▀▀  ▀▀    ▀▀    ▀▀▀ ▀▀ 
		 


		         """
BannerEnd = """ 


▄▄      ▄▄                     ▄▄       
██      ██                     ██       
▀█▄ ██ ▄█▀  ▄████▄    ██▄████  ██ ▄██▀  
 ██ ██ ██  ██▀  ▀██   ██▀      ██▄██    
 ███▀▀███  ██    ██   ██       ██▀██▄   
 ███  ███  ▀██▄▄██▀   ██       ██  ▀█▄  
 ▀▀▀  ▀▀▀    ▀▀▀▀     ▀▀       ▀▀   ▀▀▀  

   ▄▄▄▄      ██                         ▄▄▄▄     
  ██▀▀▀      ▀▀                         ▀▀██     
███████    ████     ██▄████▄   ▄█████▄    ██     
  ██         ██     ██▀   ██   ▀ ▄▄▄██    ██     
  ██         ██     ██    ██  ▄██▀▀▀██    ██     
  ██      ▄▄▄██▄▄▄  ██    ██  ██▄▄▄███    ██▄▄▄  
  ▀▀      ▀▀▀▀▀▀▀▀  ▀▀    ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀  
                                      

"""
print(BannerStart)
sherlock_zapros = "sherlock "
snoop_zapros="python3 snoop.py -t 9 "
nik = input("никнейм\n")
sherlock_zapros+=nik
snoop_zapros+=nik
tor = input("Использовать сеть тор?(N/y)\n") 
if tor == "y" or tor == "Y" or tor == "YES" or tor == 'yes':
	os.system("toriptables2.py -l")
sherlock_zapros+=" --output sherlock.txt"	
os.system(sherlock_zapros)
print("шерлок завершил свою работу!")
os.system("cat sherlock.txt | grep Total")
os.system("pwd > pwd.txt")
my_filex = open("pwd.txt")
pwd = my_filex.read()
my_filex.close()
os.system("rm pwd.txt")
os.system("cd ; cd snoop/ ;"+snoop_zapros)
saioj="cd ; cd snoop/results/txt; "+ nik+".txt | Запрашиваемый"
os.system(saioj)
cp="cd ; cd snoop/results/txt; cp "+nik+".txt "+pwd
cp=cp.strip()+"/snoop.txt"
os.system(cp)
print("snoop завершил свою работу!")
os.system("cat snoop.txt | grep Запрашиваемый")
print("-"*len("| Поиск завершен успешно! |")+"\n| Поиск завершен успешно! |\n"+"-"*len("| Поиск завершен успешно! |"))
print("поиск дублей и объединение файлов")
os.system("cat snoop.txt | grep http > "+nik+".txt")
os.system("cat sherlock.txt | grep http >> "+nik+".txt")
os.system("rm sherlock.txt ; rm snoop.txt ")
file = nik+".txt"
with open (file,'r') as f:
	strings = f.read().splitlines()
os.system("> "+file)
for i in range(len(strings)):
	try:
		for i2 in range(len(strings[i])):
			if strings[i][i2]=="|":
				strings[i]=strings[i][0:i2-1]
	except:
		pass
for i in range(len(strings)):
	os.system("echo "+strings[i]+" >> "+file)
sort="cat "+file+" | sort | uniq > vremenny_file.txt"
os.system(sort)
os.system("mv vremenny_file.txt "+file)
with open (file,'r') as f:
	string = f.read().splitlines()
print(BannerEnd)

print('-'*len("| Общее число результатов после фильтрации "+str(len(string))+" |")+"\n| Филтрация завершена успешно! \n| Создан файл "+str(file)+" по пути "+str(pwd).strip()+" \n| Общее число результатов после фильтрации "+str(len(string))+" \n"+'-'*len("| Общее число результатов после фильтрации "+str(len(string))+" |"))
os.system("firefox file:///root/snoop/results/html/"+nik+".html &")
exit(1)
