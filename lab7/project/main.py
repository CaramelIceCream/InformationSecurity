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


# Найти ключ
def get_key(message, cr_message):
    cr_message = cr_message.split()
    key = []
    for i in range(0, len(message)):
        key.append((hex(ord(message[i]) ^ int(cr_message[i], 16)).lstrip('0x')).upper())
        if len(key[i]) == 1:
            key[i] = '0' + key[i]
    return ' '.join(key)

# message = 'С Новым Годом, друзья!'
# cr_message_test = '424 2c 40a 441 43c 405 40b f2 487 42e 43d 410 41e 7b df 4fc 44b 4f1 447 418 487 2a'
# key_test = '05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54 C8 0B'

print('Определим вид шифротекста при известном ключе и известном открытом тексте')
message = input('Введите текст сообщения: ')
key = input('Введите ключ: ')
cr_message_test = encode(message, key)
print('Закодированное сообщение:', cr_message_test)

print()
print('Определим ключ, с помощью которого шифротекст может быть преобразован в некоторый фрагмент текста')
message = input('Введите текст сообщения: ')
cr_message = input('Введите текст закодированного сообщения: ')
key = get_key(message, cr_message)
print('Ключ:', key)

print()
print('Декодируем сообщение при известном ключе')
cr_message = input('Введите текст закодированного сообщения: ')
key = input('Введите ключ: ')
message = decode(cr_message, key)
print('Декодированное сообщение:', message)


