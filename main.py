def convert_input(question, conversion, failure_message):
    while True:
        try:
            converted_input = conversion(input(question))
        except ValueError:
            print(failure_message)
            continue

        return converted_input


def main():
    class_count = convert_input("How many classes are you in? ", int, "Invalid class count. Please try again")

    print()
    class_gpas = []
    for i in range(class_count):
        while True:
            class_gpa = convert_input(f"Enter grade for class {i + 1} (0.0-4.0): ", float, "Invalid GPA. Please try again")

            if not 0.0 <= class_gpa <= 4.0:
                print("GPA must be between 0.0 and 4.0. Please try again")
                continue

            class_gpas.append(class_gpa)
            break

    average_gpa = sum(class_gpas) / len(class_gpas)

    print()
    print(f"Your current average GPA is {average_gpa:.2f}")

    print()
    print("Which semester do you want to anylize?")
    print("1. First semester (first half of classes rounded down)")
    print("2. Second semester (second half of classes rounded up)")

    while True:
        semester = convert_input("Enter 1 or 2: ", int, "Invalid semester. Please try again")

        if semester not in [1, 2]:
            print("Semester must be 1 or 2. Please try again")
            continue

        break

    if semester == 1:
        semester_grades = class_gpas[:class_count // 2]
    else:
        semester_grades = class_gpas[class_count // 2:]

    semester_average_gpa = sum(semester_grades) / len(semester_grades)

    print()
    print(f"Semester {semester} GPA: {semester_average_gpa:.2f}")
    print(f"Overall GPA: {average_gpa:.2f}")

    while True:
        goal_gpa = convert_input("What's your goal GPA?: ", float, "Invalid GPA. Please try again")

        if not 0.0 <= goal_gpa <= 4.0:
            print("GPA must be between 0.0 and 4.0. Please try again")
            continue

        break

    if average_gpa >= goal_gpa:
        print("Congrats! You've already met your goal!")
    else:
        goal_classes = []
        for i, class_gpa in enumerate(class_gpas):
            new_gpa = average_gpa + ((4.0 - class_gpa) / len(class_gpas))
            if new_gpa >= average_gpa:
                goal_classes.append((i, class_gpa, new_gpa))

        if goal_classes:
            print(f"Good news! You can reach your goal of {goal_gpa} by improving just ONE grade:")
            for i, goal_class, new_gpa in goal_classes:
                print(f"- If you raise your grade in class {i} from {goal_class:.2f} to 4.0, your GPA would be {new_gpa:.2f}")
        else:
            print("Too bad! You'll have to get your grade up in multiple classes to meet your goal")


if __name__ == "__main__":
    main()
