from django import template
from django.template.loader import render_to_string
from ..models import MenuStep


register = template.Library()
active_steps = []


@register.simple_tag(takes_context=True, name="draw_menu")
def draw_menu(context, menu_name):
    active_steps.clear()

    if menu_name in context:
        active_menu = MenuStep.objects.filter(id=int(context[menu_name][0])).first()
        if active_menu is None:
            menu = MenuStep.objects.filter(menu_name=menu_name, parent=None).first()
        else:
            menu = make_active(active_menu)
    else:
        menu = MenuStep.objects.filter(menu_name=menu_name, parent=None).first()

    return render_to_string('menu.html', {"menu": menu, "active_steps": active_steps})


def make_active(step: MenuStep):
    active_steps.append(step.id)
    if isinstance(step.parent, MenuStep):
        return make_active(step.parent)

    return step
