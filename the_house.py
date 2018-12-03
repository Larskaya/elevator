import time 

class House:
    def __init__(self):
        self.how_many_floors=5

class Elevator:
    def __init__(self,labels,how_many_floors, tk):
        self.where_elevator=0
        self.labels=labels
        self.count_passengers=0
        self.how_many_floors=how_many_floors
        self.show_elevator()
        self.tk=tk

    def show_elevator(self):
        print('show')
        self.labels[self.where_elevator]['text']=str('[ '+('x' * self.count_passengers)+' ]')
        print('get',self.labels[self.where_elevator]['text'])

    def elevator_goto(self,passenger_floor,target_floor):
        print('passenger floor:',passenger_floor)
        self.go_to_floor(int(passenger_floor)-1)
        self.count_passengers=2
        self.go_to_floor(int(target_floor)-1)
        self.count_passengers=0
        self.show_elevator()

    # двигает [] до нужного этажа
    def go_to_floor(self,target): 
        print('where elevator:',self.where_elevator)
        print('target:',target)
        while self.where_elevator!=int(target):
            self.labels[self.where_elevator]['text']='---'
            time.sleep(0.9)
            if self.where_elevator<int(target):
                self.where_elevator+=1
            else:
                self.where_elevator-=1
            # показывает [] на нужном этаже
            self.show_elevator()
            self.tk.update()

            print('go_to_floor check: where  target  != :', self.where_elevator, target, self.where_elevator!=target)

class Passenger:
    def __init__(self,elevator,where_am_i,where_i_want):
        self.elevator=elevator
        self.where_am_i=where_am_i
        self.where_i_want=where_i_want

    def call(self):
        self.elevator.elevator_goto(self.where_am_i,self.where_i_want)
        

         








       
