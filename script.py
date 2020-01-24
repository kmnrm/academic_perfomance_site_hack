from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Mark, Subject, Lesson, Chastisement, Commendation

def get_schoolkid(kid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid)
    except ObjectDoesNotExist:
        return print('Ученика с таким именем нет в базе')
    except MultipleObjectsReturned:
        return print('Найдено более одного ученика')
    return schoolkid


def fix_marks(kid):
    schoolkid = get_schoolkid(kid)
    try:
        marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
        marks.update(points=5)
    except AttributeError:
        pass


def remove_chastisements(kid):
    schoollkid = get_schoolkid(kid)
    try:
        chastisements = Chastisement.objects.filter(schoolkid=schoollkid)
        chastisements.delete()
    except AttributeError:
        pass


def create_commendation(kid, subject, text='Молодец!'):
    schoolkid = get_schoolkid(kid)
    try:
        lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=subject)
        lessons = lessons.order_by('date').reverse()
        lesson = lessons[:1].get()
        Commendation.objects.create(text=text, created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)
    except AttributeError:
        pass
