from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/store-achievement")
def store_achievement():
    return "Store Achievement"
@app.route("/current-achievements")
def current_achievements():
    return "Current Achievements"
@app.route("/set-goal")
def set_goal():
    return "Set Goal"

if __name__=="__main__":
    app.run(debug=True)
