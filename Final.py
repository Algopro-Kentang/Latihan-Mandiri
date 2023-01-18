import tkinter as tk
from tkinter import ttk
import planet
import math
from PIL import Image, ImageTk

# Base Frame
root = tk.Tk()
root.geometry("1920x1080")

# Frame Notebook
my_notebook = ttk.Notebook(root)
my_notebook.pack(fill="both", expand=True)

# Frame untuk halaman dasar
my_home = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_home.pack(fill="both", expand=1)

# Frame untuk matahari
my_matahari = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_matahari.pack(fill="both", expand=1)
show_matahari = ImageTk.PhotoImage(Image.open("Sun.jpg").resize((900, 500)))

# Frame untuk Merkurius
my_merkurius = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_merkurius.pack(fill="both", expand=1)
show_merkurius = ImageTk.PhotoImage(Image.open("Mercury.jpg").resize((800, 533)))

# Frame Venus
my_venus = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_venus.pack(fill="both", expand=1)
show_venus = ImageTk.PhotoImage(Image.open("Venus.jpg").resize((650, 433)))

# Frame Bumi
my_bumi = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_bumi.pack(fill="both", expand=1)
show_bumi = ImageTk.PhotoImage(Image.open("Earth.jpg").resize((700, 700)))

# Frame Mars
my_mars = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_mars.pack(fill="both", expand=1)
show_mars = ImageTk.PhotoImage(Image.open("Mars.jpeg").resize((900, 600)))

# Frame Jupiter
my_jupiter = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_jupiter.pack(fill="both", expand=1)
show_jupiter = ImageTk.PhotoImage(Image.open("Jupiter.jpg").resize((650, 650)))

# Frame Saturnus
my_saturnus = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_saturnus.pack(fill="both", expand=1)
show_saturnus = ImageTk.PhotoImage(Image.open("Saturnus.jpeg").resize((700, 467)))

# Frame Uranus
my_uranus = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_uranus.pack(fill="both", expand=1)
show_uranus = ImageTk.PhotoImage(Image.open("Uranus.jpg"))

# Frame Neptunus
my_neptunus = tk.Frame(my_notebook, width=1920, height=1080, background="black")
my_neptunus.pack(fill="both", expand=1)
show_neptunus = ImageTk.PhotoImage(Image.open("Neptune.jpeg").resize((600, 600)))

# Menambahkan Button
def button():
    my_notebook.add(my_home, text="Home")
    my_notebook.add(my_matahari, text="Matahari")
    my_notebook.add(my_merkurius, text="Merkurius")
    my_notebook.add(my_venus, text="Venus")
    my_notebook.add(my_bumi, text="Bumi")
    my_notebook.add(my_mars, text="Mars")
    my_notebook.add(my_jupiter, text="Jupiter")
    my_notebook.add(my_saturnus, text="Saturnus")
    my_notebook.add(my_uranus, text="Uranus")
    my_notebook.add(my_neptunus, text="Neptunus")

# Isi pada page Home
def Home():
    judul_home = tk.Label(my_home, text="Kelompok Kentang", background="black", foreground="white", font=("Times New Roman", 48))
    tekt_home = tk.Label(my_home, text="""1. Damara Brian Rakasiwi\t\t(L200220229)
2. Achmad Mustofa\t\t\t(L200220239)
3. Nazwa Diajeng Istika R\t\t(L200220251)
4. Faizal Dwi Saputra\t\t(L200220257)
5. Ikhlasul Rafid Naufaltama\t\t(L200220258)
6. Ulinnuha\t\t\t(L200220265)
7. Muhammad Aksal Pratama\t\t(L200220269)
8. Tutut Bagiawati\t\t\t(L200220283)""", foreground="white", background="black", font=("Times New Roman", 28))
    judul_home.pack()
    tekt_home.place(relx=0.01, rely=0.1)
    button()

