
from Base_lib import School

class sBM_School(School):
    @classmethod
    def from_School(cls, school):#convert a base school object into sBM_school, guarantee is set to be capacity
        return cls(school.id, school.prefList,school.capacity,school.capacity)

    def __init__(self, id, prefList, capacity=1, guarantee =1):
        super().__init__(id, prefList, capacity)
        self.guarantee = self.capacity

# Secure Boston Mechanism/Immediate Acceptance: [Student], [School] -> {School -> [Student]}
def SecureBM(students, schools, verbose=False):

    if type(schools[0]) == type(School(-1,[])):#if guarantee is not specified, it is set to be capacity
        for id in range(len(schools)):
            schools[id] = sBM_School.from_School(schools[id])

    counter = 1
    unassigned = set(students)

    while len(unassigned) > 0:

        direct_rejection = set()
        for student in unassigned:
            to_app = schools[student.cur_top_pref()]
            if len(to_app.held) >= to_app.capacity:
                if to_app.prefList.index(student.id) >= to_app.guarantee:
                    direct_rejection.add(student)

        for student in unassigned:
            if student not in direct_rejection:
                to_app = schools[student.cur_top_pref()]
                to_app.held.add(student)

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