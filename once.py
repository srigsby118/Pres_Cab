import random
from time import sleep
from tkinter import *
from tkinter import font
from PIL import ImageTk
from tkinter import messagebox as msg

root = Tk()
root.title("The Presidential Cabinet Guessing Game")

agency_fb24 = font.Font(family = "Agency FB", size=28)
agency_fb12 = font.Font(family = "Agency FB", size=18)
arch_daughter = font.Font(family = "Architects Daughter", size=14)
goudyhtbt = font.Font(family = "GoudyHandtooled BT", size=24)

#variables containing each question
Q1a = "Who is the Secretary of the Treasury?"
Q2b = "Who is the Director of the Central Intelligence Agency (CIA)?"
Q3c = "Who is the Secretary of the Interior?"
Q4d = "Who is the Director of the Office of Management and Budget?"
Q5e = "Who is the Secretary of Labor?"
Q6f = "Who is the U.S. Trade Representative?"
Q7g = "Who is the Secretary of Transportation?"
Q8h = "Who is the Secretary of Education?"
Q9i = "Who is the Secretary of Commerce?"
Q10j = "Who is the Secretary of Housing and Urban Development (HUD)?"
Q11k = "Who is the Director of National Intelligence?"
Q12l = "Who is the Secretary of Agriculture?"
Q13m = "Who is the Administrator of the Environmental Protection Agency (EPA)?"
Q14n = "Who is the Secretary of Defense?"
Q15o = "Who is the Secretary of State?"
Q16p = "Who is the Vice President?"
Q17q = "Who is the Attorney General?"
Q18r = "Who is the Administrator of the Small Business Administration?"
Q19s = "Who is the U.S. Representative to the United Nations (UN)?"
Q20t = "Who is the Acting Secretary of Health and Human Services?"
Q21u = "Who is the White House Chief of Staff?"
Q22v = "Who is the Secretary of Energy?"
Q23w = "Who is the Secretary of Veterans Affairs?"
Q24x = "Who is the Acting Secretary of Homeland Security?"

#variables each containing an answer
N1 = "Steven Mnuchin"
N2 = "Mike Pompeo"
N3 = "Ryan Zinke"
N4 = "Mick Mulvaney"
N5 = "Alexander Acosta"
N6 = "Robert Lighthizer"
N7 = "Elaine Chao"
N8 = "Betsy DeVos"
N9 = "Wilbur Ross"
N10 = "Ben Carson"
N11 = "Dan Coats"
N12 = "Sonny Perdue"
N13 = "Scott Pruitt"
N14 = "James Mattis"
N15 = "Rex Tillerson"
N16 = "Mike Pence"
N17 = "Jeff Sessions"
N18 = "Linda McMahon"
N19 = "Nikki Haley"
N20 = "Eric Hargan"
N21 = "John Kelly"
N22 = "Rick Perry"
N23 = "David Shulkin"
N24 = "Elaine Duke"

#list containing the variables referring to each question
questions1 = [Q1a, Q2b, Q3c, Q4d, Q5e, Q6f, Q7g, Q8h, Q9i, Q10j, Q11k, Q12l, Q13m, Q14n, Q15o, Q16p, Q17q, Q18r, Q19s, Q20t, Q21u, Q22v, Q23w, Q24x]

#list containing the variables referring to each answer - used for the answer pool
answers2 = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15,
            N16, N17, N18, N19, N20, N21, N22, N23, N24]

#dictionary containing the question and answer variables
Q_and_A = {Q1a:N1, Q2b:N2, Q3c:N3, Q4d:N4, Q5e:N5, Q6f:N6, Q7g:N7, Q8h:N8, Q9i:N9, Q10j:N10, Q11k:N11, Q12l:N12, Q13m:N13, Q14n:N14, Q15o:N15, Q16p:N16, Q17q:N17, Q18r:N18, Q19s:N19, Q20t:N20, Q21u:N21, Q22v:N22, Q23w:N23, Q24x:N24}

#list containing strings of the number of each question
ques_num_list = ["1.  ", "2.  ", "3.  ", "4.  ", "5.  ", "6 . ", "7.  ", "8.  ", "9.  ", "10.  ", "11.  ", "12.  ", "13.  ", "14.  ", "15.  ", "16.  ", "17.  ", "18.  ", "19.  ", "20 . ", "21.  ", "22.  ", "23.  ", "24.  "]
topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomleftFrame = Frame(root)
bottomleftFrame.pack(side=LEFT)
bottomrightFrame = Frame(root)
bottomrightFrame.pack(side=RIGHT)

#shuffles the questions1 list
random.shuffle(questions1)
#assigns the index 0 of the list, questions1 to the variable nq1
nq1 =  (questions1[0])
#assigns the value of nq1 to the variable correctD
correctD = Q_and_A.get(nq1)
#removes the correct answer from the answer pool
answers2.remove(correctD)
#randomly chooses three incorrect choices for each question
rand_choices1 = random.choices(answers2, k=3)
print(rand_choices1)

