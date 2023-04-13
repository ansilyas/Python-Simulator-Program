#%%
from random import choice
questions=["What is your name?","How old are you?","What is my name?"]

question=choice(questions)
answer=input(question).strip().lower()

while answer!="just because":
    answer=input("why?:").strip().lower()
    print("oh....okay")
# %%
