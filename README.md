# todo-api 📃

A todo API service.

## Local development

The python version used is 3.11.2.

### Using `docker`:

1. Clone the repo

2. cd todo-api
3. touch .env
4. Add the following to .env

   ```.env
   SQLALCHEMY_DATABASE_URI=sqlite:///todo.db
   SQLALCHEMY_TRACK_MODIFICATIONS=False
   PROPAGATE_EXCEPTIONS=True
   ```

5. `docker compose up`

### Using `pipenv`:

1. Clone the repo

2. cd todo-api
3. touch .env
4. Add the following to .env

   ```.env
   SQLALCHEMY_DATABASE_URI=sqlite:///todo.db
   SQLALCHEMY_TRACK_MODIFICATIONS=False
   PROPAGATE_EXCEPTIONS=True
   ```

5. pipenv install to install all the dependencies
6. pipenv run python app.py

If using venv or similar, then create your virtual environment and clone the repo in it.
Then you can install the dependincies using `pip install -r requirements.txt` and then run the app using `python app.py`.

## Examples

### Create new todos

```
curl http://localhost:5000/todo/ -d "content=somethingtodo" -X PUT -v
```

### List all todos

```
curl http://localhost:5000/todo/ -X GET -v
```

### See a todo

```
curl http://localhost:5000/todo/<id> -X GET -v
```

### Update todo content

```
curl http://localhost:5000/todo/<id> -d "content=somethingnewtodo" -X POST -v
```

### Delete todo

```
curl http://localhost:5000/todo/<id> -X DELETE -v
```

### Toggle todo check

```
curl http://localhost:5000/todo/<id> -X PATCH -v
```
