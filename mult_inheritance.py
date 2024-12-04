class NormalRoom:
    def calculates(self, no_rooms, days):
        if days == 1:
            room_rent = 300
        elif days > 1 and days <= 5:
            room_rent = 250
        else:
            room_rent = 200
        total_rent = room_rent * no_rooms
        return total_rent

class AcRoom:
    def ac_calculates(self, no_rooms, days):
        if days == 1:
            room_rent = 450
        elif days > 1 and days <= 5:
            room_rent = 300
        else:
            room_rent = 250
        total_rent = room_rent * no_rooms
        return total_rent

class SuiteRoom:
    def suite_calculates(self, no_rooms, days):
        if days == 1:
            room_rent = 550
        elif days >= 5:
            room_rent = 500
        else:
            room_rent = 450
        total_rent = room_rent * no_rooms
        return total_rent

class Hotel(NormalRoom, AcRoom, SuiteRoom):
    
    pass  


derived_room = Hotel()


normal_rent = derived_room.calculates(2, 3) 
ac_rent = derived_room.ac_calculates(1, 5)   
suite_rent = derived_room.suite_calculates(3, 7) 

print(f"Normal Room Rent: {normal_rent}")
print(f"AC Room Rent: {ac_rent}")
print(f"Suite Room Rent: {suite_rent}")
