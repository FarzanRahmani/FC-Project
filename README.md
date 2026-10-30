# Art Blog: Fundamentals of Computer Programming Project

A Django web project by Farzan Rahmani, created for the Fundamentals of Computer Programming course. The application presents art-related pages for books, poems, and music, with database models for user-submitted entries.

## Features and Structure

| Path | Purpose |
| --- | --- |
| `Proj/manage.py` | Django management command entry point |
| `Proj/Proj/` | Project settings, root URL configuration, and WSGI/ASGI entry points |
| `Proj/Blog/` | Views, routes, templates, models, admin registration, and migrations |
| `Proj/requirements.txt` | Original dependency pins, including Django 3.1.4 |
| `new_env/` | Historical environment directory; create a fresh local environment for use |

The blog defines routes for `art/`, `books/`, `poems/`, and `musics/`. SQLite is configured as the local database.

## Local Development

Use a Python version compatible with the original Django and package pins. These dependencies date from 2020, so installing them on a recent Python release may require compatibility work.

Create and activate a virtual environment, then run from the repository root:

```sh
python -m pip install -r Proj/requirements.txt
python Proj/manage.py migrate
python Proj/manage.py runserver
```

Open <http://127.0.0.1:8000/blog/art/>. To manage records through Django admin, first create an administrator account:

```sh
python Proj/manage.py createsuperuser
```

The development database is created by migrations; historical website content is not automatically recreated by installing dependencies.

## Project Status

The original hosted address is <https://99521271.pythonanywhere.com/blog/art/>. It is retained as a project reference, and its availability is not guaranteed.

The checked-in settings are for coursework and development, including debug mode and permissive allowed hosts. A public deployment needs its own production settings and a supported dependency stack.

## License

See [LICENSE](LICENSE) for license terms.
