# Web App Setup - Vue.js + FastAPI + Postgres
## Overview
This guide will walk you through the process of setting up a frontend and backend web app. To follow this guide accurately it is highly recommended to reproduce the development environment exactly as to minimize any installation issues.

This guide relies on some level of competency utilizing Linux based operating systems. For more help check out - [Ubuntu Basics](https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal "https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal")

---

## Section 1: Development Environment Setup
### 1.1 **Windows**
1. Visual Studio Code - [VSCode download](https://code.visualstudio.com/download "https://code.visualstudio.com/download")
2. Windows Terminal - [Windows Terminal download](https://www.microsoft.com/store/productId/9N0DX20HK701 "https://www.microsoft.com/store/productId/9N0DX20HK701")
3. Windows Subsystem for Linux (WSL2) - [WSL2 Setup](https://docs.microsoft.com/en-us/windows/wsl/install "https://docs.microsoft.com/en-us/windows/wsl/install")
4. Ubuntu - [Ubuntu download](https://www.microsoft.com/store/productId/9PDXGNCFSCZV "https://www.microsoft.com/store/productId/9PDXGNCFSCZV")

### 1.2 **Ubuntu**
From terminal run the following commands:
1. `sudo apt update`
2. `sudo snap install --classic code`

### 1.3 **Mac**
No steps at this time, however following along the linux instructions will more than likely get everything setup correctly. 

### 1.4 **VirtualBox**
1. Download VirtualBox - [VirtualBox](https://www.virtualbox.org/wiki/Downloads "https://www.virtualbox.org/wiki/Downloads")
2. Download Ubuntu - [Ubuntu](https://ubuntu.com/download/desktop "https://ubuntu.com/download/desktop")
3. Run Virtualbox and select "New".
4. Add name
5. Under "Type" select "Linux".
6. Under "Version" select "Ubuntu(64-bit)"
7. Increase Memory size to 2048
8. Create
9. Increase disk size to 25GB
10. Create
11. Goto Settings > System > Processor - increase to 2.
12. Goto Settings > Display > Video memory - increase to 64mb or 128mb
13. Goto Settings > Storage - Click the disk icon that says "Empty".
14. Click the other disk icon on the right and browse to the Ubuntu image just downloaded.
15. Click "OK"
16. Click "Start"
17. "Try or install Ubuntu"
18. Install Ubuntu - Can use all default prompts from here

### 1.5 **VS Code Extensions**
There are several extensions that will all for better development practice that can be installed from within VS Code. From the the extensions tab search and install the following.
1. ESLint
2. GitLens
3. HTML CSS Support
4. Prettier - Code Formatter
5. Python
6. Vue Language Features(Volar)

---

## Section 2: Project Folder Structure
### 2.1 **Setup Project Structure**
This is a basic project folder structure that will be used throughout the project. Git is also being setup at this phase so some familiarity with Git and its basic commands is advisable. - [Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository "https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository")

From the terminal run the following commands:
1. `sudo apt install git -y`
2. `git --version` - If there is a version number Git is installed.
3. `mkdir ~/projects ~/venv`
4. `cd ~/projects`
5. `mkdir new_project_name && cd new_project_name`
6. `mkdir backend`
7. `touch readme.md`
8. `git init`
9. `git branch -m main`

This will design the basic folder structure for a new project. It will also initialize the new project to use Git as a versioning control provision. 

---

## Section 3: Project Setup and Creation - Front End
### 3.1 **Front End Setup**
The frontend will use Vue.js as the Javascript framework and Bulma as the CSS framework. The following are required to setup the frontend
- Node.js - Server-side JS framework. Required for Vue
- npm - Node.js package manager
- Vue.js - Client-side JS framework
- Bulma - CSS framework

From the terminal run the following commands:
1. `sudo apt install nodejs npm -y`
2. `npm install -g @vue/cli`
3. `node --version && npm --version` - If there are version numbers Node and npm are installed.
4. `sudo npm install -g @vue/cli`
5. `vue --version` - If there is a version number Vue is installed.

### 3.2 **Front End Creation**
Ensure that you are in the new projects root directory before completing the steps below. For further information about Vue.js use their documentation. [Vue Docs](https://vuejs.org/guide/introduction.html "https://vuejs.org/guide/introduction.html")

3.2.1 **Vue Project Creation**
1. `vue create new_frontend_app`
2. Select the option to "Manually select features". Hit Enter.
3. Ensure the options "Babel" and "Linter/Formatter" are selected. Hit Enter.
4. Select Vue "3.x". Hit Enter.
5. Select "ESLint + Prettier". Hit Enter.
6. Select "Lint on Save". Hit Enter.
7. Select "In package.json". Hit Enter.
8. Save as preset. User can decide if they wish to save preset.<br/>
*Note: Vue will take a moment to generate the project. If any errors occur during the creation process they will need to be addressed prior to moving forward.*
9. `cd new_frontend_app`
10. `npm run serve`
11. Open a browser and go to "localhost:8080". Vue will have some boilerplate displayed.
12. Press `ctrl -c` to cancel the app server. 

3.2.2 **Vue Project Clean-up**
1. Type `sudo rm -rf .git` from within the Vue project folder. This will delete the git repo that Vue created.
2. Type `code .` from within the Vue project folder. This will open the project in VS Code.
3. Under new_frontend_app > src > assets - delete logo.png
4. Under new_frontend_app > src > components - Rename "HelloWorld.vue" to "HomeComp.vue" and remove all of the code from within the "template" element. Also, delete the "script" and "style" blocks.
5. Insert a "div" under "template" and add "HomeComp" as the text.
6. Under new_frontend_app > src > App.vue anywhere it says "HelloWorld" replace with "HomeComp"
7. Delete "img" element
8. Remove "msg" from "HomeComp" element
9. Delete "style" block
10. Run `npm run serve` and refresh page in browser to see changes.

### 3.3 **Bulma Installation and Setup**
The next steps will go over how to install Bulma and configure it for customization. 

1. From within new_frontend_app root folder run: `npm install --save-dev node-sass sass-loader bulma`
2. After installation is complete check package.json to ensure all three packages are now installed.
3. Within the `assets` folder create a file called `mystyles.scss`
4. In `mystyles.scss` add `@import "~bulma"`. This will import the default styling Bulma offers. If custom styling is desired, the following code must be used instead. This is an example of how to modify themes. Use Bulma's documentation for further information. [Bulma Docs](https://bulma.io/documentation/ "https://bulma.io/documentation/")
    
        // @import "~bulma"

        @charset "utf-8";

        // Import a Google Font
        @import url("https://fonts.googleapis.com/css?family=Nunito:400,700");

        // Set your brand colors
        $purple: #8A4D76;
        $pink: #FA7C91;
        $brown: #757763;
        $beige-light: #D0D1CD;
        $beige-lighter: #EFF0EB;

        // Update Bulma's global variables
        $family-sans-serif: "Nunito", sans-serif;
        $grey-dark: $brown;
        $grey-light: $beige-light;
        $primary: $purple;
        $link: $pink;
        $widescreen-enabled: false;
        $fullhd-enabled: false;

        // Update some of Bulma's component variables
        $body-background-color: $beige-lighter;
        $control-border-width: 2px;
        $input-border-color: transparent;
        $input-shadow: none;

        // Import only what you need from Bulma
        @import "~bulma/sass/utilities/_all.sass";
        @import "~/node_modules/bulma/sass/base/_all.sass";
        @import "~/node_modules/bulma/sass/base/_all.sass";
        @import "~/node_modules/bulma/sass/elements/button.sass";
        @import "~/node_modules/bulma/sass/elements/container.sass";
        @import "~/node_modules/bulma/sass/elements/title.sass";
        @import "~/node_modules/bulma/sass/form/_all.sass";
        @import "~/node_modules/bulma/sass/components/navbar.sass";
        @import "~/node_modules/bulma/sass/layout/hero.sass";
        @import "~/node_modules/bulma/sass/layout/section.sass";

5.  Open `main.js` and add the following under the last import. `require("@/assets/mystyles.scss")` 
6.  Add the code below to the "template" section in "HomeComp"
   
        <body>
            <h1 class="title">
                Bulma
            </h1>

            <p class="subtitle">
                Modern CSS framework based on <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox">Flexbox</a>
            </p>

            <div class="field">
                <div class="control">
                <input class="input" type="text" placeholder="Input">
                </div>
            </div>

            <div class="field">
                <p class="control">
                <span class="select">
                    <select>
                    <option>Select dropdown</option>
                    </select>
                </span>
                </p>
            </div>

            <div class="buttons">
                <a class="button is-primary">Primary</a>
                <a class="button is-link">Link</a>
            </div>
        </body>

7. `npm run serve` - Check for changes in styling.
---

## Section 4: Project Setup and Creation - Back End
### 4.1 **Back End Setup**
The backend will use Python as the primary language and pip as the package manager. The project will also utilize python virtual environments to containerize the packages that will be used. 
- Python3 - Scripting language used to write code
- Pip - Python package manager
- Virtualenv - Python virtual environment manager


1. `python3 --version` - If there is a version number Python is installed. If Python isn't installed follow the steps below.
   1. `sudo apt install software-properties-common`
   2. `sudo apt-add-repositrory ppa:deadsnakes/ppa`
   3. `sudo apt update`
   4. `sudo apt install python3.10`
2. `sudo apt install python3-pip`
3. `pip --version` If there is a version number pip is installed.
4. `sudo apt install python3.10-venv`

### 4.2 **Back End Creation**

4.2.1 **Pip Virtual Environment**
FastAPI will be used a microservice framework for the API connection between the frontend and backend. Postgres will be used as the database.
- FastAPI - Microservice framework to create APIs
- PostgresSQL - Database library
- Virtualenv - Python virtual environment manager

1. `python3.10 -m venv ~/venv/[name_of_enviroment]` - This will create a python virtual environment.
2. `source ~/venv/[name_of_enviroment]/bin/activate` - This will activate the environment.
3. `cd ~/projects/backend`
4. `touch app.py setup.py requirements.txt .gitignore`
5. In VS code browse to backend project
6. Add the following to "requirements.txt"

        FastAPI
        Uvicorn[standard]
        Jinja2
        Sqlalchemy
        Sqlalchemy-utils
        Pydantic
        Psycopg2-binary
7. `pip install -r requirements.txt` - Ensure no errors occurred.
8. `pip list` - This will show all installed python packages for the active environment

4.2.2 **Python Structure**

1. Add the following code to "setup.py"

        import os

        directories = ['api','core','crud','database','models','schemas','tests']

        for dir in directories:
            path = f'./{dir}'
            os.mkdir(dir)

            file = f'{dir}.py'
            file2 = '__init__.py'

            open(os.path.join(path, file),'w')
            open(os.path.join(path, file2),'w')
            
        
2. `python3 setup.py` - This will create a base project structure. This is entirely personal preference on how to structure a python web app project, however these are some "best practices" as per community and documentation guidelines.

4.2.3 **Run server**
1. Add the following code to "app.py".
   
        import uvicorn
        from fastapi import FastAPI

        app = FastAPI()

        @app.get('/')
        async def root():
            return {'message':'backend'}

        if __name__ == '__main__':
            uvicorn.run('app:app', host='127.0.0.1',port=5000,reload=True)

2. `uvicorn app:app` - This will launch the FastAPI server.
3. Browse to `localhost:8000` - The page should display message : "backend"

---

## Section 5: Database
This section will go over the setup and creation of a Postgres database. This section is not required for the web app to work correctly, however to store any type of data this section must be completed. 

### 5.1 **DB install**
1. `sudo apt install postgresql postgresql-contrib` - This will download Postgres and its required pacakages.
2. `sudo service postgresql start` - This will start the service for postgresql
3. `sudo nano /etc/postgresql/14/main/postgresql.conf` - This file needs to be edited to allow for communication between backend app and DB.
4. Uncomment `listen address="localhost"`
5. Replace "localhost" with "*"
6. `sudo service postgresql restart` - Allow for changes to be updated
7. `sudo service postgresql status` - Check to ensure server comes back online.

### 5.2 **User Creation**
This section will create a user that will connect from with the Python app to manage the DB.
1. `sudo -u postgres psql` - Login as admin
2. `CREATE USER [new_user] PASSWORD ['new_user_password'];CREATEDB;`
3. `\q` - Exit DB as admin
4. `psql -U [new_user] -h 127.0.0.1 -d postgres` - Login as newly created user.
5. `\q` - Exit DB as new user

### 5.3 **Database Creation**
1. `sudo -u [new_user] psql` - Login as admin
2. `CREATE DATABASE [new_db]` - Create new DB.
3. `\c` - Connect to newly created DB.
4. `CREATE TABLE IF NOT EXISTS test(id serial, connection varchar(100));` - Create new table.
5. `INSERT INTO test VALUES(default, 'Successfully Connected');` - Fill with test data.
6. `\q` - Log out.

### 5.4 **Python DB Setup**
1. In VS Code edit database > database.py with the following code. The username and password in this file need to be the same of that created for the DB in the above steps.

        from sqlalchemy import create_engine
        from sqlalchemy_utils import database_exists, create_database

        class DBConnection:

        def __init__(self) -> None:
                self.creds = {
                    'pguser':'test',
                    'pgpasswd':'test',
                    'pghost':'localhost',
                    'pgport':5432,
                    'pgdb':'test'
                }

        def get_engine(self,user, password, host, port, db):
            url = f'postgresql://{user}:{password}@{host}:{port}/{db}'

            if not database_exists(url):
                create_database(url)

            engine = create_engine(url, pool_size=50, echo=False)

            return engine    

2. Add the following code to app.py. This will test the db connection when browsing to the /test uri. If connection is successful "true" will be displayed in the browser.

        @app.get('/test')
        async def test():
            dbconn = DBConnection()

            engine = dbconn.get_engine(
                dbconn.creds['pguser'],
                dbconn.creds['pgpasswd'],
                dbconn.creds['pghost'],
                dbconn.creds['pgport'],
                dbconn.creds['pgdb']
            )
            print(engine.has_table('test'))
            return(engine.has_table('test'))

---

## Section 6: Troubleshooting
### 6.1 **Front End Issues**
1. "Parsing error: No babel config file detected." - This error will be produced by ESLint sometimes when then the frontend project isn't the root directory. 
   1. Press `ctrl+,` to open settings
   2. Search `ESlint`
   3. On that page look for "Edit in settings.json"
   4. Add the following code block
    

            "eslint.workingDirectories" : [
                    {"mode":"auto"}
            ],


### 6.2 **Back End Issues**
1. Unknown Python intrepreter - This issue occurs when using VS Code in conjunction with a python virtual environment. 
   1. `ctrl+shift+p` - This will open the command palette
   2. Search for `Python: Select Interpreter`
   3. "Enter interpreter path.." - then browse to "~/venv/[name_of_environment]/bin/python3.10"

### 6.3 **General Issues**
1. Process already running on "localhost:XXXX" - This will occur sometimes when restarting the app servers for both the frontend and backend applications.
   1. `ps aux | grep -i "name of process"` - vue, fast, uvicorn are good search criteria.
   2. Once the process has been found the first number from the left is the PID. Take note of this number.
   3. `sudo kill -9 [PID from step 2]`
   4. Restart server

[Github](https://github.com/thomape/web_app_tutorial "https://github.com/thomape/web_app_tutorial")