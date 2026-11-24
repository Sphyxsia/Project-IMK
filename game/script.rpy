# Kamu dapat taruh script game mu di file ini.
define config.mouse = {
    "default": [
        ("gui/cursor/cursor_main_button.png", 0, 0)
    ],
    "button": [
        ("gui/cursor/cursor_main_pressed.png", 5, 0)
    ]
}

transform loncat_bicara:
    yoffset 0
    easein 0.08 yoffset -15  # Karakter naik 15 pixel ke atas
    easeout 0.08 yoffset 0   # Karakter kembali ke posisi semula

transform ukuran_reza:
    zoom 0.65
    yoffset 1200
    xoffset -400

transform ukuran_dinda:
    zoom 0.65
    yoffset 1200
    xoffset 400
    
# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg room1 = "images/bg/room_night.jpg"
image bg room2 = "images/bg/room.jpg"
image bg class = "images/bg/campus_inside.png"
image bg street = "images/bg/street_morning.jpg"
image bg kereta = "images/bg/train_car.jpg"
image bg window_kereta = "images/bg/train_window.jpg"
image bg lake1 = "images/bg/lake_morning.jpg"
image bg lake2 = "images/bg/lake_dusk.jpg"
image reza idle = "images/sprites/reza.png" 
image dinda idle = "images/sprites/dinda.png" 
# Deklarasikan karakter yang digunakan di game.
define k = Character('Kiki', color="#ffffff")
define a = Character('Adek Kiki', color="#ffffff")
define i = Character('Ibu', color="#ffffff")
define b = Character('Bapak', color="#ffffff")
define d = Character('Pak Darto', color="#ffffff")
define tk1 = Character('Reza', color="#ffffff")
define tk2 = Character('Dinda', color="#ffffff")
define pr = Character('Pak Rakha', color="#ffffff")
define s = Character('Siska', color="#ffffff")
define nco = Character('???', color="#ffffff")
define nce = Character('???', color="#ffffff")
define aco = Character('???', color="#ffffff")
define ace = Character('???', color="#ffffff")
define pn = Character('Panitia', color="#ffffff")
define kr = Character('Kiki & Reza', color="#ffffff")
# Game dimulai disini.
label start:

    scene bg kereta with dissolve

    k "Halo ibuuu"

    i "Kiki! Udah sampe belum, Nak? Dari tadi Ibu khawatir jadi telepon kamu."

    k "Belum bu, kiki Masih di kereta, ini sebentar lagi nyampe kok."

    i "Alhamdulillah. Jangan sampai ketiduran ya, nanti kelewatan stasiun nya."

    k "Enggak kok Bu, Kiki melek terus dari tadi."

    i "Jangan mie instan terus nanti di sana."

    a "Kak Kikiiiiiiiii! ^w^ Kakak udah dimanaaaaaaa?"

    k "hehe hi Dek, Kakak belum nyampeeeee."

    a "masa lama banget kakkkk . situ kereta apa cara kerja pemerintah sih kak wkwkwk!"

    k "hehhh diemm! nanti kedengaran intel kakak yang kena"

    a "Wleee~, Kakak takut yaa sendirian di tempat baru, awas kak nanti ada yang ketawa tengah malem lohh ooooohhhh~?"

    k "adek pikir kakak takut! Kakak udah gede yaaa, awas aja dikamar adek nanti ada..."

    i "Sudah, sudah. Adek, jangan ganggu Kakak."

    ". . . ."

    i "Ya sudah, hati-hati di jalan ya kiki. Kalau sudah sampai kabarin Ibu ya."

    k "okay ibuu. Kiki sayang Ibu. Salam buat Adek."

    a "Aku masih disini tauuu!"

    "Panggilan berakhir, Kiki menurunkan HP dari telinganya."
    show bg window_kereta with fade
    "Kiki menoleh ke jendela dan keluar. pemandangan sawah dan rumah-rumah berganti pelan menjadi gedung-gedung kota yang asing. Cahaya sore memantul di kaca."
    show bg street with fade
    k "Hmm... jadi ini tempat baruku"

    "Time Skip"

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

    jump bab3


