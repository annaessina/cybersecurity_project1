 ## SPA SERVICE
This application allows a user to input data on SPA (kylpylä) into the database.
First, a user has to create an account.
Once this is done, the user may input data on SPA such as name, address, city,
categories, give a grade and write comments/reviews.
 
## APPLICATION FUNCTIONS
The users can register a new account or log in.
Once the users are logged in, they can leave comments or reviews.
Anyone can view reviews and comments.
 
## SETUP INSTRUCTIONS
Locally, you can get the application running as follows (Linux and macOS):
1. Clone the repository to your computer and navigate to the flask directory.
2. Create a .env file and define its contents as follows:
```bash
DATABASE_URL=postgresql:///<database-name>
SECRET_KEY=<secret-key>
```
- where the database name is name set by the user.
- The secret key can be generated using the following commands:
```bash
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```
3. Activate the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
or (Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```
If you encounter the following error:
```bash
.\venv\Scripts\Activate : File C:\Users\user\csb\flask\venv\Scripts\Activate.ps1 cannot be loaded because
running scripts is disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\venv\Scripts\Activate
+ ~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo : SecurityError: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess
```
Run PowerShell as an administrator and check the current execution policy by running:
```bash
Get-ExecutionPolicy
```
The current policy is likely set to "Restricted." To enable script execution for the current user (which will allow you to activate the virtual environment), run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Now you should be able to activate the virtual environment in the flask folder by running:
```bash
.\venv\Scripts\activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Start the database in another terminal window (on Windows run it in Git Bash):
```bash
start-pg.sh
```
6. In the original terminal window, execute the following:
```bash
$ psql
user=# CREATE DATABASE <database-name>;
```
- where the database name is the same as the one you defined in step 2.
7. Define the database schema:
```bash
psql -d <database-name> <schema.sql
```
- where the database name is the same as the one you defined in step 2.
8. Start the application:
```bash
flask run
``` 
