from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            note = request.form.get("note")
            notes.append(note)
        elif action == "delete":
            index_to_delete = int(request.form.get("index"))
            del notes[index_to_delete]
        return redirect(url_for('index'))
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