"""if there is a duplicate in the random choices, it goes through the process again until all three choices are unique"""
while (rand_choices1[0] == rand_choices1[1]) or (rand_choices1[0] == rand_choices1[2]) or (rand_choices1[1] == rand_choices1[2]):
  rand_choices1 = list(random.choices(answers2, k=3))

#adds the correct answer to the choices1 list and shuffles choices
if (rand_choices1[0] != rand_choices1[1]) and (rand_choices1[0] != rand_choices1[2]) and (rand_choices1[1] != rand_choices1[2]):
  choices1 = [rand_choices1[0], rand_choices1[1], rand_choices1[2], correctD]
  random.shuffle(choices1)
#adds correct answer back into the answer pool
  answers2.append(correctD)

header1 = Label(root, text="The Presidential Cabinet Guessing Game", fg="#004fa3", font=agency_fb24)
header1.pack(anchor=NW)

directions = LabelFrame(root, text="Directions: Select the correct answer to each question.")
directions.pack(fill=X, expand=YES, anchor=N, padx=10, pady=10, ipady=5)

print(rand_choices1)
#defines choice buttons
choice_A = Button(directions, text="first", width=20)
choice_A.configure(text=choices1[0])
choice_B = Button(directions, text="first", width=20)
choice_B.configure(text=choices1[1])
choice_C = Button(directions, text="first", width=20)
choice_C.configure(text=choices1[2])
choice_D = Button(directions, text="first", width=20)
choice_D.configure(text=choices1[3])

#assigns the choices1 list to each variable
dum_A = choices1[0]
dum_B = choices1[1]
dum_C = choices1[2]
dum_D = choices1[3]

#assigns the correct answer to the variable dummy
dummy = (correctD)

next_but = Button(directions, text="Next Question")

#good_job and try_again labels defined
good_job = Label(directions, text="FANTASTIC!")
try_again = Label(directions, text="That is incorrect. Try again!")


def right_choice_A(event):
  if dum_A == dummy:
    good_job.pack()
    next_but.pack()
  else:
    try_again.pack()
    try_again.after(1500, clear_try)

def right_choice_B(event):
  if dum_B == dummy:
    good_job.pack()
    next_but.pack()
  else:
    try_again.grid(row=5, column=2)
    try_again.after(1500, clear_try)

def right_choice_C(event):
  if dum_C == dummy:
    good_job.pack()
    next_but.pack()
  else:
    try_again.pack()
    try_again.after(1500, clear_try)

def right_choice_D(event):
  if dum_D == dummy:
    good_job.pack()
    next_but.pack()
  else:
    try_again.pack()
    try_again.after(1500, clear_try)

choice_A.bind("<Button-1>", right_choice_A)
choice_B.bind("<Button-1>", right_choice_B)
choice_C.bind("<Button-1>", right_choice_C)
choice_D.bind("<Button-1>", right_choice_D)

def clear_try():
  try_again.pack_forget()

ques_num = Label(directions, text="first")
ques_num.configure(text=ques_num_list[0] + questions1[0])

start_but = Button(directions, text="Start", fg="white", bg="#004FA3", font="Calibri", width=10)
start_but.pack(anchor=CENTER, pady=(10, 5))

def start_game(event):
  start_but.pack_forget()
  ques_num.pack(anchor=NW, padx=18, pady=7)
  choice_A.pack(anchor=NW, padx=35, pady=3)
  choice_B.pack(anchor=NW, padx=35, pady=3)
  choice_C.pack(anchor=NW, padx=35, pady=3)
  choice_D.pack(anchor=NW, padx=35, pady=3)

  print ("Choice A = ", dum_A)
  print("Choice B = ", dum_B)
  print("Choice C = ", dum_C)
  print("Choice D = ", dum_D)

start_but.bind("<Button-1>", start_game)

# creates the end of game message
end_of_game_mes = Label(directions,text="You have reached the end of the game! Hit the Quit Button to quit or the Replay Button to play again.")

# creates the quit button
quit_but = Button(directions, text="Quit Game", command=quit)

# creates the replay button
replay_but = Button(directions, text="Replay the Game")

