# PBP - Welcome to T-Pos- I mean T-Shop
An E-Commerce Web for... well... to buy and sell stuff 😁

#### Deployment 🌐
[http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/](http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/)

## Tugas 4 - PBP 2024/2025 Gasal

**Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**

Dalam Django, `HttpResponseRedirect()` dan `redirect()` digunakan untuk mengalihkan pengguna ke halaman lain. `HttpResponseRedirect()` adalah kelas yang memberikan kontrol penuh atas respons HTTP redirect, memungkinkan kustomisasi yang lebih mendalam. Sementara itu, `redirect()` adalah fungsi shortcut yang lebih sederhana dan sering digunakan untuk redirect dasar. `HttpResponseRedirect()` lebih fleksibel namun memerlukan pemahaman yang lebih baik tentang HTTP, sedangkan `redirect()` lebih mudah digunakan dan cocok untuk sebagian besar kasus.

---

**Jelaskan cara kerja penghubungan model `Product` dengan `User`!**

Di Django, hubungan antara model memungkinkan kita untuk menghubungkan data yang berbeda. Model `Product` dapat dihubungkan dengan model `User` menggunakan `ForeignKey` untuk menunjukkan bahwa setiap produk memiliki seorang pemilik.

---

**Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Authentication adalah proses memverifikasi identitas pengguna, biasanya melalui username dan password, sedangkan authorization menentukan izin pengguna setelah mereka terautentikasi. Dalam proses login, autentikasi dilakukan terlebih dahulu untuk memastikan identitas pengguna, diikuti oleh otorisasi untuk mengatur akses mereka ke sumber daya tertentu. Django mengimplementasikan autentikasi dengan sistem built-in yang memungkinkan pengguna untuk login dan logout melalui model `User`, menggunakan fungsi `authenticate()` dan `login()`, sementara otorisasi dikelola melalui permission dan groups, serta decorators seperti `@login_required` untuk membatasi akses ke view tertentu.

---

**Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django mengingat pengguna yang telah login melalui sesi dan cookies, yang menyimpan informasi seperti ID pengguna di browser. Selain untuk autentikasi, cookies juga digunakan untuk menyimpan preferensi pengguna, keranjang belanja, dan lain lain. Namun, tidak semua cookies aman, risiko seperti pencurian cookie, XSS, dan CSRF dapat terjadi jika tidak dilindungi dengan baik.

---

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**
- Buka `/main/views.py`, import `UserCreationForm` dan `AuthenticationForm` dari module `django.contrib.auth.forms`, `authenticate`, `login`, dan `logout` dari module `django.contrib.auth` ,dan `messages` dari module `django.contrib`
- Buat fungsi register(), login_user(), dan logout_user() di `/main/views.py`
- Buat dan modif berkas html-html di `/templates/` untuk presentasi register, login, dan logout
- Buka `/main/urls.py`, import `register`, `login_user`, dan `logout_user` dari module `main.views`, dan tambahkan `path` ke `urlpatterns` untuk routing URL's
- Buka `/main/views.py`, import `login_required` dari module `django.contrib.auth.decorators`, dan tambahkan decorators `@login_required(login_url='/login')` di atas function `index()`

2. **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal**
- Register dua akun
- Login salah satu akun
- Buat tiga product
- Logout
- Login ke akun satunya lagi
- Buat tiga product
- Logout

3. **Menghubungkan model Product dengan User**
- Buka `/main/models.py` dan import `User` dari module `django.contrib.auth.models`
- Tambahkan data field `user` dengan nilai `models.ForeignKey(User, on_delete=models.CASCADE)`
- Buka `/main/views.py` dan modif function `create_product()` di bagian block code `if form.is_valid() and request.method == "POST":` dari
```python
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:index")
```
menjadi
```python
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:index")
```
- Modif bagian function `index()` untuk `product_entries`
- Jalankan `python manage.py makemigrations` dan `python manage.py migrate`

4. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi**
- Import `datetime`, `HttpResponseRedirect` dari module `django.http`, dan `reverse` dari module `django.urls`
- Modif `login_user()` utk bagian block code `if form.is_valid():` dari
```python
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:index')
```
menjadi
```python
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:index"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return respone
```
- Buka `/main/views.py` dan modif function `index()` utk value dari key `name` untuk disesuaikan dengan usernya dan tambahkan key `last_login` dengan value `request.COOKIES['last_login']`
- Modif fungsi `logout_user()` dengan menambahkan `response = HttpResponseRedirect(reverse('main:login'))` dan `response.delete_cookie('last_login')` serta modif return menjadi `return response`
- Modif berkas html `/main/templates/index.html` untuk menampilkannya.