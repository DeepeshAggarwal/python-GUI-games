try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#defining global variables

score = 0
turn = 0
minutes = 0
second = 0
tens_second = 0
tenth_of_second = 0 

# helping functions

def format() : 
    global minutes , second , tens_second ,tenth_of_second
    
    if tenth_of_second == 10 :
        tenth_of_second = 0
        second += 1
    
    if second == 10 :
        second = 0
        tens_second += 1

    if tens_second == 6 :
        tens_second =0
        minutes += 1

def draw() : 
    return str(minutes) + "." + str(tens_second) + str(second) + ":" + str(tenth_of_second)

def point() :

    global turn , score

    if tenth_of_second == 0 :
        score += 1
        
    turn += 1

    return str(score) + "/" + str(turn)
#defining event handlers
def tick() :
    global tenth_of_second
    tenth_of_second += 1
    format()

def start() :
    timer.start()

def pause() : 
    timer.stop()
    point()

def reset() : 
    global minutes , second , tens_second , tenth_of_second
    minutes = 0
    second = 0
    tens_second = 0
    tenth_of_second = 0 

def output(canvas) :
    canvas.draw_text(draw() , [70,90] , 20 , "white")
    canvas.draw_text(point() , [180,10] , 10 , "red")

#creating the frames
frame = simplegui.create_frame("stopwatch" , 200 , 200)

# registering the event handlers
frame.add_button("Start" , start , 100)
frame.add_button("Stop" , pause , 100)
frame.add_button("Reset" ,reset , 100)
timer = simplegui.create_timer(1 , tick)
frame.set_draw_handler(output)

#starting the frames and timers
frame.start()
