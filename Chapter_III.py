def count_options():
    possibility_password_meet_all_the_criteria = 0

    # third criteria
    for possibility_password in range(372 ** 2, (809 ** 2) + 1):
        possibility_password = str(possibility_password)

        # second criteria
        possibility_password_never_decrease = True
        for i in range(len(possibility_password) - 1):
            if possibility_password_never_decrease:
                if possibility_password[i] <= possibility_password[i + 1]:
                    possibility_password_never_decrease = True
                else:
                    possibility_password_never_decrease = False
        if possibility_password_never_decrease:

            #  first criteria
            groups_of_adjacent_identical_digits = 0
            for i in range(1, 10):
                if possibility_password.count(str(i)) >= 2:
                    groups_of_adjacent_identical_digits += 1
            if groups_of_adjacent_identical_digits >= 2:
                possibility_password_meet_all_the_criteria += 1
    return possibility_password_meet_all_the_criteria


print(f"I have to check {count_options()} numbers.")
