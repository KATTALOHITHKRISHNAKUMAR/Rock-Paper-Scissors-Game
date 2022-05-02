from tkinter import *
import random 

root = Tk() 

root.geometry("300x300") 

root.title("Rock Paper Scissor Game") 

computer_value = { "0":"Rock", "1":"Paper", "2":"Scissor"} 

user_score = 0
comp_score = 0
def reset_game(): 
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text = "Player			 ") 
	l3.config(text = "Computer") 
	l4.config(text = "") 

def button_disable(): 
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

def isrock():
	global comp_score, user_score
	c_v = computer_value[str(random.randint(0,2))] 
	if c_v == "Rock": 
		match_result = "MATCH DRAW\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	elif c_v == "Paper":
		comp_score += 1
		match_result = "COMPUTER WON\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	else:
		user_score += 1
		match_result = "USER WON\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	l4.config(text = match_result) 
	l1.config(text = "Rock		 ") 
	l3.config(text = c_v) 
	button_disable() 

def ispaper(): 
	global comp_score, user_score
	c_v = computer_value[str(random.randint(0, 2))] 
	if c_v == "Rock":
		user_score += 1
		match_result = "USER WON\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	elif c_v == "Paper": 
		match_result = "MATCH DRAW\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	else: 
		comp_score += 1
		match_result = "COMPUTER WON\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	l4.config(text = match_result) 
	l1.config(text = "Paper		 ") 
	l3.config(text = c_v) 
	button_disable() 

def isscissor():
	global comp_score, user_score
	c_v = computer_value[str(random.randint(0,2))] 
	if c_v == "Rock": 
		comp_score += 1
		match_result = "COMPUTER WON\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	elif c_v == "Paper":
		user_score += 1
		match_result = "USER WON\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	else:
		match_result = "MATCH DRAW\n" "USER SCORE:" +str(user_score) + "\nCOMP SCORE:" +str(comp_score)
	l4.config(text = match_result) 
	l1.config(text = "Scissor		 ") 
	l3.config(text = c_v) 
	button_disable() 

Label(root, 
	text = "ROCK PAPER SCISSOR", 
	font = "normal 20 bold", 
	fg = "blue").pack(pady = 20) 

frame = Frame(root) 
frame.pack() 

l1 = Label(frame, 
		text = "Player			 ", 
		font = 10) 

l2 = Label(frame, 
		text = "VS			 ", 
		font = "normal 10 bold") 

l3 = Label(frame, text = "Computer", font = 10) 

l1.pack(side = LEFT) 
l2.pack(side = LEFT) 
l3.pack() 

l4 = Label(root, 
		text = "", 
		font = "normal 20 bold", 
		bg = "white", 
		width = 15 , 
		borderwidth = 2, 
		relief = "solid") 
l4.pack(pady = 20) 

frame1 = Frame(root) 
frame1.pack() 

b1 = Button(frame1, text = "Rock", 
			font = 10, width = 7, 
			command = isrock) 

b2 = Button(frame1, text = "Paper ", 
			font = 10, width = 7, 
			command = ispaper) 

b3 = Button(frame1, text = "Scissor", 
			font = 10, width = 7, 
			command = isscissor) 

b1.pack(side = LEFT, padx = 10) 
b2.pack(side = LEFT,padx = 10) 
b3.pack(padx = 10) 

Button(root, text = "PLAY AGAIN", 
	font = 10, fg = "red", 
	bg = "black", command = reset_game).pack(pady = 20) 

root.mainloop()
