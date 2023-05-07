from django.shortcuts import render, redirect

from .models import MenuStep
# Create your views here.


def render_menu(request):
    return render(request, "your_html.html", request.GET)


def make_example(request):
    step1 = MenuStep()
    step1.Name = "Step 1"
    step1.menu_name = "menu_1"
    step1.save()
    step1.make_children("Step 2")
    step3 = step1.make_children("Step 3")
    step3.make_children("Stpe 3.1")
    step3.make_children("Stpe 3.2")

    return redirect(render_menu)
