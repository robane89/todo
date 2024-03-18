Project: Todo List

Features:
- Add new tasks with titles and descriptions
- Edit existing tasks
- Mark tasks as completed
- Delete tasks

Technical Details:
- Built with Django framework
- Utilizes Django's ORM for database management
- Follows the MVC (Model-View-Controller) pattern for structure
- Implements basic user interface using Django templates
- Uses HTML and CSS for styling the web interface

Installation:
1. Clone the repository:
   git clone https://github.com/robane89/todo.git

2. Navigate to the project directory:
   cd todo

3. Install the required dependencies (assuming you have Python and pip installed):
   pip install -r requirements.txt

4. Run the Django migrations to set up the database:
   python manage.py makemigrations
   python manage.py migrate

6. Start the Django development server:
   python manage.py runserver

7. Access the web application at http://localhost:8000 in your web browser.


8. list of endpoints.
   
    GET /tasks/
        Description: Retrieve a list of all tasks.
        Method: GET

    POST /tasks/add/
        Description: Add a new task.
        Method: POST
        Parameters: title (string), description (string)

    POST /tasks/edit/{task_id}/
        Description: Edit an existing task.
        Method: POST
        Parameters: task_id (integer), title (string), description (string)

    POST /tasks/complete/{task_id}/
        Description: Mark a task as completed.
        Method: POST
        Parameters: task_id (integer)

    POST /tasks/delete/{task_id}/
        Description: Delete a task.
        Method: POST
        Parameters: task_id (integer)

