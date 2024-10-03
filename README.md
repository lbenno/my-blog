# How to run in terminal

## Run virtual environment 

```bash
source myvenv/bin/activate
```

## Start the app  

```bash
python3 manage.py runserver
```

## If the site displays without formattng 
It means DEBUG is set to False. 
Try uncommenting 'DEBUG = True' in the settings.py file and rerun the app. 
If formatting reappears, re-comment-out the setting and let the os.environ check run. 



## To Run files and functions in the shell

```bash
python3 manage.py shell

>>> from { file_name } import { function/Class/etc }
>>> print(function())
>>> exit()
```


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