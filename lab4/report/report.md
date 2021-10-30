---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе"
subtitle: "Лабораторная №4"
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

Получить практические навыки работы в консоли с расширенными атрибутами файлов

# Задачи работы

1. Научиться устанавливать расширенные атрибуты на файл.
2. Опробовать различные действия над файлом с установленными атрибутами 'a', 'i' и без атрибутов.

# Выполнение лабораторной работы

От имени пользователя guest определила расширенные атрибуты файла file1.txt: они оказались не заполнены (рис. -@fig:001).

![Расширенные атрибуты файла file1](../image/1.png){#fig:001 width=70%}

Установила на файле file1 права, разрешающие чтение и запись для владельца файла. Попыталась установить на файл расширенный атрибут 'а' от имени пользователя guest, но получила отказ от выполнения операции (рис. -@fig:002).

![Отказ операции смены атрибута от имени пользователя guest](../image/2.png){#fig:002 width=70%}

От имени администратора удалось установаить расширенный атрибут (рис. -@fig:003).

![Смена атрибута от имени администратора](../image/3.png){#fig:003 width=70%}

От имени пользователя guest проверила правильность атрибутов (рис. -@fig:004)

![Расширенные атрибуты file1](../image/4.png){#fig:004 width=70%}

Выполнила дозапись в файл file1 командой echo и убедилась, что слово было записано, командой cat. Попробовала выполнить следующие действия:  перезаписать в файл новый текст, переименовать файл, изменить права доступа к файлу. Получила отказ операций. Сняла расширенный атрибут с файла, после этого все операции удалось выполнить (рис. -@fig:005).

![Действия с файлом при установленном атрибуте 'а' и без атрибутов](../image/5.png){#fig:005 width=70%}

Повторила действия, заменив атрибут 'а' атрибутом 'i'. В этом случае не получилось дозаписать в файл текст. Остальные действия, кроме чтения файла, тоже не получилось выполнить. (рис. -@fig:006)

![Действия с файлом при установленном атрибуте 'i'](../image/6.png){#fig:006 width=70%}


# Вывод

Я получила практические навыки работы в консоли с расширенными атрибутами файлов. Опробовала действия на расширенных атрибутах 'а' и 'i'. 

Убедилась, что с установленным атрибутом 'a' файл может быть открыт только в режиме дозаписи. С установленным атрибутом 'i' файл полностью защищен от изменений.
