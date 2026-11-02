from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # 1. Перечисли здесь ВСЕ свои фото (они лежат в static/images/)
    photos = [
        "photo1.jpg",
        "photo2.jpg",
        "photo3.jpg",
        "photo4.jpg"  # добавь столько, сколько загрузил
    ]

    # 2. Перечисли здесь свои треки (они лежат в static/music/)
    tracks = [
        {"file": "song1.mp3", "title": "Название песни 1", "artist": "Исполнитель 1"},
        {"file": "song2.mp3", "title": "Название песни 2", "artist": "Исполнитель 2"},
        {"file": "song3.mp3", "title": "Название песни 3", "artist": "Исполнитель 3"}
    ]

    return render_template("index.html", photos=photos, tracks=tracks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)