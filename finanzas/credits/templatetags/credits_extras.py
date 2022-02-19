from django import template

def startswith(text, value):
    return text.startswith(value)


register = template.Library()
register.filter('startswith', startswith)