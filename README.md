## Tree view menu
* [RU Task](Task.md)

### How to use

1. Install all libraries `pip3 install -r requirements.txt`
2. Setup PostgreSQL and change the DATABASE config in [settings.py](menu_app/menu_app/settings.py)
3. Migrate `python manage.py makemigrations` and `python manage.py migrate`
4. Make a superuser `python manage.py createsuperuser` and run server `python manage.py runserver`
5. Open [http://127.0.0.1:8000/admin/main_menu/menustep/](http://127.0.0.1:8000/admin/main_menu/menustep/) and add your first menu row.
6. Use children field to add rows that goes under the main row and do not forget the Parent for children(The root row should set Parent as None)
7. Make your template and load the templatetags `load draw_menu`
8. Use `{% draw menu "<menu_name" %}` to show your menu
9. Go to [http://127.0.0.1:8000/make_example](http://127.0.0.1:8000/make_example) to make an example menu
