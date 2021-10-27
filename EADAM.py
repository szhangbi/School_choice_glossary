from Base_lib import (School,Student)

class EADAM_School(School):
    @classmethod
    def from_School(cls, school):#convert a base school object into sBM_school, guarantee is set to be capacity
        return cls(school.id, school.prefList,school.capacity)

    def __init__(self, id, prefList, capacity=1):
        super().__init__(id, prefList, capacity)

    def reject(self, counter): #overriding the original reject function
        # trim the self.held set down to its capacity, returning the list of rejected students.

        if len(self.held) <= self.capacity:
            return set()
        else:
            sortedStudents = sorted(list(self.held), key=lambda student: self.prefList.index(
                student.id))  # immediate invoked function expression
            self.held = set(sortedStudents[:self.capacity])

            for student in sortedStudents[:self.capacity]:
                student.win_at.add(self.id)

            for student in sortedStudents[self.capacity:]:
                if self.id in student.win_at:
                    student.lose_at = [self.id, counter]

            return set(sortedStudents[self.capacity:])

class EADAM_Student(Student):
    @classmethod
    def from_Student(cls, student):#convert a base school object into sBM_school, guarantee is set to be capacity
        return cls(student.id, student.prefList)

    def __init__(self, id, prefList):
        super().__init__(id, prefList)
        self.win_at = set()
        self.lose_at = []

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
            unassigned |= school.reject(counter)

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

# EADAM [Student], [School] -> {School -> [Student]}
def EADAM(students, schools, verbose=False):

    if type(schools[0]) == type(School(-1,[])):#if guarantee is not specified, it is set to be capacity
        for id in range(len(schools)):
            schools[id] = EADAM_School.from_School(schools[id])

    if type(students[0]) == type(Student(-1,[])):#if guarantee is not specified, it is set to be capacity
        for id in range(len(students)):
            students[id] = EADAM_Student.from_Student(students[id])

    round = 0

    if verbose:
        print('Round ' + str(round) + ": ")
    matching = Defer_Acceptance(students, schools, verbose)

    interruptors = set()

    while interruptors or round == 0:
        round += 1

        last_step = 0
        interruptors = set()
        for student in students:
            if len(student.lose_at):
                if last_step < student.lose_at[1]:
                    last_step = student.lose_at[1]

        for student in students:
            if len(student.lose_at):
                if last_step == student.lose_at[1]:
                    interruptors.add(student.id)
                    if verbose:
                        print('interrupting pair: (' + str(student.id) + ',' + str(
                            student.lose_at[0]) + ') at step ' + str(student.lose_at[1]))

        if interruptors:
            for school in schools:
                school.held = set()
            for student in students:
                if student.id in interruptors:
                    student.prefList.remove(student.lose_at[0])
                student.rejections = 0
                student.engaged = False
                student.win_at = set()
                student.lose_at = []

            if verbose:
                print('Round ' + str(round) + ": ")
            matching = Defer_Acceptance(students, schools, verbose)

        else:
            continue

    return matching
