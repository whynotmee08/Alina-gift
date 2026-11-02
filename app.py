from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    photos = [
        "photo1.jpg",
        "photo2.jpg",
        "photo3.jpg",
        "photo4.jpg",
        "photo5.jpg"
    ]

    tracks = [
        {"file": "song1.mp3", "title": "Влюбленные глаза ", "artist": "Isko"},
        {"file": "song2.mp3", "title": "Капкан", "artist": "VALID"},
        {"file": "song3.mp3", "title": "Картина", "artist": "BY МЕТРИКА, dxrk.exe"}
    ]

    return render_template("index.html", photos=photos, tracks=tracks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)