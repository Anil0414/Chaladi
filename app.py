from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory database to store the to-do items
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_item = request.form.get('todo')
    if todo_item:
        todos.append(todo_item)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
