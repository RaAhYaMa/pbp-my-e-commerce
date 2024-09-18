# PBP - Welcome to T-Pos- I mean T-Shop
An E-Commerce Web for... well... to buy and sell stuff 😁

#### Deployment 🌐
[http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/](http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/)

## Tugas 3 - PBP 2024/2025 Gasal
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery penting dalam pengimplementasian sebuah platform karena memastikan keterhubungan dan integrasi sistem, memungkinkan akses data real-time atau near-real-time, serta menjaga akurasi dan konsistensi data. Dengan data delivery yang efektif, platform dapat menangani volume data tinggi secara skalabel, meningkatkan kinerja, dan memudahkan pemantauan serta pengelolaan data. Selain itu, data delivery yang baik juga memperhatikan aspek keamanan dan privasi, serta meningkatkan pengalaman pengguna dengan menyajikan informasi yang cepat dan akurat.

---

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Bagi saya lebih suka JSON karena strukturnya lebih mirip seperti dictionary dan secara space lebih sedikit ketimbang XML.

JSON lebih populer dibandingkan XML karena kesederhanaannya yang membuatnya lebih mudah dibaca dan ditulis, serta efisiensinya dalam hal ukuran file dan kecepatan pemrosesan. JSON juga sangat kompatibel dengan JavaScript, yang merupakan bahasa utama untuk pengembangan web modern, sehingga memudahkan integrasi dan pengelolaan data dalam aplikasi web. Meskipun XML menawarkan struktur yang lebih kompleks dan dukungan untuk validasi yang lebih mendalam, JSON sering kali lebih disukai karena kemudahan penggunaannya dan dukungan luas dalam ekosistem teknologi saat ini.

---

**Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**

Metode `is_valid()` pada form Django adalah sebuah fungsi yang sangat krusial dalam memastikan kualitas dan keamanan data yang diinputkan pengguna. Ketika sebuah form dikirimkan, metode ini akan memeriksa apakah semua data yang dimasukkan memenuhi persyaratan validasi yang telah ditentukan, seperti jenis data, panjang karakter, dan format. Jika semua data valid, `is_valid()` akan mengembalikan nilai True dan memungkinkan kita untuk memproses data tersebut lebih lanjut. Sebaliknya, jika ada data yang tidak valid, metode ini akan mengembalikan nilai False.

---

**Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

`csrf_token` adalah fitur keamanan penting di Django yang berfungsi mencegah serangan Cross-Site Request Forgery (CSRF). Serangan CSRF terjadi ketika penyerang memaksa pengguna untuk melakukan tindakan tidak diinginkan di sebuah situs web. `csrf_token` menghasilkan token unik untuk setiap form, yang kemudian diverifikasi saat form dikirim. Dengan demikian, Django dapat membedakan antara permintaan yang sah dari pengguna dan permintaan palsu yang dikirim oleh penyerang. Jika `csrf_token` tidak digunakan, aplikasi web menjadi rentan terhadap serangan CSRF dan data pengguna dapat disalahgunakan.

---

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. **Membuat input `form` untuk menambahkan objek model pada app sebelumnya.**
- Buat skeleton sebagai kerangka views di `base.html`, masukkan ke `TEMPLATES` di `settings.py`, dan modif `index.html` agar sesuaikan dengan `base.html`.
- Modif objek di `models.py` agar setiap objek memiliki primary key dan migrasikan.
- Buat `forms.py`, import `ModelForm` dari module `django.forms` dan import `Product` dari module `main.models`.
- Buat class `ProductForm` yang akan dijadikan sebagai penerimaan modelnya seperti ini
```python
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
- Buka `views.py`, import `redirect` dari module `django.shortcuts`, dan import `ProductForm` dari module `main.forms`.
- Buat functions `create_product` untuk pembuatan objek seperti ini
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:index")

    context = {
        "form": form
    }

    return render(request, "create_product.html", context)
```
- Modif fungsi `index` dengan ditambahkan variabel yang bernilai semua instance objek.
- Buat path yang sesuai di `urls.py`.
- Buat html form yang sesuai di `create_product.html`.
- Modif `index.html` biar diadakan tombol ke html form.

2. **Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**
- Buka `views.py`, import `HttpResponse` dari module `django.http`, dan import `serializers` dari module `django.core`.
- Buat fungsi-fungsi ini di `views.py`
```python
# XML
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# JSON
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# XML by ID
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# JSON by ID
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

3. **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
- Buka `urls.py`dan import `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` dari module `main.views`.
- Buat masing-masing routing di variabel `urlpatterns`, contohnya yg `show_xml` di route pake `path("xml/", show_xml, name="show_xml")`.

---

**Postman**
- XML
![xml](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/xml.png)
- XML by ID
![xml_by_id](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/xml_by_id.png)
- JSON
![json](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/json.png)
- JSON by ID
![json_by_id](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/json_by_id.png)