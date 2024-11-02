from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS progress (id INTEGER PRIMARY KEY, video_id TEXT, completed BOOLEAN)')
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT video_id, completed FROM progress')
    videos = cursor.fetchall()
    conn.close()
    return render_template('index.html', videos=videos)

@app.route('/complete/<video_id>')
def complete(video_id):
    conn = sqlite3.connect('database.db')
    conn.execute('UPDATE progress SET completed = 1 WHERE video_id = ?', (video_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
