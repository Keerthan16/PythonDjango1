from django import template

register=template.Library()

@register.filter(name="lucky")
def luckyNumber(value,arg):
    name=(value.split())
    sum=0
    for x in name:
        sum+=len(x)*3
    sum+=arg
    print(sum)
    return str(sum)

#instead of decorator we can also use
#register.filter('luckyNumber',luckyNumber)
