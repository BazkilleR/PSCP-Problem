"""Muddled Menu"""

def muddled_menu():
    """aaaaa"""
    course = []

    while True:
        food_input = input()

        if food_input == "DONE":
            break

        if food_input == "CLOSED":
            return "Full Course: [] Reversed: []"

        if food_input == "SOMETHING'S WRONG":
            course = []
            continue

        # Handle "Can't do" command
        if food_input.startswith("Can't do"):
            food_to_remove = food_input.split(": ", 1)[1].strip()  # Get the food item to remove
            if food_to_remove in course:
                course.remove(food_to_remove)
            continue

        # Split food name and course number
        food_name, course_number = food_input.split("#", 1)
        food_name = food_name.strip()  # Clean up the food name

        if course_number.strip() == "N":
            course.append(food_name)  # If #N, append at the end
        else:
            position = int(course_number.strip())  # Convert to integer
            course.insert(position - 1, food_name)  # Insert at the specified position

    reversed_course = list(course)
    reversed_course.reverse()

    return f"Full Course: {course} Reversed: {reversed_course}"

print(muddled_menu())
