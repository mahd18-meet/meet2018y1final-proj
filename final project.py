import turtle
greeting=turtle.clone()
welcome=turtle.clone()

turtle.hideturtle()
greeting.hideturtle()
welcome.hideturtle()

greeting.penup()
welcome.penup()

greeting.goto(-250,0)
welcome.goto(-460,-200)

for letter in "Hello guest!":
    greeting.write(letter, move=True, font=("Times New Roman",60,"normal"))
    greeting.forward(10)
    
for letter2 in "Welcome to TROJAN clothing!":
    welcome.write(letter2,move=True,font=("Times New Roman",40,"normal"))
    welcome.forward(10)

turtle.ontimer(greeting.clear,10000)
turtle.ontimer(welcome.clear,10000)

screen=turtle.Screen()

turtle.register_shape("earth.gif")
turtle.register_shape("animals.gif")
turtle.register_shape("wave.gif")
turtle.register_shape("tree.gif")

test=True
test1=True
test2=True
test3=True

clothes_type = turtle.textinput('Shirt type',"Would you prefer hoodies or shirts?")

while test:
    clothes_type = clothes_type.lower()
    if clothes_type == 'shirts' or clothes_type == 'shirt':
        test = False
    elif clothes_type == 'hoodies' or clothes_type=='hoodie':
        test = False
    elif clothes_type == 'abdallah':
        clothes_type.lower()
        screen.bgpic('supremehoodie.gif')
        test1 = False
        test2=False
        test3=False
        test = False
    elif clothes_type=='ahmad':
        clothes_type.lower()
        screen.bgpic('ahmad.gif')
        test1 = False
        test2=False
        test3=False
        test = False
    else:
        clothes_type = turtle.textinput('Whoops! We don\'t have that...',"Would you prefer hoodies or shirts?")

while test1:
    color = turtle.textinput('Color?',"What color would you like: grey, black, blue or red?")
    
    def make_clothes():
        global screen
        clothes_type.lower()
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
              
    color = color.lower()
    if color == 'red':
        test1=False
        make_clothes()
    elif color == 'blue':
        make_clothes()
        test1=False
    elif color =='grey':
        make_clothes()
        test1=False
    elif color=='black':
        make_clothes()
        test1=False
    else:
       nocolor=turtle.textinput('Error'," **PRESS OK**")

while test3:
    sorl=turtle.textinput('Logo or slogan?',"Would you like to have a logo on your "+clothes_type+" or a slogan?")
    sorl=sorl.lower()
    if sorl== 'slogan':
        def make_slogan():
            slogan=turtle.clone()
            slogan.pencolor('white')
            slogan.penup()
            slogan_text=turtle.textinput('Slogan?','What would you like to be written on your '+clothes_type+'? (Less than 8 characters)')
            slogan.goto(-100,50)
            if len(slogan_text)>8:
                wrongslogan=turtle.textinput("**PRESS OK**","Your input is longer than 8 characters")
                make_slogan()
            elif len(slogan_text)==1:
                slogan.goto(-20,40)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
            elif len(slogan_text)==2:
                slogan.goto(-20,40)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
            elif len(slogan_text)==3:
                slogan.goto(-30,50)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
            elif len(slogan_text)==4:
                slogan.goto(-50,50)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
            elif len(slogan_text)==5:
                slogan.goto(-50,50)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
            elif len(slogan_text)==6:
                slogan.goto(-60,50)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
            elif len(slogan_text)==7:
                slogan.goto(-70,50)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
            elif len(slogan_text)==8:
                slogan.goto(-80,50)
                slogan.write(slogan_text,font=("Purisa",30,'normal'))
        make_slogan()
        test3=False
    elif sorl=="logo":
        def put_logo():
            global logo
            global test2
            while test2:
                logo = turtle.textinput('Logo?','What logo would you like on your '+clothes_type+' Earth, Tree, Animals, Wave.')
                logo = logo.lower()
                if logo=="earth":
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
                    logo = turtle.textinput('Whoops! We don\'t have that ...','What logo would you like on your '+clothes_type+' Earth, Tree, Animals, Wave.')
        put_logo()
        test3=False
    else:
        sorl=turtle.textinput("whoops! we don\'t have this kind of design","Would you like to have a logo on your "+clothes_type+" or a slogan?")
     
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
def price():
    price_turtle=turtle.clone()
    price_turtle.penup()
    price_turtle.pencolor('green')
    
    if clothes_type=='hoodies' or clothes_type=='hoodie':
        price_turtle.goto(-75,-400)
        price_turtle.write(("$30"),font=("Arial",70,'normal'))
    elif clothes_type=='shirt' or clothes_type=='shirts':
        price_turtle.goto(-75,-400)
        price_turtle.write(("$20"),font=("Arial",70,'normal'))
    elif clothes_type=='abdallah' or clothes_type=='ABDALLAH':
        price_turtle.goto(-100,-400)
        price_turtle.write(('$500'),font=("Arial",70,'normal'))
    elif clothes_type=='ahmad' or clothes_type=='AHMAD':
        price_turtle.goto(-150,-400)
        price_turtle.write(('$1000'),font=("Arial",70,'normal'))
    
make_clothes()
price()




    



















