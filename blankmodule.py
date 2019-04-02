print('''
Multiple choic quize using python
Usint classes, if statements and loops

 ''')

from question import question
question_promt=[
"what colors are Apples?\n (a)Red/Green \n (b) Purple \n (c) Orange \n\n ",
"what colors are Bannas?\n (a)Teal \n (b) Magenta \n (c) Yellow\n\n ",
"what colors are strawberries?\n (a)Yellow \n (b) Red \n (c) Blue\n\n ",
]

questions =[
 question(question_promt[0], "a"),
 question(question_promt[1], "c"),
 question(question_promt[2], "b")

 ]



def run_test(questions):
    score=0
    for question in questions:
        answer = input(question_promt)
        if answer == question_answer:
            score+=1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(question)






print('''

 ''')

print('''


 ''')


print('''

 ''')