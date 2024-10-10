import turtle
"""
def get_color(color, A):
     if color == 0:
          return 'black'
     
     elif color == 1:
         return 'white'
     elif color == 2:
         return 'red'
     elif color == 3:
          return 'yellow'
     elif color == 4:
          return 'orange'	
     elif color == 5:
          return 'green'
     elif color == 6:
          return 'yellowgreen'
     elif color == 7:
          return 'sienna'
     elif color == 8:
          return 'tan'
     elif color == 9:
          return 'gray'
     
     else: A
     return 'dark gray'

"""

def draw_color_pixel(color_string, turtle):
     draw_rectangle
 
     


def draw_line(x0, y0, x1, y1): 


    turtle.penup()
    turtle.goto(x0,y0)
    turtle.pendown()
    turtle.goto(x1,y1)



def draw_rectangle(x0, y0, len, hgt, clr):
    turtle.fillcolor(clr) 
    turtle.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    turtle.end_fill()
     


num_colms = 20
num_rows = 20
x_cord = -150
y_cord = 150


for virtical_row in range(num_rows):
    for horizontel_row in range(num_colms):
    
        if horizontel_row <5:
            draw_rectangle(x_cord, y_cord, 15, 15, 'red' )

        elif horizontel_row >4 and horizontel_row <15: 
            draw_rectangle(x_cord, y_cord, 15, 15, 'green' )

        else:
            draw_rectangle(x_cord, y_cord, 15, 15, 'blue' )

        x_cord = x_cord + 15

    x_cord = -150
    y_cord = y_cord - 15   
