from django import template
from web.models import StaticPages
from uawp import settings


register = template.Library()

#@register.inclusion_tag('_menu.html', takes_context=True)
#def menu(context):
#    context['get_static_pages'] = Static_pages.objects.filter(show_in_menu=True)
#    return context

@register.inclusion_tag('_nav.html', takes_context=True)
def navigation(context):
    context['get_static_pages'] = StaticPages.objects.filter(show_in_menu=True)
    return context
