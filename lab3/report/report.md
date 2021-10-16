---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе"
subtitle: "Лабораторная №3"
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

Получить практические навыки работы в консоли с атрибутами файлов для групп пользователей.

# Задачи работы

1. Научиться добавлять пользователей в группу.
2. Заполнить таблицу, сопоставляющую различные действия и права доступа для группы.
3. Выявить минимальные необходимые права доступа для различных действий в системе для группы.

# Выполнение лабораторной работы

В установленной операционной системе создала пользователя guest2 аналогично пользователю guest, созданному во 2 лабораторной. Добавила пользователя guest2 в группу guest (рис. -@fig:001).

![Создание пользователя guest2 и добавление в группу](../image/1.png){#fig:001 width=70%}

Осуществила вход в систему от двух пользователей на двух разных консолях: guest на первой консоли и guest2 на второй консоли. Для обоих пользователей командой pwd определила директорию, в которой нахожусь - это оказались домашние папки пользователей guest и guest2. В приглашении командной строки указано имя пользователя и знак ~. (рис. -@fig:002, рис. -@fig:003).

![Вход в систему через пользователя guest](../image/2.png){#fig:002 width=70%}

![Вход в систему через пользователя guest2](../image/3.png){#fig:003 width=70%}

Уточнила имена пользователей, командой groups определила, в какие группы входят пользователи. Вывод команды аналогичен выводу команд id -Gn и id -G. (рис. -@fig:004, рис. -@fig:005).

![Информация о группах пользователя guest](../image/4.png){#fig:004 width=70%}

![Информация о группах пользователя guest2](../image/5.png){#fig:005 width=70%}

Получила эту же информацию, посмотрев содержимое файла /etc/group (рис. -@fig:006)

![Вывод файла /etc/group](../image/6.png){#fig:006 width=70%}

От имени пользователя guest2 выполнила регистрацию пользователя guest2 в группе guest командой newgrp guest.

От имени пользователя guest изменила права директории /home/guest, разрешив все действия для пользователей группы. От имени пользователя guest сняла с директории /home/guest/dir1 все атрибуты (рис. -@fig:007).

![Изменения атрибутов от имени guest](../image/7.png){#fig:007 width=70%}

Теперь от имени пользователя guest2 можно зайти в домашнюю папку guest, но не в папку dir1 (рис. -@fig:008)

![Проверка снятия атрибутов](../image/8.png){#fig:008 width=70%}

Меняя атрибуты у директории dir1 и файла file1 от имени пользователя guest и делая проверку от пользователя guest2, заполнила табл. 3.1,
определив опытным путём, какие операции разрешены, а какие нет (рис. -@fig:009, рис. -@fig:010).

![Установленные права и разрешённые действия для групп](../image/9.png){#fig:009 width=70%}

![Установленные права и разрешённые действия для групп](../image/10.png){#fig:010 width=70%}


На основании заполненной таблицы определила минимально необходимые права для выполнения пользователем guest2 операций
внутри директории dir1 и заполнила табл. 3.2  (рис. -@fig:011).

![Минимальные права для совершения операций от имени пользователей входящих в группу](../image/11.png){#fig:011 width=70%}

# Вывод

Я получила практические навыки работы в консоли с атрибутами файлов и каталогов для групп пользователей.
