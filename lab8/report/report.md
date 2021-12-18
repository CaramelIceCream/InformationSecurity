---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе"
subtitle: "Лабораторная №8"
author: "Дерябина Мария Сергеевна"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: Times New Roman
romanfont: Times New Roman
sansfont: Times New Roman
monofont: Times New Roman
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Освоить на практике применение режима однократного гаммирования
на примере кодирования различных исходных текстов одним ключом.


# Теоретическая часть

Если даны две телеграммы Центра, то шифротексты обеих телеграмм можно получить по формулам режима
однократного гаммирования:
C1 = P1 ^ K,
C2 = P2 ^ K. 
Чтобы найти открытый текст, зная шифротекст
двух телеграмм, зашифрованных одним ключом, надо сложить по модулю 2 эти два равенства. 
Тогда с учётом свойства операции XOR

1 ^ 1 = 0, 1 ^ 0 = 1 ,

получаем:

C1 ^ C2 = P1 ^ K ^ P2 ^ K = P1 ^ P2.

Предположим, что одна из телеграмм является шаблоном — т.е. имеет текст фиксированный формат, в который вписываются значения полей.
Допустим, что злоумышленнику этот формат известен. Тогда он получает
достаточно много пар C1 ^ C2 (известен вид обеих шифровок). Тогда зная
P1, имеем:

C1 ^ C2 ^ P1 = P1 ^ P2 ^ P1 = P2.

Таким образом, злоумышленник получает возможность определить те
символы сообщения P2, которые находятся на позициях известного шаблона сообщения P1. В соответствии с логикой сообщения P2, злоумышленник имеет реальный шанс узнать ещё некоторое количество символов сообщения P2. 
Действуя подобным образом, злоумышленник даже если не прочитает оба
сообщения, то значительно уменьшит пространство их поиска.

# Выполнение лабораторной работы

Написала программу на языке Python, позволяющую шифровать и
дешифровать данные в режиме однократного гаммирования.
Программа имеет 3 функции:

1. decode(cr_message, key). Данная функция принимает зашифрованное сообщение и ключ (в виде строк с шестнадцатиричными значениями). 
  Для каждого значения зашифрованного сообщения выполняется сложение по модулю 2 с сответствующим значением ключа. Функция возвращает строку с расшифрованным сообщением (рис. -@fig:001).

![Функция для дешифрования сообщения](../image/1.png){#fig:001 width=70%}

2. def encode(message, key). Данная функция принимает исходное сообщение и ключ. 
  Каждый символ сообщения преобразовывется в число, соответствующее его коду в системе Unicode. Далее выполняется сложение по модулю 2 между получившимися кодами и соответствующими значениями ключа.
  Функция возвращает зашифрованное сообщение в виде строки с шестнадцатиричными значениями (рис. -@fig:002).

![Функция для шифрования сообщения](../image/2.png){#fig:002 width=70%}

3. get_message(cr_message1, cr_message2, message2). Данная функция принимает зашифрованное сообщение, шаблон исходного сообщения и зашифрованное шаблонное сообщение.
  Выполняется сложение по модулю 2 между значениями закодированного сообщения, кодами символов шаблонного сообщения и  значениями закодированного шаблонного сообщения.
  Функция возвращает строку с расшифрованным сообщением(рис. -@fig:003).

![Функция для дешифрования сообщения без ключа](../image/3.png){#fig:003 width=70%}


Написала код с вызовом функций для тестирования (рис. -@fig:004).

![Вызов функций для тестирования](../image/4.png){#fig:004 width=70%}


Протестировала программу на сообщенииях 'С Новым Годом, друзья!' и 'Желаю счастья и любви!'. 
Вначале программа определила вид шифротекста сообщений (при одинаковом ключе). Далее была вызвана функция get_message(), в которую были переданы шифротекст первого сообщения, а также исходный текст и шифротекст второго сообшения. После обработки этих данных, функция корректно определила исходный текст первого сообщения (рис. -@fig:005).

![Тестирование программы](../image/5.png){#fig:005 width=70%}

# Вывод

Я освоила на практике применение режима однократного гаммирования на примере кодирования различных исходных текстов одним ключом. Определила способ, при котором злоумышленник может прочитать оба текста, не
зная ключа и не стремясь его определить.
