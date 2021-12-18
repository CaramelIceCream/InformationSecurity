# Декодировать сообщение
def decode(cr_message, key):
    message = []
    cr_message = cr_message.split()
    key = key.split()
    for i in range(0, len(cr_message)):
        message.append(chr(int(cr_message[i], 16) ^ int(key[i], 16)))
    return ''.join(message)


# Закодировать сообщение
def encode(message, key):
    cr_message = []
    key = key.split()
    for i in range(0, len(message)):
        cr_message.append((hex(ord(message[i]) ^ int(key[i], 16)).lstrip('0x')).upper())
        if len(cr_message[i]) == 1:
            cr_message[i] = '0' + cr_message[i]
    return ' '.join(cr_message)


def get_message(cr_message1, cr_message2, message2):
    message1 = []
    cr_message1 = cr_message1.split()
    cr_message2 = cr_message2.split()
    for i in range(0, len(cr_message1)):
        message1.append(chr(int(cr_message1[i], 16) ^ int(cr_message2[i], 16) ^ ord(message2[i])))
    return ''.join(message1)

# message = 'С Новым Годом, друзья!'
# message2 = 'Желаю счастья и любви!'
# cr_message_test_1 = '424 2c 40a 441 43c 405 40b f2 487 42e 43d 410 41e 7b df 4fc 44b 4f1 447 418 487 2a'
# cr_message_test_2 = '413 439 42C 44F 440 6E 476 495 4A4 451 44B 462 46D 77 4C7 E8 430 4FC 441 466 4F0 2A'
# key_test = '05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54 C8 0B'

print('Определим вид шифротекста_1 при известном ключе и известном открытом тексте')
message = input('Введите текст сообщения_1: ')
key = input('Введите ключ: ')
cr_message_test = encode(message, key)
print('Закодированное сообщение_1:', cr_message_test)

print()
print('Определим вид шифротекста_2 при известном ключе и известном открытом тексте')
message = input('Введите текст сообщения_2: ')
key = input('Введите ключ: ')
cr_message_test = encode(message, key)
print('Закодированное сообщение_2:', cr_message_test)

print()
print('Декодируем сообщение при его известном шифротексте, имея известный шаблон и его шифротекст')
cr_message1 = input('Введите текст закодированного сообщения: ')
message2 = input('Введите текст шаблонного сообщения: ')
cr_message2 = input('Введите текст закодированного шаблонного сообщения: ')
message1 = get_message(cr_message1, cr_message2, message2)
print('Декодированное сообщение:', message1)




