FONT = ("Verdana",10)

from tkinter import *
import os
import time
import datetime

class TouchGui():
	def __init__(touchObj):
		touchObj.touch_window = Toplevel()

		touchObj.file_label = Label(touchObj.touch_window,text="File Name:",font=FONT)
		touchObj.file_label.place(x=90,y=20)

		touchObj.file_name_text=Entry(touchObj.touch_window,width=30,font=FONT)
		touchObj.file_name_text.grid(padx=240,pady=20)

		touchObj.source_label = Label(touchObj.touch_window,text="Path:",font=FONT)
		touchObj.source_label.place(x=90,y=88)

		touchObj.source_path_text=Entry(touchObj.touch_window,width=30,font=FONT)
		touchObj.source_path_text.grid(padx=240,pady=20)

		touchObj.atime_label = Label(touchObj.touch_window,text="Access time:",font=FONT)
		touchObj.atime_label.place(x=90,y=157)

		touchObj.atime_text=Entry(touchObj.touch_window,width=30,font=FONT)
		touchObj.atime_text.grid(padx=240,pady=20)

		touchObj.mtime_label = Label(touchObj.touch_window,text="Modification time:",font=FONT)
		touchObj.mtime_label.place(x=90,y=220)

		touchObj.mtime_text=Entry(touchObj.touch_window,width=30,font=FONT)
		touchObj.mtime_text.grid(padx=270,pady=20)
		
		touchObj.touch_button=Button(touchObj.touch_window,text="Submit",font=FONT)
		touchObj.touch_window.bind("<Return>",touchObj.touch_file)
		touchObj.touch_button.grid(pady=40)

		# prefill the access and modifcation time fields with the current time
		touchObj.atime_text.insert(0,datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		touchObj.mtime_text.insert(0,datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

	# function to create file if it does not exist
	# also modifies modification and access time of a file
	def touch_file(touchObj,event):
		file_name = touchObj.file_name_text.get()
		print("\nfile:",file_name)

		source = touchObj.source_path_text.get()
		print("source:",source)

		path = source + "/" + file_name + ".txt"
		print("path:",path)

		flag = True

		# check if path is valid
		if(os.path.exists(source) == True):
			# check if file exists at path
			if(os.path.isfile(path) == False):
				try:
					# create file only if file does not exists
					new_file = open(path,mode="w")
					print("***File created successfully***")
					new_file.close()

				except:
					print("***Failed to create file***")
					flag = False
			else:
				print("***File exists***")

			if(flag == True):
			
				# input access time and modification time from user
				new_atime = touchObj.atime_text.get()
				new_mtime = touchObj.mtime_text.get()

				# split string into date and time as list elements
				atime_list = new_atime.split(" ")
				mtime_list = new_mtime.split(" ")

				# print("atime list:",atime_list)
				# print("mtime list:",mtime_list)

				# split date into separate components
				atime_date = atime_list[0].split("-")
				mtime_date = mtime_list[0].split("-")

				# print("atime date:",atime_date)
				# print("mtime date:",mtime_date)

				# split time into separate components
				atime_time = atime_list[1].split(":")
				mtime_time = mtime_list[1].split(":")

				# print("atime time:",atime_time)
				# print("mtime time:",mtime_time)

				# convert all string elements to int
				int_atime = [int(x) for x in atime_date + atime_time]
				int_mtime = [int(x) for x in mtime_date + mtime_time]

				# append three 0s as time.mktime() requires 9 arguments
				for i in range(0,3):
					int_atime.append(0)
					int_mtime.append(0)

				# print("atime int:",int_atime)
				# print("mtime int:",int_mtime)

				# convert time to epoch time
				atime = time.mktime(tuple(int_atime))
				mtime = time.mktime(tuple(int_mtime))

				try:
					os.utime(path,(atime,mtime))

					# clear all fields after modifying time
					touchObj.file_name_text.delete(0,"end")
					touchObj.source_path_text.delete(0,"end")
					touchObj.atime_text.delete(0,"end")
					touchObj.mtime_text.delete(0,"end")

				except Exception as e:
					print("***Failed to modify time***")
					print(e)


		else:
			print("***Invalid path***")

		touchObj.touch_window.destroy()