#Next Question button method
def next_ques(event):
  """if the list, questions1 is empty, it displays the end of game message, quit button, and the replay button"""
  if len(questions1) == 1:
    #makes question and number disappear
    ques_num.pack_forget()
    end_of_game_mes.pack()
    quit_but.pack()
    good_job.pack_forget()
    #makes the next button disappear
    next_but.pack_forget()
    # make previous choices disappear
    choice_A.pack_forget()
    choice_B.pack_forget()
    choice_C.pack_forget()
    choice_D.pack_forget()
  else:
    print(len(questions1))
    print("test")

    good_job.pack_forget()

    #makes question and number disappear
    ques_num.pack_forget()

    #removes index 0 from the list, questions1
    questions1.remove(questions1[0])

    #removes index 0 from the list, ques_num_list
    ques_num_list.remove(ques_num_list[0])

    #makes the next button disappear when clicked
    next_but.pack_forget()

    #makes previous choices disappear
    choice_A.pack_forget()
    choice_B.pack_forget()
    choice_C.pack_forget()
    choice_D.pack_forget()

    # assigns the index 0 of the list, questions1 to the variable nq1
    nq1 = (questions1[0])

    # assigns the value of nq1 to the variable correctD
    correctD = Q_and_A.get(nq1)

    # removes the correct answer from the answer pool
    answers2.remove(correctD)

    # randomly chooses three incorrect choices for each question

    #configure new question and number
    ques_num.configure(text=ques_num_list[0] + questions1[0])

    #displays new question and number
    ques_num.pack(anchor=NW, padx=18, pady=7)

    #create new choices
    rand_choices1 = random.choices(answers2, k=3)


    #duplicates avoided
    while (rand_choices1[0] == rand_choices1[1]) or (rand_choices1[0] == rand_choices1[2]) or (rand_choices1[1] == rand_choices1[2]):
      rand_choices1 = list(random.choices(answers2, k=3))

    #copies new choices to choices1 list
    if (rand_choices1[0] != rand_choices1[1]) and (rand_choices1[0] != rand_choices1[2]) and (rand_choices1[1] != rand_choices1[2]):
      choices1 = [rand_choices1[0], rand_choices1[1], rand_choices1[2], correctD]

      #shuffles new choices
      random.shuffle(choices1)
      #adds correct answer back into the answer pool
      answers2.append(correctD)
    #configures new text on the new choice buttons
    choice_A.configure(text=choices1[0], width=20)
    choice_B.configure(text=choices1[1], width=20)
    choice_C.configure(text=choices1[2], width=20)
    choice_D.configure(text=choices1[3], width=20)

    #assigns dummy variables to new choices
    dum_A = choices1[0]
    dum_B = choices1[1]
    dum_C = choices1[2]
    dum_D = choices1[3]

    #assigns correct dummy variable to correct answer variable
    dummy = (correctD)

    #good_job and try_again labels defined
    try_again = Label(directions, text="That is incorrect. Try again!")

    #method to clear the try again message after the next button is clicked
    def clear_try():
      try_again.pack_forget()



    #method bound to choice A button
    #shows the good_job message if choice A is correct and then displays the next button
    #good_job message is cleared after 3 seconds
    def right_choice_A(event):
      if dum_A == dummy:
        good_job.pack()
        next_but.pack()

      #if choice A is clicked, but not correct, the try again message shows
      #try again message disappears after 3 seconds
      else:
        try_again.pack()
        try_again.after(1500, clear_try)

    # method bound to choice B button
    # shows the good_job message if choice B is correct and then displays the next button
    # good_job message is cleared after 3 seconds
    def right_choice_B(event):
      if dum_B == dummy:
        good_job.pack()
        next_but.pack()

      # if choice B is clicked, but not correct, the try again message shows
      # try again message disappears after 3 seconds
      else:
        try_again.pack()
        try_again.after(1500, clear_try)

    # method bound to choice Cbutton
    # shows the good_job message if choice C is correct and then displays the next button
    # good_job message is cleared after 3 seconds
    def right_choice_C(event):
      if dum_C == dummy:
        good_job.pack()
        next_but.pack()

      # if choice C is clicked, but not correct, the try again message shows
      # try again message disappears after 3 seconds
      else:
        try_again.pack()
        try_again.after(1500, clear_try)

    # method bound to choice D button
    # shows the good_job message if choice D is correct and then displays the next button
    # good_job message is cleared after 3 seconds
    def right_choice_D(event):
      if dum_D == dummy:
        good_job.pack()
        next_but.pack()

      # if choice D is clicked, but not correct, the try again message shows
      # try again message disappears after 3 seconds
      else:
        try_again.pack()
        try_again.after(1500, clear_try)

    #binds the above methods to each choice button
    choice_A.bind("<Button-1>", right_choice_A)
    choice_B.bind("<Button-1>", right_choice_B)
    choice_C.bind("<Button-1>", right_choice_C)
    choice_D.bind("<Button-1>", right_choice_D)

    #display choices
    choice_A.pack(anchor=NW, padx=35, pady=3)
    choice_B.pack(anchor=NW, padx=35, pady=3)
    choice_C.pack(anchor=NW, padx=35, pady=3)
    choice_D.pack(anchor=NW, padx=35, pady=3)

    #make sure Start button is gone
    start_but.pack_forget()

#binds Next button and Skip Question button to methods
next_but.bind("<Button-1>", next_ques)


root.mainloop()