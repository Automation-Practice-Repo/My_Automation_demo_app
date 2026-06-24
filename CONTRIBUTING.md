# Contributing to My Auto Prac

Thank you for your interest in contributing to **My Auto Prac**! We welcome contributions from everyone. This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

---

## How to Contribute

### 1. Report Bugs

Found a bug? Please create an issue with:

- **Title**: Clear, descriptive title
- **Description**: Detailed explanation of the bug
- **Steps to Reproduce**: Clear steps to reproduce the issue
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: OS, Python version, browser (if applicable)
- **Screenshots**: If applicable

**Example Issue Template:**
```
Title: Login page shows 500 error with special characters in password

Description:
When entering a password with special characters like @#$%, the login page returns a 500 error.

Steps to Reproduce:
1. Go to login page
2. Enter email: test@example.com
3. Enter password: P@$$w0rd!
4. Click login
5. Error occurs

Expected: User should be logged in
Actual: 500 Server Error

Environment: macOS, Python 3.9, Chrome
```

### 2. Suggest Features

Have an idea? Open a feature request with:

- **Title**: Clear feature name
- **Description**: Detailed explanation
- **Use Case**: Why this feature is needed
- **Mockup/Example**: If applicable

**Example Feature Request:**
```
Title: Add task categories/tags

Description:
Users should be able to organize tasks with categories or tags.

Use Case:
I manage tasks across different projects and need to group them by project name.

Proposed Solution:
- Add a "category" field to Task model
- Add category filter in dashboard
- Show category as badge on task card
```

### 3. Improve Documentation

Documentation improvements are always welcome:

- Typos and grammar fixes
- Clearer explanations
- Additional examples
- Better formatting

---

## Development Setup

### Prerequisites
- Python 3.9+
- Git
- Virtual environment (venv)

### Setup Steps

1. **Fork the repository**
   ```bash
   # Go to https://github.com/Automation-Practice-Repo/My_Automation_demo_app
   # Click "Fork" button
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/My_Automation_demo_app.git
   cd my_auto_prac
   ```

3. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

5. **Create development branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

6. **Make your changes**
   - Follow the code style guidelines
   - Write clear, descriptive commit messages
   - Test your changes thoroughly

7. **Run tests** (if available)
   ```bash
   pytest tests/
   ```

---

## Submission Process

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] Comments added for complex logic
- [ ] No debug code or console.log statements
- [ ] Changes tested locally
- [ ] Documentation updated
- [ ] Commit messages are clear and descriptive

### Submit a Pull Request

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request" button
   - Select your branch
   - Fill in the PR template

3. **PR Description Template**
   ```markdown
   ## Description
   Brief description of changes

   ## Related Issues
   Closes #123

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation
   - [ ] Refactoring

   ## Testing
   How to test the changes

   ## Screenshots (if applicable)
   Add screenshots if UI changes

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-reviewed changes
   - [ ] Tested locally
   - [ ] Added/updated tests
   - [ ] Updated documentation
   ```

4. **Wait for Review**
   - Maintainers will review your PR
   - Address any requested changes
   - PR will be merged once approved

---

## Code Style Guidelines

### Python Style (PEP 8)

```python
# Good
def create_user(username, email):
    """Create a new user with validation."""
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user

# Bad
def create_user(u,e):
    user=User(username=u,email=e)
    db.session.add(user)
    db.session.commit()
    return user
```

### Naming Conventions

- **Functions**: `snake_case` → `create_task()`, `get_user_by_id()`
- **Classes**: `PascalCase` → `User`, `Task`, `DatabaseManager`
- **Constants**: `UPPER_SNAKE_CASE` → `MAX_RETRIES`, `DEFAULT_PORT`
- **Private methods**: `_snake_case` → `_validate_input()`

### Comments

```python
# Good - explains WHY
if user.last_login is None:
    # Mark as first-time user for onboarding flow
    user.is_first_login = True

# Bad - explains WHAT (code already does this)
# Set is_first_login to True
user.is_first_login = True
```

