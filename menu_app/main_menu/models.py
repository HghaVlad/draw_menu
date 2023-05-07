from django.db import models
# Create your models here.


class MenuStep(models.Model):

    id = models.AutoField(models.IntegerField, primary_key=True)
    Name = models.CharField(max_length=100)
    menu_name = models.CharField(max_length=100)
    parent = models.ForeignKey("main_menu.MenuStep", blank=True, null=True, on_delete=models.CASCADE, related_name="myparent")
    children = models.ManyToManyField("main_menu.MenuStep", related_name="mychildren", blank=True, null=True)

    def make(self, parent, child_name: str):
        self.parent = parent
        self.Name = child_name
        self.menu_name = parent.menu_name

    def make_children(self, child_name: str):
        new_menu_step = MenuStep()
        new_menu_step.make(self, child_name)
        new_menu_step.save()
        self.children.add(new_menu_step)
        return new_menu_step
