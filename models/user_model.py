pengguna = [
    {"id": 1, "nama": "budi", "email": "budi@gmail.com"},
    {"id": 2, "nama": "jay", "email": "jay@gmail.com"}
]

def detail_pengguna_by_id(id_pengguna):
    for user in pengguna:
        if user["id"] == id_pengguna:
            return user
    return None

def tambah_pengguna(nama, email):
    new_user = {
        "id": len(pengguna) + 1,
        "nama": nama,
        "email": email
    }
    pengguna.append(new_user)
    return new_user

def hapus_pengguna(id_pengguna):
    for p in pengguna:
        if p["id"] == id_pengguna:
            pengguna.remove(p)
            return True
    return False