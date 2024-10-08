# PBP - Welcome to T-Pos- I mean T-Shop
An E-Commerce Web for... well... to buy and sell stuff 😁

#### Deployment 🌐
[http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/](http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/)

## Tugas 5 - PBP 2024/2025 Gasal

**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Apabila sebuah elemen memiliki beberapa definisi style, style yang akan berlaku adalah style yang memiliki prioritas paling tinggi. Urutan prioritasnya, dari yang paling tinggi ke yang paling rendah, adalah sebagai berikut: style yang ditulis langsung di dalam elemen (inline style), style yang didefinisikan dalam file style eksternal atau internal, dan terakhir style bawaan browser.

---

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

Responsive design adalah konsep penting dalam pengembangan web yang membuat tampilan situs web secara otomatis menyesuaikan diri dengan berbagai ukuran layar perangkat. Dengan responsive design, pengguna dapat mengakses situs web dengan nyaman dari berbagai perangkat, meningkatkan pengalaman pengguna, SEO, dan konversi. Contoh situs web yang sudah menerapkan responsive design adalah Google, Facebook, dan Amazon, sementara beberapa situs web pemerintah atau perusahaan kecil belum sepenuhnya menerapkannya.

---

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Margin, border, dan padding adalah tiga properti CSS yang digunakan untuk mengatur tata letak elemen di halaman web. Margin adalah jarak di sekitar elemen, border adalah garis tepi elemen, sedangkan padding adalah jarak antara konten dengan batas elemen. Cara implementasi di css itu pake selector terus pake property matgin, border, dan padding. Kalau mau lebih spesifik berdasarkan arah, bisa pake -top, -bottom, -right, -left.

---

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

Flexbox, yang bekerja dalam satu dimensi, sangat baik untuk mengatur tata letak sederhana seperti navbar atau card layout. Sementara itu, Grid Layout, yang bekerja dalam dua dimensi, memungkinkan Anda membuat tata letak yang lebih kompleks seperti halaman beranda dengan beberapa kolom dan baris. Keduanya menawarkan cara yang lebih efisien dan modern dibandingkan dengan metode tata letak tradisional.

---

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. **Implementasikan fungsi untuk menghapus dan mengedit product.**
- Buka `/main/views.py`, buat function `edit_product()` untuk edit product pada salah satu product di basis data user dan `delete_product()` untuk delete product dari basis data user
- Buka `/main/urls.py`, import `edit_product` dan `delete_product` dari module `main.views`, dan routing `edit_product` and `delete_product`.
- Buat `/main/templates/edit_product.html` untuk presentasi layar bagian edit product.
- Di `/main/templates/index.html` buat button edit untuk edit product dan delete untuk delete product di setiap product.

2. **Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:**
- Buatlah file `/static/css/global.css`
- Di file html `/templates/base.html` tambahkan `<script src="https://cdn.tailwindcss.com"></script>` dan `<link rel="stylesheet" href="{% static 'css/global.css' %}"/>`
- Isikan `/static/css/global.css` dengan ini
```css
.form-style form input, .form-style form textarea, .form-style form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}

.form-style form input:focus, .form-style form textarea:focus, .form-style form select:focus {
    outline: none;
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.animate-shine {
    background: linear-gradient(120deg, rgba(59, 130, 246, 0.3), rgba(59, 130, 246, 0.1) 50%, rgba(59, 130, 246, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}

.card-product {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card-product:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}
```
- Buka `/my_e_commerce/settings.py`, di variabel `MIDDLEWARE` tambahkan `'whitenoise.middleware.WhiteNoiseMiddleware',` di bawah `'django.middleware.security.SecurityMiddleware',`.
- Tambahkan ini di `/my_e_commerce/settings.py`
``` python
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'
```
1. **Kustomisasi halaman login, register, dan tambah product semenarik mungkin.**
- Saya implementasi kustomisasi menggunakan framework tailwind css dan pake metode inline style dan external css file (pake `/static/css/global.css`).
- `/main/templates/login.html`
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <h2 class="mt-6 text-center text-black text-3xl font-extrabold">
      Login to your account
    </h2>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required placeholder="Password">
        </div>
      </div>
      <div>
        <button type="submit" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out w-full">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-blue-600 hover:text-blue-500">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```

- `/main/templates/register.html`
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
      Create your account
    </h2>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            {{ field }}
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>
      <div>
        <button type="submit" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out w-full">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-blue-600 hover:text-blue-500">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```

