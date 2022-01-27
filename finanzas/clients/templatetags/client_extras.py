from django import template

register = template.Library()

def date_format(date):
    mounths = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    return f'{date.day} {mounths[date.month - 1]} {date.year}'

   
def date_simple_format(date):
    return f'{date.day}/{date.month}/{date.year}'


register.filter('date_format', date_format)
register.filter('date_simple_format', date_simple_format)
