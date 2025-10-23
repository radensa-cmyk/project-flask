from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def halaman_utama():
    return render_template('index.html')

@app.route('/profil')
def halaman_profil():
    return "Ini adalah halaman profil saya."

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/2')
def halaman_2():
    # Data tentang dirimu
    nama = "Abu Musa"
    hobi = "Ngoding dan desain UI/UX"
    sekolah = "HSI BOARDING SCHOLL"
    return render_template('profil.html', nama=nama, hobi=hobi, sekolah=sekolah)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/teman')
def halaman_teman():
    daftar_teman = ["dapa", "saal", "ngad", "borr"]

#    ubah daftar_teman = []
    return render_template('teman.html', daftar_teman=daftar_teman)



# tamu

@app.route('/index')
def index():
    return '<h1>Selamat Datang, enjoying togethr!</h1><a href="/bukutamu">Buka Buku Tamu</a>'

@app.route('/bukutamu', methods=['GET', 'POST'])
def buku_tamu():
    if request.method == 'POST':
        # Ambil data dari form
        nama = request.form['nama']
        pesan = request.form['pesan']
        # Kirim kembali ke template dengan data terbaru
        return render_template('bukutamu.html', nama_terbaru=nama, pesan_terbaru=pesan)
    else:
        # Saat halaman baru dibuka (GET)
        return render_template('bukutamu.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# miniprojek

# from flask import Flask, render_template, request

# app = Flask(__name__)

semua_pesan = []

@app.route('/miniproject', methods=['GET', 'POST'])
def halaman_lain():
    global semua_pesan

    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan = request.form.get('pesan')

        if nama and pesan:
            data_baru = {'nama': nama, 'pesan': pesan}
            semua_pesan.append(data_baru)

    return render_template('miniproject2.html', semua_pesan=semua_pesan)

if __name__ == '__main__':
    app.run(debug=True)

    