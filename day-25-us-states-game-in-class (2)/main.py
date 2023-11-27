import turtle
import pandas

FONT = ('Arial', 10, 'normal')
guessed_states = []





screen = turtle.Screen()
screen.title("U.S Sates Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
t = []


data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()


while len(guessed_states) < 50:
    answer_state = screen.textinput(f'Guess the state {len(guessed_states)}/50', 'enter a state name:')
    if answer_state == "Exit":
        missing_states = [s for s in all_states if s not in guessed_states]
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.color('black')
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item(), True, 'center', FONT)





