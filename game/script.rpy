# Kamu dapat taruh script game mu di file ini.
define config.mouse = {
    "default": [
        ("images/gui/cursor/cursor_main_button.png", 0, 0)
    ],
    "button": [
        ("images/gui/cursor/cursor_main_pressed.png", 5, 0)
    ]
}

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg room1 = "images/room_night.jpg"
image bg room2 = "images/room.jpg"
image bg class = "images/campus_inside.png"
image bg street = "images/street_morning.jpg"
# Deklarasikan karakter yang digunakan di game.
define k = Character('Kiki', color="")
define a = Character('Adek Kiki', color="")
define i = Character('Ibu', color="")
define b = Character('Bapak', color="")
define d = Character('Pak Darto', color="")
define tk1 = Character('Reza', color="")
define tk2 = Character('Dinda', color="")
define d = Character('Pak Rakha', color="")
define s = Character('Siska', color="")
define nco = Character('???', color="")
define nce = Character('???', color="")
define aco = Character('???', color="")
define ace = Character('???', color="")

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

    show bg room2 with fade
    "Pagi itu,token listrik kos Kiki habis. HP-nya tinggal 3 persen, sementara tugas kuliah harus dikirim sebelum malam."

    k "Duh, akhir bulan! HP sisa 3 persen. deadline tugas malam ini lagi!"

    k "Uang tinggal 20ribu, gimana nih!"

    k "Ah!!, kan ada panel surya bekas tugas kemaren. kalau masih bisa dipakai harusnya masalah listrik bias teratasi."

    show bg class with pixellate
    "Kiki mengigat kembali cara kerja sistem energi surya yang pernah ia pelajari."

    k "Pertama, cahaya matahari mengenai panel surya."

    k "Panel mengubah energi cahaya manjedi listrik. Sirkuit membantu mengatur listrik yang masuk ke baterai."

    k "Setelah tersimpan, keluaran daya dari baterai atau power bank yang sesuai bisa digunakan untuk mengisi HP."

    k "Sekarang, tinggal mengatur urutannya!"

    show bg room2 with pixellate
default minigame = 0
default pilihan_m1 = []

label m1:

    $ pilihan_m1 = []

    "Pilih semua komponen sesuai urutan yang benar."

    jump m1_pilihan


label m1_pilihan:

    menu:
        "Matahari" if "Matahari" not in pilihan_m1:
            $ pilihan_m1.append("Matahari")
            jump m1_pilihan

        "Panel Surya" if "Panel Surya" not in pilihan_m1:
            $ pilihan_m1.append("Panel Surya")
            jump m1_pilihan

        "Baterai" if "Baterai" not in pilihan_m1:
            $ pilihan_m1.append("Baterai")
            jump m1_pilihan

        "Ponsel" if "Ponsel" not in pilihan_m1:
            $ pilihan_m1.append("Ponsel")
            jump m1_pilihan

        "Konfirmasi":
            jump m1_cek

        "Kembali ke awal":
            jump m1
        
label m1_cek:

    if pilihan_m1 == ["Matahari", "Panel Surya", "Baterai", "Ponsel"]:
        jump m1_berhasil

    else:
        jump m1_gagal


label m1_berhasil:

    "Kiki berhasil menyusun sistemnya. Daya tersimpan di power bank dan digunakan untuk mengisi HP."

    $ minigame += 1

    k "Yes! HP-ku mulai terisi. Sekarang aku bisa mengirim tugas tepat waktu!"

    k "Energi matahari merupakan sumber energi terbarukan, tetapi kita tetap perlu menyimpan dan menggunakannya dengan benar."

    jump bab2


label m1_gagal:

    "Kiki menemukan bahwa urutan perangkatnya belum tepat. Ia memeriksa kembali diagram energi yang pernah dipelajari."
    
    k "Oh, urutannya belum benar. Aku perlu memahami fungsi setiap perangkat dengan lebih baik."

    k "Aku tetap bisa belajar dari kesalahan ini."

    jump bab2


label bab2:

    "bab 2 On Progress"

    return
