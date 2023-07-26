from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
#Since I'm using Hiragana and kanji, encoding needs to be specified to utf8
try:
    with open("D://Documents/Kuliah/100days/day-31/data/words_to_learn_p1.csv", "r", encoding="utf8") as word_file: 
        word_df= pandas.read_csv(word_file)
        words_dict = word_df.to_dict(orient='records')
except FileNotFoundError:
    with open("D://Documents/Kuliah/100days/day-31/data/japan_words_p1.csv", "r", encoding="utf8") as word_file: 
        word_df= pandas.read_csv(word_file)
        words_dict = word_df.to_dict(orient='records')

memorized_word_index = []
index_chosen = 0

def create_card(title, card_image, *args):
    text_y_pos = 263
    card.create_image(400, 263, image=card_image)
    card.create_text(400, 140, text=title, font=("Ariel", 40, "italic"))
    for texts in args:
        card.create_text(400, text_y_pos, text=texts, font=("Ariel", 60, "bold"))
        text_y_pos += 65
# This has too many global variable declaration, maybe it could be done better? I did this because function used for button
# cannot take any argument. Also, I cannot return any value from this function. I could come back to this in the future and maybe I would have
# a better solution by then. Currently, I just want it to work :D. (10 mins later) Okay Nvm I figured it out. I can minimize the global 
# variable declaration by using lambda in the button function, Neat!
def new_word(memorized_index, dict_of_words, front_image, back_image):
    global index_chosen
    check_button.config(state=DISABLED)
    x_button.config(state=DISABLED)
    try:
        card.delete("all")
    except UnboundLocalError:
        pass
    creating_card = True
    while creating_card:
        index_chosen = random.randint(0, len(dict_of_words)-1)
        if index_chosen not in memorized_index:
            create_card("Japanese", front_image, dict_of_words[index_chosen]['Japan'], dict_of_words[index_chosen]['Romaji'])
            creating_card = False
    window.after(3000, create_card, "English", back_image, dict_of_words[index_chosen]['Definitions'])
    check_button.config(state=NORMAL)
    x_button.config(state=NORMAL)

def new_word_memorized(memorized_index, dict_of_words, front_image, back_image):
    global memorized_word_index
    global index_chosen
    memorized_word_index.append(index_chosen)
    new_word(memorized_index, dict_of_words, front_image, back_image)

def create_csv(dict, memorized_index):
    for index in memorized_index:
        dict.remove(dict[index])
    df = pandas.DataFrame.from_dict(dict)
    with open("D://Documents/Kuliah/100days/day-31/data/words_to_learn_p1.csv", "w", encoding="utf8", newline='') as csvfile:
        df.to_csv(csvfile, index=False)
    window.quit()


window = Tk()
window.title("Japanese Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

check_image = PhotoImage(file="D://Documents/Kuliah/100days/day-31/images/right.png")
check_button = Button(image=check_image, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, bd=0, command=lambda: new_word_memorized(memorized_word_index, words_dict, frontcard_image, backcard_image))
check_button.grid(row = 1, column = 1)

x_image = PhotoImage(file="D://Documents/Kuliah/100days/day-31/images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, bd=0, command=lambda: new_word(memorized_word_index, words_dict, frontcard_image, backcard_image))
x_button.grid(row = 1, column = 0)

card = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
frontcard_image = PhotoImage(file="D://Documents/Kuliah/100days/day-31/images/card_front.png")
backcard_image = PhotoImage(file="D://Documents/Kuliah/100days/day-31/images/card_back.png")
card.create_image(400, 263, image=frontcard_image)
new_word(memorized_word_index, words_dict, frontcard_image, backcard_image)
card.grid(row=0, column=0, columnspan=2)

window.protocol("WM_DELETE_WINDOW", lambda: create_csv(words_dict, memorized_word_index))
window.mainloop()