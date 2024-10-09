# PBP - Welcome to T-Pos- I mean T-Shop
An E-Commerce Web for... well... to buy and sell stuff 😁

#### Deployment 🌐
[http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/](http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/)

## Tugas 6 - PBP 2024/2025 Gasal

**Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**

JavaScript adalah bahasa pemrograman yang esensial dalam pengembangan aplikasi web karena memungkinkan interaktivitas. Ia didukung oleh semua browser modern, menawarkan ekosistem yang kaya dengan pustaka dan framework serta mendukung pemrograman asinkron untuk efisiensi dalam pengolahan data. Dengan kemampuannya untuk memuat konten tanpa _refresh_ halaman dan mengintegrasikan berbagai API, JavaScript meningkatkan pengalaman pengguna secara signifikan.

---

**Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**

Penggunaan `await` dengan `fetch()` memungkinkan kita untuk menunggu respons dari permintaan sebelum melanjutkan eksekusi kode, sehingga kita dapat memproses data yang diterima dengan benar. Tanpa  await , kode akan melanjutkan tanpa menunggu hasil, yang bisa menyebabkan akses ke data yang belum tersedia, menghasilkan `undefined`, atau menciptakan perilaku yang tidak terduga dan kesalahan sulit dilacak.

---

**Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?**

Menggunakan decorator `csrf_exempt` pada view untuk AJAX `POST` penting karena dapat mempermudah integrasi dengan permintaan yang tidak selalu menyertakan token CSRF, yang dapat menyebabkan penolakan oleh Django.

---

**Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**

Pembersihan data input pengguna dilakukan di backend untuk memastikan keamanan dan konsistensi, karena data dapat dimanipulasi di frontend. Dengan menerapkan pembersihan di backend, kita dapat melindungi dari serangan seperti XSS, memastikan validasi ganda, dan menjamin bahwa semua data yang diterima, terlepas dari sumbernya, telah dibersihkan dengan cara yang sama.

---

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. **AJAX `GET`**

- Buka `/main/views.py` dan hapus kode `product_entries = Product.objects.filter(user=request.user)` dan `"product_entries": product_entries,` di function `index()`
- Ubah `data = Product.objects.all()` menjadi `data = Product.objects.filter(user=request.user)` di function `show_xml()` dan `show_json()`
- Buka `/main/templates/index.html` dan delete bagian kode ini
```html
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {% if not product_entries %}
                <div class="col-span-1 md:col-span-2 lg:col-span-3 text-center p-6 rounded-lg border border-gray-300">
                    <div class="flex justify-center">
                        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4">
                    </div>
                    <p class="text-lg">Belum ada product yang terdaftar</p>
            {% else %}
                {% for p in product_entries %}
                    {% include "card_product.html" with p=p %}
                {% endfor %}
            {% endif %}
        </div>
```
dan ubah menjadi ini
```html
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="product_cards"></div>
```
- Tambahkan kode ini di dalam kode block `<script>`
```javascript
        async function getProducts() {
            return fetch("{% url 'main:show_json' %}").then((res) => res.json());
        }

        async function refreshProducts() {
            const productCardsContainer = document.getElementById("product_cards");
            productCardsContainer.innerHTML = ""; // Clear existing content
            let html = "";

            const productEntries = await getProducts();
            if (productEntries.length === 0) {
                html = `<div class="col-span-1 md:col-span-2 lg:col-span-3 text-center p-6 rounded-lg border border-gray-300">
                            <div class="flex justify-center">
                                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4">
                            </div>
                            <p class="text-lg">Belum ada product yang terdaftar</p>
                        </div>`;
            } else {
                productEntries.forEach((p) => {
                    html += `<div class="bg-blue-100 border border-blue-300 rounded-lg p-4 shadow-md card-product">
                                <h2 class="text-lg font-semibold text-blue-800">${p.fields.name}</h2>
                                <p class="text-gray-700">Price: ${p.fields.price}</p>
                                <p class="text-gray-600">${p.fields.description}</p>
                                <div class="flex justify-between mt-4">
                                    <a href="/edit/${p.pk}">
                                        <button class="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700">Edit</button>
                                    </a>
                                    <a href="/delete/${p.pk}">
                                        <button class="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700">Delete</button>
                                    </a>
                                </div>
                            </div>`;
                });
            }

            productCardsContainer.innerHTML = html; // Add the new content
        }

        refreshProducts();
```

2. **AJAX `POST`**
- Buka `/main/views.py` dan import `csrf_exempt` dari module `django.views.decorators.csrf`, import `require_POST` dari module `django.views.decorators.http`, dan import `strip_tags` dari module `django.utils.html`
- Buat `add_product_ajax()` seperti ini
```python
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
- Buka `/main/urls.py` dan import `add_product_ajax` dari module `main.views`
- Tambahkan routing `add_product_ajax` ke url "create-ajax/"
- Buka `main/templates/index.html` dan buat modal sebagai form untuk menambahkan product seperti ini
```html
        <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
            <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 border-b rounded-t bg-blue-600 text-white">
                    <h3 class="text-xl font-semibold">
                        Add New Product Entry
                    </h3>
                    <button type="button" class="text-white bg-transparent hover:bg-blue-700 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="px-6 py-4 space-y-6 form-style">
                    <form id="productEntryForm">
                        <div class="mb-4">
                            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                            <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-blue-700" required>
                        </div>
                        <div class="mb-4">
                            <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                            <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-blue-700" required>
                        </div>
                        <div class="mb-4">
                            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                            <textarea id="description" name="description" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-blue-700" required></textarea>
                        </div>
                    </form>
                </div>
                <!-- Modal footer -->
                <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
                    <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
                    <button type="submit" id="submitproductEntry" form="productEntryForm" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg">Save</button>
                </div>
            </div>
        </div>
```
- Buat button untuk memunculkan modalnya
```html
            <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out" onclick="showModal();">
                Add New Product by AJAX
            </button>
```
- Buat script di kode block `<script>` untuk memunculkan dan menutupi modal serta penanganan untuk menambahkan product
```javascript
        function addProductEntry() {
            fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#productEntryForm')),
            })
            .then(response => refreshProducts())

            document.getElementById("productEntryForm").reset(); 
            document.querySelector("[data-modal-toggle='crudModal']").click();

            return false;
        }
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        function showModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');

            modal.classList.remove('hidden'); 
            setTimeout(() => {
                modalContent.classList.remove('opacity-0', 'scale-95');
                modalContent.classList.add('opacity-100', 'scale-100');
            }, 50); 
        }

        function hideModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');

            modalContent.classList.remove('opacity-100', 'scale-100');
            modalContent.classList.add('opacity-0', 'scale-95');

            setTimeout(() => {
                modal.classList.add('hidden');
            }, 150); 
        }

        document.getElementById("cancelButton").addEventListener("click", hideModal);
        document.getElementById("closeModalBtn").addEventListener("click", hideModal);
        document.getElementById("productEntryForm").addEventListener("submit", (e) => {
            e.preventDefault();
            addProductEntry();
        });
```