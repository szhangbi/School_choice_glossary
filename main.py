import Base_lib
from Base_lib import (Student, School)
from BM import Immediate_Acceptance
from DA import Defer_Acceptance
from SecureBM import SecureBM
from EADAM import EADAM


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cases = Base_lib.gen_all_prio_pref_3()
    students, schools =  Base_lib.initialize_problem(cases[25])

    Immediate_Acceptance(students, schools, True)

    students, schools =  Base_lib.initialize_problem(cases[25])
    Defer_Acceptance(students, schools, True)

    students, schools = Base_lib.initialize_problem(cases[25])
    SecureBM(students, schools, True)

    students = [Student(0,[1,2,0,3,-1]), Student(1,[2,0,1,3,-1]), Student(2,[0,1,2,3,-1]),Student(3,[1,0,2,3,-1]),Student(4,[0,1,2,3,-1])]
    schools = [School(0,[0,2,1,3,4],2),School(1,[1,3,0,2,4],1),School(2,[0,1,2,3,4],1),School(3,[0,1,2,3,4],1),School(-1,[0,1,2,3,4],5)]
    DA_macthing = Defer_Acceptance(students, schools, True)

    i_dict=['i','j','k','l','m']
    s_dict= {0:'a',1:'b',2:'c',3:'d',-1:'nill'}
    i_str = ''
    s_str = ''
    for i in students:
        i_str = i_str +i_dict[i.id] +' | '
    for s in DA_macthing:
        s_str = s_str + s_dict[s]+ ' | '
    print(i_str)
    print(s_str)

    students = [Student(0,[1,2,0,3,-1]), Student(1,[2,0,1,3,-1]), Student(2,[0,1,2,3,-1]),Student(3,[1,0,2,3,-1]),Student(4,[0,1,2,3,-1])]
    schools = [School(0,[0,2,1,3,4],2),School(1,[1,3,0,2,4],1),School(2,[0,1,2,3,4],1),School(3,[0,1,2,3,4],1),School(-1,[0,1,2,3,4],5)]
    BM_macthing = Immediate_Acceptance(students, schools, True)
    s_str = ''
    for s in BM_macthing:
        s_str = s_str + s_dict[s] + ' | '
    print(i_str)
    print(s_str)

    students = [Student(0,[1,2,0,3,-1]), Student(1,[2,0,1,3,-1]), Student(2,[0,1,2,3,-1]),Student(3,[1,0,2,3,-1]),Student(4,[0,1,2,3,-1])]
    schools = [School(0,[0,2,1,3,4],2),School(1,[1,3,0,2,4],1),School(2,[0,1,2,3,4],1),School(3,[0,1,2,3,4],1),School(-1,[0,1,2,3,4],5)]
    sBM_macthing = SecureBM(students, schools, True)
    s_str = ''
    for s in sBM_macthing:
        s_str = s_str + s_dict[s] + ' | '
    print(i_str)
    print(s_str)

    students = [Student(0,[1,2,0,3,-1]), Student(1,[2,0,1,3,-1]), Student(2,[0,1,2,3,-1]),Student(3,[1,0,2,3,-1]),Student(4,[0,1,2,3,-1])]
    schools = [School(0,[0,2,1,3,4],2),School(1,[1,3,0,2,4],1),School(2,[0,1,2,3,4],1),School(3,[0,1,2,3,4],1),School(-1,[0,1,2,3,4],5)]
    EADAM_macthing = EADAM(students, schools, True)
    s_str = ''
    for s in EADAM_macthing:
        s_str = s_str + s_dict[s] + ' | '
    print(i_str)
    print(s_str)
