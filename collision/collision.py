try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#defining global variables
position = [100 , 20]
vel = [3,0.7]
time = 0

#defining helper functions


#defining event handlers

#canvas draw handler
def output(canvas):
    canvas.draw_circle(position , 5 , 2 ,"green","white")
    canvas.draw_line([50,50],[180,50],1,"blue")
    canvas.draw_line([180,50],[180,140],1,"blue")
    canvas.draw_line([50,140],[180,140],1,"blue")
    canvas.draw_line([50,140],[50,50],1,"blue")
    canvas.draw_text("(50,50)" ,[56,63] , 10 ,"green" )
    canvas.draw_text("(180,50)" ,[135,63] , 10 ,"green" )
    canvas.draw_text("(50,140)" ,[56,130] , 10 ,"green" )
    canvas.draw_text("(180,140)" ,[130,130] , 10 ,"green" )
    
    #update position
    position[0] += vel[0]
    position[1] += vel[1]
        
    if position[1] <= 5 or position[1] >= 215:
        vel[1] = -vel[1]
        while position[1] <= 5 or position[1] >= 215:
            position[1] += vel[1]


    elif position[0] <= 5 or position[0] >= 215:
        vel[0] = -vel[0]
        while position[0] <= 5 or position[0] >= 215:
            position[0] += vel[0]
        
    elif (position[1] >=45 and position[1] <= 50) and (position[0] >= 50 and position[0] <= 180):
        
        vel[1] = -vel[1]
        while (position[1] >=45 and position[1] <= 50) and (position[0] >= 50 and position[0] <= 180):
            position[1] += vel[1]
        
    elif (position[0] >= 45 and position[0] <= 50) and (position[1] >= 50 and position[1] <= 140):
        vel[0] = -vel[0]
        while (position[0] >= 45 and position[0] <= 50) and (position[1] >= 50 and position[1] <= 140):
            position[0] += vel[0]
        
    elif (position[1] >= 135 and position[1] <= 140) and (position[0] >= 50 and position[0] <= 180):
        vel[1] = -vel[1]  
        while (position[1] >= 135 and position[1] <= 140) and (position[0] >= 50 and position[0] <= 180):
            position[1] += vel[1]

    elif (position[0] >= 180 and position[0] <= 185) and (position[1] >= 50 and position[1] <= 140):
        vel[0] = -vel[0]
        while (position[0] >= 180 and position[0] <= 185) and (position[1] >= 50 and position[1] <= 140):
            position[0] += vel[0]


    
#creating the frame
frame = simplegui.create_frame("collision" , 220 , 220)
frame.set_draw_handler(output)


#starting the frame
frame.start()
