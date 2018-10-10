from app import app
from flask import render_template, request
from app.models import Todo, TodoForm
from datetime import datetime

@app.route('/')
def index():
    form = TodoForm(request.form)
    todos = Todo.objects.all().order_by('-id')
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST',])
def add():
    form = request.form
    #form = TodoForm(request.form)
    #if form.validate():
    content = form['content']
    print('content:',content)
    todo = Todo(content=content)
    todo.save()
    todos = Todo.objects.order_by('time')
    return render_template('index.html', todos=todos)

@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = request.form
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos)

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = request.form
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')