label m1_gagal:

    "Kiki menemukan bahwa urutan perangkatnya belum tepat. Ia memeriksa kembali diagram energi yang pernah dipelajari."
    
    k "Oh, urutannya belum benar. Aku perlu memahami fungsi setiap perangkat dengan lebih baik."

    k "Aku tetap bisa belajar dari kesalahan ini."

    jump bab3


label bab2:

    "Beberapa minggu kemudian, Kiki menerima telepon dari rumah. Masalah air sumur belum selesai."

    i "Kiki, kondisi Dinda masih perlu diperhatikan. Ia sempat mengalami gangguan perut, dan kami sedang mengikuti saran dokter."
    
    k "Bagaimana dengan air sumurnya, Bu?"

    i "Airnya masih terlihat keruh. Kami belum tahu pasti apa penyebabnya. Untuk sementara, kami menggunakan sumber air yang lebih aman."

    k "Aku pulang akhir pekan ini, ya, Bu. Aku ingin melihat apa yang bisa kubantu."

    " Kiki tiba di kampung dan melihat pekerjaan pemasangan jaringan air yang sedang dilakukan warga."

    k "Pak Darto, saya boleh membantu pekerjaan ini? Saya ingin keluarga saya dan warga punya akses air yang lebih aman. Upahnya juga bisa membantu biaya keluarga."

    d "Tentu, Nak. Tapi pemasangan pipa air minum tidak boleh asal sambung."

    k "Apa yang harus saya perhatikan, Pak?"

    d "Pertama, ikuti jalur dari sumber atau tangki menuju rumah. Kedua, pastikan pipa air minum terpisah dari saluran limbah dan tidak mudah tercemar. Ketiga, sambungannya harus rapat dan sistemnya perlu diperiksa."

    k "Jadi, air yang sudah mengalir belum tentu langsung aman untuk diminum?"

    d "Betul. Kita juga harus memastikan sumbernya layak dan kualitas airnya memenuhi persyaratan."

    jump minigame_pipa

    label minigame_pipa:

    $ pipe_generate_board()

    call screen pipe_puzzle

    if _return:

        k "Yes! Semua pipanya sudah tersambung!"

        $ minigame += 1

    else:

        k "Sepertinya aku perlu mencoba lagi nanti."

    return

    
    jump bab3

