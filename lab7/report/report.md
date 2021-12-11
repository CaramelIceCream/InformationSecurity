---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе"
subtitle: "Лабораторная №7"
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


# Теоретическая часть

Гаммирование представляет собой наложение (снятие) на открытые (зашифрованные) данные последовательности элементов других данных,
 полученной с помощью некоторого криптографического алгоритма, для получения зашифрованных (открытых) данных. Наложение
гаммы — это сложение её элементов с элементами открытого (закрытого)
текста по некоторому фиксированному модулю, значение которого представляет собой известную часть алгоритма шифрования.
Наложение гаммы представляет собой выполнение операции
сложения по модулю 2 (XOR) между элементами
гаммы и элементами подлежащего сокрытию текста. 
Такой метод шифрования является симметричным, так как двойное прибавление одной и той же величины по модулю 2 восстанавливает исходное значение, а шифрование и расшифрование выполняется одной и той же программой.
Если известны ключ и открытый текст, то задача нахождения шифротекста заключается в применении к каждому символу открытого текста следующего правила:

Ci = Pi ^ Ki, 

где Ci — i-й символ получившегося зашифрованного послания, Pi — i-й
символ открытого текста, Ki — i-й символ ключа, i = 1, m. Размерности
открытого текста и ключа должны совпадать, и полученный шифротекст
будет такой же длины.
Если известны шифротекст и открытый текст, то задача нахождения
ключа решается также, а именно, обе части равенства необходимо сложить по модулю 2 с Pi
:

Ci ^ Pi = Pi ^ Ki ^ Pi = Ki,

Ki = Ci ^ Pi.

Открытый текст имеет символьный вид, а ключ — шестнадцатеричное
представление. Ключ также можно представить в символьном виде, воспользовавшись таблицей ASCII-кодов.

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

3. get_key(message, cr_message). Данная функция принимает исходное сообщение и закодированное сообщение.
  Выполняется сложение по модулю 2 между кодами символов исходного сообщения и значениями закодированного сообщения.
  Функция возвращает ключ, с помощью которого исходный текст был закодирован (рис. -@fig:003).

![Функция для определения ключа шифрования](../image/3.png){#fig:003 width=70%}


Написала код с вызовом функций для тестирования (рис. -@fig:004).

![Вызов функций для тестирования](../image/4.png){#fig:004 width=70%}


Протестировала программу на сообщении 'С Новым Годом, друзья!'. При вызове различных функций убедилась, что программа корректно выполняет следующие задачи (рис. -@fig:005):

1. Определяет вид шифротекста при известном ключе и известном открытом тексте.
2. Определяет ключ, с помощью которого шифротекст может быть преобразован в некоторый фрагмент текста.
3. Выполняет дешифрование текста при известном ключе.

![Тестирование программы](../image/5.png){#fig:005 width=70%}



# Вывод

Я освоила на практике применение режима однократного гаммирования, разработала программу, выполняющую различные функции: шифрование и дешифрование текста, определение ключа.