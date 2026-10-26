# Catatan Minggu 02: Struktur OOP: Class, Object, Encapsulation

## Yang saya kerjakan
Saya menjalankan perintah yang terdapat di core/src/main/java/id/ac/upb/asetpinjam/model/Aset.java, seperti membuat class Aset, membuat field private (kode, nama, status, dan kondisi), terus saya membuat kontruktor dengan validasi null agar nilainya tidak kosong dan  saya juga  membuat getter untuk membaca data dan setter untuk ubah nama, status, dan validasi agar isisnya tidak kosong.

## Keputusan desain
Saya menggunakan isblank() untuk memastikan bahwa kode dan nama aset tidak kosong atau hanya berisi spasi. Saya juga menetapkan status awal aset menjadi TERSEDIA dan kondisinya menjadi BAIK. Selain itu, saya menggunakan getter untuk mengambil data dan setter untuk mengubah data. Dengan begitu, data aset dapat dikelola dengan lebih teratur dan aman.

## Kendala
Kendala saya adalah masih kesulitan memahami fungsi getter, setter, dan validasi data menggunakan isBlank(). Saya perlu lebih banyak mempelajarinya  agar lebih memahami cara kerja kode tersebut.

## Penggunaan AI
- Alat yang dipakai: chatgpt
- Bagian yang dibantu AI: pd bagian output yg terus menerus error
- Prompt utama: bantu saya agar hasil output tidak error dan berikan saya penjelasan mengenai itu
- Yang saya ubah atau tolak dari saran AI, dan alasannya:saya menolak bagian perbaikan error disuruh mengganti salah satu kode tapi saya tidak menggantinya karena tidak seharusnya diganti .
- Satu hal yang saya pahami lebih baik sekarang:lebih memahami mana cara kerja class
