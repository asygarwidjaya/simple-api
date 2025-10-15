from flask import Flask, jsonify, Response
import json
from routes.users import users_bp

app = Flask(__name__)
app.register_blueprint(users_bp)

@app.route('/')
def home():
    return jsonify({
        "message": "Selamat datang di simple API pengguna",
        "endpoints yang tersedia": {
            "GET /pengguna": "Menampilkan daftar pengguna",
            "POST /pengguna": "Menambahkan pengguna baru",
            "GET /pengguna/(id)": "Menampilkan detail pengguna",
            "DELETE /pengguna/(id)": "Menghapus pengguna"
        }
    })

if __name__ == '__main__':
    app.run(debug=True)