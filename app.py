from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    photos = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]
    tracks = [
        {"file": "track1.mp3", "title": "Название 1", "artist": "Исполнитель 1"},
        {"file": "track2.mp3", "title": "Название 2", "artist": "Исполнитель 2"},
    ]
    return render_template("index.html", photos=photos, tracks=tracks)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)