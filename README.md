# django-user-model-options
Repo with in-depth coverage of high level concepts from a poster session I did at PyCon 2017 in Portland, OR, May 21, 2017.

An in-depth discussion of each of the three options I presented for customizing the Django User model can be found in [this blog post](https://medium.com/agatha-codes/options-objects-customizing-the-django-user-model-6d42b3e971a4) on [_Agatha_](https://medium.com/agatha-codes), a blog I started to share some of the problem solving I've had to do when working on my software projects.

All of these projects use Django 1.11, Python 3.5.2 and the default SQLite3 database.

Each project in this repo covers one of the three options and stands on its own.  To run a project:

- Navigate to the relevant repo and clone it

- Create a Python3 virtual environment `python3 -m venv myvenv`

- Install the requirements.txt file `pip install -r requirements.txt`

- Create a superuser `python manage.py createsuperuser` and complete the prompts

- Start the server with `python manage.py runserver`

- To try the form, navigate to `localhost:8000` in your browser

- To try the admin interface, navigate to `localhost:8000/admin` in your browser and sign in with the credentials you entered when you ran the `createsuperuser` command

If you have any comments, questions or problems with the examples, please create an issue in this repo.

Thanks for visiting!!
