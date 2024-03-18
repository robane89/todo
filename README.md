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

Usage:
- Upon accessing the web application, you will see a list of tasks if any are present.
- To add a new task, click on the "Add Task" button and fill out the form.
- To edit a task, click on the "Edit" button next to the task you want to modify.
- To mark a task as completed, click on the "Mark as Completed" button next to the task.
- To delete a task, click on the "Delete" button next to the task.

