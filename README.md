## Dokumentasi Request dan Response

### 1. GET /api/v1/books

**Request:**

```bash
curl -i http://127.0.0.1:5000/api/v1/books
```

**Response (200 OK):**

```json
{
  "status": "success",
  "total": 5,
  "data": [
    {"id": 1, "title": "Laskar Pelangi", "author": "Andrea Hirata", "year": 2005, "stock": 30}
  ]
}
```

### 2. POST /api/v1/books (data valid)

**Request:**

```bash
curl -i -X POST http://127.0.0.1:5000/api/v1/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Ronggeng Dukuh Paruk","author":"Ahmad Tohari","year":1982,"stock":7}'
```

**Response (201 Created):**

```json
{
  "status": "success",
  "message": "Buku berhasil ditambahkan",
  "data": {"id": 6, "title": "Ronggeng Dukuh Paruk", "author": "Ahmad Tohari", "year": 1982, "stock": 7}
}
```

### 3. POST /api/v1/books (data tidak valid)

**Request:**

```bash
curl -i -X POST http://127.0.0.1:5000/api/v1/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Tanpa Author"}'
```

**Response (400 Bad Request):**

```json
{
  "status": "error",
  "message": "Data tidak valid! Field 'title', 'author', 'year', dan 'stock' wajib diisi."
}
```

## Screenshot Pengujian

![GET books]![alt text](image.png)
![POST books]![alt text](image-1.png) & ![alt text](image-2.png)