# Взлом электронного журнала успеваемости

Скрипт позволяет самовольно вносить изменения в школьный электронный журнал успеваемости [devman](https://dvmn.org).

## Перед запуском

Скрипт включает себя **3** функции, которые способны выполнить определенные действия в электронном журнале:
1. `fix_marks` исправляет все "двойки" и "тройки" на "пятерки" у конкретного учащегося.
2. `remove_chastisements` удаляет из базы электронного журнала все замечания от учителей, относящиеся к конкретному учащемуся.
3. `create_commendation` вносит одну похвалу от учителя по конкретному предмету для конкретного учащегося. Похвала будет записана к последнему проведенному по этому предмету уроку.

## Как запустить
Перед запуском скрипта откройте [электронный дневник школы](https://github.com/devmanorg/e-diary/tree/master).

Откройте окно коммандой строки и зайдите в **shell**:
```
$python manage.py shell
```

Откройте `script.py` в любом текстовом редакторе, скопируйте его содержимое и вставьте в **shell**:
```
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
>>> from datacenter.models import Schoolkid, Mark, Subject, Lesson, Chastisement, Commendation
>>>
    ...
>>>...         pass
...
```

Пример запуска комманд скрипта:
```
>>> fix_marks('Фролов Иван')
>>>

>>> remove_chastisements('Фролов Иван')
>>>

>>> create_commendation('Фролов Иван', 'Математика', text='Чертит идеальные биссектрисы')
>>>

>>> fix_marks('Степан')
Найдено более одного ученика        #действие не выполнится
>>>
>>> remove_chastisements('George Gordon Byron')
Ученика с таким именем нет в базе          #действие не выполнится
>>>
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и Django на сайте [devman](https://dvmn.org).

