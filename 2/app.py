from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title': 'Home Page',
        'user': 'Akash',
        'items': ['Machine Learning', 'Flask', 'Python', 'SQL'],
        'show_banner': True
    }
    return render_template('index.html', **data)

@app.route('/dashboard')
def dashboard():
    stats = [
        {'label': 'Models Trained', 'value': 12, 'color': 'blue'},
        {'label': 'Accuracy',       'value': '94%', 'color': 'green'},
        {'label': 'Datasets',       'value': 8,  'color': 'purple'},
    ]
    return render_template('dashboard.html', title='Dashboard', stats=stats)

@app.route('/profile')
def profile():
    user = {
        'name': 'Akash',
        'role': 'Data Scientist',
        'skills': ['Python', 'Flask', 'Scikit-learn'],
        'active': True
    }
    return render_template('profile.html', title='Profile', user=user)

if __name__ == '__main__':
    app.run(debug=True)