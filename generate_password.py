import random

def generate_password():

    long=int(input('cuantos caracteres quieres que incluya tu contraseña?'))
    upper_input=int(input('escribe 1 si quieres incluir mayúsculas, de lo contrario escribe 0'))
    lower_input=int(input('escribe 1 si quieres incluir minúsculas, de lo contrario escribe 0'))
    numbers_input=int(input('escribe 1 si quieres incluir números, de lo contrario escribe 0'))
    esp_chars_input=int(input('escribe 1 si quieres incluir caracteres especiales, de lo contrario escribe 0'))

    
    list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_esp_chars=['!', '"', '#', '$', '%', '&', "'", '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '^', '_', '`', '{', '|', '}', '~']

    symbols= {
        'type': ['upper', 'lower', 'numbers', 'esp_chars'], 
        'list': [list_upper, list_lower, list_numbers, list_esp_chars], 
        'exists': [upper_input, lower_input, numbers_input, esp_chars_input]
        }

    include=[]
    list_password=[]

    for i in range(0, len(symbols['type'])):
        if symbols['exists'][i]==1:
            include.extend(symbols['list'][i])
    
    for j in range(1, (long + 1)):
        aleatorio=random.randint(0, len(include)-1)
        list_password.extend(include[aleatorio])

    password=''.join(list_password)

    return password
#jejejej mi colaboración
