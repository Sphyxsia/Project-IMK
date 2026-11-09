# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg room1 = "images/room_night.jpg"
image bg room2 = "images/room.jpg"
image bg class = "images/campus_inside.png"
image bg street = "images/street_morning.jpg"
# Deklarasikan karakter yang digunakan di game.
define k = Character('Kiki')
define a = Character('Adek Kiki')
define i = Character('Ibu')
define b = Character('Bapak')
define d = Character('Pak Darto')
define tk1 = Character('Reza')
define tk2 = Character('Dinda')
define d = Character('Pak Rakha')
define s = Character('Siska')
define nco = Character('???')
define nce = Character('???')
define aco = Character('???')
define ace = Character('???')

# Game dimulai disini.
label start:

    scene bg room1 with dissolve
    i "Kiki, sudah makan?"

    k "Sudah, Bu. Tadi beli nasi sama telur. Biar hemat, hehe."

    b "Hemat boleh, tapi jangan sampai sakit."

    a "Kak Kiki! Kapan pulang? Aku mau oleh-oleh!"

    k "Nanti kalau libur, ya. Kakak bawain stiker."

    a "Asyik! Tapi, Kak, perutku agak sakit dari tadi."

    i "Ibu sedang memperhatikan air sumur kita. Beberapa hari ini airnya terlihat keruh."

    k "Keruh? Dinda tadi minum air sumur?"

    i "ya, Nak. Ibu belum tahu apa penyebabnya. Mulai sekarang, kita cari sumber air yang aman dulu."

    b "Kita juga perlu mencari tahu kenapa sumurnya berubah."

    k "Baik, Bu. Jangan diminum dulu kalau belum dipastikan aman. Kalau Dinda masih sakit, bawa periksa ke tenaga kesehatan, ya."

    "Panggilan berakhir, Kiki memikirkan keluarganya. Ia ingin membantu, tetapi ia harus belajar mancari solusi yang tepata, bukan sekedar menebak penyebab masalah."

    scene bg room2 with fade
    "Pagi itu,token listrik kos Kiki habis. HP-nya tinggal 3 persen, sementara tugas kuliah harus dikirim sebelum malam."

    k "Duh, akhir bulan! HP sisa 3 persen. deadline tugas malam ini lagi!"

    k "Uang tinggal 20ribu, gimana nih!"

    k "Ah!!, kan ada panel surya bekas tugas kemaren. kalau masih bisa dipakai harusnya masalah listrik bias teratasi."

    scene bg class with fade
    "Kiki mengigat kembali cara kerja sistem energi surya yang pernah ia pelajari."

    k "Pertama, cahaya matahari mengenai panel surya."

    k "Panel mengubah energi cahaya manjedi listrik. Sirkuit membantu mengatur listrik yang masuk ke baterai."

    k "Setelah tersimpan, keluaran daya dari baterai atau power bank yang sesuai bisa digunakan untuk mengisi HP."

    k "Sekarang, tinggal mengatur urutan perangkatnya!"

    return