### HTML/CSS

```html
<!-- Use semantic HTML -->
<article class="task-card">
  <h2>{{ task.title }}</h2>
  <p>{{ task.description }}</p>
</article>

<!-- Use BEM naming for CSS classes -->
.task-card {}
.task-card__title {}
.task-card__description {}
```

### JavaScript

```javascript
// Use camelCase for variables and functions
const getUserTasks = () => {
  const tasks = [];
  return tasks;
};

// Use meaningful names
const activeUsers = users.filter(u => u.isActive); // Good
const a = users.filter(u => u.isActive);          // Bad
```

---

## Commit Message Guidelines

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style (formatting, semicolons, etc.)
- **refactor**: Code refactoring
- **perf**: Performance improvements
- **test**: Test updates
- **chore**: Build/dependency updates

### Examples

```
Good:
feat(task): Add task priority filtering
fix(auth): Resolve login session timeout issue
docs(readme): Add API documentation
refactor(models): Simplify user validation logic

Bad:
updated stuff
fixed bug
changes
FIX EVERYTHING
```

### Subject Line Rules

- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter
- No period at the end
- Max 50 characters

### Body Rules (Optional)

- Wrap at 72 characters
- Explain WHAT and WHY, not HOW
- Reference issues: "Closes #123"

### Example Full Commit

```
feat(api): Add task statistics endpoint

Add new /api/stats endpoint that returns task statistics
for the current user including total, completed, pending,
and in_progress counts.

This allows frontend dashboards to display real-time
statistics without fetching all tasks.

Closes #45
```

---

## Testing

### Writing Tests

Tests should be clear and descriptive:

```python
def test_create_task_with_valid_data():
    """Test creating a task with all required fields."""
    task = Task(
        title="Test Task",
        user_id=1
    )
    db.session.add(task)
    db.session.commit()
    
    assert task.id is not None
    assert task.title == "Test Task"

def test_create_task_without_title():
    """Test that task creation fails without title."""
    task = Task(user_id=1)  # Missing title
    
    with pytest.raises(IntegrityError):
        db.session.add(task)
        db.session.commit()
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_models.py

# Run with coverage
pytest --cov=app tests/

# Run with verbose output
pytest -v
```

---

## Documentation Standards

### Docstrings

```python
def create_task(title, user_id, description=None, priority="medium"):
    """
    Create a new task for a user.
    
    Args:
        title (str): Task title (required, max 200 chars)
        user_id (int): ID of the task owner
        description (str, optional): Task description
        priority (str, optional): Priority level (low/medium/high)
    
    Returns:
        Task: Created task object
    
    Raises:
        ValueError: If title is empty or user_id invalid
        IntegrityError: If database operation fails
    
    Example:
        >>> task = create_task("Learn Flask", user_id=1)
        >>> print(task.title)
        'Learn Flask'
    """
    if not title:
        raise ValueError("Title cannot be empty")
    
    task = Task(title=title, user_id=user_id, 
                description=description, priority=priority)
    db.session.add(task)
    db.session.commit()
    return task
```

---

## Git Workflow

### Typical Workflow

1. Create feature branch
   ```bash
   git checkout -b feature/add-notifications
   ```

2. Make commits
   ```bash
   git add .
   git commit -m "feat(email): Add email notification service"
   ```

3. Keep branch updated
   ```bash
   git fetch origin
   git rebase origin/main
   ```

4. Push changes
   ```bash
   git push origin feature/add-notifications
   ```

5. Create Pull Request on GitHub

### Before Merging

- Ensure branch is up-to-date with main
- All tests pass
- Code review approved
- CI/CD checks pass

---

## Getting Help

- **Questions**: Open a Discussion on GitHub
- **Issues**: Check existing issues first
- **Documentation**: See README.md and docs folder
- **Chat**: Join our community chat (if available)

---

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project README

---

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to My Auto Prac!** 🙏

For questions, please open an issue or discussion on GitHub.
