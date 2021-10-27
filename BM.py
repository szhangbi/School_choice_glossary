


# Boston Mechanism/Immediate Acceptance: [Student], [School] -> {School -> [Student]}
def Immediate_Acceptance(students, schools, verbose=False):
    counter = 1
    unassigned = set(students)

    while len(unassigned) > 0:

        direct_rejection = set()

        for student in unassigned:
            if len(schools[student.cur_top_pref()].held) >= schools[student.cur_top_pref()].capacity:
                direct_rejection.add(student)

        for student in unassigned :
            if student not in direct_rejection:
                schools[student.cur_top_pref()].held.add(student)

        unassigned = direct_rejection

        if verbose:
            app = ""
            for school in schools:
                app = app + "{"
                for student in students:
                    if student.cur_top_pref() == school.id:
                        app = app + str(student.id) + ","
                if app[-1] == ",":
                    app = app[:-1] + "} | "
                else:
                    app = app + "} | "
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

    marriage = list()

    for student in students:
        marriage.append(student.prefList[student.rejections])

    return marriage