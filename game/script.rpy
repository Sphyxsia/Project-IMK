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
define k = Character('Kiki', color="#005F99")          
define a = Character('Adek Kiki', color="#B36B00")   
define i = Character('Ibu', color="#9E3B18")         
define b = Character('Bapak', color="#2B5B6C")     
define d = Character('Pak Darto', color="#2E6B27")   
define tk1 = Character('Reza', color="#C44900")       
define tk2 = Character('Dinda', color="#A81C48")      
define pr = Character('Pak Rakha', color="#4F2D9E")   
define s = Character('Siska', color="#9E2A2B")        
define nco = Character('???', color="#3D444D")        
define nce = Character('???', color="#3D444D")
define aco = Character('???', color="#3D444D")
define ace = Character('???', color="#3D444D")
define pn = Character('Panitia', color="#0E665E")      
define kr = Character('Kiki & Reza', color="#4A701C") 
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

    jump bab2


label m1_gagal:

    "Kiki menemukan bahwa urutan perangkatnya belum tepat. Ia memeriksa kembali diagram energi yang pernah dipelajari."
    
    k "Oh, urutannya belum benar. Aku perlu memahami fungsi setiap perangkat dengan lebih baik."

    k "Aku tetap bisa belajar dari kesalahan ini."

    jump bab2


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
        jump pipe_win
    else:
        jump pipe_lose


label pipe_win:

    k "Yes! Semua pipanya sudah tersambung!"

    $ minigame += 1

    jump bab3


label pipe_lose:

    k "Sepertinya aku perlu mencoba lagi nanti."

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


default pipe_board = set()

