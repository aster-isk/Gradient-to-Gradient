import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw   

def get_images(directory):
    """ returns PIL.Image objects for all the images in directory
    if directory is not specified, uses current directory
    returns file list and image list
    """
    if directory == 'current':
        directory = os.getcwd()
    else:
        directory = directory
    
    image_list = []
    file_list = []
    
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with non-images in file
    return image_list, file_list

def make_border(original_image, logo_name, border_percent, border_color):
    """ gives a border thats half transparent half color you choose
    """
    #set the thiccness of the rounded corners
    width, height = original_image.size
    border_width = int(border_percent * min(width, height))
    new_width = width + border_width
    new_height = height + border_width
    new_size = (new_width, new_height)
    

    
    #start with transparent border
    border = PIL.Image.new('RGB', (new_size))
    drawing_layer = PIL.ImageDraw.Draw(border)
    
    
    # Draw 1 rectangle to fill diagonal
    drawing_layer.polygon([(0,new_height),(new_width,new_height),(0,0),(0,new_width)],
                            fill=(225, 0, 0))
                         
    plt.imshow(border)
    
    #paste image & border
    border.paste(original_image, ((border_width/2), (border_width/2)), mask=None)

    
    width, height = original_image.size
    border_width = int(border_percent * min(width, height))
    new_width = width + border_width
    new_height = height + border_width
    new_size = (new_width, new_height)
    
    directory = os.getcwd()
    logo_file = os.path.join(directory, logo_name)  
    logo_image = PIL.Image.open(logo_file)
    
    #resize logo
    logo_width, logo_height = logo_image.size
    resized_ratio = logo_height / (border_width/2)
    resized_width = logo_width / resized_ratio
    logo_resized = logo_image.resize((resized_width, (border_width/2)))
    
    logo_x = (((border_width/4) + resized_width))
    
    border.paste(logo_resized, ((width/2), (height/4)), mask=None)
    
    return border
    
def logo_it(border_color, border_percent, directory):
    """ saves a modfied version of each image in directory.
        makes file for modified images in directory if one does not exist
    """

    # create a new directory 'logoed'
    new_directory = os.path.join(directory, 'logoed')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        filename, filetype = os.path.splitext(file_list[n])
        new_image = make_border(image_list[n], 'logo.png', border_percent, border_color)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        