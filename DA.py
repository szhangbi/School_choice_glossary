

def Defer_Acceptance(students, schools, verbose=False):
    unassigned = set(students)

    counter = 1

    while len(unassigned) > 0:
        for student in unassigned:
            schools[student.cur_top_pref()].held.add(student)
        unassigned = set()

        if verbose:
            app = ""
            for school in schools:
                app = app + str(school.held) + " | "

        for school in schools:
            unassigned |= school.reject()

        if verbose:
            temp = ""
            for school in schools:
                temp = temp + str(school.held) + " | "

        for student in unassigned:
            student.rejections += 1

        if verbose:
            print('Step: ' + str(counter) + '\n' + app + '\n' + temp)
        counter += 1

    matching = list()

    for student in students:
        matching.append(student.prefList[student.rejections])

    return matching