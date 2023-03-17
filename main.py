#########################
# IMPORTS				#
#########################

from teacher import Teacher

from exam_simulator import Exam

#########################
# MAIN               	#
#########################

# create an instance of the Teacher class

teacher = Teacher()

# creates test based on topic requested,
# along with the number of possible answers per questions,
# and the number of questions 

student_view, answers = teacher.create_full_test()

# create an instance of the Exam class

exam = Exam(student_view, answers, store_test=True, topic=teacher.test_creator.topic)

# run exam simulation

student_answers = exam.take()

print(student_answers)

# grades the exam

grade = exam.grade(student_answers)

print(grade)

