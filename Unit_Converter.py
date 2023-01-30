import tkinter as tk
from tkinter import messagebox

global recoveryCounter
recoveryCounter = 1

window = tk.Tk()
window.geometry("1000x1000")
window.title("Unit Converter")
frame = tk.Frame()
entry = tk.Entry()

windowTitle = tk.Label(text="Peters Unit Converted", background="black", foreground="orange")
windowTitle.pack(pady=20)

def enter():
    pass

def instruction():
    instructionWindow = tk.Tk()

    instructionWindow.configure(background="black")
    instructionWindow.title("Features and Instructions")
    features = tk.Label(instructionWindow, text= "---------------Features---------------\n\n\n"
                                                + "1. Convert unit with unit converted and save to display window.\n\n"
                                                + "2. Verify conversion formula\n\n"
                                                + "3. Clear conversion history\n\n"
                                                + "4. Recover cleared history\n\n\n\n\n\n"
                                                + "---------------Instructions---------------", background="black", foreground="orange")
    instruction = tk.Label(instructionWindow, text="Converting Unit\n\n        Step 1. Select input unit.\n        Step 2. Select output unit.\n        Step 3. Enter value into input entry field.\n\n        (Optional Step. Click \"Show Equation\" button to verify conversion.)\n\n        Step 4. Click \"Convert Value\" button or press Enter. \n\n\n\n"
                                                   + "View Conversion Formula\n\n        Step 1. Click \"Show Equation\" button.\n\n\n\n"
                                                   + "Clear History Window\n\n        Step 1. Click \"Clear History\" button.\n        Step 2. Confirm to proceed with clearing history.\n\n\n\n"
                                                   + "Recover Cleared History\n\n        Step 1. Click \"Undo Clear\" button", background="black", foreground="orange",justify=tk.LEFT)

    features.pack( pady=(20,0), padx=20, fill="both")
    instruction.pack( pady=20, padx=20, fill="both")
    instructionWindow.attributes('-topmost', True)
    instructionWindow.mainloop()


def showEquation():

    inputUnit = inputUnitVar.get()
    outputUnit = outputUnitVar.get()

    equation = "Select Units to display equation"
    title = "Conversion Equation"

    if inputUnit == "inches" and outputUnit == "feet":
        equation = "output = input / 12 "
        title = "Inches to Feet"
    elif inputUnit == "feet" and outputUnit == "inches":
        equation = "output = input * 12 "
        title = "Feet to Inches"


    messagebox.showinfo(title,equation)

def createWindow():
    newWindow = tk.Tk()
    newWindow.geometry("300x100")
    newWindow.configure(background="black")
    formula = tk.Label(newWindow, text = "Select Units to display formula", background="black", foreground="orange")

    inputUnit = inputUnitVar.get()
    outputUnit = outputUnitVar.get()

    equation = "Select Units to display equation"
    title = "Conversion Equation"

    if inputUnit == "inches" and outputUnit == "feet":
        formula.config( text = "output = input / 12 ")
        newWindow.title("Inches to Feet")


    elif inputUnit == "feet" and outputUnit == "inches":
        formula.config(text="output = input * 12 ")
        newWindow.title("Feet to Inches")

    formula.pack(expand=True)
    newWindow.mainloop()

def appendValues():
    historyDisplay.configure(state="normal")
    historyDisplay.insert(tk.END,"example output unit = example input unit" + "\n")
    historyDisplay.configure(state="disabled")
    historyDisplay.see("end")


def clearHistory():

    global history

    confirm = tk.messagebox.askokcancel(title="Clear History", message="Proceed with clearing history")

    if confirm:
        historyDisplay.configure(state="normal")
        historyDisplay.delete("end-1c linestart", "end")
        historyDisplay.tag_add("history", "1.0", "end")
        historyDisplay.tag_config("history", background = "black")
        history = historyDisplay.get("1.0",tk.END)
        historyDisplay.configure(state="disabled")

        historyDisplay.configure(state="normal")
        historyDisplay.delete("1.0", tk.END)
        historyDisplay.configure(state="disabled")


def undoClear():
    global history
    global recoveryCounter

    if history == None:
        return

    historyDisplay.delete("end-1c linestart", "end")
    current = historyDisplay.get("1.0",tk.END)
    historyDisplay.configure(state="normal")
    historyDisplay.delete("1.0", "end")
    historyDisplay.insert(tk.INSERT, history)
    historyDisplay.insert(tk.INSERT, "---End of Recovery "+ str(recoveryCounter) + "---" + "\n\n")
    historyDisplay.insert("end", current)
    historyDisplay.delete("end-1c linestart", "end")
    recoveryCounter = recoveryCounter + 1
    history = None
    historyDisplay.see("end")



#Set Grid
inputOutputFrame = tk.Frame(window)
inputOutputFrame.columnconfigure(0, weight=1)
inputOutputFrame.columnconfigure(1, weight=1)
inputOutputFrame.columnconfigure(2, weight=1)
inputOutputFrame.columnconfigure(3, weight=1)
inputOutputFrame.columnconfigure(4, weight=1)
inputOutputFrame.columnconfigure(5, weight=1)
inputOutputFrame.configure(background="black")

