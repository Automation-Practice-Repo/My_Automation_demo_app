from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Task
from datetime import datetime

# Blueprints
auth_bp = Blueprint('auth', __name__)
task_bp = Blueprint('task', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

# ==================== AUTH ROUTES ====================
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if not all([username, email, password, confirm]):
            flash('All fields are required', 'error')
            return redirect(url_for('auth.register'))

        if password != confirm:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('auth.register'))

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('task.dashboard'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('auth.login'))

# ==================== TASK ROUTES ====================
@task_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('task.dashboard'))
    return redirect(url_for('auth.login'))

@task_bp.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    stats = {
        'total': len(tasks),
        'completed': len([t for t in tasks if t.status == 'completed']),
        'pending': len([t for t in tasks if t.status == 'pending']),
        'in_progress': len([t for t in tasks if t.status == 'in_progress'])
    }
    return render_template('dashboard.html', tasks=tasks, stats=stats)

@task_bp.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority', 'medium')
        due_date = request.form.get('due_date')

        if not title:
            flash('Title is required', 'error')
            return redirect(url_for('task.new_task'))

        task = Task(
            title=title,
            description=description,
            priority=priority,
            user_id=current_user.id
        )

        if due_date:
            task.due_date = datetime.fromisoformat(due_date)

        db.session.add(task)
        db.session.commit()

        flash('Task created successfully', 'success')
        return redirect(url_for('task.dashboard'))

    return render_template('new_task.html')

@task_bp.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('task.dashboard'))

    if request.method == 'POST':
        task.title = request.form.get('title', task.title)
        task.description = request.form.get('description', task.description)
        task.priority = request.form.get('priority', task.priority)
        task.status = request.form.get('status', task.status)

        due_date = request.form.get('due_date')
        if due_date:
            task.due_date = datetime.fromisoformat(due_date)

        db.session.commit()
        flash('Task updated successfully', 'success')
        return redirect(url_for('task.dashboard'))

    return render_template('edit_task.html', task=task)

@task_bp.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('task.dashboard'))

    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully', 'success')
    return redirect(url_for('task.dashboard'))

# ==================== API ROUTES ====================
@api_bp.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    status = request.args.get('status')
    priority = request.args.get('priority')
    search = request.args.get('search')

    query = Task.query.filter_by(user_id=current_user.id)

    if status:
        query = query.filter_by(status=status)

    if priority:
        query = query.filter_by(priority=priority)

    if search:
        query = query.filter(Task.title.ilike(f'%{search}%'))

    tasks = query.all()
    return jsonify([task.to_dict() for task in tasks])

@api_bp.route('/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()

    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400

    task = Task(
        title=data['title'],
        description=data.get('description'),
        priority=data.get('priority', 'medium'),
        user_id=current_user.id
    )

    if data.get('due_date'):
        task.due_date = datetime.fromisoformat(data['due_date'])

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201

@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    return jsonify(task.to_dict())

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    task.priority = data.get('priority', task.priority)

    if data.get('due_date'):
        task.due_date = datetime.fromisoformat(data['due_date'])

    db.session.commit()
    return jsonify(task.to_dict())

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task_api(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted successfully'}), 200

@api_bp.route('/stats', methods=['GET'])
@login_required
def get_stats():
    tasks = Task.query.filter_by(user_id=current_user.id).all()

    return jsonify({
        'total': len(tasks),
        'completed': len([t for t in tasks if t.status == 'completed']),
        'pending': len([t for t in tasks if t.status == 'pending']),
        'in_progress': len([t for t in tasks if t.status == 'in_progress']),
        'high_priority': len([t for t in tasks if t.priority == 'high'])
    })
