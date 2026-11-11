# Kamu dapat taruh script game mu di file ini.
define config.mouse = {
    "default": [
        ("gui/cursor/cursor_main_button.png", 0, 0)
    ],
    "button": [
        ("gui/cursor/cursor_main_pressed.png", 5, 0)
    ]
}

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg room1 = "images/bg/room_night.jpg"
image bg room2 = "images/bg/room.jpg"
image bg class = "images/bg/campus_inside.png"
image bg street = "images/bg/street_morning.jpg"
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
    jump bab3

label bab3:

    "Kiki sampai di sebuah danau."

    "Ia melihat banyak sampah yang mengotori air."

    k "Aku harus membersihkan sampah ini!"

    $ lake_start()

    call screen lake_game("lake_win", "lake_lose")

    return


init python:
    import random
    LAKE_FISH_IMAGES = [
    "images/lake/fish_1.webp",
    "images/lake/fish_2.webp",
    "images/lake/fish_3.webp",
    "images/lake/fish_4.webp",
    ]
    LAKE_TRASH_IMAGES = [
        "images/lake/fish_trash_1.png",
        "images/lake/fish_trash_2.png",
        "images/lake/fish_trash_3.png",
    ]
    LAKE_HEALTH_IMAGES = [
        "images/healthbar/1.png",
        "images/healthbar/2.png",
        "images/healthbar/3.png",
        "images/healthbar/4.png",
    ]
    LAKE_TRASH_PER_ROUND = [3, 5, 8]
    LAKE_SHUFFLE_SECONDS = [8, 6, 4]
    LAKE_MISTAKE_LIMIT = 3
    LAKE_TIME_LIMIT = 40
    LAKE_GRID_COLS = 8
    LAKE_GRID_ROWS = 4
    LAKE_CELL_SIZE = 250

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
        xsize 2560 ysize 1440

        # replace "black" with your lake background image if you have one
        add "black"

        if lake_between:
            text "ROUND [lake_round + 1]":
                xalign 0.5 yalign 0.5 size 200 color "#ffffff"

        elif lake_round < len(LAKE_TRASH_PER_ROUND):
            # ---- fish grid ----
            grid LAKE_GRID_COLS LAKE_GRID_ROWS spacing 0:
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


## ---------------------------------------------------------------
## TEST LABELS (delete these once it works in your real script)
## ---------------------------------------------------------------
label lake_test:
    scene black
    $ lake_start()
    call screen lake_game("lake_win", "lake_lose")

label lake_win:
    "You cleaned the lake!"
    jump bab3

label lake_lose:
    "You lost... try again."
    jump lake_test