# Isi pada page Matahari
def Matahari():
    matahari = planet.Planet()
    judul_matahari = tk.Label(my_matahari, text="Matahari", background="black", foreground="white", font=("Times New Roman", 48))
    teks_matahari = ttk.Label(my_matahari, text=f"""Matahari atau Surya adalah bintang di pusat tata surya.
Bentuknya nyaris bulat dan terdiri dari plasma panas bercampur medan magnet.
Diameternya sekitar 1.392.684 km,kira-kira 109 kali diameter Bumi, 
dan massanya (sekitar 2×1030 kilogram, 330.000 kali massa Bumi) mewakili kurang lebih 99,86 % massa total tata surya. 
Matahari merupakan benda langit terbesar di galaksi Bima Sakti yang besarnya bahkan 10 kali planet terbesar tata surya, Jupiter.

Luas permukaan Matahari adalah {math.ceil(matahari.luas()):,} km²
Volume Matahari adalah {math.ceil(matahari.volume()):,} km³""", background="black", foreground="white", font=("Times New Roman", 24))
    gambar_matahari = tk.Label(my_matahari, image=show_matahari)
    judul_matahari.pack()
    teks_matahari.place(relx=0.01, rely=0.1)
    gambar_matahari.place(relx=0.26, rely=0.45)
    Home()

# Isi pada page Merkurius
def Merkurius():
    merkurius = planet.Planet(2439.5)
    judul_merkurius = tk.Label(my_merkurius, text="Merkurius", background="black", foreground="white", font=("Times New Roman", 48))
    isi_merkurius = ttk.Label(my_merkurius, text=f"""Merkurius adalah planet terkecil di Tata Surya sekaligus yang terdekat dari Matahari. 
Periode revolusi planet ini merupakan yang terpendek dari semua planet di Tata Surya, yakni 87,79 hari. 
Seperti halnya Venus, Merkurius merupakan planet inferior yang letak orbitnya berada di sebelah dalam orbit Bumi, dan ketika diamati dari Bumi, 
jarak sudutnya dari Matahari tidak pernah melebihi 28°. 
Karena jarak yang dekat dengan Matahari, planet ini hanya dapat dilihat di dekat ufuk barat setelah matahari terbenam atau ufuk timur sebelum matahari terbit, 
atau biasanya ketika aram. Merkurius akan tampak seperti bintang yang terang jika diamati pada waktu tersebut, 
tetapi sering kali jauh lebih sulit untuk diamati daripada Venus. 
Jika diamati dari teleskop, Merkurius akan menampilkan serangkaian fase yang mirip dengan fase Venus dan Bulan, 
ketika bergerak di orbit bagian dalamnya yang relatif terhadap Bumi dan terjadi berulang dalam satu siklus sinodiknya, 
yakni sekitar 116 hari.

Luas Permukaan Merkurius adalah {math.ceil(merkurius.luas()):,} km²
Volume Merkurius adalah {math.ceil(merkurius.volume()):,} km³
""", background='black', foreground='white', font=("Times New Roman", 20))
    gambar_merkurius = tk.Label(my_merkurius, image=show_merkurius)
    judul_merkurius.pack()
    isi_merkurius.place(relx=0.01, rely=0.1)
    gambar_merkurius.place(relx=0.57, rely=0.4)
    Matahari()

