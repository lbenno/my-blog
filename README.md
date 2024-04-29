

# How to deploy

## Push to GitHub


```bash
git status
git add .
git status
git commit -m "<insert message>"
git push
```



## Deploy to the Web
Open PythonAnywhere

Open the bash console 

#### Pull from Github to PythonAnywhere

```bash
cd lbenno.pythonanywhere.com
git pull
```


#### Load static files to PythonAnywhere

```bash
python manage.py collectstatic
```


#### Run Migrations in PythonAnywhere

Ensure migrations were made before the git pull into Pythonanywhere.

```bash
python manage.py makemigrations
python manage.py migrate
```

Then, from Pythonanywhere
```bash
python manage.py migrate
```

#### Deploy to the Web

Got to the 'Web' section of PythonAnywhere and click <span style="background-color: navy;">'Reload lbenno/pythonanywhere.com'<span>