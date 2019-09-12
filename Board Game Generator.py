import tkinter as tk
import random
import os

window = tk.Tk()
window.title('Game Generator')

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#makes space patterns
def gen_pat(gb_size):
    pat_list =  []
    move_list =  []
    space_list = []
    s = 0
    
    m = random.randrange(gb_size*2)
    mo = 4
    for r in range(8):
        direction = random.randrange(gb_size/2)
        pat_list +=  [direction]
        
    for r in range(2):
        move = random.randrange((gb_size/2))
        move_list +=  [move]
     
    r = pat_list[0]
    l = pat_list[1]
    u = pat_list[2]
    d = pat_list[3]

   
    e = move_list[0]
    n = move_list[1]

    while mo <= int(gb_size*gb_size) and mo >= 0:
        for s in range(r + 1):
            if m <= int(gb_size*gb_size):
                m += (s)
                space_list += [m]
                s += 1
            m = mo
        for s in range(l):
            if m >= 0:
                m -= (s)
                space_list += [m]
                s += 1
            m = mo
        for s in range(u):
            if m <= int(gb_size*gb_size):
                m += (gb_size*s)
                space_list += [m]
                s += 1
            m = mo
        for s in range(d):
            if m >= 0:
                m -= (gb_size*s)
                space_list += [m]
                s += 1
            m = mo
        mo = (mo + e +(n*gb_size))

    return space_list

#makes gameboard list
def create_gb(gb_size, tp_sqrs):

   coor_list = []
   space_list = []
   change_type = []
   current_space  = 0
   k = 0
   
   if gb_size % 2 != 0:
       gb_size += 1
   else:
       gb_size = gb_size
   
   for s in range(tp_sqrs):
       type_list = gen_pat(gb_size)
       space_list += [type_list]
       current_space += len(type_list)
       change_type += [current_space]
    
   for x in range(gb_size*gb_size):
        coor_list += [0]
           
   for k in range(len(space_list)):
       t_list = space_list[k]
       for nk in range(len(t_list)):
            if t_list[nk] >= 0 and t_list[nk] < (gb_size*gb_size):
                coor_list[t_list[nk]] = k + 1
                nk += 1
       k += 1
    
   return coor_list
 
#creates initial conditions, ie game board and piece #/types/movements
#def create_ic(gb_size, tp_squares, num_piece, tp_piece, win_condition, mirror board):
    
def piece_gen(gb_size, rows, type_piece):
    piece_count = gb_size * rows
    piece_type_count = piece_count
    piece_type_list = []
    piece_move_count_list = []
    move_dir_list = ['up/down', 'L', 'diagonal']
    piece_move_dir_list = []
    piece_list = []
    piece_list_con = []
    piece_coor_list = []
    x = 0
    
    for c in range(type_piece - 1):
        piece_type_num = random.randint(1, (piece_type_count - (type_piece - (c))))
        piece_type_count -= piece_type_num 
        piece_type_list += [piece_type_num]
    piece_type_list += [piece_count - (piece_count - piece_type_count)]
    
    for b in range(type_piece):
        rand = random.randint(0, 2) 
        piece_move_dir_list += [move_dir_list[rand]]
        
    while x < type_piece:
        random_x = random.randint(1,gb_size)
        random_y = random.randint(1,gb_size)
        if gb_size % random_x == 0 and  gb_size % random_y == 0:
            x += 1
            random_move_count = (random_x,random_y)
            piece_move_count_list += [random_move_count]
    
    for l in range(type_piece):
        piece_list += [(l, piece_move_dir_list[l], piece_move_count_list[l])]
        for j in range(piece_type_list[l]):
            piece_list_con += [l]
            
    for k in range(piece_count):
        random_choice = random.randint(0, len(piece_list_con) - 1)
        piece_coor_list += [piece_list_con[random_choice]]
        piece_list_con.remove(piece_list_con[random_choice])
        
    return piece_coor_list, piece_list

def hexstring(color):

    RGB_hex = hex(color)
    hex_digits = RGB_hex[2:] 
    if len(hex_digits)==1:
        hex_digits = '0' + hex_digits 
    return hex_digits

def create_board(gb_size, tp_sqrs, piece_rows, type_piece, game_name):
    x = 1
    
    new_directory = os.path.join(dname, 'games') 
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  

    piece_coor_list, piece_list = piece_gen(gb_size, piece_rows, type_piece)
    coor_list = create_gb(gb_size, tp_sqrs)
    win_conditions  = ['Checkers', 'Point Collection: Collect' + str(int(gb_size*type_piece/2)) + 'Points', 'Capture A Side', 'Chess: Capture All Piece #' + str(random.randint(0, type_piece - 1))]
    random_con = random.randint(0, (len(win_conditions)-1))
    og_game = game_name
    while os.path.exists(os.path.join(new_directory,game_name +'.txt')):
        game_name = og_game + '_' + str(x)
        x += 1
        
    f = open(os.path.join(new_directory,game_name +'.txt'),'w')
    
    f.write(game_name + ' Randomly Generated Rules' + '\n')
    
    f.write('Win Condition: ' + win_conditions[random_con] + '\n')
    
    f.write('Piece Types' + '\n')
    for k in range(type_piece):
        f.write(str(piece_list[k]) + '\n')
        
    f.write('Piece Setup' + '\n')
    for j in range(piece_rows):
        f.write(str(piece_coor_list[(j*gb_size):((j*gb_size)+gb_size)]) + '\n')
        
    f.write('Game Board' + '\n')
    for n in range(gb_size):
        f.write(str(coor_list[(n*gb_size):((n*gb_size)+gb_size)]) + '\n')
        
    f.close()
    
    editor.insert(tk.END, game_name + '\n')
    
    editor.insert(tk.END, 'Win Condition: ' + win_conditions[random_con] + '\n')
    
    editor.insert(tk.END, 'Piece Types' + '\n')
    for k in range(type_piece):
        editor.insert(tk.END, str(piece_list[k]) + '\n')
        
    editor.insert(tk.END, 'Piece Setup' + '\n')
    for j in range(piece_rows):
        editor.insert(tk.END, str(piece_coor_list[(j*gb_size):((j*gb_size)+gb_size)]) + '\n')
        
    editor.insert(tk.END, 'Game Board' + '\n')
    for n in range(gb_size):
        editor.insert(tk.END, str(coor_list[(n*gb_size):((n*gb_size)+gb_size)]) + '\n')
    
    editor.insert(tk.END, 'Game Saved to: ' + game_name +'.txt')
                           
    editor.see(tk.END)
    
    paint_board(gb_size, tp_sqrs, piece_rows, type_piece, game_name, new_directory)

