# Django Demo Setup

## Step 1: Create a Virtual Environment

Create a virtual environment to manage project dependencies in isolation.

```bash
python -m venv myenv
```

## Step 2: Activate the Virtual Environment

Activate the virtual environment.

- **Windows:**

  ```bash
  myenv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source myenv/bin/activate
  ```

## Step 3: Install Requirements

Install the required packages listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Step 4: Apply Database Migrations

Create migration files and apply them to the database.

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 5: Start the Server

Start the Django development server.

```bash
python manage.py runserver
```

Once these steps are completed, the Django project should be accessible at

`http://127.0.0.1:8000/`

in your web browser.