- `/main/templates/create_product.html`
```html
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Create Product</title>
{% endblock meta %}

{% block content %}
{% include "navbar.html" with username=request.user.username %} <!-- Ini buat navbar.html nanti -->
<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Add New Product</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            {{ field }}
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out w-full">
            Create Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

- `/main/templates/edit_product.html`
```html
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include "navbar.html" with username=request.user.username %} <!-- Ini buat navbar.html nanti -->
<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                      {{ field.label }}
                  </label>
                  {{ field }}
                  {% if field.help_text %}
                    <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out w-full">
                  Edit Product
              </button>
          </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```
2. **Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:**

**Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.**

**Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).**

**Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!**

- Nanti bisa menggunakan conditional untuk mengasih tampilan yang berbeda antara belum ada product dan sudah ada product.
- Untuk informasi nama dan kelas di card pake `card_info.html` dan product di card pake `card_product.html` yang akan ada tombol edit dan delete
- `main/templates/card_info.html`
```html
<div class="bg-blue-500 text-black rounded-lg p-4 shadow-md animate-shine">
    <h2 class="text-xl font-bold">Name: {{ name }}</h2>
    <h3 class="text-lg">Class: {{ class }}</h3>
</div>
```

- `main/templates/card_product.html`
```html
<div class="bg-blue-100 border border-blue-300 rounded-lg p-4 shadow-md card-product">
    <h2 class="text-lg font-semibold text-blue-800">{{ p.name }}</h2>
    <p class="text-gray-700">Price: {{ p.price }}</p>
    <p class="text-gray-600">{{ p.description }}</p>
    <div class="flex justify-between mt-4">
        <a href="{% url 'main:edit_product' p.pk %}">
            <button class="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700">Edit</button>
        </a>
        <a href="{% url 'main:delete_product' p.pk %}">
            <button class="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700">Delete</button>
        </a>
    </div>
</div>
```

- `/main/templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>T-Shop</title>
</head>
<body>
    {% extends "base.html" %}
    {% load static %}
    {% block content %}
    
    {% include "navbar.html" with username=request.user.username %} <!-- Ini buat navbar.html nanti -->

    <div class="container mx-auto px-4 py-8">
        <div class="text-center mb-8">
            <h1 class="text-3xl font-bold text-gray-800">Welcome to {{ title }}</h1>
        </div>
        
        <div class="mb-6">
            {% include "card_info.html" with name=name class=class %}
            <div class="bg-blue-100 text-blue-800 p-4 rounded-lg shadow-md mt-4">
                <h5 class="font-semibold">Terakhir login:</h5>
                <p>{{ last_login }}</p>
            </div>
        </div>

        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Products</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {% if not product_entries %}
                <div class="col-span-1 md:col-span-2 lg:col-span-3 text-center p-6 rounded-lg border border-gray-300">
                    <div class="flex justify-center">
                        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4">
                    </div>
                    <p class="text-lg">Belum ada product yang terdaftar</p>
                </div>
            {% else %}
                {% for p in product_entries %}
                    {% include "card_product.html" with p=p %}
                {% endfor %}
            {% endif %}
        </div>

        <div class="flex justify-center mt-6">
            <a href="{% url 'main:create_product' %}">
                <button class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out">
                    Add New Product
                </button>
            </a>
        </div>
    </div>

    {% endblock content %}
</body>
</html>
```

3. **Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.**
- Di navigation bar ini akan ada judul (T-Shop), Home, nama user, tombol logout, dan lain-lain yang belum diimplementasi.
- Nanti buat 2 div, yang satu untuk desktop yang satu untuk mobile devices.
- `/main/templates/navbar.html`
```html
<nav class="bg-blue-600 p-4">
    <div class="flex justify-between items-center">
        <div class="text-white text-xl font-bold">T-Shop</div>
        <div class="hidden md:flex items-center space-x-4">
            <a href="{% url 'main:index' %}" class="text-white font-bold text-xl hover:text-gray-200">Home</a>
            <div class="text-white text-xl font-bold">Products</div>
            <div class="text-white text-xl font-bold">Categories</div>
            <div class="text-white text-xl font-bold">Cart</div>
            <span class="text-white font-bold text-xl">Welcome, {{ username }}</span>
            <a href="{% url 'main:logout' %}">
                <button class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300 ease-in-out">
                    Logout
                </button>
            </a>
        </div>
        <div class="md:hidden">
            <button id="hamburger" class="text-white focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
            </button>
        </div>
    </div>
    <!-- Mobile menu -->
    <div id="mobile-menu" class="hidden">
        <div class="flex flex-col mt-2">
            <a href="{% url 'main:index' %}" class="text-white font-bold text-xl hover:text-gray-200">Home</a>
            <div class="text-white text-xl font-bold">Products</div>
            <div class="text-white text-xl font-bold">Categories</div>
            <div class="text-white text-xl font-bold">Cart</div>
            <span class="text-white font-bold text-xl">Welcome, {{ username }}</span>
            <a href="{% url 'main:logout' %}">
                <button class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300 ease-in-out mt-2">
                    Logout
                </button>
            </a>
        </div>
    </div>
</nav>

<script>
    document.getElementById('hamburger').onclick = function() {
        var menu = document.getElementById('mobile-menu');
        menu.classList.toggle('hidden');
    }
</script>
```