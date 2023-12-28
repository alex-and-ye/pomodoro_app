from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
num_ticks = 1
timer = None
timer_on = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global num_ticks, reps, timer_on
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    timer_name.config(text="Timer")
    tick.config(text="")
    num_ticks = 1
    reps = 0
    timer_on = False


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, timer_on
    if not timer_on:
        timer_on = True
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        reps += 1
        if reps % 2 == 1:
            timer_name.config(text="Work", fg=GREEN)
            count_down(work_sec)
        elif reps == 8:
            timer_name.config(text="Break", fg=RED)
            count_down(long_break_sec)
        else:
            timer_name.config(text="Break", fg=PINK)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    global num_ticks, timer, timer_on
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            ticks = "✔" * num_ticks
            tick.config(text=ticks)
            num_ticks += 1
        timer_on = False
        start_timer()
        if reps == 9:
            reset_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_name = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW, highlightthickness=0)
timer_name.grid(column=1, row=0)

start = Button(text="Start", fg=RED, font=(FONT_NAME, 20, "bold"), height=2, width=5, command=start_timer)
start.grid(column=0, row=2)

tick = Label(fg=GREEN, font=(FONT_NAME, 35), bg=YELLOW, highlightthickness=0)
tick.grid(column=1, row=3)

reset = Button(text="Reset", fg=RED, font=(FONT_NAME, 20, "bold"), height=2, width=5, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
