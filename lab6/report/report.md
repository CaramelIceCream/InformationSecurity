---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе"
subtitle: "Лабораторная №6"
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

Развить навыки администрирования ОС Linux. Получить первое практическое знакомство с технологией SELinux.
Проверить работу SELinux на практике совместно с веб-сервером Apache.


# Подготовка лабораторного стенда

Для выполнения работы, установила веб-сервер Apache (рис. -@fig:001).

![Установка Apache](../image/1.png){#fig:001 width=70%}

В конфигурационном файле /etc/httpd/conf/httpd.conf задала параметр ServerName

![Конфигурационный файл httpd.conf](../image/2.png){#fig:002 width=70%}

Отключила пакетный фильтр (../image/3.png){#fig:003 width=70%} 

![Отключение пакетного фильтра](../image/3.png){#fig:003 width=70%}


# Выполнение лабораторной работы

## Изучение политики и контектса SELinux

Вошла в систему и убедилась, что
SELinux работает в режиме enforcing политики targeted с помощью команд getenforce и sestatus (рис. -@fig:004).

![Статус SELinux](../image/4.png){#fig:004 width=70%}

Запустила веб-сервер Apache. (рис. -@fig:005).

![Старт веб-сервера Apache](../image/5.png){#fig:005 width=70%}

Нашла веб-сервер в списке процессов. Его контекст безопасности - "system_u:system:r:httpd_t:s0" (рис. -@fig:006).

![Контекст безопасности веб-сервера Apache](../image/6.png){#fig:006 width=70%}

Посмотрела текущее состояние переключателей SELinux для Apache. Многие их них отключены (рис. -@fig:007).

![Состояние переключателей SELinux для Apache](../image/7.png){#fig:007 width=70%}

Посмотрела статистику по политике. Количество пользователей - 8, ролей - 14, типов - 4934 (рис. -@fig:008).

![Статистика по политике SELinux](../image/8.png){#fig:008 width=70%}

Определила тип поддиректорий, находящихся в директории /var/www. Тип каталога cgi-bin - httpd_sys_script_exec_t, тип каталога html - httpd_sys_content_t (рис. -@fig:009).

![Типы поддиректорий в директории /var/www](../image/9.png){#fig:009 width=70%}

 Исходя из прав доступа каталога /var/www/html, только суперпользователю разрешено создание файлов в нем. От имени суперпользователя создала файл test.html (рис. -@fig:010).

![Файл /var/www/html/test.html](../image/10.png){#fig:010 width=70%}

Контекст созданного файла - unconfined_u:object_r:httpd_sys_content_t:s0. Так
как по умолчанию пользователи CentOS являются свободными от типа, созданному файлу test.html был сопоставлен пользователь unconfined_u. Роль object_r используется по умолчанию для файлов на «постоянных» носителях и на сетевых файловых системах. Тип httpd_sys_content_t позволяет процессу httpd получить доступ к файлу. Благодаря наличию последнего типа можно получить доступ к файлу
при обращении к нему через браузер (рис. -@fig:011).

![Контекст файла test.html](../image/11.png){#fig:011 width=70%}

Обратилась к файлу через веб-сервер, введя в браузере адрес http://127.0.0.1/test.html (рис. -@fig:012).

![Доступ к файлу test.html через браузер](../image/12.png){#fig:012 width=70%}

Изменила контекст файла test.html на samba_share_t, к которому процесс httpd не должен иметь доступа (рис. -@fig:013).

![Изменение контекста файла test.html](../image/13.png){#fig:013 width=70%}

Снова попробовала получить доступ к файлу через браузер, получила сообщение об ошибке(рис. -@fig:014).

![Сообщение об ошибке после смены конекста](../image/14.png){#fig:014 width=70%}

Посмотрела лог ошибок веб-сервера Apache и системный лог. В них появились записи о запрете доступа к файлу. В системном логе появилась информация о необходимости сменить тип файла test.html, чтобы демон httpd мог к нему обращаться(рис. -@fig:015, рис. -@fig:016).

![Лог ошибок Apache](../image/15.png){#fig:015 width=70%}

![Системный лог-файл](../image/16.png){#fig:016 width=70%}


## Изменение TCP-порта

В соотсветствии с новой политикой, порт 81 входит в список портов по умолчанию, поэтому я изменила порт с 80 на 82 в файле /etc/httpd/conf/httpd.conf (рис. -@fig:017).

![Изменение TCP-порта](../image/17.png){#fig:017 width=70%}

При перезапуске веб-сервера произошел сбой. В файле /var/log/messages появилась запись о запрете доступа через порт 82 и необходимости изменить тип порта (рис. -@fig:020). В файле /var/log/audit/audit.log появилась запись о неудачной попытке запуска веб-сервера (рис. -@fig:023). В файле /var/log/httpd/error_log есть запись только о завершении работы веб-сервера (рис. -@fig:021). В файле /var/log/httpd/access_log не появилось новых записей (рис. -@fig:022).

![/var/log/messages](../image/20.png){#fig:020 width=70%}

![/var/log/audit/audit.log](../image/23.png){#fig:023 width=70%}

![/var/log/httpd/error_log](../image/21.png){#fig:021 width=70%}

![/var/log/httpd/access_log](../image/22.png){#fig:022 width=70%}

Добавила порт 82 к списку портов http_port_t. После этого удалось запустить веб-сервер (рис. -@fig:024).

![Добавление 82 порта и перезапуск веб-сервера](../image/24.png){#fig:024 width=70%}

Вернула контекст httpd_sys_cоntent__t к файлу /var/www/html/ test.html и попробовала получить доступ к файлу через веб-сервер, введя в браузере  http://127.0.0.1:82/test.html (рис. -@fig:025).

![Доступ к файлу test.html через 82 порт](../image/25.png){#fig:025 width=70%}

Вернула порт 80 в конфигурационный файл, удалила привязку http_port_t к 82 порту и удалила файл /var/www/html/test.html (рис. -@fig:026, рис. -@fig:027).

![Восстановление исходных настроек файла httpd.conf](../image/26.png){#fig:026 width=70%}

![Восстановление исходных настроек](../image/27.png){#fig:027 width=70%}

# Вывод

Я развила навыки администрирования ОС Linux. 
Получила практическое знакомство с технологией SELinux.
Проверила работу SELinux на практике совместно с веб-сервером Apache.
