# Flask SQLAlchemy Demo

A little Demo how SQLAlchemy works together with Flask, Postgres and Python.

I spent waay too long because of the following error:

```
This typically means that you attempted to use functionality that needed the current application. To solve this, set up an application context with app.app_context().  See the documentation for more information.
```

Instead of using Ipython I used the `flask shell` command. This way I can use the `app.app_context()` function and I can use the `db` object.

## Instructions

start the virtual environment

Go to Terminal and type:

1. flask shell
2. db.create_all()

Now you can use the db object and create new entries in the database.
