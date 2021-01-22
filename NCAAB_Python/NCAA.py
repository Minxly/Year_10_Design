from tkinter import *
from sportsreference.ncaab.schedule import Schedule
from tkinter import messagebox


def remove():
    for widget in rgFrame.winfo_children():
        widget.destroy()
        gLabel.config(text="")
        wLabel.config(text="")


def earnings_check():

    remove()

    wLabel.config(text="")
    gLabel.config(text="")
    listy = []
    eNe = entry_1.get()
    eN = eNe.replace(" ", "-")
    eD = entry_2.get()

    if len(eD + eN) == 0:
        messagebox.showerror("Error", "Please Enter Details", icon="warning")
        return

    if len(eD and eN) >= 1:
        gLabel.config(text="")

        pName = eN

        games = Schedule(pName)

        for game in games:
            gDate = game.date

            if gDate == eD:
                gLabel.config(text=pName + " " + game.result + " vs " + game.opponent_name)
                contact.config(bg="white")
                return

    if len(eN) == 0:
        messagebox.showerror("Error", "Please Enter A Team", icon="warning")
        return

    if len(eD) == 0:

        gLabel.config(text="")
        wLabel.config(text="Note That Games That Haven't \n Happened Will Be Listed As A Loss")

        games = Schedule(eN)

        pName = eN.replace("-", " ")

        for game in games:
            listy.append(pName + " " + game.result + " vs " + game.opponent_name + " " + game.date)
            contact.config(bg="white")

        for item in listy:
            newLabel = Label(rgFrame, text=item)
            newLabel.config(font=("Arial", 9))
            newLabel.pack()


root = Tk()

root.title("NCAAB SCORES")

root.geometry("400x850")

menuFrame_1 = Frame(root, bg="#060273", height="30")
menuFrame_1.pack(fill=X)

spaceFrame_1 = Frame(root, height="15")
spaceFrame_1.pack(fill=X)

tFrame_1 = Frame(root)
title_1 = Label(tFrame_1, text="Team or Both To View Games")
title_1.config(font=("Arial", 18))
title_1.pack()
sTitle = Label(tFrame_1, text="Make Sure Team Entered Is Valid")
sTitle.config(font=("Arial", 11))
sTitle.pack()
tFrame_1.pack()

spaceFrame_2 = Frame(root, height="5")
spaceFrame_2.pack(fill=X)

mainFrame_1 = Frame(root, borderwidth="2", relief=SUNKEN, width="300", height="100")
mainFrame_1.pack(fill=None, expand=False, ipady="4")

lFrame_1 = Frame(mainFrame_1)
label_1 = Label(lFrame_1, text="Team Name", bg="white", fg="black", height=2)
label_2 = Label(lFrame_1, text="Date", bg="white", fg="black", height=2)
label_1.grid(row=1, sticky=W)
label_2.grid(row=3, sticky=W)
lFrame_1.pack(side=LEFT)

eFrame_1 = Frame(mainFrame_1)
entry_1 = Entry(eFrame_1)
entry_2 = Entry(eFrame_1)
entry_1.grid(row=5, ipady=5)
entry_2.grid(row=6, ipady=5)
eFrame_1.pack(side=RIGHT)

spaceFrame_3 = Frame(root)
sTitle_2 = Label(spaceFrame_3, text="Enter The Date In The Correct Form\n"
                                                "(Ex. Wed, Dec 16, 2020)")
sTitle_2.config(font=("Arial", 11))
sTitle_2.pack()
spaceFrame_3.pack(fill=X, ipady="2")

bFrame_1 = Frame(root)
enter_1 = Button(bFrame_1, text="Enter", command=earnings_check, width=8, height=1)
enter_1.config(font=("Arial", 16))
enter_1.grid(row=0, columnspan=4)
bFrame_1.pack()

spaceFrame_4 = Frame(root, height="10")
spaceFrame_4.pack(fill=X)

menuFrame_2 = Frame(root, bg="#060273", height="30")
menuFrame_2.pack(fill=X)

rFrame = Frame(root, height="560")
rFrame.pack()

rtFrame = Frame(rFrame, height="20")
title_2 = Label(rtFrame, text="Results")
title_2.config(font=("Arial", 18))
title_2.pack()
rtFrame.pack(fill=X)

rstFrame = Frame(rFrame, height="35")
wLabel = Label(rstFrame, text="")
gLabel = Label(rstFrame, text="")
wLabel.pack()
gLabel.pack()
rstFrame.pack(fill=X)


rgFrame = Frame(rFrame, height="470", width="400")
rgFrame.pack(fill=None, expand=False)
rgFrame.pack_propagate(False)

bMenuFrame_1 = Frame(root, height="30")
contact = Label(bMenuFrame_1, text="For Troubleshooting Contact matt.lipton@ucc.on.ca", bg="#060273", fg="white")
contact.pack(fill=X)
bMenuFrame_1.pack(fill=X, side=BOTTOM)

bFrame_2 = Frame(root)
bFrame_2.pack(side=BOTTOM)


root.mainloop()