label bab3:

    scene bg room2
    k "Oh iya, hari ini aku kerja bakti di danau. Hmm…. jam sembilan... Masih sempet lah yak. Berangkat ah."

    scene bg street with moveinright
    show bg lake1 with pixellate
    tk1 "Woi, Ki!" 

    show reza idle at ukuran_reza, left with moveinleft
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "Sini sini! Tumben nggak telat."
    
    k "Iya lahh, Aku kan anak rajin."

    show dinda idle at ukuran_dinda, right with moveinright
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "Rajin dari mana? Kemarin aja kamu bilang malas ikut."
    
    k "iyahh yang kemarin udah ditangkep aparat, aku kloningan nya."
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "Hahaha, plot twist banget."
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "Udah udah. Itu panitianya udah mulai ngumpulin orang-orang. Ayo ke sana."
    

    scene bg lake1 with dissolve
    "Para relawan berkumpul. Panitia berdiri di depan membawa kantong-kantong sampah."

    pn "Selamat pagi, Teman-teman relawan! Terima kasih sudah datang. Hari ini tugas kita cukup simple: membersihkan Danau Bougainvillea dari sampah."
    show reza idle at ukuran_reza, left with moveinleft
    show dinda idle at ukuran_dinda, right with moveinright
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "(bisik ke Kiki) kok GAMPANG. Liat aja tuh sampahnya segunung."
    
    pn "Mungkin kelihatannya cuma kayak kerja bakti biasa. Tapi Danau Bougainvillea ini salah satu sumber mata air utama yang digunakan masyarakat sekitar. Kalau airnya kotor, banyak orang akan terkena dampak nya, kita tidak boleh membiarkan hal itu terjadi."
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "Ternyata sepenting itu..."
    
    k "Kalau gitu kita harus kerja yang bener nih."

    pn "Betul. Silahkan ambil kantong sampah dan sarung tangan, kita mulai dari sisi danau. Nanti kita  cek lagi nanti. Semangat ya!"

    "Kiki, Reza, dan Dinda mulai memungut sampah botol, plastik, dan ranting di tepi danau."

    scene bg lake1 with dissolve
    show reza idle at ukuran_reza, loncat_bicara, left with moveinleft
    tk1 "Ki, taruhan yuk. Siapa yang paling banyak ngambil sampah, dia menang."

    k "Hah? Taruhan apaan?"
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "Yang kalah traktir makan siang gratis. Gimana?"

    k "Oke. mulai siapin duitnya aja, Za."
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "liat aja nanti duit siapa yang akan habis."
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "Rasakan jurus Kantong Sampah Lubang Hitam Raksasa!"

    k "Tcih! Gitu doang? Nih, rasakan jurus serangan rudal botol plastik, nyahuu!"
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "Curang! Itu botol sampah punyaku!"


    scene bg lake1 with dissolve
    tk2 "(menghela napas) Kalian berdua..."
    show dinda idle at ukuran_dinda, left with moveinleft
    "Dinda menghampiri dengan tangan di pinggang."
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "KIKI! REZA! Kerja yang bener dong! Dari tadi bercanda terus, sampahnya masih banyak tuh!"
    show reza idle at ukuran_reza, loncat_bicara

    kr "Ehh iya, maaf, Din..."
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "Kita di sini mau bersihin danau, bukan lomba adu kumpulan sampah. Ayo lanjut kerja."

    "Mereka bertiga kembali bekerja dengan serius."

    $ lake_start()

    call screen lake_game("lake_win", "lake_lose")

label lake_win:

    scene bg lake1 with dissolve
    show reza idle at ukuran_reza, loncat_bicara, left with moveinleft
    tk1 "(terkapar di rumput) huft…. Capek... Oke, oke, aku ngaku kalah, Ki."

    k "Hehe, makanya jangan belagu pake nantangin lagii."
    show dinda idle at ukuran_dinda, loncat_bicara, right with moveinright
    tk2 "hadeh kalian ini, baru serius kalau udah denger makan siang."

    k "Tapi liat deh. Danaunya jadi bersih banget."
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "Iya. Rasanya puas banget ya."

    "Para panitia datang memeriksa, lalu mengangguk puas."

    pn "Luar biasa! Terima kasih banyak, ya. Danau ini jadi bersih kembali berkat kalian."
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "Nah, soal taruhan tadi… boleh minggu depan aja ga ki belum dapet setoran hehe"

    k "eits gabisa! Traktir sekarang Mie ayam pak rusdi ya!"
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "Aku ikut dong!"
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "dih kok jadinya traktir berdua ;-;, dompetku udah mulai nangis nih."

    "Danau kembali bersih dan mereka makan mie ayam bareng bertiga."

    jump ending

label lake_lose:

    scene bg lake2 with dissolve
    show reza idle at ukuran_reza, loncat_bicara, left with moveinleft
    tk1 "YES! Aku menang, Ki! Jangan lupa yaaaa!"

    k "Iya iya… duh Padahal dikit lagi."

    "Para panitia datang untuk memeriksa. Wajah mereka tampak ragu setelah melihat sekeliling."

    pn "Hmm... ternyata masih banyak sampah di sini."

    "Suasana berubah hening. Kiki, Reza, dan Dinda saling pandang."

    k "Kami minta maaf, Kak. Usaha kami belum cukup."
    show dinda idle at ukuran_dinda, loncat_bicara, right with moveinright
    tk2 "Maaf, kami terlalu banyak bercanda tadi."
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "(menunduk) Maaf, Kak. Ini salah kami juga."

    "Panitia tersenyum dan menepuk pundak mereka."

    pn "Tidak apa-apa, kok. Kami yang akan lanjutkan besok. Kalian sudah bantu banyak hari ini. Kami tidak mau merepotkan kalian lagi, jadi kalian boleh pulang. Terima kasih banyak atas bantuannya hari ini."

    k "...Baik, Kak. Terima kasih juga."

    "Ketiganya berjalan meninggalkan danau dengan langkah lesu."
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "(pelan) Jadi... mie ayamnya gimana?"
    show dinda idle at ukuran_dinda, loncat_bicara
    tk2 "duh lagi nggak enak, Za. Lain kali aja deh."

    k "iya nanti aja, udah hilang mood ku (sama duit ku wkwkwk)"
    show reza idle at ukuran_reza, loncat_bicara
    tk1 "Iya... aku juga. Mending pulang dulu."

    "Mereka tidak jadi makan mie ayam bareng. Masing-masing pulang ke rumah/kos."

    jump ending

