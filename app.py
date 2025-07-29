
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/projects')
def project():
    return render_template('project.html')
@app.route('/skills')
def skills():
    skills = [
        {"name": "Java", "icon": "fab fa-java"},
        {"name": "Python", "icon": "fab fa-python"},
        {"name": "C", "icon": "fas fa-code"},
        {"name": "Data Structures", "icon": "fas fa-sitemap"},

        {"name": "HTML5", "icon": "fab fa-html5"},
        {"name": "CSS3", "icon": "fab fa-css3-alt"},
        {"name": "JavaScript", "icon": "fab fa-js"},
        {"name": "React.js", "icon": "fab fa-react"},
        {"name": "Vue.js", "icon": "fab fa-vuejs"},
        {"name": "Flask", "icon": "fas fa-flask"},
        {"name": "MongoDB", "icon": "fas fa-leaf"},
        {"name": "Node.js", "icon": "fab fa-node-js"},
        {"name": "Git", "icon": "fab fa-git-alt"},
        {"name": "GitHub", "icon": "fab fa-github"},
        {"name": "Database (SQL)", "icon": "fas fa-database"},
        {"name": "Spring Boot", "icon": "fas fa-leaf"},  # Custom choice
    ]
    return render_template('skills.html', skills=skills)
@app.route('/resume')
def resume():
    return render_template('resume.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/projects')
def project():
    return render_template('project.html')
@app.route('/skills')
def skills():
    skills = [
        {"name": "Java", "icon": "fab fa-java"},
        {"name": "Python", "icon": "fab fa-python"},
        {"name": "C", "icon": "fas fa-code"},
        {"name": "Data Structures", "icon": "fas fa-sitemap"},

        {"name": "HTML5", "icon": "fab fa-html5"},
        {"name": "CSS3", "icon": "fab fa-css3-alt"},
        {"name": "JavaScript", "icon": "fab fa-js"},
        {"name": "React.js", "icon": "fab fa-react"},
        {"name": "Vue.js", "icon": "fab fa-vuejs"},
        {"name": "Flask", "icon": "fas fa-flask"},
        {"name": "MongoDB", "icon": "fas fa-leaf"},
        {"name": "Node.js", "icon": "fab fa-node-js"},
        {"name": "Git", "icon": "fab fa-git-alt"},
        {"name": "GitHub", "icon": "fab fa-github"},
        {"name": "Database (SQL)", "icon": "fas fa-database"},
        {"name": "Spring Boot", "icon": "fas fa-leaf"},  # Custom choice
    ]
    return render_template('skills.html', skills=skills)
@app.route('/resume')
def resume():
    return render_template('resume.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

