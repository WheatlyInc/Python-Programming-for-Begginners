def example():
    x = 1
    y = 3
    print(x + y)

def addition(num1, num2):
    answer = num1 + num2
    return answer

def website(font, background_color, font_size, font_color):
    print('font:', font)
    print('bg:', background_color)
    print('Font size:', font_size)
    print('Font color:', font_color)
#OR:
'''
def website(font = 'TNR',
            background_color = 'white'
            fonnt_size = 19,
            font_color = black)
    print('font:', font)
    print('bg:', background_color)
    print('Font size:', font_size)
    print('Font color:', font_color)
    
#These are default parameters, and i can call the function like this to use those default parameters:
website()
#or like this to use custom parameters:
website(font_color = 'black', font_size = '11')
'''

x = addition(5,6)
print(x)

print

website('TNR', 'white', '11', 'black')
#OR:
'''
website(font_color='black',
        font='TNR',
        background_color='white',
        font_size='11')
'''