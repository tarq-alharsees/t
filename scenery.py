import turtle

# to set the screen size and world coordinats
turtle.screensize(800, 600)  
turtle.setworldcoordinates(-600, -500, 600, 600)  

def draw_rectangle(color, width, height):
    """
    This def function draws a filled rectangle with color, width and height as the parameters, we will call this function later on in the code inside of difrent functions and give it 
    the values for color, width and height, when we draw the cake layers, candle, table top and table legs.
    """
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

def draw_circle(color, radius):
    """
    This def function draws a filled circle with color and radius as the parameters, we will call this function later on in the code inside of difrent functions and give it the values for 
    color and radius when we draw the cherry and candle flame.
    """
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_candle(base_color, flame_color, width, height):
    """
    This def function draws the base of the candle and its flame
    """
    draw_rectangle(base_color, width, height)                                           
    turtle.up()                                                                        
    turtle.left(90)                                                                    
    turtle.forward(height)                                                              
    turtle.right(90)  
    turtle.forward(width / 2)  
    turtle.down()                                                                      
    draw_circle(flame_color, width / 3)                                                 
    turtle.left(90)                                 
    turtle.up()                                                                        
    turtle.backward(height)                                                             
    turtle.down()
                                                                     

def draw_leg(x, y): 
    """
    This def function draws 1 leg at the extact location (x,y) which we will specify in the next function
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    draw_rectangle("brown", 10, 60)  # this is the color, width and height for the leg

def draw_cake_legs(base_width, base_height):
    """
    here we will specify the extact location for each leg 
    """
    leg_spacing = 30  #  the space between the left and right legs
    draw_leg(-base_width / 2 + 5 , -base_height - 60)  # left leg
    draw_leg(-base_width / 2 + 5 + leg_spacing, -base_height - 60)  # left leg
    draw_leg(base_width / 2 - 15 - leg_spacing, -base_height - 60)  # right leg
    draw_leg(base_width / 2 - 15,-base_height - 60)  # right leg

def draw_table(base_width, base_height, base_color):
    """
    this def function draws the thin table-top that is a bit wider than the cake and calls, the table legs function to draw the legs 
    """
    extended_width = base_width + 20  # adds 20 units to the orgiginal base width and called it extended_width
    turtle.up()
    turtle.goto(-extended_width / 2, -base_height)
    turtle.down()
    draw_rectangle(base_color, extended_width, base_height) # to draw table top
    draw_cake_legs(extended_width, base_height)  # to draw legs under the base
    turtle.up()
    turtle.goto(-base_width / 2, 0)  # to reset position of  the turtle and start drawing the cake layers
    turtle.down()

def draw_cake(base_width, layer_heights, layer_colors, cherry_color, cherry_radius):
    """
    this def function will draw the cake layers and cherry with the specifid parameters that it will 
    take from the user input 
    """
    turtle.speed(10)                                                                                                   #################   speed
    

    draw_table(base_width, 10, "gray")  # to draw the table top

    current_height = 0

    # first layer

    draw_rectangle(layer_colors[0], base_width, layer_heights[0])
    turtle.left(90)
    turtle.forward(layer_heights[0])
    turtle.right(90)
    current_height += layer_heights[0] #to add the height of the current layer to current_height

    # second layer

    draw_rectangle(layer_colors[1], base_width, layer_heights[1])
    turtle.left(90)
    turtle.forward(layer_heights[1])
    turtle.right(90)
    current_height += layer_heights[1]

    # third layer

    draw_rectangle(layer_colors[2], base_width, layer_heights[2])
    turtle.left(90)
    turtle.forward(layer_heights[2])
    turtle.right(90)
    current_height += layer_heights[2]

    # to draw the cherry on top of the cake
    turtle.up()
    turtle.goto(0, current_height)
    turtle.down()
    draw_circle(cherry_color, cherry_radius)

    # to draw a candle on top of the cake
    turtle.up()
    turtle.goto(-100, current_height)  # to offcenter position for the candle
    turtle.down()
    draw_candle("white", "orange", 20, 40)  # candle dimensions

    turtle.hideturtle()
    turtle.done()

def main():

    """this function will take the specifications for the cake and cherry from the user """

    print("Let's draw a cake!")
    base_width = int(input("How wide do you want the cake to be (from 110 to 800): "))
    layer_heights = [
        int(input("How high do you want layer 1 to be (from 10 to 55): ")),
        int(input("How high do you want layer 2 to be (from 10 to 55): ")),
        int(input("How high do you want layer 3 to be (from 10 to 55): "))
    ]
    layer_colors = [
        input("What color do you want layer 1 to be: "),
        input("What color do you want layer 2 to be: "),
        input("What color do you want layer 3 to be: ")
    ]
    cherry_color = input("Enter the color of the cherry on top: ")
    cherry_radius = int(input("How big do you want the cherry to be (from 20 to 50): "))

    """this call will take the user input and execute it in the draw cake function we wrote earlier  """
    
    draw_cake(base_width, layer_heights, layer_colors, cherry_color, cherry_radius)

if __name__ == "__main__": # to check if the script is being run directly or being imported as a module
    main()