def paint_board(gb_size, tp_sqrs, piece_rows, type_piece, game_name, new_directory):
    piece_coor_list, piece_list = piece_gen(gb_size, piece_rows, type_piece)
    coor_list = create_gb(gb_size, tp_sqrs)
    color_list = []
    redlist = []
    greenlist = []
    bluelist = []
    color_x_list = []
    redplist = []
    greenplist = []
    blueplist = []
    square_size = 600/gb_size
    m = 0
    n = 0
    f = 0
    d = 0
    canvas.create_rectangle(0, 0, 600, 600, fill = '#F0F0F0', outline = '#F0F0F0')
    
    for c in range(tp_sqrs):
        red = random.randint(1, 255)
        blue = random.randint(1, 255)
        green = random.randint(1, 255)
        red_hex = hexstring(red)
        green_hex = hexstring(green)
        blue_hex = hexstring(blue)
        new_hex = ('#' +  red_hex + green_hex + blue_hex)
        color_list += [new_hex]
        redlist += [red]
        greenlist += [green]
        bluelist += [blue]
        
    for l in range(type_piece):
        red = random.randint(1, 255)
        blue = random.randint(1, 255)
        green = random.randint(1, 255)
        red_hex = hexstring(red)
        green_hex = hexstring(green)
        blue_hex = hexstring(blue)
        new_hex = ('#' +  red_hex + green_hex + blue_hex)
        color_x_list += [new_hex]
        redplist += [red]
        greenplist += [green]
        blueplist += [blue]
            
    for h in range(gb_size):
        for s in range(gb_size):
            canvas.create_rectangle((s*square_size),(h*square_size), 
                                    ((s*square_size)+square_size), 
                                    ((h*square_size)+square_size), 
                                    fill= color_list[int(coor_list[m])-1])
            m += 1    
            
    for j in range(piece_rows):
        for p in range(gb_size):
            reverse = gb_size - p -1
            reverse_ver = gb_size - j  - 1
            canvas.create_oval((p*square_size),(j*square_size), 
                                    ((p*square_size)+square_size), 
                                    ((j*square_size)+square_size), 
                                    fill= color_x_list[int(piece_coor_list[n])])
            canvas.create_oval((reverse*square_size),(reverse_ver*square_size), 
                                    ((reverse*square_size)+square_size), 
                                    ((reverse_ver*square_size)+square_size), 
                                    fill= color_x_list[int(piece_coor_list[n])])
            n += 1
      
def gen_input():
    tp_sqrs = int(e2.get())
    piece_rows = int(e3.get())
    type_piece = int(e4.get())
    gb_size = int(e1.get())
    game_name = str(e5.get())
    if game_name == '':
        game_name = str(gb_size) + str(tp_sqrs) + str(piece_rows) + str(type_piece)
        e5.insert(0, str(game_name))
    create_board(gb_size, tp_sqrs, piece_rows, type_piece, game_name)  
    
def gen_random():
    gb_size = random.randint(1, 50)
    tp_sqrs = random.randint(1, gb_size -1)
    piece_rows = random.randint(1, gb_size - int(gb_size/2) - 1)
    type_piece = random.randint(1, piece_rows * gb_size)
    game_name = str(e5.get())
    if game_name == '':
        game_name = str(gb_size) + str(tp_sqrs) + str(piece_rows) + str(type_piece)
    e1.delete(0, 50)
    e1.insert(0, str(gb_size))
    e2.delete(0, 50)
    e2.insert(0, str(tp_sqrs))
    e3.delete(0, 50)
    e3.insert(0, str(piece_rows))
    e4.delete(0, 50)
    e4.insert(0, str(type_piece))
    e5.insert(0, str(game_name))
    create_board(gb_size, tp_sqrs, piece_rows, type_piece, game_name)
    
tk.Label(window, 
         text="Board Height/Width:").grid(row=1)
tk.Label(window, 
         text="# of Types of Squares:").grid(row=2)
tk.Label(window, 
         text="# of Rows of Pieces:").grid(row=3)
tk.Label(window, 
         text="# of Types of Piece").grid(row=4)
tk.Label(window, 
         text="Game Name").grid(row=0)

editor = tk.Text(window, height=40, width=60)
editor.grid(column=2, row=0, columnspan=1,rowspan=6)

canvas = tk.Canvas(window, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=8, column=4)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)
e5 = tk.Entry(window)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=0, column=1)

b1 = tk.Button(window, 
          text='Generate', 
          command=gen_input)
b1.grid(row=6, column=0)

b2 = tk.Button(window, 
          text='Random', 
          command=gen_random)
b2.grid(row=6, column=1)

tk.mainloop()
