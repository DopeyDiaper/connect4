from tkinter import messagebox

from tkinter import *


root = Tk()
root.title('Connect 4')
# buttons y = 120
# root.geometry("740x600")


clicked = True
count = 0


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)

    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)

    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)
    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)
    b28.config(state=DISABLED)

    b29.config(state=DISABLED)
    b30.config(state=DISABLED)
    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)
    b34.config(state=DISABLED)
    b35.config(state=DISABLED)

    b36.config(state=DISABLED)
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)
    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)
    b49.config(state=DISABLED)

def check_line(srow, scol, dirow, dicol):
        plyr = grd[srow][scol]["text"]
        if plyr == " ":
            return False
        
        cnt = 0
        for i in range(4):
            row = srow + i * dirow
            col = scol + i * dicol
            # print(str(row) + " ,"+str(col))
            if 0 <= row < 7 and 0 <= col < 6 and grd[row][col]["text"] == plyr:
                cnt += 1
            else:
                break
        return cnt == 4

def checkifwon():
    global winner,count
    winner = False
    directions = [
        (0, 1),  
        (1, 0), 
        (1, 1),  
        (-1, 1)  
    ]

    for row in range(7):
        for col in range(6):
            for dirow, dicol in directions:
                if check_line(row, col, dirow, dicol):
                    winner = True
                    messagebox.showinfo("Connect 4", "CONGRATULATIONS! " +str(grd[row][col]['text'])+ " wins!!")
                    disable_all_buttons()
                    return
    
    if count == 42 and winner == False:
        messagebox.showinfo("Connect 4", "It's a tie")
        disable_all_buttons()
        return
    return

def whosturn(a):
    if a%2==0:
        return "red"
    return "yellow"

def b_click(bt):
    global clicked, count,b1,b2,b3,b4,b5,b6,b7,row1,row2,row3,row4,row5,row6,row7
    
    if bt["text"] != "F" and bt==b1:
        for b in range(len(row1)):
            if row1[b]["text"] != " " and row1[b-1]["text"] == " ":
                row1[b-1].config(bg=whosturn(count))
                row1[b-1]["text"] = whosturn(count)
            elif b==5 and row1[b]["text"] == " ":
                row1[5].config(bg=whosturn(count))
                row1[5]["text"] = whosturn(count)
        if row1[0]["text"] != " ":
            b1["text"] = "F"
        count += 1
        checkifwon()
    elif bt["text"] != "F" and bt==b2:
        for b in range(len(row2)):
            if row2[b]["text"] != " " and row2[b-1]["text"] == " ":
                row2[b-1].config(bg=whosturn(count))
                row2[b-1]["text"] = whosturn(count)
            elif b==5 and row2[b]["text"] == " ":
                row2[5].config(bg=whosturn(count))
                row2[5]["text"] = whosturn(count)
        if row2[0]["text"] != " ":
            b2["text"] = "F"
        count += 1
        checkifwon()
    elif bt["text"] != "F" and bt==b3:
        for b in range(len(row3)):
            if row3[b]["text"] != " " and row3[b-1]["text"] == " ":
                row3[b-1].config(bg=whosturn(count))
                row3[b-1]["text"] = whosturn(count)
            elif b == 5 and row3[b]["text"] == " ":
                row3[5].config(bg=whosturn(count))
                row3[5]["text"] = whosturn(count)
        if row3[0]["text"] != " ":
            b3["text"] = "F"
        count += 1
        checkifwon()
    elif bt["text"] != "F" and bt==b4:
        for b in range(len(row4)):
            if row4[b]["text"] != " " and row4[b-1]["text"] == " ":
                row4[b-1].config(bg=whosturn(count))
                row4[b-1]["text"] = whosturn(count)
            elif b == 5 and row4[b]["text"] == " ":
                row4[5].config(bg=whosturn(count))
                row4[5]["text"] = whosturn(count)
        if row4[0]["text"] != " ":
            b4["text"] = "F"
        count += 1
        checkifwon()
    elif bt["text"] != "F" and bt==b5:
        for b in range(len(row5)):
            if row5[b]["text"] != " " and row5[b-1]["text"] == " ":
                row5[b-1].config(bg=whosturn(count))
                row5[b-1]["text"] = whosturn(count)
            elif b == 5 and row5[b]["text"] == " ":
                row5[5].config(bg=whosturn(count))
                row5[5]["text"] = whosturn(count)
        if row5[0]["text"] != " ":
            b5["text"] = "F"
        count += 1
        checkifwon()
    elif bt["text"] != "F" and bt==b6:
        for b in range(len(row6)):
            if row6[b]["text"] != " " and row6[b-1]["text"] == " ":
                row6[b-1].config(bg=whosturn(count))
                row6[b-1]["text"] = whosturn(count)
            elif b == 5 and row6[b]["text"] == " ":
                row6[5].config(bg=whosturn(count))
                row6[5]["text"] = whosturn(count)
        if row6[0]["text"] != " ":
            b6["text"] = "F"
        count += 1
        checkifwon()
    elif bt["text"] != "F" and bt==b7:
        for b in range(len(row7)):
            if row7[b]["text"] != " " and row7[b-1]["text"] == " ":
                row7[b-1].config(bg=whosturn(count))
                row7[b-1]["text"] = whosturn(count)
            elif b == 5 and row7[b]["text"] == " ":
                row7[5].config(bg=whosturn(count))
                row7[5]["text"] = whosturn(count)
        if row7[0]["text"] != " ":
            b7["text"] = "F"
        count += 1
        checkifwon()
    # elif b["text"] == " " and b==b2:
    #     b["text"] = "O"
    #     clicked = True
    #     count += 1
    #     checkifwon()
    else:
        messagebox.showerror("Connect 4", "Hey! That column is already full\npick another one")
    print(count)


