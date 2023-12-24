class Elevator:
    def __init__(self):
        self.__first_floor = 0
        self.__last_floor = 16
        self.current_floor = 3
        self.floors_to_last_floor = self.__last_floor - self.current_floor

    def __go_up(self):
        # If the current floor is the topmost
        if self.current_floor == self.__last_floor:
            return

        self.current_floor += 1
        print(f"Going up! Next floor: {self.current_floor}")

    def __go_down(self):
        # If the current floor is the bottom
        if self.current_floor == self.__first_floor:
            return

        self.current_floor -= 1
        print(f"Going down! Next floor: {self.current_floor}")

    def __go_to_floor(self, target_floor):
        if (target_floor < self.__first_floor) or (target_floor > self.__last_floor):
            print("Error! Floor is out of range.")
            return

        if self.current_floor == target_floor:
            print(f"You are currently on that floor!")
            return

        while True:
            if self.current_floor < target_floor:
                self.__go_up()
            elif self.current_floor > target_floor:
                self.__go_down()
            else:
                print(f"You have arrived on the target floor! ({target_floor})")
                return

    def __calculate_query_order(self, floors_list: list):
        final_query_list = []
        low_values_sorted = sorted([x for x in floors_list if x < self.current_floor])
        high_values_sorted = sorted([x for x in floors_list if x > self.current_floor])

        print(f"Floors before current floor: ", *[str(x) for x in low_values_sorted])
        print("Floors after current floor: ",  *[str(x) for x in high_values_sorted])

        if self.floors_to_last_floor <= self.current_floor:
            # Going upwards
            final_query_list += high_values_sorted
            final_query_list += low_values_sorted[::-1]
            return final_query_list
        # Going down
        final_query_list += low_values_sorted[::-1]
        final_query_list += high_values_sorted
        return final_query_list

    def execute_query(self, query_to_calc):
        calculated_query = self.__calculate_query_order(query_to_calc)
        print("Calculated order:", *[str(x) for x in calculated_query])
        print()

        print(f"Current floor: {self.current_floor}")
        for floor in calculated_query:
            print(f"Next Stop - Floor: {floor}")
            self.__go_to_floor(floor)


# Enter the floors to stop on
query = [2, 10, 3, 5, 8, 1, 15]

elevator = Elevator()
elevator.execute_query(query)


"""
Example output

Floors before current floor:  1 2
Floors after current floor:  5 8 10 15
Calculated order: 2 1 5 8 10 15

Current floor: 3
Next Stop - Floor: 2
Going down! Next floor: 2
You have arrived on the target floor! (2)
Next Stop - Floor: 1
Going down! Next floor: 1
You have arrived on the target floor! (1)
Next Stop - Floor: 5
Going up! Next floor: 2
Going up! Next floor: 3
Going up! Next floor: 4
Going up! Next floor: 5
You have arrived on the target floor! (5)
Next Stop - Floor: 8
Going up! Next floor: 6
Going up! Next floor: 7
Going up! Next floor: 8
You have arrived on the target floor! (8)
Next Stop - Floor: 10
Going up! Next floor: 9
Going up! Next floor: 10
You have arrived on the target floor! (10)
Next Stop - Floor: 15
Going up! Next floor: 11
Going up! Next floor: 12
Going up! Next floor: 13
Going up! Next floor: 14
Going up! Next floor: 15
You have arrived on the target floor! (15)
"""
