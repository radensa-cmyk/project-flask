from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)

@app.route('/')
def halaman_utama():
    return render_template('index.html')

@app.route('/profil')
def halaman_profil():
    return "Ini adalah halaman profil saya."


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
        
        nama = request.form['nama']
        pesan = request.form['pesan']
       
        return render_template('bukutamu.html', nama_terbaru=nama, pesan_terbaru=pesan)
    else:
        
        return render_template('bukutamu.html')



semua_pesan = []

@app.route('/', methods=['GET'])
def home():
    
    return redirect(url_for('bukutamu'))

@app.route('/bukutamu', methods=['GET', 'POST'])
def bukutamu():
    global semua_pesan

    if request.method == 'POST':
       
        nama = request.form.get('nama', '').strip()
        pesan = request.form.get('pesan', '').strip()

        if nama and pesan:
            
            semua_pesan.insert(0, {'nama': nama, 'pesan': pesan})
        
        
            return redirect(url_for('bukutamu'))
        else:
          
            error = "Nama dan Pesan wajib diisi."
            return render_template('bukutamu.html', semua_pesan=semua_pesan, error_backend=error)

    
    return render_template('bukutamu.html', semua_pesan=semua_pesan)







@app.route('/portfolio')
def halaman_portfolio():
    return render_template('portfolio.html')

@app.route('/loading')
def halaman_loading():
    return render_template('loading.html')

@app.route('/python')
def halaman_python():
    return render_template('python.html')

@app.route('/frontend')
def halaman_frontend():
    return render_template('frontend.html')

@app.route('/chocolate')
def halaman_chocolate():
    return render_template('chocolate.html')

@app.route('/travel')
def halaman_travel():
    return render_template('travel.html')

@app.route('/3d')
def halaman_3d():
    return render_template('3d.html')

@app.route('/fuxica')
def halaman_fuxica():
    return render_template('fuxica.html')

@app.route('/devbeats')
def halaman_devbeats():
    return render_template('devbeats.html')






if __name__ == '__main__':
    app.run(debug=True)


    