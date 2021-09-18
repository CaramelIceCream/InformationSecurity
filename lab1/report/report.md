---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе"
subtitle: "Лабораторная №1"
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

Приобрести практические навыки установки операционной системы на виртуальную машину, настроить необходимые для дальнейшей работы сервисы


# Задачи работы

1. Скачать образ виртуальной машины CentOS.
2. Создать виртуальную машину Base из скачанного образа.
3. Установить и настроить операционную систему.

# Выполнение лабораторной работы

Скопировала образ виртуальной машины CentOS-8.4.2105-x86_64-dvd1.iso в каталог С:\\msderyabina.
Запустила виртуальную машину VirtualBox. Проверила в свойствах VirtualBox месторасположение каталога для 
виртуальных машин (рис. -@fig:001).

![Окно "Свойства" VirtualBox](image/1.png){#fig:001 width=70%}

Создала новую виртуальную машину. Указала имя - Base, тип - Linux, RedHat (рис. -@fig:002).

![Окно "Имя машины и тип ОС"](image/2.png){#fig:002 width=70%}

Указала размер оперативной памяти, выделенной виртуальной машине - 1024 МБ (рис. -@fig:003).

![Окно "Размер оперативной памяти"](image/3.png){#fig:003 width=70%}

Задала конфигурацию жёсткого диска — загрузочный, VDI (BirtualBox
Disk Image), динамический виртуальный диск (рис. -@fig:004,  -@fig:005).

![Окно "Мастер создания виртуального диска"](image/4.png){#fig:004 width=70%}

![Окно "Формат хранения"](image/5.png){#fig:005 width=70%}

Задала размер диска - 40 ГБ, его расположение - C:\\msderyabina\\Base\\Base.vdi (рис. -@fig:006).

![Окно "Расположение и размер виртуального диска"](image/6.png){#fig:006 width=70%}

Проверила, что папка для снимков виртуальной машины Base имеет путь 
С:\\msderyabina\\Base\\Snapshots (рис. -@fig:007).

![Окно "Расположение и размер виртуального диска"](image/7.png){#fig:007 width=70%}

Добавила новый привод оптических дисков и выбрала образ
CentOS-8.4.2105-x86_64-dvd1.iso (рис. -@fig:008).

![Окно "Выбор образа оптического диска"](image/8.png){#fig:008 width=70%}


Запустила виртуальную машину Base, выбрала установку системы на жёсткий диск.

Установила русский язык для интерфейса и раскладки клавиатуры (рис. -@fig:009).

![Установка русского языка](image/9.png){#fig:009 width=70%} 

В качестве имени машины указала "msderyabina.localdomain"
(рис. -@fig:010).

![Сетевое имя виртуальной машины](image/10.png){#fig:010 width=70%} 

Указала часовой пояс "Москва" (рис. -@fig:011).

![Часовой пояс](image/11.png){#fig:011 width=70%} 

Установила пароль для root (рис. -@fig:012).

![Установка пароля для root](image/12.png){#fig:012 width=70%} 

Создала пользователя msderyabina (рис. -@fig:013).

![Создание пользователя](image/13.png){#fig:013 width=70%} 

Выбрала устройство для установки операционной системы (рис. -@fig:014).

![Выбор устройства](image/14.png){#fig:014 width=70%} 


Завершила установку операционной системы. Запустила виртуальную машину Base и настроила её (рис. -@fig:015, -@fig:016).

![Лицензионное соглашение](image/16.png){#fig:015 width=70%} 

![Настройка операционной системы](image/17.png){#fig:016 width=70%} 

Подключилась к виртуальной машине с помощью созданной учетной записи (рис. -@fig:017).

![Подключение к виртуальной машине](image/15.png){#fig:017 width=70%} 

На виртуальной машине Base запустила терминал, перешла под учетную запись root с помощью команды su.

С помощью команды yum update обновила системные файлы и установила Midnight Commander (рис. -@fig:018, -@fig:019).

![Обновление yum](image/18.png){#fig:018 width=70%} 

![Установка mc](image/19.png){#fig:019 width=70%} 

После установки необходимых программ завершила работу виртуальной машины. 


Для того чтобы другие виртуальные машины могли использовать машину Base и её конфигурацию, изменила тип Base на "множественное подключение" (рис. -@fig:020).

![Менеджер виртуальных носителей: множественное подключение](image/20.png){#fig:020 width=70%} 

На основе виртуальной машины Base создала машину Host2, выбрав "Использовать существующий жёсткий диск" Base.dvi (рис. -@fig:021).

![Менеджер виртуальных носителей: множественное подключение](image/21.png){#fig:021 width=70%} 

# Вывод

Я приобрела практические навыки установки операционной системы CentOS на виртуальную машину, настроила необходимые для дальшейшей работы сервисы.