# Isi pada page Venus
def Venus():
    venus = planet.Planet(6046)
    judul_venus = tk.Label(my_venus, text="Venus", background="black", foreground="white", font=("Tiems New Roman", 48))
    text_venus = ttk.Label(my_venus, text=f"""Venus adalah planet terdekat kedua dari Matahari setelah Merkurius. 
Planet ini mengorbit Matahari selama 224,7 hari Bumi. 
Venus tidak memiliki satelit alami dan dinamai dari dewi cinta dan kecantikan dalam mitologi Romawi. 
Venus adalah planet kebumian dan kadang-kadang disebut planet saudara Bumi karena ukuran, gravitasi, dan komposisi yang mirip. 
Namun, dalam hal lain planet ini sangat berbeda dari Bumi. 
Planet ini memiliki atmosfer terpadat dengan terdiri dari 96% karbon dioksida.
Tekanan atmosfer permukaan Venus 92 kali lebih besar daripada Bumi.
Dengan rata-rata suhu permukaan sebesar 462 °C menjadikan Venus planet terpanas di Tata Surya.
Venus diselimuti oleh lapisan buram yang terdiri dari awan asam sulfat yang sangat reflektif,
sehingga permukaannya tidak dapat dilihat dari luar angkasa. 
Permukaan Venus sendiri bergurun, kering, dan diselingi oleh batuan yang diperbarui secara periodik oleh aktivitas vulkanik.

Luas Permukaan Venus adalah {math.ceil(venus.luas()):,} km²
Volume Venus adalah {math.ceil(venus.volume()):,} km³""", background='black', foreground='white', font=("Times New Roman", 26))
    gambar_venus = tk.Label(my_venus, image=show_venus)
    judul_venus.pack()
    text_venus.place(relx=0.01, rely=0.1)
    gambar_venus.place(relx=0.65, rely=0.55)
    Merkurius()

# Isi pada page Bumi
def Bumi():
    bumi = planet.Planet(6371)
    judul_bumi = tk.Label(my_bumi, text="Bumi", background="black", foreground="white", font=("Times New Roman", 48))
    text_bumi = ttk.Label(my_bumi, text=f"""Bumi adalah planet ketiga dari Matahari yang merupakan planet terpadat dan terbesar kelima dari delapan planet dalam Tata Surya. 
Bumi juga merupakan planet terbesar dari empat planet kebumian di Tata Surya. 
Bumi terkadang disebut dengan dunia atau Planet Biru.
Bumi terbentuk sekitar 4,54 miliar tahun yang lalu, dan kehidupan sudah muncul di permukaannya paling tidak sekitar 3,5 miliar tahun yang lalu.
Biosfer Bumi kemudian secara perlahan mengubah atmosfer dan kondisi fisik dasar lainnya, yang memungkinkan terjadinya perkembangbiakan organisme serta pembentukan lapisan ozon, 
yang bersama medan magnet Bumi menghalangi radiasi surya berbahaya dan mengizinkan makhluk hidup mikroskopis untuk berkembang biak dengan aman di daratan.
Sifat fisik, sejarah geologi, dan orbit Bumi memungkinkan kehidupan untuk bisa terus bertahan.

Luas Permukaan Bumi adalah {math.ceil(bumi.luas()):,} km²
Volume Bumi adalah {math.ceil(bumi.volume()):,} km³""", background='black', foreground='white', font=("Times New Roman", 18))
    gambar_bumi = tk.Label(my_bumi, image=show_bumi)
    judul_bumi.pack()
    text_bumi.place(relx=0.01, rely=0.1)
    gambar_bumi.place(relx=0.628, rely=0.28)
    Venus()

# Isi pada page Mars
def Mars():
    mars = planet.Planet(3396)
    judul_mars = tk.Label(my_mars, text="Mars", background="black", foreground="white", font=("Times New Roman", 48))
    teks_mars = ttk.Label(my_mars, text=f"""Planet Mars adalah planet terdekat ke 4 dari Matahari.
Planet mars memiliki julukan Red planet/Planet merah karena memiliki warna kemerah-merahan.
Adapun waktu yang diperlukan Planet Merah ini untuk mengelilingi matahari yaitu sekitar 687 hari dengan jarak rata-rata 227.000.000 km. 
Planet Mars memiliki suhu serta kelembaban dan juga masa yang sama dengan Planet Bumi yang memungkinkan makhluk hidup bisa tinggal di Planet ini. 
Planet Mars memiliki dua satelit yaitu Satelit Phobos dan Satelit Deimos.
Bukti menunjukkan bahwa planet ini pernah ditemukan oleh lebih banyak orang daripada sekarang, tetapi masih belum jelas apakah makhluk hidup pernah ada. 
“Penyelidikan” pada pertengahan tahun 1970-an melakukan eksperimen untuk mencari mikroorganisme di tanah Mars, 
eksperimen tersebut menghasilkan hasil yang positif, termasuk peningkatan sementara CO2 saat terkena udara dan nutrisi.

Luas Permukaan Mars adalah {math.ceil(mars.luas()):,} km²
Volume Planet Mars adalah {math.ceil(mars.volume()):,} km³""", foreground='white', background='black', font=("Times New Roman", 20))
    gambar_mars = tk.Label(my_mars, image=show_mars)
    judul_mars.pack()
    teks_mars.place(relx=0.01, rely=0.1)
    gambar_mars.place(relx=0.52, rely=0.37)
    Bumi()

