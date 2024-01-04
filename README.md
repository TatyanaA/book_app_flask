# Book Application
## Setup

- Clone the repository to your computer:
```bash
git clone git@github.com:TatyanaA/book_app_flask.git
```
- Enter to the folder with clonned repo:

```bash
cd `path_to_your_folder`
```

- Open the application in VScode
```bash
code .
```  
- Install packages: 
```bash
pip install pipenv
pipenv shell
pipenv install 
pipenv install flask flask-cors
pipenv install python-dotenv 
pipenv install flask-sqlalchemy psycopg2-binary
```
- Create .env
```bash
touch .env
```
- Add to the .env file 
    SQLALCHEMY_DATABASE_URI=<link to your DB>
    FLASK_DEBUG=
- Seed the database: 
```bash
python seed.py
```
-Run the app
```bash
python app.py
```
You can see the app here:
`http://localhost:4000/`

## Endpoits

"GET /books" - show list of books
"GET /books/<int:id>", - show the book with choosen id
"POST /books", - create a new book (use `https://hoppscotch.io/`)
"PATCH /books/<int:id>", - update book's parameters (use `https://hoppscotch.io/`)
"DELETE /books/<int:id>" - delete the book with id (use `https://hoppscotch.io/`)


