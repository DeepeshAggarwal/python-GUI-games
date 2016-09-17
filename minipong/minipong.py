try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


WIDTH = 800
HEIGHT = 400
BAR_LEFT_POSITION = [5 , HEIGHT//2-40]
BAR_RIGHT_POSITION = [WIDTH-5, HEIGHT//2-40]
PLAYER1 = 0
PLAYER2 = 0
BALL_POSITION = [WIDTH//2 , HEIGHT//2]
VELOCITY = [1.5,-1]

def re_start():
    global PLAYER1, PLAYER2
    PLAYER1 = 0
    PLAYER2 = 0
    new_game()


# defining the helper functions
def new_game():
    global BAR_LEFT_POSITION , BAR_RIGHT_POSITION , BALL_POSITION ,VELOCITY, PLAYER1, PLAYER2
    BAR_LEFT_POSITION = [5 , HEIGHT//2-40]
    BAR_RIGHT_POSITION = [WIDTH-5, HEIGHT//2-40]
    BALL_POSITION = [WIDTH//2 , HEIGHT//2]
    VELOCITY = [1.5,-0.7]
    
#event handlers

def key_down(key):
    
    if key == simplegui.KEY_MAP["W"]:
        if BAR_LEFT_POSITION[1] >= 20:
            BAR_LEFT_POSITION[1] -= 20
            
        else:
            BAR_LEFT_POSITION[1] = 0
            
    elif key == simplegui.KEY_MAP["S"]:
        if BAR_LEFT_POSITION[1] <= HEIGHT-105 :
            BAR_LEFT_POSITION[1] += 20
            
        else:
            BAR_LEFT_POSITION[1] = HEIGHT-80
    
    elif key == simplegui.KEY_MAP["up"]:
        if BAR_RIGHT_POSITION[1] >= 20:
            BAR_RIGHT_POSITION[1] -= 20
            
        else:
            BAR_RIGHT_POSITION[1] = 0
            
    elif key == simplegui.KEY_MAP["down"]:
        if BAR_RIGHT_POSITION[1] <= HEIGHT-105:
            BAR_RIGHT_POSITION[1] += 20
            
        else:
            BAR_RIGHT_POSITION[1] = HEIGHT-80

def tick():
    VELOCITY[0] *= 1.5
    VELOCITY[1] *= 1.5
        
# defining drawing event functions

def output(canvas):
    
    global PLAYER1 , PLAYER2
    # drawing the events
    canvas.draw_line([10,0] , [10,400] , 1 , "white")
    canvas.draw_line([790,0] , [790,400] , 1 , "white")
    canvas.draw_line([WIDTH//2,0] , [WIDTH//2,400] , 1 , "white")
    canvas.draw_line(BAR_LEFT_POSITION , [BAR_LEFT_POSITION[0], BAR_LEFT_POSITION[1]+80] , 10 , "white")
    canvas.draw_line(BAR_RIGHT_POSITION , [BAR_RIGHT_POSITION[0], BAR_RIGHT_POSITION[1]+80] , 10 , "white")
    canvas.draw_circle(BALL_POSITION , 20 , 2 , "red" , "white")
    canvas.draw_text(str(PLAYER1) ,[200,50],30,"red" )
    canvas.draw_text(str(PLAYER2) ,[WIDTH/2+200,50],30,"red" )
    
    
    # updating the position of the ball
    
    BALL_POSITION[0] += VELOCITY[0]
    BALL_POSITION[1] += VELOCITY[1]
    
    # colliding with the walls
    
    if BALL_POSITION[1] <= 20 or BALL_POSITION[1] >= 380 :
        VELOCITY[1] = -VELOCITY[1]
    
    elif (BALL_POSITION[0] <= 30 and (BALL_POSITION[1] > BAR_LEFT_POSITION[1] and BALL_POSITION[1] < BAR_LEFT_POSITION[1]+80 )):
        VELOCITY[0] = -VELOCITY[0]
    
    elif (BALL_POSITION[0] >= 770 and (BALL_POSITION[1] >= BAR_RIGHT_POSITION[1] and BALL_POSITION[1] <= BAR_RIGHT_POSITION[1]+80 )):
        
        VELOCITY[0] = -VELOCITY[0]
        
    elif BALL_POSITION[0] <= 30 and (not(BALL_POSITION[1] > BAR_LEFT_POSITION[1] and BALL_POSITION[1] < BAR_LEFT_POSITION[1]+80 )) :
        PLAYER2 += 1
        new_game()
     
    elif BALL_POSITION[0] >= 770 and (not(BALL_POSITION[1] >= BAR_RIGHT_POSITION[1] and BALL_POSITION[1] <= BAR_RIGHT_POSITION[1]+80 )) :
        PLAYER1 += 1
        new_game()
        
      
# creating the frames
frame = simplegui.create_frame("pong" , WIDTH , HEIGHT)
frame.set_draw_handler(output)
frame.set_keydown_handler(key_down)
button1 = frame.add_button("NEW GAME" , re_start , 100)

#creating the timer
timer= simplegui.create_timer(10000 , tick )

#starting the frame and timer
frame.start()
timer.start()        