label ending:

    return


default pipe_board = []
default pipe_message = ""

init python:

    import random

    PIPE_COLS = 5
    PIPE_ROWS = 6

    # cell[1] = True berarti BLACK/permanen.
    # cell[1] = False berarti BROWN/bisa diputar.
    PIPE_IMAGES = {
        ("I", True): "images/minigame/pipe/pipe_i_black.png",
        ("R", True): "images/minigame/pipe/pipe_r_black.png",
        ("T", True): "images/minigame/pipe/pipe_t_black.png",

        ("I", False): "images/minigame/pipe/pipe_i_brown.png",
        ("R", False): "images/minigame/pipe/pipe_r_brown.png",
        ("T", False): "images/minigame/pipe/pipe_t_brown.png",
    }

    # Arah: N=0, E=1, S=2, W=3

    PIPE_BASE = {
        "I": [0, 2],
        "R": [0, 1],
        "T": [0, 2, 3],
    }

    def pipe_rotate_dirs(dirs, angle):
        steps = angle // 90
        return sorted([(d + steps) % 4 for d in dirs])

    def pipe_find_rotation(kind, target):
        for angle in [0, 90, 180, 270]:
            if pipe_rotate_dirs(PIPE_BASE[kind], angle) == sorted(target):
                return angle
        return 0

    
    def pipe_generate_board():

        # Membuat jalur zigzag yang melewati semua kotak
        # Membuat jalur zigzag per kolom.
        # START: kiri atas.
        # FINISH: kanan bawah.

        path = []

        for c in range(PIPE_COLS):

            if c % 2 == 0:
                rows = range(PIPE_ROWS)
            else:
                rows = range(PIPE_ROWS - 1, -1, -1)

            for r in rows:
                path.append((r, c))

        start = path[0]
        finish = path[-1]

        # Membuat jalur antar kotak
        edges = set()

        def add_edge(a, b):
            edges.add(tuple(sorted((a, b))))

        for i in range(len(path) - 1):
            add_edge(path[i], path[i + 1])

        # Tambahkan cabang agar muncul pipa T
        candidates = []

        for r in range(PIPE_ROWS):
            for c in range(PIPE_COLS):

                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc

                    if nr >= PIPE_ROWS or nc >= PIPE_COLS:
                        continue

                    a = (r, c)
                    b = (nr, nc)
                    edge = tuple(sorted((a, b)))

                    if edge not in edges:
                        candidates.append(edge)

        random.shuffle(candidates)

        added = 0

        for a, b in candidates:

            if added >= 4:
                break

            degree_a = sum(a in e for e in edges)
            degree_b = sum(b in e for e in edges)

            if a in (start, finish) or b in (start, finish):
                continue

            if degree_a == 2 and degree_b == 2:
                edges.add((a, b))
                added += 1

        # Menentukan koneksi tiap pipa
        connections = {
            (r, c): set()
            for r in range(PIPE_ROWS)
            for c in range(PIPE_COLS)
        }

        for a, b in edges:

            dr = b[0] - a[0]
            dc = b[1] - a[1]

            if dr == -1:
                d = 0
            elif dc == 1:
                d = 1
            elif dr == 1:
                d = 2
            else:
                d = 3

            connections[a].add(d)
            connections[b].add((d + 2) % 4)

        # START menerima koneksi dari luar sebelah kiri.
        connections[start].add(3)

        # FINISH mengeluarkan koneksi ke luar sebelah kanan.
        connections[finish].add(1)

        board = []

        for r in range(PIPE_ROWS):
            for c in range(PIPE_COLS):

                dirs = sorted(connections[(r, c)])

                if len(dirs) == 3:
                    kind = "T"
                elif len(dirs) == 2:
                    if (dirs[1] - dirs[0]) % 4 == 2:
                        kind = "I"
                    else:
                        kind = "R"
                else:
                    raise Exception(
                        "Pipa memiliki konektor tidak valid: {}".format(dirs)
                    )

                target = pipe_find_rotation(kind, dirs)

                # START dan FINISH selalu permanen karena memakai gambar khusus.
                # Kotak lainnya: Black permanen, Brown bisa diputar.
                is_endpoint = (r, c) == start or (r, c) == finish
                fixed = is_endpoint or (random.random() < 0.25)

                if fixed:
                    rotation = target
                else:
                    choices = [
                        angle for angle in [0, 90, 180, 270]
                        if angle != target
                    ]
                    rotation = random.choice(choices)

                board.append([
                    kind,
                    fixed,
                    rotation,
                    target
                ])

        store.pipe_board = board
        store.pipe_message = ""



    def pipe_rotate(index):

        cell = store.pipe_board[index]

        # Black dan endpoint tidak bisa diputar.
        if cell[1]:
            return

        # Putar pipa 90 derajat.
        cell[2] = (cell[2] + 90) % 360

        # Refresh screen agar kondisi menang diperiksa ulang.
        renpy.restart_interaction()


    def pipe_is_solved():

        board = store.pipe_board

        if len(board) != PIPE_COLS * PIPE_ROWS:
            return False

        # cell[2] adalah rotasi saat ini.
        # cell[3] adalah rotasi solusi yang disimpan generator.
        for cell in board:

            current_dirs = pipe_rotate_dirs(
                PIPE_BASE[cell[0]], cell[2]
            )

            target_dirs = pipe_rotate_dirs(
                PIPE_BASE[cell[0]], cell[3]
            )

            if current_dirs != target_dirs:
                return False

        return True



