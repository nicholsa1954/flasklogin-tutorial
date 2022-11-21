# Flask-Login Tutorial

![Python](https://img.shields.io/badge/Python-v^3.9-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v2.1.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Login](https://img.shields.io/badge/Flask--Login-v0.6.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-WTF](https://img.shields.io/badge/Flask--WTF-v1.0.0-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-v2.5.1-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/flasklogin-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/flasklogin-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/flasklogin-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/flasklogin-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/flasklogin-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/flasklogin-tutorial/network)

![Flask Login](https://raw.githubusercontent.com/toddbirchard/flasklogin-tutorial/master/flask_login_tutorial/static/dist/img/flasklogin%402x.jpg)

Add user authentication to your Flask app.

Other resources:
    Unit testing: https://testdriven.io/blog/flask-pytest/
    Template inheritance: http://exploreflask.com/en/latest/templates.html
    Multi-page apps: https://dash.plotly.com/urls (see the section on "Multi-Page Apps Without Pages")
	Navbars and controls:
		https://www.w3schools.com/howto/howto_css_dropdown_navbar.asp
    General on flask: 
        http://exploreflask.com/en/latest/
	Tables:
		https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates
		https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
    General Flask development, intro course:
        https://pythonhow.com/python-tutorial/flask/web-development-with-python-and-flask/



* **Tutorial**: https://hackersandslackers.com/flask-login-user-authentication/
* **Demo**: https://flasklogin.hackersandslackers.app

## Getting Started

Get set up locally in two steps:

### I. Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.
* `LESS_BIN`: Path to your local LESS installation via `which lessc` (optional for static assets).
* `ASSETS_DEBUG`: Debug asset creation and bundling in `development` (optional).
* `LESS_RUN_IN_DEBUG`: Debug LESS while in `development` (optional).
* `COMPRESSOR_DEBUG`: Debug asset compression while in `development` (optional).

*Remember never to commit secrets saved in .env files to Github.*

### II. Installation

Get up and running with `make deploy`:

```shell
$ git clone https://github.com/toddbirchard/flasklogin-tutorial.git
$ cd flasklogin-tutorial
$ make deploy
``` 

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
