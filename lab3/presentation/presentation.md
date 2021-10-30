---
## Front matter
lang: ru-RU
title: Отчет по лабораторной работе №3
author: Дерябина Мария
institute: RUDN University, Moscow, Russian Federation
date: 2021

## Formatting
mainfont: Times New Roman
romanfont: Times New Roman
sansfont: Times New Roman
monofont: Times New Roman
toc: false
slide_level: 2
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

## Цель работы

Получить практические навыки работы в консоли с атрибутами файлов для групп пользователей


## Задачи работы

1. Научиться добавлять пользователей в группу.
2. Заполнить таблицу, сопоставляющую различные действия и права доступа для группы.
3. Выявить минимальные необходимые права доступа для различных действий в системе для группы.

## Выполнение. Добавление пользователя в группу

В установленной операционной системе создала пользователя guest2 аналогично пользователю guest, созданному во 2 лабораторной. Добавила пользователя guest2 в группу guest.

![Создание пользователя guest2 и добавление в группу](../image/1.png){#fig:001 width=70%}

## Информация о пользователях

Осуществила вход в систему от двух пользователей на двух разных консолях: guest на первой консоли и guest2 на второй консоли.

Уточнила имена пользователей, командой groups определила, в какие группы входят пользователи.

![Информация о группах пользователя guest](../image/4.png){#fig:002 width=70%}

## Изменение прав доступа

От имени пользователя guest2 выполнила регистрацию пользователя guest2 в группе guest командой newgrp guest.

От имени пользователя guest изменила права директории /home/guest, разрешив все действия для пользователей группы. От имени пользователя guest сняла с директории /home/guest/dir1 все атрибуты.

![Изменение прав доступа для dir1](../image/5.png){#fig:003 width=70%}

## Изменение прав доступа

![Проверка снятия атрибутов](../image/8.png){#fig:004 width=70%}

## Таблица «Установленные права и разрешённые действия для групп]»

![](../image/9.png){#fig:007 width=70%}

## Таблица «Установленные права и разрешённые действия для групп]»

![](../image/10.png){#fig:008 width=70%}

## Таблица «Минимальные права для совершения операций для групп]»

![](../image/11.png){#fig:009 width=70%} 

## Выводы

Я получила практические навыки работы в консоли с атрибутами файлов и каталогов для групп пользователей.
