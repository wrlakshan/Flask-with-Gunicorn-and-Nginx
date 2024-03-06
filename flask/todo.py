from flask import Flask, render_template, request, redirect, url_for
import os  # Import the os module


app = Flask(__name__)

# Accessing the APP_NAME environment variable with a default value
app_name = os.getenv('APP_NAME', 'DefaultAppName')

# This will store tasks in memory
tasks = [{"id": 1, "content": "Learn Flask"}, {"id": 2, "content": "Build a CRUD app"}]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, app_name=app_name)

@app.route('/add', methods=['POST'])
def add_task():
    if request.method == "POST":
        task_content = request.form['content']
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "content": task_content})
        return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = next((task for task in tasks if task["id"] == id), None)
    if request.method == 'POST':
        task['content'] = request.form['content']
        return redirect(url_for('index'))
    return render_template('update.html', task=task)

@app.route('/delete/<int:id>')
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