# Isi pada page Jupiter
def Jupiter():
    jupiter = planet.Planet(69911)
    judul_jupiter = tk.Label(my_jupiter, text="Jupiter", background="black", foreground="white", font=("Times New Roman", 48))
    teks_jupiter = ttk.Label(my_jupiter, text=f"""Jupiter atau Yupiter adalah planet terdekat kelima dari Matahari setelah Merkurius, Venus, Bumi, dan Mars. 
Planet ini juga merupakan planet terbesar di Tata Surya. 
Jupiter merupakan raksasa gas dengan massa seperseribu massa Matahari dan dua setengah kali jumlah massa semua planet lain di Tata Surya. 
Planet ini dan raksasa gas lain di Tata Surya
Jupiter sebagian besar terdiri dari hidrogen dan helium. 
Seperempat massa Jupiter merupakan helium, walaupun jumlahnya hanya sepersepuluh komposisi Jupiter. 
Planet ini mungkin memiliki inti berbatu yang terdiri dari unsur-unsur berat, namun tidak memiliki permukaan yang padat layaknya raksasa gas lainnya.

Luas Permukaan Jupiter adalah {math.ceil(jupiter.luas()):,} km²
Volume Jupiter {math.ceil(jupiter.volume()):,} km³""", foreground='white', background='black', font=("Times New Roman", 20))
    gambar_jupiter = tk.Label(my_jupiter, image=show_jupiter)
    judul_jupiter.pack()
    teks_jupiter.place(relx=0.01, rely=0.1)
    gambar_jupiter.place(relx=0.655, rely=0.33)
    Mars()

# Isi pada page Saturnus
def Saturnus():
    saturnus = planet.Planet(58232)
    judul_saturnus = tk.Label(my_saturnus, text="Saturnus", background="black", foreground="white", font=("Times New Roman", 48))
    isi_saturnus = ttk.Label(my_saturnus, text=f"""Saturnus adalah planet keenam dari Matahari dan merupakan planet terbesar kedua di Tata Surya setelah Jupiter. 
Saturnus juga merupakan sebuah raksasa gas yang memiliki radius rata-rata sekitar 9 kali radius rata-rata Bumi. 
Massa jenis rata-rata Saturnus hanya 1/8 massa jenis rata-rata Bumi, tetapi dengan volume yang lebih besar dari Bumi, massa Saturnus tercatat 95 kali massa Bumi. 
Saturnus dinamai menurut dewa kesejahteraan dan agribudaya dalam mitologi Yunani; simbol astronominya (♄) melambangkan sabit yang digunakan oleh dewa tersebut.

Luas Permukaan Saturnus adalah {math.ceil(saturnus.luas()):,} km²
Volume Saturnus adalah {math.ceil(saturnus.volume()):,} km³
""", foreground='white', background='black', font=("Times New Roman", 20))
    gambar_saturnus = tk.Label(my_saturnus, image=show_saturnus)
    judul_saturnus.pack()
    isi_saturnus.place(relx=0.01, rely=0.1)
    gambar_saturnus.place(relx=0.625, rely=0.24)
    Jupiter()

