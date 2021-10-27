
class School(object):
    def __init__(self, id, prefList, capacity=1):
        self.prefList = prefList
        self.capacity = capacity
        self.held = set()
        self.id = id

    def reject(self):
        # trim the self.held set down to its capacity, returning the list of rejected students.

        if len(self.held) <= self.capacity:
            return set()
        else:
            sortedStudents = sorted(list(self.held), key=lambda student: self.prefList.index(
                student.id))  # immediate invoked function expression
            self.held = set(sortedStudents[:self.capacity])

            return set(sortedStudents[self.capacity:])

    def __repr__(self):
        return repr(self.id)

class Student(object):
    def __init__(self, id, prefList):
        self.prefList = prefList
        self.rejections = 0 # num rejections is also the index of the next option
        self.id = id
        self.engaged = False

    def cur_top_pref(self):
        return self.prefList[self.rejections]

    def __repr__(self):
        return repr(self.id)

import itertools
def gen_all_prio_pref_3():
    profiles = []
    for prioR in itertools.permutations([j for j in range(0, 3) if j != 0]):
        for prioG in itertools.permutations([j for j in range(0, 3) if j != 1]):
            for prioB in itertools.permutations([j for j in range(0, 3) if j != 2]):
                for prefL1 in itertools.permutations([i for i in range(3)]):
                    for prefL2 in itertools.permutations([i for i in range(3)]):
                        for prefL3 in itertools.permutations([i for i in range(3)]):
                            profiles.append([[0]+list(prioR),[1]+list(prioG),[2]+list(prioB),
                                             list(prefL1),list(prefL2),list(prefL3)])
    return profiles


def initialize_problem(profile,students = [], schools = []):
    students = []
    schools = []

    for id in range(0,3):
        students.append(Student(id,profile[id+3]))

    for id in range(0,3):
        schools.append(School(id,  profile[id], 1))

    return students, schools

