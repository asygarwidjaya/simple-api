from flask import Blueprint, jsonify, request
from models.user_model import pengguna, tambah_pengguna, detail_pengguna_by_id, hapus_pengguna

users_bp =  Blueprint ('pengguna', __name__)

@users_bp.route('/pengguna', methods=['GET'])
def get_all_users():
    return jsonify({
        "status": "success",
        "data": pengguna
    }), 200

@users_bp.route('/pengguna/<int:id_pengguna>', methods=['GET'])
def detail_pengguna(id_pengguna):
    pengguna = detail_pengguna_by_id(id_pengguna)
    if pengguna:
        return jsonify({
            "status": "success",
            "data": pengguna
        }), 200
    return jsonify({
        "status": "failed",
        "message": "Pengguna tidak ditemukan"
    }), 404

@users_bp.route('/pengguna', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not all(key in data for key in ("nama", "email")):
        return jsonify({
            "status": "failed",
            "message": "Data tidak lengkap"
        }), 400
    
    new_user = tambah_pengguna(data["nama"], data["email"])
    return jsonify({
        "status": "success",
        "data": new_user
    }), 201

@users_bp.route('/pengguna/<int:id_pengguna>', methods=['DELETE'])
def delete_user(id_pengguna):
    if hapus_pengguna(id_pengguna):
        return jsonify({
            "status": "success",
            "message": "Pengguna berhasil dihapus"
        }), 200
    return jsonify({
        "status": "failed",
        "message": "Pengguna tidak ditemukan"
    }), 404