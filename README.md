# PBP - Welcome to T-Pos- I mean T-Shop
An E-Commerce Web for... well... to buy and sell stuff 😁

## Tugas 2 - PBP 2024/2025 Gasal
**Implementasi?**
1. **Punya koneksi internet, laptop dengan IDE, dan motivasi untuk melakukan**
2. **Membuat sebuah proyek Django baru**
- Buat repo/direktori/folder baru
- Buat virtual environment dan jalankan
- Install Django dan dependencies lainnya (jika ada)
- Setelah udh siap semua, jalankan perintah `python manage.py startproject [nama project] .` untuk membuat proyeknya. Perintah yang saya jalankan adalah `python manage.py startproject my_e_commerce .`
3. **Membuat aplikasi dengan nama main pada proyek tersebut**
- Setelah buat proyek, jalankan perintah `python manage.py startapp main` agar Django membuat aplikasi main dan berkas2 yang dibutuhkan seperti `views.py`
4. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
- Di `/my_e_commerce/urls.py` import `path` dan `include` dari module `django.urls`
- Di variabel list `urlpatterns`, tambahkan elemen `path("", include("main.urls"))` yang akan mengarahkan ke tampilan templates di `main`
5. **Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut**
- Di `/main/models.py` import `models` dari module `django.db`
- Buat class bernama `Product` dengan inheritance ke class `models.Model` sebagai superclass-nya
- Di dalam class `Product` buatlah atribut `name` dengan tipe `CharField` dengan `max_length=70`, `price` dengan tipe `IntegerField`, dan `description` dengan tipe `TextField`
- Jalankan perintah `python manage.py makemigrations` untuk membuat migrasi model
- Jalankan perintah `python manage.py migrate` untuk menerapkan migrasinya
6. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**
- Di `/main/` buatlah folder baru bernama `templates`
- Di `/main/templates/` buatlah berkas HTML baru, saya buatnya `index.html`
- Di `/main/views.py` import `render` dari module `django.shortcuts`
- Buatlah fungsi yang menerima argumen `request`, saya buatnya `index(request)`
- Di dalam fungsinya, buatlah variabel bertipe dictionary yang didalamnya berisi nama aplikasi, nama, dan kelas
- Di `/main/templates/index.html` buatlah html yg akan memunculkan judul, nama, dan kelas
7. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**
- Di `/main/` buatlah berkas baru bernama `urls.py`
- Di `/main/urls.py` import `path` dari module `django.urls` dan import `index` dari module `main.views`
- Buat variabel `app_name` dengan nilai `"main"`
- Buat variabel bertipe list `urlpatterns` dan tambahkan elemen `path('', index, name="index")` agar dapat memetakannya
8. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**
- Buat repo di github dan push ke github
- Buat proyek baru di PWS
- Tambahkan url PWS ke `/my_e_commerce/settings.py` (push ke github jika mau)
- Push repo lokal ke PWS
- Build dan running proyeknya di PWS
9. **Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut**
- Buat README.md dan kasih deskripsi sedikit tentang proyeknya dan jawab pertanyaannya (Oh no recursive ヽ(ﾟДﾟ)ﾉ)

**Bagan**

![bagan django](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/Bagan%20Django.png)

**Fungsi Git? 🛠️**

Git adalah sistem kontrol versi yang memungkinkan pengembang melacak perubahan kode, bekerja secara kolaboratif, dan mengelola berbagai versi perangkat lunak. Dengan fitur branching dan merging, Git memfasilitasi pengembangan fitur baru tanpa mempengaruhi kode utama dan membantu menyelesaikan konflik perubahan. Sistem ini terdistribusi, memberikan setiap pengembang salinan lengkap dari proyek, sehingga meningkatkan keandalan dan keamanan data. Git juga mendukung integrasi dengan alat otomatisasi untuk build, pengujian, dan deployment, mempermudah proses pengembangan perangkat lunak modern.

**Kenapa Django? ❓**

Django sering jadi pilihan pertama untuk belajar pengembangan perangkat lunak karena kemudahan yang ditawarkannya. Dengan fitur-fitur bawaan seperti sistem autentikasi dan panel admin, kita bisa fokus pada logika aplikasi tanpa terlalu pusing memikirkan detail teknis. Dokumentasinya yang lengkap dan komunitasnya yang aktif juga bikin belajar jadi lebih lancar. Plus, strukturnya yang jelas membantu kamu memahami praktik terbaik dalam coding. Jadi, Django bukan hanya memudahkan belajar, tapi juga memberi pondasi kuat untuk proyek-proyek yang lebih besar nanti.

**Mengapa model pada Django disebut sebagai ORM?**

Model di Django disebut ORM (Object-Relational Mapping) karena mereka menghubungkan objek Python dengan tabel basis data. Dengan ORM, kita dapat berinteraksi dengan data menggunakan metode Python daripada menulis SQL langsung. Setiap model Django mewakili tabel di basis data, dan atribut dalam model menjadi kolom tabel tersebut, menyederhanakan pengelolaan data dan relasi antar tabel.
