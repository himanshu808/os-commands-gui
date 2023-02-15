FONT = ("Verdana",10)

from tkinter import *
import os

class CatGui():
	def __init__(catObj):
		catObj.cat_window = Toplevel()

		catObj.file_label = Label(catObj.cat_window,text="File Name:",font=FONT)
		catObj.file_label.place(x=90,y=20)

		catObj.file_name_text = Entry(catObj.cat_window,width=30,font=FONT)
		catObj.file_name_text.grid(padx=200,pady=20,sticky=W)	

		catObj.source_label = Label(catObj.cat_window,text="Path:",font=FONT)
		catObj.source_label.place(x=90,y=88)

		catObj.source_path_text = Entry(catObj.cat_window,width=30,font=FONT)
		catObj.source_path_text.grid(padx=200,pady=20,sticky=W)

		catObj.cpy_label = Label(catObj.cat_window,text="Copy To:",font=FONT)
		catObj.cpy_label.place(x=90,y=160)

		catObj.cpy_name_text = Entry(catObj.cat_window,width=30,font=FONT)
		catObj.cpy_name_text.grid(padx=200,pady=20,sticky=W)	

		catObj.contents_label = Label(catObj.cat_window,text="Contents:",font=FONT)
		catObj.contents_label.place(x=90,y=230)

		catObj.contents_text = Text(catObj.cat_window,height=10,font=FONT)
		catObj.contents_text.grid(padx=200,pady=20)
		catObj.contents_text.configure(state="disabled")

		catObj.add_label = Label(catObj.cat_window,text="Add text:",font=FONT)
		catObj.add_label.place(x=90,y=495)

		catObj.add_text = Text(catObj.cat_window,height=10,font=FONT)
		catObj.add_text.grid(padx=200,pady=20)
		catObj.add_text.bind("<Key>",catObj.change_btn)

		catObj.cat_button = Button(catObj.cat_window,text="View",command=catObj.cat_file,font=FONT)
		catObj.cat_button.grid(pady=10)

		catObj.cpy_button = Button(catObj.cat_window,text="Copy",command=catObj.cpy_file,font=FONT)
		catObj.cpy_button.grid(padx=40,pady=10)


	# function to append data in an existing file
	def cat_file(catObj):
		# change button text to "View" everytime it is pressed
		catObj.cat_button.configure(text="View")

		file_name = catObj.file_name_text.get()
		print("\nfile:",file_name)

		source = catObj.source_path_text.get()
		print("source:",source)

		flag = True

		# check if source path is valid
		if(os.path.exists(source) == False):
			print("***Invalid path***")
			flag = False

		path = source + "/" + file_name + ".txt"
		print("path:",path)

		if(flag == True):
			try:
				# opening in r+ mode to make sure that the file exists
				source_file = open(path,mode="r+")

				data = source_file.read()
				print("original data:",data,end="")

				# change state of text area from disabled to normal before inserting
				catObj.contents_text.configure(state="normal")
				catObj.contents_text.delete("1.0","end")
				catObj.contents_text.insert("1.0",data)
				catObj.contents_text.configure(state="disabled")

				# get data from the user
				new_data = catObj.add_text.get("1.0","end")

				# seek till the end of the file to append data
				source_file.seek(source_file.tell()-1)
				print("seek:",source_file.tell())
				source_file.write(new_data)
				source_file.close()

				# opening the file again to read the new data and display in the contents text area
				source_file = open(path,mode="r+")

				new_data = source_file.read()
				print("new data:",new_data)
				
				# displaying new contents in the text area
				catObj.contents_text.configure(state="normal")
				catObj.contents_text.delete("1.0","end")
				catObj.contents_text.insert("1.0",new_data)
				catObj.contents_text.configure(state="disabled")

				# clearing the input text area once the data is appended
				catObj.add_text.delete("1.0","end")
				source_file.close()	
			
			except FileNotFoundError:
				print("***File does not exist***")

	# function to copy data from one file to another
	# creates the target file with the specified name if it does not exist
	# overwrites file if it exists
	def cpy_file(catObj):
		# get source file name
		src_file = catObj.file_name_text.get()
		print("\nsource file:",src_file)

		# get target file name
		trgt_file = catObj.cpy_name_text.get()
		print("target file:",trgt_file)

		# get source path
		source = catObj.source_path_text.get()
		print("source path:",source)

		source_path = source + "/" + src_file + ".txt"
		print("path:",source_path)

		trgt_path = source + "/" + trgt_file + ".txt"
		print("target path:",trgt_path)

		flag = True

		# check if the source path is valid
		if(os.path.exists(source) == False):
			print("***Invalid path***")
			flag = False

		# make sure the source file and target file are different
		if(src_file == trgt_file):
			print("***Target file name should be different than source file name***")
			flag = False

		if(flag == True):
			try:
				file = open(source_path,mode="r")

				data = file.read()
				print("data:",data)

				file.close()

				# create target file if it does not exist. otherwise overwrite
				if(os.path.isfile(trgt_path) == False):
					print("***File created***")
				file = open(trgt_path,mode="w")
				file.write(data)
				file.close()

				print("***Copied Successfully***")


			except FileNotFoundError:
				print("***File does not exist***")
	

	def change_btn(catObj,event):
		# change button text from "View" to "Save" each time any key is pressed in the input text area
		catObj.cat_button.configure(text="Save")

	










