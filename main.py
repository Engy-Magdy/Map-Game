import turtle,pandas
screen=turtle.Screen()
screen.bgpic("Map.gif")
screen.setup(753,432)
screen.title("Map Game")

data=pandas.read_csv("coordinates.csv")
countries=data.country.to_list()
guessed=[]
while len(guessed)<22:
      answer=screen.textinput(title=f"{len(guessed)}/22 guessed ",prompt="Type a country and hit Enter!").title()
      if answer in guessed:
                continue
      if answer in countries: 
        guessed.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_x=data[data.country==answer]["x"].item()
        country_y=data[data.country==answer]["y"].item()
        t.goto(country_x,country_y)
        t.fillcolor("red")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.write(answer,font=("courie",15))
      elif answer=="Exit":   
        screen.bye()
     
      with open("Missing Countries.csv","w") as file:
       for country in countries:
        if country not in guessed:
          file.write(f'{country}\n')

turtle.mainloop()
