

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



#### Deploy to the Web