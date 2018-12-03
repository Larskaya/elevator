from tkinter import *
from classes_elevator import *

root = Tk()
house = House(9)

def create_stages():
	counter=0
	all_label=[]
	x = house.how_many_floors 
	while x>counter:
		label=Label(bg='white',fg='black', width=10)
		label.grid(row=x,column=1)
		all_label.append(label)
		x-=1
	return all_label

stages = create_stages()

elevator=Elevator(stages, house.how_many_floors, root)

# создаем поля ввода на каждый этаж
def create_stages_fields():
	all_entry=[]
	counter=0
	x=house.how_many_floors 
	while x>counter:
		entry=Entry(width=20, bg='PaleTurquoise')
		entry.grid(row=x, column=0)
		all_entry.append(entry)
		x-=1
	return all_entry

all_entries=create_stages_fields()

# вызываем лифт
def call_the_elevator(event):
	# смотрим откуда и куда ехать
	from_to_floors = find_need_entry()
	# отправляем лифт по полученным данным
	elevator.elevator_goto(from_to_floors[0], from_to_floors[1])
	# clean inputs
	for entry in all_entries:
		entry.delete(0,END)


def find_need_entry():
    x=1
    for e in all_entries: 
        final_floor=e.get()
        if len(final_floor)>0:
            start_floor=x
            return start_floor, final_floor
        x+=1
    return 0, 0


call_button=Button(text="call")
call_button.grid(row=house.how_many_floors+1,column=0)
call_button.bind('<1>',call_the_elevator)

root.geometry("500x500")
root.mainloop()

passenger=Passenger(elevator,4,1)#start_floor,final_floor)

passenger.call()



