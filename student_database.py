# create function to display student info
def student_info():
    # Create lists for student info
    name_list = ['', 'Tina', 'Kyra', 'Brittany', 'Bernie', 'Tree']
    hometown_list = ['', 'Chicago', 'Detroit', 'Denver', 'Phoenix', 'Salt Lake City']
    favorite_food_list = ['', 'Banana', 'Pancakes', 'Dirt', 'Spaghetti', 'Deer Meat']

    num_students = len(name_list) - 1  # allows us to start at 1 instead of 0
    for particular_student in range(1, num_students + 1):  # prompts for particular student
        student_number = int(input("Enter a Student number, using 1 as your start: "))

        # checking if student number is valid
        if num_students + 1 > student_number >= 1:
            print("Name:", name_list[student_number])

            # prompt for category selection/validating category
            category = input("What category would you like to display? (hometown or favorite food): ")

            if category == "hometown":  # if hometown follows this
                print("hometown:", hometown_list[student_number])
            elif category == "favorite food":  # if favorite food follows this
                print("favorite food:", favorite_food_list[student_number])
            else:
                print("Invalid category")  # checking to ensure valid category
        else:
            print("Invalid student number")

        # ask for whether user wants to learn about another student
        another_student = input("Would you like to learn about another student? (yes or no): ")
        if another_student != "yes":
            break


student_info()
