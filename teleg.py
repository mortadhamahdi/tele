import time, requests, webbrowser
import sys as n
import time as mm
r = requests.session()
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 80)
te = 'By @al7asubji'
print("""
 ██████  ██   ██  █████ 
██       ██   ██ ██   ██ 
██       ███████ ███████ ┌─┐ ┌─┐ ┬┌─ ┬─┐  
██       ██   ██ ██   ██ ├┤  │   ├┴┐ ├┬┘  
 ██████  ██   ██ ██   ██ └─┘ └─┘ ┴ ┴ ┴└─  
            TELEGRAM USERNAME""")
print("""
[1] >> For start Press 1
""")

if vv1ck == '1':
	webbrowser.open('https://t.me/al7asubji')
	slow('      *****************************')
	print('Accounts should be placed in a file named user.txt')
	print('    ↓↓↓')
	print('[>] Enter your ID : ')
	ID = input(' ')
	print('[>] Enter Token bot : ')
	token = input(' ')
	time.sleep(1.7)
	slow('      *****************************')
	sl = 'user.txt'
	print(' ')
	m = """
	[☑️] TELEGRAM USER :
	"""
	def tle():
		j = 1
		file = open(sl, 'r')
		while True:
			user = file.readline().split('\n')[0]
						
			if user == '':
				break		
			url = f"https://t.me/{user}"
			req = r.get(url)
			if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				
				print(f"  [{j}] Available     >> [ {user} ]")
				try:
					req = r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={m}\n[+] user >> [ @{user} ]\n\n{te}')
				except NameError:
					pass
				
				with open('Available.txt', 'a') as x:
					tl = '[] NEW USER -->  '
					x.write(tl + user + '\n')
				
			else:
				print(f"  [{j}] Not Available >> [ {user} ]")				
			j += 1	
			time.sleep(1)
		
	tle()
else:
	print('      ******************************')
	print('              wrong number')
