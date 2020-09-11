image_str = [
    '################################',
    '#                              #',
    '#     ############              #',
    '#     #          #              #',
    '#     ########   #              #',
    '#           ##   #              #',
    '#     ########   #              #',
    '#     ########   #              #',
    '#     #          #              #',
    '#     ############              #',
    '#                              #',
    '################################',

]

image = []

for s in image_str:
    image.append(list(s))

def print_image():
    for i in image:
        print("".join(i))

def floodfill(row, col, char):
    # if the pixel at row, col is not a space: return
    #set the characted at this "pixel" to char
    #do something
    # floodfile(something else)
    if image[row][col] != ' ':
        return
    
    image[row][col] = char

    floodfill(row-1, col, char)
    floodfill(row+1, col, char)
    floodfill(row, col-1, char)
    floodfill(row, col+1, char)

floodfill(5, 15, 'x')


print_image()