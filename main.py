
from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the grammar route
@app.route('/grammar')
def grammar():
    return render_template('grammar.html')

# Define the vocabulary route
@app.route('/vocabulary')
def vocabulary():
    return render_template('vocabulary.html')

# Define the exercises route
@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

# Define the about route
@app.route('/about')
def about():
    return render_template('about.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