screen pipe_puzzle():

    modal True

    add "#172426"

    text "START":
        color "#39ff55"
        size 25
        xalign 0.5
        ypos 100

    text "FINISH":
        color "#39ff55"
        size 25
        xalign 0.5
        ypos 800

    text "PIPE CONNECTION":
        xalign 0.5
        ypos 12
        size 32
        color "#ffffff"

    text "Putar pipa Brown sampai semua jalur tersambung":
        xalign 0.5
        ypos 55
        size 16
        color "#dddddd"

    
    fixed:

        $ cell_size = 68
        $ board_width = PIPE_COLS * cell_size
        $ board_height = PIPE_ROWS * cell_size

        $ board_x = (config.screen_width - board_width) // 2
        $ board_y = (config.screen_height - board_height) // 2 + 30

        # Label START
        text "START":
            color "#39ff55"
            size 22
            xpos board_x - 85
            ypos board_y + 18

        # Label FINISH
        text "FINISH":
            color "#39ff55"
            size 22
            xpos board_x - 85
            ypos board_y + (PIPE_ROWS - 1) * cell_size + 18

        
        for i, cell in enumerate(pipe_board):

            $ row = i // PIPE_COLS
            $ col = i % PIPE_COLS

            $ px = board_x + col * cell_size
            $ py = board_y + row * cell_size

            $ image_path = PIPE_IMAGES[(cell[0], cell[1])]

            # START
            if i == 0:

                add Transform(
                    "images/minigame/pipe/pipe_start.png",
                    zoom=2
                ):
                    xpos px
                    ypos py

            # FINISH
            elif i == len(pipe_board) - 1:

                add Transform(
                    "images/minigame/pipe/pipe_done.png",
                    zoom=2
                ):
                    xpos px
                    ypos py

            # BLACK: tidak bisa diputar
            elif cell[1]:

                add Transform(
                    image_path,
                    zoom=2,
                    rotate=cell[2]
                ):
                    xpos px
                    ypos py

            # BROWN: bisa diputar
            else:

                imagebutton:
                    idle Transform(
                        image_path,
                        zoom=2,
                        rotate=cell[2]
                    )

                    hover Transform(
                        image_path,
                        zoom=2,
                        rotate=cell[2]
                    )

                    xpos px
                    ypos py

                    action Function(pipe_rotate, i)


    if pipe_is_solved():

        frame:
            xalign 0.5
            yalign 0.95

            vbox:
                spacing 8

                text "SEMUA PIPA TERSAMBUNG!" color "#40e68b"

                textbutton "LANJUT":
                    xalign 0.5
                    action Return(True)

    else:

        textbutton "KELUAR":
            xalign 0.95
            yalign 0.95
            action Return(False)


