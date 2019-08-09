try:
    print('Running the try...')
    print('5' + x)

except TypeError as t:
    print('TypeError triggered')

except NameError as n:
    print('NameError triggered')

except Exception as e:
    print('General Exception')