from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the 'index.html' template
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)