def reset():
    global count,b1, b2, b3, b4, b5, b6, b7,b8, b9, b10, b11, b12, b13, b14,b15, b16, b17, b18, b19, b20, b21,b22, b23, b24, b25, b26, b27, b28,b29, b30, b31, b32, b33, b34, b35,b36, b37, b38, b39, b40, b41, b42,b43, b44, b45, b46, b47, b48, b49,row1,row2,row3,row4,row5,row6,row7,grd
    global clicked,count
    count = 0

    b1 = Button(root,text = "Click Me", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
    b1.config(bg="gray")
    b2 = Button(root,text = "Click Me", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2))
    b2.config(bg="gray")
    b3 = Button(root,text = "Click Me", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3))
    b3.config(bg="gray")
    b4 = Button(root,text = "Click Me", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4))
    b4.config(bg="gray")
    b5 = Button(root,text = "Click Me", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5))
    b5.config(bg="gray")
    b6 = Button(root,text = "Click Me", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6))
    b6.config(bg="gray")
    b7 = Button(root,text = "Click Me", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7))
    b7.config(bg="gray")

    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b10 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b11 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b12 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b13 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b14 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")

    b15 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b16 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b17 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b18 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b19 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b20 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b21 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")

    b22 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b23 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b24 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b25 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b26 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b27 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b28 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")

    b29 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b30 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b31 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b32 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b33 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b34 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b35 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")

    b36 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b37 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b38 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b39 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b40 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b41 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b42 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")

    b43 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b44 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b45 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b46 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b47 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b48 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
    b49 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")



    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)
    b5.grid(row=0, column=4)
    b6.grid(row=0, column=5)
    b7.grid(row=0, column=6)

    b8.grid(row=1, column=0)
    b9.grid(row=1, column=1)
    b10.grid(row=1, column=2)
    b11.grid(row=1, column=3)
    b12.grid(row=1, column=4)
    b13.grid(row=1, column=5)
    b14.grid(row=1, column=6)

    b15.grid(row=2, column=0)
    b16.grid(row=2, column=1)
    b17.grid(row=2, column=2)
    b18.grid(row=2, column=3)
    b19.grid(row=2, column=4)
    b20.grid(row=2, column=5)
    b21.grid(row=2, column=6)

    b22.grid(row=3, column=0)
    b23.grid(row=3, column=1)
    b24.grid(row=3, column=2)
    b25.grid(row=3, column=3)
    b26.grid(row=3, column=4)
    b27.grid(row=3, column=5)
    b28.grid(row=3, column=6)

    b29.grid(row=4, column=0)
    b30.grid(row=4, column=1)
    b31.grid(row=4, column=2)
    b32.grid(row=4, column=3)
    b33.grid(row=4, column=4)
    b34.grid(row=4, column=5)
    b35.grid(row=4, column=6)

    b36.grid(row=5, column=0)
    b37.grid(row=5, column=1)
    b38.grid(row=5, column=2)
    b39.grid(row=5, column=3)
    b40.grid(row=5, column=4)
    b41.grid(row=5, column=5)
    b42.grid(row=5, column=6)

    b43.grid(row=6, column=0)
    b44.grid(row=6, column=1)
    b45.grid(row=6, column=2)
    b46.grid(row=6, column=3)
    b47.grid(row=6, column=4)
    b48.grid(row=6, column=5)
    b49.grid(row=6, column=6)

    row1 = [b8, b15, b22, b29, b36, b43]
    row2 = [b9, b16, b23, b30, b37, b44]
    row3 = [b10, b17, b24, b31, b38, b45]
    row4 = [b11, b18, b25, b32, b39, b46]
    row5 = [b12, b19, b26, b33, b40, b47]
    row6 = [b13, b20, b27, b34, b41, b48]
    row7 = [b14, b21, b28, b35, b42, b49]
    grd = [ row1,row2,row3,row4,row5,row6,row7]

