# flask-example

## Install

```bash
  $ virtualenv venv

  $ source venv/bin/activate

  $ pip install -r requirements.txt
```

&nbsp;

## Start

```bash
  $ cd app

  $ python app.py
```

&nbsp;

## Migration

```bash
  $ cd app

  # if not exists 'migrations' folder
  $ python manage.py db init

  # if changed or added something model
  $ python manage.py db migrate

  # after 'migrate' command
  $ python manage.py db upgrade
```