#Set label
inputLabel = tk.Label(inputOutputFrame, text="Input:", background="black", foreground="orange")
outputLabel = tk.Label(inputOutputFrame, text="Output:", background="black", foreground="orange")

#Set dropdown menu
options = ["meter", 'feet', "inches"]

inputUnitVar = tk.StringVar(inputOutputFrame,value = "Unit")
outputUnitVar = tk.StringVar(inputOutputFrame,value = "Unit")

inputUnit = tk.OptionMenu(inputOutputFrame, inputUnitVar, *options )
inputUnit.configure(background="black", foreground="orange", highlightcolor="purple", highlightbackground="black",activebackground="orange", activeforeground="black",)
inputUnit["menu"].config(background="black", foreground="orange", activebackground="Orange", activeforeground="black")
outputUnit = tk.OptionMenu(inputOutputFrame, outputUnitVar, *options)
outputUnit.configure(background="black", foreground="orange", highlightcolor="blue", highlightbackground="black", activebackground="orange", activeforeground="black")
outputUnit["menu"].config(background="black", foreground="orange", activebackground="Orange", activeforeground="black")

#Set entry

input = tk.Entry(inputOutputFrame)
input.configure(background="orange", foreground="black")
output =tk.Entry(inputOutputFrame)
output.configure(background="white", foreground="orange", highlightcolor="blue", highlightbackground="Yellow",selectbackground= "blue", selectforeground="yellow", disabledbackground="orange", disabledforeground="black", state="disabled")



#Add to grid
inputLabel.grid(row=0,column=0, sticky=tk.W+tk.E)
input.grid(row=0,column=1,sticky= tk.W+tk.E)
inputUnit.grid(row=0,column=2, sticky= tk.W+tk.E)


outputLabel.grid(row=0,column=3, sticky= tk.W+tk.E)
output.grid(row=0,column=4,sticky= tk.W+tk.E)
outputUnit.grid(row=0,column=5, sticky= tk.W+tk.E)

inputOutputFrame.pack(fill="x")


# Set buttons for converting and show
buttonFrame1 = tk.Frame(window)
buttonFrame1.columnconfigure(0, weight=1)
buttonFrame1.columnconfigure(1, weight=1)
buttonFrame1.configure(background="black")

equationButton = tk.Button(buttonFrame1,
    text="Show Equation",
    activebackground="black",
    activeforeground="orange",
    command=createWindow

)

# Show equaiton button and convert button
equationButton.configure(background="black", foreground="orange", pady=20)
equationButton.bind("<Enter>", lambda e: equationButton.config(fg='black', bg='orange'))
equationButton.bind("<Leave>", lambda e: equationButton.config(fg='orange', bg='black'))


convertButton = tk.Button(buttonFrame1, text = "Convert Value", activebackground="black", activeforeground="orange", command=appendValues)
convertButton.configure(background="black", foreground="orange", pady=20)
convertButton.bind("<Enter>", lambda e: convertButton.config(fg='black', bg='orange'))
convertButton.bind("<Leave>", lambda e: convertButton.config(fg='orange', bg='black'))
window.bind("<Return>", lambda event: appendValues())

#grid for equation and convert button
equationButton.grid(row=0,column = 0,sticky= tk.W+tk.E)
convertButton.grid(row=0,column = 1,sticky= tk.W+tk.E)

buttonFrame1.pack(fill="x")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#History Title
historyTitle = tk.Label(text="------------------------------------------------------------------------------------------------------------------------   Conversion History   ------------------------------------------------------------------------------------------------------------------------")
historyTitle.configure(background="black", foreground="orange")
historyTitle.pack(pady=(40,10))

#History display box
historyDisplay = tk.Text()
historyDisplay.configure(background="black",foreground="orange", state="disabled")
historyDisplay.pack(fill="both", expand=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Button Grid

buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0, weight = 1)
buttonFrame.columnconfigure(1, weight = 1)
buttonFrame.configure(background="black")


#Buttons
clearHistoryButton = tk.Button(buttonFrame, text="Clear History", command=clearHistory)
clearHistoryButton.bind("<Enter>", lambda e: clearHistoryButton.config(fg='black', bg='orange'))        #Change color when cursor hovered over
clearHistoryButton.bind("<Leave>", lambda e: clearHistoryButton.config(fg='orange', bg='black'))        #Change color when cursor leaves.
clearHistoryButton.configure(background="black",foreground="orange",activebackground="black", activeforeground="orange", pady=20)

undoClearButton = tk.Button(buttonFrame, text = "Undo Clear", command= undoClear)
undoClearButton.bind("<Enter>", lambda e: undoClearButton.config(fg='black', bg='orange'))        #Change color when cursor hovered over
undoClearButton.bind("<Leave>", lambda e: undoClearButton.config(fg='orange', bg='black'))        #Change color when cursor leaves.
undoClearButton.configure(background="black",foreground="orange", activebackground="black", activeforeground="orange", pady=20)



#Add buttons to grid
clearHistoryButton.grid(row=0,column=0, sticky=tk.W+tk.E)
undoClearButton.grid(row=0, column = 1, sticky=tk.W + tk.E)

buttonFrame.pack(fill="x", pady=30)

entry = tk.Entry
window.configure(background="black",
                 borderwidth=10,
                 height=40,
                 width=100
)

instruction()

window.mainloop()