# Isi pada  page Uranus
def Uranus():
    uranus = planet.Planet(25362)
    judul_uranus = tk.Label(my_uranus, text="Uranus", background="black", foreground="white", font=("Times New Roman", 48))
    isi_uranus = ttk.Label(my_uranus, text=f"""Uranus berasal dari nama Latin Ūranus untuk nama dewa Yunani Οὐρανός adalah planet ketujuh dari Matahari. 
Uranus merupakan planet yang memiliki jari-jari terbesar ketiga sekaligus massa terbesar keempat di Tata Surya. 
Uranus juga merupakan satu-satunya planet yang namanya berasal dari tokoh dalam mitologi Yunani, dari versi Latinisasi nama dewa langit Yunani Ouranos. 
Komposisi Uranus serupa dengan Neptunus, dan keduanya mempunyai komposisi kimiawi yang berbeda dari raksasa gas yang lebih besar, Jupiter dan Saturnus. 
Karenanya, para astronom sering menempatkan Uranus dan Neptunus dalam kategori raksasa es untuk membedakan keduanya dari raksasa gas. 
Atmosfer Uranus serupa dengan Jupiter dan Saturnus karena kandungan utamanya adalah hidrogen dan helium, tetapi mengandung lebih banyak unsur es seperti air, amonia dan metana, bersama dengan sisa hidrokarbon. 
Atmosfer Uranus merupakan atmosfer planet terdingin di Tata Surya, dengan suhu terendah mencapai 49 K −224 °C; −371 °F. 
Atmosfer Uranus mempunyai struktur awan berlapis-lapis dan kompleks, serta diperkirakan lapisan awan terendahnya terdiri atas air dan lapisan awan tertingginya terdiri atas metana. 
Bagian dalam Uranus sebagian besar terdiri atas es dan bebatuan.

Luas Permukaan Uranus adalah {math.ceil(uranus.luas()):,} km²
Volume Uranus adalah {math.ceil(uranus.volume()):,} km³
""", foreground='white', background='black', font=("Times New Roman", 15))
    gambar_uranus = tk.Label(my_uranus, image=show_uranus)
    judul_uranus.pack()
    isi_uranus.place(relx=0.01, rely=0.1)
    gambar_uranus.place(relx=0.6, rely=0.31)
    Saturnus()

# Isi pada page Neptunus
def Neptunus():
    neptunus = planet.Planet(24.622)
    judul_neptunus = tk.Label(my_neptunus, text="Uranus", background="black", foreground="white", font=("Times New Roman", 48))
    isi_neptunus = ttk.Label(my_neptunus, text=f"""Neptunus merupakan planet terjauh (kedelapan) jika ditinjau dari Matahari.
Planet ini dinamai dari dewa lautan Romawi. Neptunus merupakan planet terbesar keempat berdasarkan diameter (49.530 km) dan terbesar ketiga berdasarkan massa. 
Massa Neptunus tercatat 17 kali lebih besar daripada Bumi, dan sedikit lebih kecil daripada Uranus. 
Neptunus mengorbit Matahari pada jarak 30,1 sa atau sekitar 4.450 juta km. 
Periode rotasi planet ini adalah 16,1 jam, sedangkan periode revolusinya adalah 164,8 tahun.
Komposisi penyusun planet ini mirip dengan Uranus, dan komposisi keduanya berbeda dari raksasa gas Jupiter dan Saturnus.
Atmosfer Neptunus mengandung hidrogen, helium, hidrokarbon, kemungkinan nitrogen, dan kandungan es yang besar seperti es air, amonia, dan metana. 
Astronom kadang-kadang mengategorikan Uranus dan Neptunus sebagai raksasa es untuk menekankan perbedaannya.

Luas Permukaan planet ini adalah {math.ceil(neptunus.luas()):,} km²
Volume planet ini {math.ceil(neptunus.volume()):,} km³
""", foreground='white', background='black', font=("Times New Roman", 20))
    gambar_neptunus = tk.Label(my_neptunus, image=show_neptunus)
    judul_neptunus.pack()
    isi_neptunus.place(relx=0.01, rely=0.1)
    gambar_neptunus.place(relx=0.68, rely=0.37)
    Uranus()

Neptunus()
root.mainloop()