init python:

    import pygame_sdl2 as pygame

    # ---------------- LEVEL (edit di sini) ----------------
    # '#' = dinding (tidak bisa diisi)
    # '.' = koridor
    # angka = node checkpoint (juga koridor)
    PIPE_MAP = [
        "1..2#.5",
        "#.#.#..",
        "......#",
        ".#3#.#.",
        "....4..",
    ]

    # Segmen oranye yang sudah ada di awal (petunjuk), pasangan sel (baris, kolom)
    PIPE_HINT_EDGES = [
        ((0, 0), (0, 1)),
    ]

    # ---------------- TAMPILAN ----------------
    PIPE_CELL = 120        # ukuran satu kotak grid (px)
    PIPE_LANE = 40         # lebar koridor
    PIPE_INK = 16          # tebal garis oranye
    PIPE_DEAD = 16         # zona netral di sekitar titik tengah kotak
    PIPE_HIT = 22          # toleransi kursor ke kiri/kanan koridor

    PIPE_PAPER = (230, 216, 181, 255)
    PIPE_GRID = (207, 192, 154, 255)
    PIPE_WALL = (110, 96, 66, 255)
    PIPE_LANE_COLOR = (255, 250, 238, 255)
    PIPE_ORANGE = (255, 138, 31, 255)
    PIPE_DARK = (74, 63, 42, 255)
    PIPE_WHITE = (255, 255, 255, 255)

    PIPE_ROWS = len(PIPE_MAP)
    PIPE_COLS = len(PIPE_MAP[0])

    # ---------------- DATA LEVEL ----------------

    def pipe_edge(a, b):
        """Segmen = pasangan dua sel bersebelahan, selalu terurut."""
        return tuple(sorted((a, b)))

    def pipe_build():
        cells = set()
        nodes = {}
        for r, row in enumerate(PIPE_MAP):
            for c, ch in enumerate(row):
                if ch != "#":
                    cells.add((r, c))
                    if ch.isdigit():
                        nodes[int(ch)] = (r, c)

        # Segmen hanya ada antara dua sel koridor yang bersebelahan.
        # Karena itu garis TIDAK bisa melompat lewat dinding.
        edges = []
        for (r, c) in sorted(cells):
            for dr, dc in ((0, 1), (1, 0)):
                n = (r + dr, c + dc)
                if n in cells:
                    edges.append(pipe_edge((r, c), n))
        return cells, nodes, edges

    PIPE_CELLS, PIPE_NODES, PIPE_EDGES = pipe_build()

    def pipe_center(cell):
        return (cell[1] * PIPE_CELL + PIPE_CELL // 2,
                cell[0] * PIPE_CELL + PIPE_CELL // 2)

    # ---------------- LOGIKA ----------------

    def pipe_generate_board():
        """Mulai level dari awal (tanpa refresh layar)."""
        store.pipe_board = set(pipe_edge(a, b) for a, b in PIPE_HINT_EDGES)

    def pipe_reset():
        """Dipakai tombol RESET."""
        pipe_generate_board()
        renpy.restart_interaction()

    def pipe_reach(start):
        """Semua sel yang bisa dicapai dari 'start' lewat segmen oranye."""
        adj = {}
        for a, b in store.pipe_board:
            adj.setdefault(a, set()).add(b)
            adj.setdefault(b, set()).add(a)

        seen = set([start])
        stack = [start]
        while stack:
            cur = stack.pop()
            for nxt in adj.get(cur, ()):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return seen

    def pipe_status():
        """{nomor: True/False}. True (centang) bila node tersambung ke node lain."""
        status = {}
        for num, cell in PIPE_NODES.items():
            reach = pipe_reach(cell)
            status[num] = any(
                other != cell and other in reach
                for other in PIPE_NODES.values()
            )
        return status

    def pipe_is_solved():
        """Menang bila semua node ada dalam satu rangkaian."""
        first = PIPE_NODES[min(PIPE_NODES)]
        reach = pipe_reach(first)
        return all(cell in reach for cell in PIPE_NODES.values())

    def pipe_edge_at(x, y):
        """Segmen koridor di bawah kursor (atau None)."""
        for e in PIPE_EDGES:
            x1, y1 = pipe_center(e[0])
            x2, y2 = pipe_center(e[1])
            if y1 == y2:        # horizontal
                lo = min(x1, x2) + PIPE_DEAD
                hi = max(x1, x2) - PIPE_DEAD
                if lo <= x <= hi and abs(y - y1) <= PIPE_HIT:
                    return e
            else:               # vertikal
                lo = min(y1, y2) + PIPE_DEAD
                hi = max(y1, y2) - PIPE_DEAD
                if lo <= y <= hi and abs(x - x1) <= PIPE_HIT:
                    return e
        return None

    # ---------------- PAPAN (gambar + input mouse) ----------------

    class PipeBoard(renpy.Displayable):

        def __init__(self, **kwargs):
            super(PipeBoard, self).__init__(**kwargs)
            self.dragging = False
            self.mode = "fill"          # "fill" atau "erase"
            self.visited = set()
            self.last_edge = None
            self.last_pos = (0, 0)

        # ---- gambar ----
        def render(self, width, height, st, at):
            w = PIPE_COLS * PIPE_CELL
            h = PIPE_ROWS * PIPE_CELL
            rv = renpy.Render(w, h)
            cv = rv.canvas()

            # kertas + grid
            cv.rect(PIPE_PAPER, (0, 0, w, h))
            for i in range(PIPE_COLS + 1):
                cv.line(PIPE_GRID, (i * PIPE_CELL, 0), (i * PIPE_CELL, h), 1)
            for i in range(PIPE_ROWS + 1):
                cv.line(PIPE_GRID, (0, i * PIPE_CELL), (w, i * PIPE_CELL), 1)

            # koridor: garis tepi dulu, lalu isi
            for width_, color in ((PIPE_LANE + 6, PIPE_WALL),
                                  (PIPE_LANE, PIPE_LANE_COLOR)):
                half = width_ // 2
                for cell in PIPE_CELLS:
                    x, y = pipe_center(cell)
                    cv.rect(color, (x - half, y - half, width_, width_))
                for e in PIPE_EDGES:
                    cv.line(color, pipe_center(e[0]), pipe_center(e[1]), width_)

            # tinta oranye
            for e in store.pipe_board:
                p1 = pipe_center(e[0])
                p2 = pipe_center(e[1])
                cv.line(PIPE_ORANGE, p1, p2, PIPE_INK)
                cv.circle(PIPE_ORANGE, p1, PIPE_INK // 2)
                cv.circle(PIPE_ORANGE, p2, PIPE_INK // 2)

            # node checkpoint
            status = pipe_status()
            for num, cell in PIPE_NODES.items():
                x, y = pipe_center(cell)
                ok = status[num]
                ring = PIPE_ORANGE if ok else PIPE_DARK

                cv.circle(PIPE_WHITE, (x, y), 24)
                cv.circle(ring, (x, y), 24, 4)

                if ok:
                    # centang
                    cv.lines(PIPE_ORANGE, False,
                             [(x - 10, y), (x - 3, y + 9), (x + 11, y - 9)], 5)
                else:
                    # silang
                    cv.line(PIPE_DARK, (x - 9, y - 9), (x + 9, y + 9), 4)
                    cv.line(PIPE_DARK, (x - 9, y + 9), (x + 9, y - 9), 4)

                # nomor di pojok kiri atas node
                txt = renpy.render(
                    Text(str(num), size=26, color="#4a3f2a", bold=True),
                    w, h, st, at)
                tw, th = txt.get_size()
                rv.blit(txt, (x - 32 - tw / 2.0, y - 32 - th / 2.0))

            return rv

        # ---- input ----
        def apply(self, e):
            if self.mode == "fill":
                store.pipe_board.add(e)
            else:
                store.pipe_board.discard(e)
            self.visited.add(e)
            self.last_edge = e
            renpy.redraw(self, 0)

        def drag_to(self, x, y):
            px, py = self.last_pos
            dist = max(abs(x - px), abs(y - py))
            steps = max(1, int(dist // 6))     # titik antara, supaya tidak ada segmen terlewat

            for s in range(1, steps + 1):
                sx = px + (x - px) * s / float(steps)
                sy = py + (y - py) * s / float(steps)
                e = pipe_edge_at(sx, sy)

                if e is None or e in self.visited:
                    continue

                # harus menyambung dari segmen sebelumnya (tidak boleh melompat)
                if self.last_edge is not None and not (set(e) & set(self.last_edge)):
                    continue

                self.apply(e)

            self.last_pos = (x, y)

        def event(self, ev, x, y, st):

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                e = pipe_edge_at(x, y)
                if e is not None:
                    self.dragging = True
                    self.visited = set()
                    self.last_edge = None
                    self.last_pos = (x, y)
                    # klik di koridor kosong = isi, di koridor oranye = hapus
                    self.mode = "erase" if e in store.pipe_board else "fill"
                    self.apply(e)

            elif ev.type == pygame.MOUSEMOTION and self.dragging:
                if ev.buttons[0]:
                    self.drag_to(x, y)
                else:
                    self.dragging = False
                    renpy.restart_interaction()

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1 and self.dragging:
                self.dragging = False
                renpy.restart_interaction()     # cek menang di screen

            return None


# ============================================================
#  SCREEN
# ============================================================

screen pipe_puzzle():

    modal True

    add "#2b2417"

    text "PLAN OF ESCAPE ROUTE":
        xalign 0.5
        ypos 14
        size 34
        color "#ffffff"

    text "Seret di lorong untuk menggambar jalur. Klik jalur oranye untuk menghapusnya.":
        xalign 0.5
        ypos 62
        size 18
        color "#dddddd"

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (PIPE_COLS * PIPE_CELL, PIPE_ROWS * PIPE_CELL)
        add PipeBoard()

    textbutton "RESET":
        xalign 0.97
        ypos 20
        text_size 28
        text_color "#ff8a1f"
        text_hover_color "#ffffff"
        action Function(pipe_reset)

    if pipe_is_solved():

        frame:
            xalign 0.5
            yalign 0.95

            vbox:
                spacing 8

                text "Completed!" color "#ff8a1f" size 34 xalign 0.5

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


