class Company:
      def __init__(self,name,address):
          self.name = name
          self.bus = []
          self.routes = []
          self.drivers = []
          self.counter = []
          self.manager = []
          self.supervisor=[]
          self.fare = []

class Driver:
       def __init__(self,name,license,age):
            self.license = license
            self.name = name
            self.age = age

class counter:
    def __init__(self):
        pass
    def purchase_a_ticket(self,start,destination):
        pass

class Passenger:
    pass

class supervisor:
    pass

red_mia = Driver("Fahim","1146767",32)