my_menu = Menu(root)
root.config(menu=my_menu)

# create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()



# def disable_all_buttons():
#     b1.config(state=DISABLED)
#     b2.config(state=DISABLED)
#     b3.config(state=DISABLED)
#     b4.config(state=DISABLED)
#     b5.config(state=DISABLED)
#     b6.config(state=DISABLED)
#     b7.config(state=DISABLED)

# def checkifwon():
#     global winner
#     winner = False
#     if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
#         b1.config(bg="red")
#         b2.config(bg="red")
#         b3.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()
#     elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
#         b4.config(bg="red")
#         b5.config(bg="red")
#         b6.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()
#     elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
#         b7.config(bg="red")
#         b8.config(bg="red")
#         b9.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()

#     elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
#         b1.config(bg="red")
#         b4.config(bg="red")
#         b7.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()
#     elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
#         b2.config(bg="red")
#         b5.config(bg="red")
#         b8.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()
#     elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
#         b3.config(bg="red")
#         b6.config(bg="red")
#         b9.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()
#     elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
#         b1.config(bg="red")
#         b5.config(bg="red")
#         b9.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()
#     elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
#         b3.config(bg="red")
#         b5.config(bg="red")
#         b7.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! X wins!!")
#         disable_all_buttons()

#     # check for Os

#     elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
#         b1.config(bg="red")
#         b2.config(bg="red")
#         b3.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()
#     elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
#         b4.config(bg="red")
#         b5.config(bg="red")
#         b6.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()
#     elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
#         b7.config(bg="red")
#         b8.config(bg="red")
#         b9.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()

#     elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
#         b1.config(bg="red")
#         b4.config(bg="red")
#         b7.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()
#     elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
#         b2.config(bg="red")
#         b5.config(bg="red")
#         b8.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()
#     elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
#         b3.config(bg="red")
#         b6.config(bg="red")
#         b9.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()
#     elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
#         b1.config(bg="red")
#         b5.config(bg="red")
#         b9.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()
#     elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
#         b3.config(bg="red")
#         b5.config(bg="red")
#         b7.config(bg="red")
#         winner = True
#         messagebox.showinfo("Tic Tac Toe", "CONGRATULATIOS! O wins!!")
#         disable_all_buttons()

#     # check if tie
#     if count == 9 and winner == False:
#         messagebox.showinfo("Tic Tac Toe", "It's a tie")
#         disable_all_buttons()

# def b_click(b):
#     pass
#     # global clicked, count
    
#     # if b["text"] == " " and clicked == True:
#     #     b["text"] = "X"
#     #     clicked = False
#     #     count += 1
#     #     checkifwon()
#     # elif b["text"] == " " and clicked == False:
#     #     b["text"] = "O"
#     #     clicked = True
#     #     count += 1
#     #     checkifwon()
#     # else:
#     #     messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\npick another one")

# # def reset():
# #     global b1,b2,b3,b4,b5,b6,b7
# #     global clicked,count
# #     clicked = True
# #     count = 0

# #     b1 = Button(root,text = " ", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
# #     b2 = Button(root,text = " ", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2))
# #     b3 = Button(root,text = " ", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3))

# #     b4 = Button(root,text = " ", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4))
# #     b5 = Button(root,text = " ", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5))
# #     b6 = Button(root,text = " ", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6))

# #     b7 = Button(root,text = " ", font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7))

# #     b1.grid(row=0, column=0)
# #     b2.grid(row=0, column=1)
# #     b3.grid(row=0, column=2)

# #     b4.grid(row=0, column=3)
# #     b5.grid(row=0, column=4)
# #     b6.grid(row=0, column=5)

# #     b7.grid(row=0, column=6)
#     # b8.grid(row=2, column=1)
#     # b9.grid(row=2, column=2)


# my_menu = Menu(root)
# root.config(menu=my_menu)

# # create options menu
# options_menu = Menu(my_menu, tearoff=False)
# my_menu.add_cascade(label="Options",menu=options_menu)
# options_menu.add_command(label="Reset Game", command=reset)

# reset()
# root.mainloop()






# # disable all the buttons



# # checked to see if someone won


# # button clicked gunction

# # State game over
# def reset():
#     global b1,b2,b3,b4,b5,b6,b7,b8,b9
#     global clicked,count
#     clicked = True
#     count = 0
#     # bui;d buttons






# root.mainloop()