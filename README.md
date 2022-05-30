# Steps to Deploy a NextJs and Flask on Heroku

## Step 1.
In **package.json** file of your nextjs app replace the code with below written code
from:
```sh
"scripts": {
 "build": "next build "
}
```
to:
```sh
"scripts": {
  "build": "next build && next export"
}
```
"next export" allows you to export your Next.js application to static HTML, which can be run standalone without the need of a Node.js server.

## Step 2.
In **next.config.js** file add the following code:
```sh
module.exports = {
  images: {
    loader: 'akamai',
    path: '/',
  },
}
```

## Step 3.
Run the following command in frontend folder:
```sh
npm run build 
```
Output will be generated in **/frontend/out**   folder. 
"next export" builds an HTML version of your app. During next build, getStaticProps and getStaticPaths will generate an HTML file for each page in your pages directory (or more for dynamic routes). Then, "next export" will copy the already exported files into the correct directory. getInitialProps will generate the HTML files during next export instead of next build.

## Step 4.
Make the following changes in **app.py** file of flask app:
```sh
app = Flask(__name__, static_url_path='/', static_folder='./frontend/out')
```

## Step 5.
Add the routes in **app.py** :
```sh
@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(err):
    return app.send_static_file('404.html')
```
It looks for html pages generated in step 3 command in **out/** directory in Step 3.

## Step 6.
Remove the following from **.gitignore** file:
```sh
/build
/.next/
/out/
.next
```

## Step 7.
Make sure to add **gunicorn** in your **requirements.txt** file

## Step 8.
Create **Procfile** in root directory and add the following in it:
```sh
web:  gunicorn app:app
```

## Step 9.
Add a **favicon.ico** file in **/frontend/out/** folder to display the icon for your website.

## Step 10.
Push your code to heroku

*** 
The End
