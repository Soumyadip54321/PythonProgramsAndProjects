# This prog demonstrates the power of function in py

def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0 "+name)


trip_planner_welcome("Soumyadip Sikdar")


def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


estimate = estimated_time_rounded(7.6)


def destination_setup(origin,destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in "+origin)
    print("You are travelling to " + destination)
    print("You will be travelling by " + mode_of_transport)
    print("It will take approximately ", estimated_time, "hrs to get there")


destination_setup("Bediapara", "Kalindi", estimate)