init python:
    import random
    LAKE_FISH_IMAGES = [
    "images/minigame/lake/fish_1.webp",
    "images/minigame/lake/fish_2.webp",
    "images/minigame/lake/fish_3.webp",
    "images/minigame/lake/fish_4.webp",
    ]
    LAKE_TRASH_IMAGES = [
        "images/minigame/lake/fish_trash_1.png",
        "images/minigame/lake/fish_trash_2.png",
        "images/minigame/lake/fish_trash_3.png",
    ]
    LAKE_HEALTH_IMAGES = [
        "images/minigame/healthbar/1.png",
        "images/minigame/healthbar/2.png",
        "images/minigame/healthbar/3.png",
        "images/minigame/healthbar/4.png",
    ]
    LAKE_TRASH_PER_ROUND = [3, 5, 8]
    LAKE_SHUFFLE_SECONDS = [8, 6, 4]
    LAKE_MISTAKE_LIMIT = 3
    LAKE_TIME_LIMIT = 40
    LAKE_GRID_COLS = 8
    LAKE_GRID_ROWS = 4

    LAKE_CELL_SIZE = min(
        config.screen_width // LAKE_GRID_COLS,
        config.screen_height // (LAKE_GRID_ROWS + 1)
)

    lake_round = 0              # 0, 1, 2
    lake_trash_left = 0         # trash clicks still needed this round
    lake_mistakes = 0
    lake_time_left = LAKE_TIME_LIMIT
    lake_since_shuffle = 0
    lake_cells = []             # each cell: [image, is_trash, flipped]
    lake_shake = False
    lake_failed = False
    lake_between = False 

    def lake_generate_grid():
        # a brand new grid: every cell is a random fish, except ONE trash fish
        total = LAKE_GRID_COLS * LAKE_GRID_ROWS
        trash_slot = random.randint(0, total - 1)
        cells = []
        for i in range(total):
            flipped = random.choice([True, False])
            if i == trash_slot:
                cells.append([random.choice(LAKE_TRASH_IMAGES), True, flipped])
            else:
                cells.append([random.choice(LAKE_FISH_IMAGES), False, flipped])
        return cells

    def lake_begin_round():
        global lake_trash_left, lake_cells, lake_since_shuffle, lake_between
        lake_trash_left = LAKE_TRASH_PER_ROUND[lake_round]
        lake_cells = lake_generate_grid()
        lake_since_shuffle = 0
        lake_between = False
        renpy.restart_interaction()

    def lake_start():
        global lake_round, lake_mistakes, lake_time_left
        global lake_shake, lake_failed, lake_between
        lake_round = 0
        lake_mistakes = 0
        lake_time_left = LAKE_TIME_LIMIT
        lake_shake = False
        lake_failed = False
        lake_between = False
        lake_begin_round()

    def lake_pick(index):
        global lake_trash_left, lake_mistakes, lake_shake, lake_failed
        global lake_between, lake_round, lake_cells, lake_since_shuffle
        if lake_between or lake_failed:
            return
        cell = lake_cells[index]

        if cell[1]:
            # clicked the trash fish
            lake_trash_left -= 1
            renpy.play("audio/sfx/right_input.ogg", channel="sfx")
            if lake_trash_left <= 0:
                # round cleared
                lake_round += 1
                if lake_round < len(LAKE_TRASH_PER_ROUND):
                    lake_between = True   # show banner, then next round
            else:
                # instantly refresh: brand new fish, new single trash fish
                lake_cells = lake_generate_grid()
                lake_since_shuffle = 0
        else:
            # clicked a normal fish
            lake_mistakes += 1
            lake_shake = True
            renpy.play("audio/sfx/wrong_input.ogg", channel="sfx")
            if lake_mistakes >= LAKE_MISTAKE_LIMIT:
                lake_failed = True
        renpy.restart_interaction()

    def lake_tick():
        # called once per second
        global lake_time_left, lake_since_shuffle, lake_cells
        if lake_between or lake_failed or lake_round >= len(LAKE_TRASH_PER_ROUND):
            return
        lake_time_left = max(0, lake_time_left - 1)
        lake_since_shuffle += 1
        if lake_since_shuffle >= LAKE_SHUFFLE_SECONDS[lake_round]:
            # too slow: refresh the grid (still only one trash fish)
            lake_cells = lake_generate_grid()
            lake_since_shuffle = 0
        renpy.restart_interaction()

    def lake_clear_shake():
        global lake_shake
        lake_shake = False
        renpy.restart_interaction()


