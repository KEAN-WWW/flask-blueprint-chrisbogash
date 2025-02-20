from flask import Flask, render_template
from application.bp.homepage.homepage import homepage

# initialize Flask service
app = Flask(__name__)
# register blueprint

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

app.register_blueprint(homepage)

if __name__ == "__main__":
    app.run(debug=True)
