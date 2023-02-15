FONT = ("Verdana",10)

from tkinter import *
import os

class MoveGui():
	def __init__(moveObj):
		moveObj.move_window = Toplevel()

		moveObj.file_label = Label(moveObj.move_window,text="File Name:",font=FONT)
		moveObj.file_label.place(x=90,y=20)

		moveObj.file_name_text=Entry(moveObj.move_window,width=30,font=FONT)
		moveObj.file_name_text.grid(padx=200,pady=20)

		moveObj.source_label = Label(moveObj.move_window,text="Source path:",font=FONT)
		moveObj.source_label.place(x=90,y=88)

		moveObj.source_path_text=Entry(moveObj.move_window,width=30,font=FONT)
		moveObj.source_path_text.grid(padx=200,pady=20)

		moveObj.dest_label = Label(moveObj.move_window,text="Destination path:",font=FONT)
		moveObj.dest_label.place(x=90,y=155)

		moveObj.dest_path_text=Entry(moveObj.move_window,width=30,font=FONT)
		moveObj.dest_path_text.grid(padx=270,pady=20)
		
		moveObj.move_button=Button(moveObj.move_window,text="Move",font=FONT)
		moveObj.move_window.bind("<Return>",moveObj.move_file)
		moveObj.move_button.grid(pady=40)


	# function to move file from source path to destination
	def move_file(moveObj,event):
		# print("move_file")
		file_name = moveObj.file_name_text.get()
		print("\nfile:",file_name)

		source = moveObj.source_path_text.get()
		print("source:",source)

		dest = moveObj.dest_path_text.get()
		print("dest:",dest)

		source_path = source + "/" + file_name + ".txt"
		print("path:",source_path)

		# check if source path is valid
		flag = True
		if(os.path.exists(source) == True):
			try:
				# open in read mode to make sure the file exists
				source_file = open(source_path,mode="r")
				data = source_file.read()
				print("\ndata:",data)

			except FileNotFoundError:
				print("***File does not exist***")
				flag = False
		else:
			flag = False
			print("***Invalid source path***")

		dest_path = dest + "/" + file_name + ".txt"
		print("dest path:",dest_path)

		# check if destination path is valid
		if(os.path.exists(dest) == True):
			if(flag == True):
				# check if file already exists at destination path.
				# move only if file does not exists in destination directory
				if(os.path.isfile(dest_path) == False):
					try:
						dest_file = open(dest_path,mode="w")
						dest_file.write(data)
						print("***Move Successful***")
						os.remove(source_path)
						dest_file.close()

						# clear all fields after move is successful
						moveObj.file_name_text.delete(0,"end")
						moveObj.source_path_text.delete(0,"end")
						moveObj.dest_path_text.delete(0,"end")
					except:
						print("***Move failed***")
				else:
					print("***File already exists***")
		else:
			print("***Invalid destination path***")








