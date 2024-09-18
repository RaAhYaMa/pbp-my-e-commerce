# PBP - Welcome to T-Pos- I mean T-Shop
An E-Commerce Web for... well... to buy and sell stuff 😁

#### Deployment 🌐
[http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/](http://raden-ahmad33-tshop.pbp.cs.ui.ac.id/)

## Tugas 3 - PBP 2024/2025 Gasal
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery penting dalam pengimplementasian sebuah platform karena memastikan keterhubungan dan integrasi sistem, memungkinkan akses data real-time atau near-real-time, serta menjaga akurasi dan konsistensi data. Dengan data delivery yang efektif, platform dapat menangani volume data tinggi secara skalabel, meningkatkan kinerja, dan memudahkan pemantauan serta pengelolaan data. Selain itu, data delivery yang baik juga memperhatikan aspek keamanan dan privasi, serta meningkatkan pengalaman pengguna dengan menyajikan informasi yang cepat dan akurat.

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Bagi saya lebih suka JSON karena strukturnya lebih mirip seperti dictionary dan secara space lebih sedikit ketimbang XML.

JSON lebih populer dibandingkan XML karena kesederhanaannya yang membuatnya lebih mudah dibaca dan ditulis, serta efisiensinya dalam hal ukuran file dan kecepatan pemrosesan. JSON juga sangat kompatibel dengan JavaScript, yang merupakan bahasa utama untuk pengembangan web modern, sehingga memudahkan integrasi dan pengelolaan data dalam aplikasi web. Meskipun XML menawarkan struktur yang lebih kompleks dan dukungan untuk validasi yang lebih mendalam, JSON sering kali lebih disukai karena kemudahan penggunaannya dan dukungan luas dalam ekosistem teknologi saat ini.

**Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**

Metode `is_valid()` pada form Django adalah sebuah fungsi yang sangat krusial dalam memastikan kualitas dan keamanan data yang diinputkan pengguna. Ketika sebuah form dikirimkan, metode ini akan memeriksa apakah semua data yang dimasukkan memenuhi persyaratan validasi yang telah ditentukan, seperti jenis data, panjang karakter, dan format. Jika semua data valid, `is_valid()` akan mengembalikan nilai True dan memungkinkan kita untuk memproses data tersebut lebih lanjut. Sebaliknya, jika ada data yang tidak valid, metode ini akan mengembalikan nilai False.

**Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

`csrf_token` adalah fitur keamanan penting di Django yang berfungsi mencegah serangan Cross-Site Request Forgery (CSRF). Serangan CSRF terjadi ketika penyerang memaksa pengguna untuk melakukan tindakan tidak diinginkan di sebuah situs web. `csrf_token` menghasilkan token unik untuk setiap form, yang kemudian diverifikasi saat form dikirim. Dengan demikian, Django dapat membedakan antara permintaan yang sah dari pengguna dan permintaan palsu yang dikirim oleh penyerang. Jika `csrf_token` tidak digunakan, aplikasi web menjadi rentan terhadap serangan CSRF dan data pengguna dapat disalahgunakan.

**Postman**
- XML
![xml](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/xml.png)
- XML by ID
![xml_by_id](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/xml_by_id.png)
- JSON
![json](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/json.png)
- JSON by ID
![json_by_id](https://github.com/RaAhYaMa/pbp-my-e-commerce/blob/master/src/common/images/json_by_id.png)