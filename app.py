import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("India States Coordinate Collector")
screen.bgpic("new_india_state.gif")

states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
    "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
    "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
    "Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan",
    "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
    "Uttarakhand","West Bengal"
]

data = []

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

def get_coordinates(x, y):
    state = screen.textinput(
        title="State Name",
        prompt="Enter state name:"
    )
    if state:
        state = state.title()
        writer.goto(x, y)
        writer.write(state, align="center", font=("Arial", 8, "normal"))
        data.append({"state": state, "x": int(x), "y": int(y)})
        print(state, x, y)

screen.onscreenclick(get_coordinates)
screen.mainloop()

# Save after closing window
df = pd.DataFrame(data)
df.to_csv("new_india_state.csv", index=False)
print("CSV saved as new_india_state.csv")
