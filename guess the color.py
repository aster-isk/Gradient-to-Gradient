import Tkinter
import random


root = Tkinter.Tk()
root.wm_title('Guess the Number!')

number_intvar = Tkinter.IntVar() 
number_intvar.set(0) 

text = Tkinter.Label(root, text='Use the \n colors to \n guess the \n number!')
text.grid(row=0, column=0)

canvas = Tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

random_number = random.randint(1,501)
red_value = 0
green_value = 0
def color_decimal(slider_int, random_number):
    '''this nasty boy changes the distance of the slider from the 
    randomly generated number into a color'''
    
    
    if (slider_int - random_number) == 125 or (slider_int - random_number) == -125:
            red_value = 255
            green_value = 255
    else:
        
        if slider_int < random_number:
            if (random_number - slider_int) <= 125 and (random_number - slider_int) > 0:
                red_value = int(round(((random_number - slider_int))*2.04))
                green_value = 255
            if (random_number - slider_int) >= 125 and (random_number - slider_int) <= 250:
                red_value = 255
                green_value = int(round(255 - (((random_number - slider_int) - 125)*2.04)))
                
        if slider_int > random_number:
            if (slider_int - random_number) <= 125 and (random_number - slider_int) < 0:
                red_value = int(round((slider_int - random_number))*2.04)
                green_value = 255
            if (slider_int - random_number) >= 125 and (slider_int - random_number) <= 250:
                red_value = 255
                green_value = int(round(255 - (((slider_int - random_number) - 125)*2.04)))
                
        
        if (slider_int - random_number) > 250 or (random_number - slider_int) > 250:
            red_value = 255
            green_value = 0
            
                
        if slider_int == random_number:
                red_value = 0
                green_value = 255
                
    if (slider_int - random_number) == 125 or (slider_int - random_number) == -125:
            red_value = 255
            green_value = 255
    
    return red_value, green_value

def hexstring(color_value):
    
    # Convert to hex
    slider_hex = hex(color_value)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits
    
def color_changed(new_intval):
    slider_int = number_intvar.get()
    red_dec, green_dec = color_decimal(slider_int, random_number)
    red_hex = hexstring(red_dec)
    green_hex = hexstring(green_dec)
    
    canvas.create_rectangle(0, 0, 300, 300, 
    outline="#000000", fill= '#' + \
                               red_hex + \
                               green_hex + \
                               '00')
    if slider_int == random_number:
        canvas.create_text(150, 100, text='Correct! \n Great Job!', font=('Arial', -50))   
    
number_slider = Tkinter.Scale(root, from_=0, to=500, variable=number_intvar, 
                           orient=Tkinter.HORIZONTAL,   
                           label='Number', command=color_changed)
number_slider.grid(row=1, column=0, sticky=Tkinter.E)                           
  
  
'''
def random_number_generate():
    random_number = random.randint(1,501)
    return random_number

Button = Tkinter.Button(root,text= 'Random Number!',
            command = random_number_generate, background="red")
Button.grid(row =2, column=0)
'''

#######
# Event Loop
####### color_decimal(240, 500)
root.mainloop()                        