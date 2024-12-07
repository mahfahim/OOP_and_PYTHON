class star_cinema:
    _hall_list = []
    def __init__(self):
        pass
    @classmethod
    def entry_hall(cls,hall_obj):
        cls._hall_list.append(hall_obj)
        print(f"Hall {hall_obj._hall_no} is successfully added")



class hall(star_cinema):

    def __init__(self,hall_no,rows,cols):
        self._hall_no = hall_no
        self._rows = rows
        self._cols = cols
        self._seats = {}
        self._show_list = []
        star_cinema.entry_hall(self)
        
        

    def entry_show(self,show_id,movie_name,time):
        show_tuple = (show_id,movie_name,time)
        self._show_list.append(show_tuple)

        self._seats[show_id] = [[0 for x in range(self._cols)] for x in range(self._rows)]   
        print(f"Show no {show_id} added successfully")


    def book_seats(self,show_id,row,col):
    
        if show_id not in self._seats:
            print("Invalid Show ID!")

        elif row >= self._rows or row < 0 or col < 0 or col >= self._cols:
            print("This seat is not exist in this hall")

        elif self._seats[show_id][row][col] == 0 :
            self._seats[show_id][row][col]=1
            print(f"Seat ({row},{col}) is booked for you")

        elif self._seats[show_id][row][col] == 1:
            print("This seat is already booked")
        
            
    def view_show_list(self):
        print("Today all shows are : ")
        
        if not self._show_list:
            print("No shows are available")
            return
        for id,nam,t in self._show_list:
            print(f"Show_ID: {id} , Movie_name: {nam} , Time: {t}")
    
    def view_available_seats(self,show_id):
        print(f"Available seats for Show id {show_id}: ")
        if show_id not in self._seats:
            print("This show is not found")
            return

        for i in range(self._rows):
            for j in range(self._cols):
               if self._seats[show_id][i][j] == 0:
                    print(f"Seat({i},{j})")        
        
     
 


h1 = hall(111,5,3)
h2 = hall(222,4,1)
h3 = hall(333,4,3)
h4 = hall(444,2,3)
h5 = hall(555,4,2)
print()

h1.entry_show(10,"Jane Man","7:30 PM")
h2.entry_show(20,"Ura Dhura","8:30 PM")
h3.entry_show(30,"Digbaji","9:30 PM")
h4.entry_show(40,"Khela Hobe","6:30 PM")
h5.entry_show(50,"Le Halua","5:30 PM")
print()

halls = [h1,h2,h3,h4,h5]

while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")

    step = int(input("Enter OPTION : "))

    if step == 1:
        a = int(input("Enter Hall No: "))
    
        for h in halls:
            if h._hall_no == a:
                h.view_show_list()
                break
        else:
            print("Hall not found")


    elif step == 2:
        a = int(input("Enter Hall No: "))
        for h in halls:
           if h._hall_no == a:
              break
        else:
            print("Hall not found")
            continue
        x = int(input("Enter Show ID: "))
        flag = True
        for h in halls:
               if h._hall_no == a:
                    h.view_available_seats(x)
                    flag = False
                    break
                
        if flag == True:
            print("This show is not in this hall")

    elif step == 3:
        a = int(input("Enter Hall No: "))
        for h in halls:
           if h._hall_no == a:
              break
        else:
            print("Hall not found")
            continue
        x  = int(input("Enter Show ID: "))
        y  = int(input("Enter row of seat : "))
        z  = int(input("Enter coloum of seat : "))
        flag = True
        for h in halls:
               if h._hall_no == a:
                    h.book_seats(x,y,z)
                    flag=False
                    break
        if flag == True:
            print("This show is not in this hall")

    elif step == 4:
        print("Exit")
        break
    
    print()


