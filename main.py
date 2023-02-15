FONT = ("Verdana",10)

#initialize move window gui
def create_move():
	moveObj = MoveGui()

#initialize touch window gui
def create_touch():
	touchObj = TouchGui()

#initialize cat window gui
def create_cat():
	catObj = CatGui()

def shutdown():
	try:
		for i in range(11,0,-1):
			print("***Shutting down in",i-1,"seconds...***  \r",end="")
			time.sleep(1)
		os.system("shutdown now") 
	except KeyboardInterrupt:
		print("\nKeyboard Interrupt")
		sys.exit()

def reboot():
	try:
		for i in range(11,0,-1):
			print("***Rebooting in",i-1,"seconds...***  \r",end="")
			time.sleep(1)
		os.system("shutdown -r now")
	except KeyboardInterrupt:
		print("\nKeyboard Interrupt")
		sys.exit()
		

if __name__ == '__main__':
	from tkinter import *
	from move import *
	from touch import *
	from cat import *
	import os
	import time

	try:
		root=Tk()

		move_btn=Button(root,text="Move",command=create_move,font=FONT)
		move_btn.grid(row=10,column=100,padx=50,pady=100)
		
		touch_btn=Button(root,text="Touch",command=create_touch,font=FONT)
		touch_btn.grid(row=10,column=200,padx=50,pady=100)
		
		cat_btn=Button(root,text="Cat",command=create_cat,font=FONT)
		cat_btn.grid(row=10,column=300,padx=50,pady=100)

		shutdown_btn=Button(root,text="Shutdown",command=shutdown,font=FONT)
		shutdown_btn.grid(row=10,column=400,padx=50,pady=100)

		reboot_btn=Button(root,text="Reboot",command=reboot,font=FONT)
		reboot_btn.grid(row=10,column=500,padx=50,pady=100)

		exit_btn=Button(root,text="Exit",command=root.destroy,font=FONT)
		exit_btn.grid(row=10,column=600,padx=50,pady=100)

		root.mainloop()
	
	except KeyboardInterrupt:
		print("Keyboard Interrupt")
		sys.exit()
	