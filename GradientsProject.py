import math
import Tkinter
import random

rand_a = random.randint(1, 50)
rand_b = random.randint(1, 50)
rand_c = random.randint(1, 50)
rand_x = random.randint(1, 50)
rand_y = random.randint(1, 50)
rand_step = random.randint(1, 1000)
rand_equ = random.randint(1, 3)

root = Tkinter.Tk()
root.wm_title('Gradients')

#Constant Values
a_intvar = Tkinter.IntVar() 
a_intvar.set(rand_a) 
b_intvar = Tkinter.IntVar()
b_intvar.set(rand_b)
c_intvar = Tkinter.IntVar()
c_intvar.set(rand_c)

#X & Y values
x_intvar = Tkinter.IntVar() 
x_intvar.set(rand_x) 
y_intvar = Tkinter.IntVar()
y_intvar.set(rand_y)

#Step Size
step_intvar = Tkinter.IntVar()
step_intvar.set(rand_step)

#Choose Equation
equation_intvar = Tkinter.IntVar()

#Canvas
canvas = Tkinter.Canvas(root, width=475, height=790, background='#FFFFFF')
canvas.grid(row=0, rowspan=8, column=1)
text = Tkinter.Label(root, text='Slope of the Directional Derivative                            Direction of the gradient            ')
text.grid(row=8, column=1) 

#Editor
editor = Tkinter.Text(root, width=15)
editor.grid(column=3, row=3, columnspan=2, rowspan=4)

'''
Calculates Gradient and then the Directional Derivative accordingly, 
calculates radian of derivative in terms of theta is the angle created between the tangent line and the horizontal plane.
'''
    
def calculate_values(x, y, a, b, c, step_size, equation_value):
    #calculates and saves gradient vector values of z = sin(ax)*cos(by)/c, 
    #z = sin(ax^2)+by(siny)+cx(sinx), z = 1/(a(x^2+y^2))and magnatude values
    pi = math.pi
    vector_list = []
    magnatude_list = []
    drv_list = []
    radiens_list = []
    gra_radians_list = []
    x = x
    y = y
    
    for s in range(0, 100):
        if equation_value == 1:
            dev_respect_x = ((a/c)*math.cos(a*x)*math.cos(b*y))
            dev_respect_y = ((-1*a/c)*(math.sin(a*x))*(math.sin(b*y)))

        if equation_value == 2:
            dev_respect_x = .1*(a*2*x*math.cos(a*x**2)+c*x*math.cos(x)+c*math.sin(x))
            dev_respect_y = .1*(b*y*math.cos(y)+b*math.sin(y))
            
        if equation_value == 3:
            dev_respect_x = (-1*c*2*a*x)/((a*x**2)+(b*y**2))
            dev_respect_y = (-1*c*2*b*y)/((a*x**2)+(b*y**2))
        
        m = math.sqrt(dev_respect_x**2 + dev_respect_y**2) #magnatude
        v_x = dev_respect_x/m
        v_y = dev_respect_y/m
        v = (v_x, v_y) #unit vector
        
        x = x + (m*(step_size/100))
        y = y + (m*(step_size/100))
        
        dev_respect_v = (dev_respect_x*v_x) + (dev_respect_y*v_y)
        
        vector_list += [v]
        magnatude_list += [m]
        drv_list += [dev_respect_v]
        
        radiens = math.atan(dev_respect_v)
        radiens_list += [radiens]
        
        if v_x == 0:
            gra_radians =  pi/4
        else:
            gra_radians =  math.atan(v_y/v_x) 
        gra_radians_list += [gra_radians/2] 
    
    return drv_list, radiens_list, dev_respect_x, gra_radians_list

#Turns the calculated radian value into a corrisponding RGB value on a color wheel that is reduced from 0 to pi radians
def make_hue(rdns):
    pi = math.pi
    red = 0
    green = 0
    blue = 0
    
    while rdns > 6.2831853071/4:
        rdns -= 6.28318530/4
    while rdns < 0:
        rdns += 6.2831853071/4
        
    if rdns >= pi/4 and rdns <= 5*pi/12:
            red = 255
    elif rdns > pi/6 and rdns < pi/4:
            redratio = ((rdns - (pi/6))/(pi/12))
            red = int(round(225*redratio))
    elif rdns > 5*pi/12 and rdns < pi/2:
            redratio = ((pi/2 - rdns)/(pi/12))
            red = int(round(225*redratio))
    
            
    if rdns >= pi/12 and rdns <= 2*pi/6:
            green = 255
    elif rdns > 0 and rdns < (pi/12):
            greenratio = ((rdns)/(pi/12))
            green = int(round(225*greenratio))
    elif rdns > pi/4 and rdns < 4*pi/12:
            greenratio = (((4*pi/12) - rdns)/(pi/12))
            green = int(round(225*greenratio))

            
    if (rdns >= 0 and rdns <= pi/12) or (rdns >= 4*pi/12 and rdns <= pi/2):
            blue = 255
    elif rdns > 5*pi/12 and rdns < pi/2:
            blueratio = ((rdns - (5*pi/12))/(pi/12))
            blue = int(round(225*blueratio))
    elif rdns > pi/12 and rdns < pi/6:
            blueratio = (((pi/6) - rdns)/(pi/12))
            blue = int(round(225*blueratio))

            
    hue = (red, green, blue)
            
    return hue, red, green, blue

