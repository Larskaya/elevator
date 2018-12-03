from tkinter import *
from the_house import *

root = Tk()
house = House()

def add_label():
	counter=0
	all_label=[]
	x = house.how_many_floors 
	while x>counter:
		label=Label(bg='white',fg='black',width=10)
		label.grid(row=x,column=1)
		all_label.append(label)
		x-=1
	return all_label
add_label()

elevator=Elevator(add_label(),house.how_many_floors,root)

def add_entry():

	all_entry=[]
	counter=0
	x=house.how_many_floors 
	while x>counter:
		entry=Entry(width=20,bg='PaleTurquoise')
		entry.grid(row=x,column=0)
		all_entry.append(entry)
		x-=1
	return all_entry

all_entries=add_entry()

def call_the_elevator(event):
	find_need_entry(all_entries)
	for entry in all_entries:
		entry.delete(0,END)

global final_floor
global start_floor
def find_need_entry(all_entry):
    x=1
    for e in all_entry: 
        final_floor=e.get()
        if len(final_floor)>0:           
            start_floor=x
        x+=1

passenger=Passenger(elevator,4,1)#start_floor,final_floor)

passenger.call()

call_button=Button(text="call")
call_button.grid(row=house.how_many_floors+1,column=0)
call_button.bind('<1>',call_the_elevator)

root.geometry("500x500")
root.mainloop()




