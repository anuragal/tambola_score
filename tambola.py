import numpy as np

ticket = np.array([[0, 11, 28, 0, 0, 52, 0, 74, 80], 
                   [0, 16, 0, 33, 42, 54, 67, 0, 0],
                   [3, 18, 0, 0, 47, 0, 68, 0, 88]
                  ])

class Tambola:
    def __init__(self, ticket, name):
        self.ticket = ticket
        self.name = name
        self.all_crossed = False

        self.corners = set()
        self.first_line = set()
        self.second_line = set()
        self.third_line = set()
        self.first_half = set()
        self.second_half = set()
        self.full_house = set()
        self.early_five = set()

        self.find_corner_numbers()
        self.first_line = self.find_line(1)
        self.second_line = self.find_line(2)
        self.third_line = self.find_line(3)
        self.find_first_half()
        self.find_second_half()
        self.find_full_house()
        self.find_early_five()

    def find_line(self, line_num):
        return set([x for x in self.ticket[line_num - 1] if x != 0])
    
    def find_corner_numbers(self):
        for num in self.ticket[0]:
            if num != 0:
                self.corners.add(num)
                break
        for num in self.ticket[0][-1:]:
            if num != 0:
                self.corners.add(num)
                break
        for num in self.ticket[2]:
            if num != 0:
                self.corners.add(num)
                break
        for num in self.ticket[2][-1:]:
            if num != 0:
                self.corners.add(num)
                break

    def find_first_half(self):
        for row in range(3):
            for num in self.ticket[row]:
                if num <= 45 and num != 0:
                    self.first_half.add(num)

    def find_second_half(self):
        for row in range(3):
            for num in self.ticket[row]:
                if num > 45 and num != 0:
                    self.second_half.add(num)

    def find_full_house(self):
        for row in range(3):
            for num in self.ticket[row]:
                if num != 0:
                    self.full_house.add(num)

    def find_early_five(self):
        for row in range(3):
            for num in self.ticket[row]:
                if num != 0:
                    self.early_five.add(num)

    def check_and_cross(self, new_num):
        if new_num in self.corners and len(self.corners) > 0:
            self.corners.discard(new_num)
            if len(self.corners) == 0:
                print("Corner Done on number " + str(new_num))

        if new_num in self.first_line and len(self.first_line) > 0:
            self.first_line.discard(new_num)
            if len(self.first_line) == 0:
                print("First Line Done on number " + str(new_num))

        if new_num in self.second_line and len(self.second_line) > 0:
            self.second_line.discard(new_num)
            if len(self.second_line) == 0:
                print("Second Line Done on number " + str(new_num))

        if new_num in self.third_line and len(self.third_line) > 0:
            self.third_line.discard(new_num)
            if len(self.third_line) == 0:
                print("Third Line Done on number " + str(new_num))

        if new_num in self.first_half and len(self.first_half) > 0:
            self.first_half.discard(new_num)
            if len(self.first_half) == 0:
                print("First Half Done on number " + str(new_num))

        if new_num in self.second_half and len(self.second_half) > 0:
            self.second_half.discard(new_num)
            if len(self.second_half) == 0:
                print("Second Half Done on number " + str(new_num))
                
        if new_num in self.full_house and len(self.full_house) > 0:
            self.full_house.discard(new_num)
            if len(self.full_house) == 0:
                self.all_crossed = True
                print("Full house Done on number " + str(new_num))

        if new_num in self.early_five and len(self.early_five) > 0:
            self.early_five.discard(new_num)
            if len(self.early_five) == 10:
                print("Early Five Done on number " + str(new_num))

    def print_all(self):
        print(self.corners)
        print(self.first_line)
        print(self.second_line)
        print(self.third_line)
        print(self.first_half)
        print(self.second_half)
        print(self.full_house)
        print(self.early_five)


if __name__ == "__main__":
    tambola_obj = Tambola(ticket, "Anurag")
    #tambola_obj.print_all()
    print("Enter Tambola Number")
    while True:
        input_number = int(input())
        if input_number == -1:
            break
        
        tambola_obj.check_and_cross(input_number)
        if tambola_obj.all_crossed == True:
            break
