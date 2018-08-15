import turtle
greeting=turtle.clone()

turtle.hideturtle()
greeting.hideturtle()
greeting.penup()
greeting.goto(-200,0)
for letter in "Hello guest!":
    greeting.write(letter, move=True, align="left", font=("Times New Roman",60,"normal"))
    greeting.forward(10)

turtle.ontimer(greeting.clear,50)

background_list= []
logo_list=[]
turtle.register_shape("earth.gif")
turtle.register_shape("animals.gif")
turtle.register_shape("wave.gif")
turtle.register_shape("tree.gif")

clothes_type =input("Would you prefer hoodies or shirts?")


test=True
while test:
    clothes_type = clothes_type.lower()
    if clothes_type == 'shirts' or clothes_type == 'shirt':
        test = False
    elif clothes_type == 'hoodies' or clothes_type=='hoodie':
        test = False
    else:
        print('Whoops! We don\'t have that type of clothing, try again!')
        clothes_type =input("Would you prefer hoodies or shirts?")


test1 = True
while test1:
    color = input("What color would you like: grey, black, blue or red?")
    color = color.lower()
    if color == 'red':
        test1=False
    elif color == 'blue':
        test1=False
    elif color =='grey':
        test1=False
    elif color=='black':
       test1=False
    else:
       print("whoops! We don\'t have "+color+", try again!")
sorl=input("Would you like to have a logo on your "+clothes_type+" or a slogan?")
test3=True
while test3:
    if sorl== 'slogan':
        def make_slogan():
            slogan=turtle.clone()
            slogan.penup()
            slogan_text=input('What would you like to be written on your '+clothes_type+'?')
            slogan.goto(-100,50)
            slogan.write(slogan_text,font=("Roboto",60,'normal'))
        make_slogan()
        test3= False
    elif sorl=="logo":
        def put_logo():
            global logo
            test2 = True
            while test2:
                logo = input('What logo would you like on your '+clothes_type+' Earth, Tree, Animals, Wave.')
                logo = logo.lower()
                if logo=="earth" :
                    earth=turtle.clone()
                    earth.shape("earth.gif")
                    earth.penup()
                    earth.goto(0,50)
                    earth.stamp()
                    test2 = False
                elif logo=="animals" or logo=='animal':
                    animals=turtle.clone()
                    animals.shape("animals.gif")
                    animals.penup()
                    animals.goto(0,50)
                    animals.stamp()
                    test2 = False
                elif logo=="wave" or logo=='waves':
                    wave=turtle.clone()
                    wave.shape("wave.gif")
                    wave.penup()
                    wave.goto(0,50)
                    wave.stamp()
                    test2 = False
                elif logo=="tree":
                    tree=turtle.clone()
                    tree.shape("tree.gif")
                    tree.penup()
                    tree.goto(0,50)
                    tree.stamp()
                    test2 = False
                else:
                    print('Whoops! We don\'t have that logo, try again!')
                    logo = input('What logo would you like on your '+clothes_type+' Earth, Tree, Animals, Wave.')


        put_logo()
        test3=False
    else:
        print("whoops! we don\'t have this kind of design")
        sorl=input("Would you like to have a logo on your "+clothes_type+" or a slogan?")
     
def make_clothes():
    clothes_type.lower()
    screen=turtle.Screen()
    if clothes_type == 'hoodie' or clothes_type=='hoodies':
        if color=='red':
            screen.bgpic('redhoodie.gif')         
        elif color=='blue':
            screen.bgpic('bluehoodie.gif')
        elif color=='grey':
            screen.bgpic('greyhoodie.gif')
        elif color=='black':
            screen.bgpic('blackhoodie.gif')
    if clothes_type=='shirt' or clothes_type=='shirts':
        if color=='red':
            screen.bgpic('red.gif')
        elif color=='grey':
            screen.bgpic('grey.gif')
        elif color=='blue':
            screen.bgpic('blue.gif')
        elif color=='black':
            screen.bgpic('black.gif')
make_clothes()






    



