#Turns each Decimal Value to a Hexadecimal Value which is what Tkinter uses
def hexstring(color):

    RGB_hex = hex(color)
    hex_digits = RGB_hex[2:] 
    if len(hex_digits)==1:
        hex_digits = '0' + hex_digits 
    return hex_digits
    
def paint_canvas(new_intval):
    x = x_intvar.get()
    y = y_intvar.get()
    a = a_intvar.get()
    b = b_intvar.get()
    c = c_intvar.get()
    step_size = step_intvar.get()
    equation_value = equation_intvar.get()
    
    
    row_counter = 0

    s = 0    
    
    equations_list = ['z = sin(' + str(a) + '*' + str(x) + ')*cos(' + str(b) + '*' +  str(y) + ')/' + str(c), 
                        'z = sin(' + str(a) + '*' + str(x) + '^2)+' + str(b) + '*' +  str(y) + '(sin(' + str(y) + '))+' + str(c) + '*' +  str(x) + '(sin('  + str(x) + '))', 
                        'z = 1/(' + str(a) + '(' + str(x) + '^2+' + str(y) + '^2))']
    
    hue_list = []
    red_hex_list = []
    green_hex_list = []
    blue_hex_list =[]
    hue_list2 = []
    red_hex_list2 = []
    green_hex_list2 = []
    blue_hex_list2 =[]
          
    drv_list, radiens_list, dev_respect_x, gra_radians_list = calculate_values(x, y, a, b, c, step_size, equation_value)

            
    for radiens in range(len(radiens_list)): 
        rdns = radiens_list[radiens]
        hue, red, green, blue= make_hue(rdns)
        hue_list += [hue]
        red_hex = hexstring(red)
        red_hex_list += [red_hex]
        green_hex = hexstring(green)
        green_hex_list += [green_hex]
        blue_hex = hexstring(blue)
        blue_hex_list += [blue_hex]
   
    for radians in range(len(gra_radians_list)): 
        rdns2 = gra_radians_list[radians]
        hue2, red2, green2, blue2 = make_hue(rdns2)
        hue_list2 += [hue]
        red_hex2 = hexstring(red2)
        red_hex_list2 += [red_hex2]
        green_hex2 = hexstring(green2)
        green_hex_list2 += [green_hex2]
        blue_hex2 = hexstring(blue2)
        blue_hex_list2 += [blue_hex2] 
    
    editor.insert(Tkinter.END, equations_list[equation_value-1] + '\n')
            
    for n in range(10):
        editor.insert(Tkinter.END, str(n*10) + '   #' + \
                            red_hex_list[n*10] + \
                            green_hex_list[n*10] + \
                            blue_hex_list[n*10] + '\n')
        editor.see(Tkinter.END)
        
    for n in range(10):
        editor.insert(Tkinter.END, str(n*10) + '   #' + \
                            red_hex_list2[n*10] + \
                            green_hex_list2[n*10] + \
                            blue_hex_list2[n*10] + '\n')                        
        editor.see(Tkinter.END)
        
    line_width = 8
    
    while row_counter < 100:
        height = row_counter*line_width
        canvas.create_line(0, height, 240, height, fill= '#' + \
                            red_hex_list[int(row_counter)] + \
                            green_hex_list[int(row_counter)] + \
                            blue_hex_list[int(row_counter)], width=line_width)
        canvas.create_line(240, height, 480, height, fill= '#' + \
                            red_hex_list2[int(row_counter)] + \
                            green_hex_list2[int(row_counter)] + \
                            blue_hex_list2[int(row_counter)], width=line_width)
        row_counter += 1
           

#Constant Values
a_slider = Tkinter.Scale(root, from_=1, to=50, variable=a_intvar, orient=Tkinter.HORIZONTAL, label='a', command=paint_canvas)
a_slider.grid(row=0, column=0, sticky=Tkinter.E)
b_slider = Tkinter.Scale(root, from_=1, to=50, variable=b_intvar, orient=Tkinter.HORIZONTAL, label='b', command=paint_canvas)
b_slider.grid(row=1, column=0, sticky=Tkinter.E)
c_slider = Tkinter.Scale(root, from_=1, to=50, variable=c_intvar, orient=Tkinter.HORIZONTAL, label='c', command=paint_canvas)
c_slider.grid(row=2, column=0, sticky=Tkinter.E)

#X & Y values
x_slider = Tkinter.Scale(root, from_=1, to=50, variable=x_intvar, orient=Tkinter.HORIZONTAL, label='x',command=paint_canvas )
x_slider.grid(row=4, column=0, sticky=Tkinter.E)
y_slider = Tkinter.Scale(root, from_=1, to=50, variable=y_intvar, orient=Tkinter.HORIZONTAL, label='y', command=paint_canvas)
y_slider.grid(row=5, column=0, sticky=Tkinter.E)

#Step Size
step_slider = Tkinter.Scale(root, from_=1, to=1000, variable=step_intvar, orient=Tkinter.HORIZONTAL, label='Step Percent', command=paint_canvas)
step_slider.grid(row=6, column=0, sticky=Tkinter.E)

#Choose Equation
equation_slider = Tkinter.Scale(root, from_=1, to=3, variable=equation_intvar, orient=Tkinter.VERTICAL, command=paint_canvas)
equation_slider.grid(row=0, rowspan=3, column=2, sticky=Tkinter.E)
text = Tkinter.Label(root, text='z = sin(ax)*cos(by)/c\n\n\nz = sin(ax^2)+by(siny)+cx(sinx)\n\n\nz = 1/(a(x^2+y^2))', justify= Tkinter.LEFT)
text.grid(row=1, column=4)

root.mainloop()