screen lake_game(win_label, lose_label):
    modal True

    # one timer for everything (countdown + reshuffle)
    timer 1.0 repeat True action Function(lake_tick)

    if lake_shake:
        timer 0.3 action Function(lake_clear_shake)

    # ---- end conditions ----
    if lake_time_left <= 0 or lake_failed:
        timer 0.6 action Jump(lose_label)
    if lake_round >= len(LAKE_TRASH_PER_ROUND):
        timer 0.6 action Jump(win_label)

    # ---- banner between rounds ----
    if lake_between:
        timer 1.5 action Function(lake_begin_round)

    fixed:
        xsize config.screen_width
        ysize config.screen_height

        # replace "black" with your lake background image if you have one
        add "black"

        if lake_between:
            text "ROUND [lake_round + 1]":
                xalign 0.5 yalign 0.5 size 200 color "#ffffff"

        elif lake_round < len(LAKE_TRASH_PER_ROUND):
            # ---- fish grid ----
            grid LAKE_GRID_COLS LAKE_GRID_ROWS spacing -20:
                xalign 0.5 yalign 0.55
                for i, cell in enumerate(lake_cells):
                    imagebutton:
                        idle cell[0]
                        hover cell[0]
                        xysize (LAKE_CELL_SIZE, LAKE_CELL_SIZE)
                        at lake_swim(cell[2]), (lake_shake_tf if lake_shake else lake_still)
                        action Function(lake_pick, i)

            # ---- HUD ----
            text "ROUND [lake_round + 1] / [len(LAKE_TRASH_PER_ROUND)]":
                xalign 0.05 ypos 50 size 70 color "#ffffff"

            # health bar: 1.png full, 2.png 1/3 lost, 3.png 2/3 lost, 4.png dead
            add LAKE_HEALTH_IMAGES[min(lake_mistakes, len(LAKE_HEALTH_IMAGES) - 1)]:
                xalign 0.5 ypos 30

            text "[int(lake_time_left)]":
                xalign 0.95 ypos 50 size 100 color "#8c3434"


## ---- Transforms ----
transform lake_still:
    xoffset 0

transform lake_shake_tf:
    linear 0.05 xoffset -8
    linear 0.05 xoffset 8
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset 0

# gentle bobbing so every fish looks like it's swimming; flipped = faces the other way
transform lake_swim(flipped=False):
    xzoom (-1.0 if flipped else 1.0)
    subpixel True
    block:
        ease renpy.random.uniform(0.8, 1.6) yoffset -8
        ease renpy.random.uniform(0.8, 1.6) yoffset 8
        repeat


label lake_test:
    scene black
    $ lake_start()
    call screen lake_game("lake_win", "lake_lose")


