import os
def ty():
	if os.name == 'nt':
		_ = os.system ('cls')
	else:
		_ = os.system ('clear')
b='\033[36m'
j='\033[33m'
z='\033[32m'
k='\033[31m'
s='\033[34m'
f='\033[35m'
def kek():
	print('Выполнено.......Termux Cod\nАвторы..........',k,'W',b,'o',f,'l',z,'F',j,'a',s,'k','...',k,'T',b,'o',j,'p',b,'o',s,'1',z,'u',f,'s',b,'\nСообщество вк...https:\\m.vk.com\termux_cod')
	lol= input('Ваш ник: ')
	print('\n\033[37mБелый\n\033[36mБирюзовый\n\033[33mЖелтый\n\033[32mЗеленый\n\033[31mКрасный\n\033[34mСиний\n\033[35mФиолетовый\n\033[30mЧерный',b'(Черный)\n')
	
	color=input('Выберите цвет: ')

	if color=='1':
            to='37m' 
	if color=='2':
	    to='36m' 
	if color=='3':
	    to='33m' 
	if color=='4':
	    to='32m' 
	if color=='5':
	    to='31m' 
	if color=='6':
	    to='34m' 
	if color=='7':
	    to='35m' 
	if color=='8':
	    to='30m' 

	with open ('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w+') as file:
		try:
			file = file.write (r"PS1='\[\e[{0}\]{1}~ \[\e[0m\]'".format (to,lol))
			print ('\033[32mNick изменен :)')
		except:
			print ('\033[31mЛол, что-то не так, обратись в тех.поддержку группы')
ty()
kek()
