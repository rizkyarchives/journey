from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
texts = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    global reps
    global texts
    window.after_cancel(timer)
    canvas.itemconfig(text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    texts = ""
    check_label.config(text=texts)
    start_button.config(state= NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state= DISABLED)
    global reps
    global texts
    reps += 1
    window.lift()
    window.attributes("-topmost", True)
    window.attributes("-topmost", False)
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(int(LONG_BREAK_MIN * 60))
    elif reps % 2 == 1 and reps < 8:
        timer_label.config(text="Work", fg=GREEN)
        count_down(int(WORK_MIN * 60))
    elif reps % 2 == 0 and reps < 8:
        timer_label.config(text="Break", fg=PINK)
        count_down(int(SHORT_BREAK_MIN * 60))
    elif reps == 9:
        reset()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(sec):
    global timer
    global reps
    global texts
    canvas.itemconfig(text, text=f"{int(sec/60):02d}:{sec%60:02d}")
    if sec != 0:
        timer = window.after(1000, count_down, sec - 1)
    else:
        if reps % 2 == 1 and reps < 8:
            texts = texts + "✔"
        check_label.config(text=texts)
        timer = window.after(1000, start_timer)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
image_file = PhotoImage(file="tomato.gif")
canvas.create_image(100, 112, image=image_file)
text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=2, column=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
