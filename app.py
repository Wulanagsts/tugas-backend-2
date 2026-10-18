from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database simulasi untuk data produk
books = [
    {"id": 1, "title": "Laskar Pelangi", "author": "Andrea Hirata", "year": 2005, "stock": 30},
    {"id": 2, "title": "Perahu Kertas", "author": "Dee Lestari", "year": 2003, "stock": 10},
    {"id": 3, "title": "Cantik itu Luka", "author": "Eka Kurniawan", "year": 2002, "stock": 9},
    {"id": 4, "title": "Negeri 5 Menara", "author": "A.Fuadi", "year": 2009, "stock": 6},
    {"id": 5, "title": "Bumi Manusia", "author": "Pramoedya Ananta Toer", "year": 1980, "stock": 5}
]

@app.route("/", methods=["GET"])
def root_health_check():
    return (
        jsonify(
            {
                "status": "success",
                "message": "Selamat Belajar Dasar Pemrograman Backends",
                "version": "1.0.0",
            }
        ),
        200,
    )

# 1. HTTP GET: Mengambil Seluruh buku
@app.route('/api/v1/books', methods=['GET'])
def get_all_books():
    return jsonify({
        "status": "success",
        "total": len(books),
        "data": books
    }), 200

# 2. HTTP POST: Menambahkan Buku Baru
@app.route('/api/v1/books', methods=['POST'])
def create_book():
    # Memvalidasi Content-Type request harus JSON
    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Payload harus berformat application/json"
        }), 400

    data = request.get_json()
    required_fields = ["title", "author", "year", "stock"]
    if not all (field in data for field in required_fields):
        return jsonify({
            "status": "error",
            "message": "Data tidak valid! Field 'title', 'author', 'year', dan 'stock' wajib diisi."
        }), 400

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "stock": data["stock"],
    }
    books.append(new_book)
    return jsonify({
        "status": "success",
        "message": "Buku berhasil ditambahkan",
        "data": new_book
    }), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)