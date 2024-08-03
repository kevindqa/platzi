
def message_creator (name):
    disp = {'laptop': "Laptops are portable computers suitable for work and entertainment.",
            'smartphone': "Smartphones are handheld devices that combine a phone with a computer.",
            'tablet': "Tablets are portable touch-screen devices that are larger than smartphones but smaller than laptops.",
            'smartwatch': "Smartwatches are wearable devices that offer a variety of functions, including fitness tracking and notifications."}
    if name in disp:
        return disp[name]
    else :
        return 'no se tiene informacion del dispositivo'


product_name = input( ) 

name = message_creator(product_name)

print (name)