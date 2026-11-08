# Catatan Minggu 04 :Polymorphism

## Yang saya kerjakan
Saya mengerjakan bagian perhitungan denda pada proyek Aset-Pinjam, khususnya untuk kelas Laptop dan AlatLab. Saya mencoba menerapkan konsep overriding, yaitu membuat method dengan nama yang sama tetapi memiliki aturan perhitungan yang berbeda. Selain itu, saya juga menambahkan validasi supaya jumlah hari keterlambatan tidak boleh negatif. Setelah selesai, saya mencoba menjalankan pengujian menggunakan Maven untuk melihat apakah kode sudah benar.

## Keputusan desain
Saya memutuskan untuk menggunakan method hitungDenda() pada masing-masing kelas. Untuk Laptop, denda dikalikan dua kali biaya dasar, sedangkan AlatLab dikalikan empat kali biaya dasar. Saya juga menggunakan method ValidateHariTerlambat() dari kelas Aset supaya tidak perlu membuat validasi yang sama berulang kali.
## Kendala
Kendala yang saya alami adalah saat menjalankan pengujian Maven, ternyata masih ada beberapa pengujian yang gagal. Awalnya saya bingung karena belum memahami arti pesan error yang muncul. Saya mencoba membaca laporan pengujian dan mengecek kembali kode yang sudah dibuat. Selain itu, saya juga sempat mengalami masalah saat menyimpan file karena muncul peringatan konflik perubahan pada editor.

## Penggunaan AI
- Alat yang dipakai: Kelas AlatLab.java, Laptop.java, dan method hitungDenda() pada kelas Aset.java.
- Bagian yang dibantu AI:bagian code yg salah , kelas ruang, laptop, dan alatlab saat error
- Prompt utama:Bantu saya memahami dan memperbaiki kode Java pada bagian perhitungan denda serta mengatasi error saat menjalankan pengujian Maven.
- Yang saya ubah atau tolak dari saran AI, dan alasannya: Saya menyesuaikan kode berdasarkan struktur program dan hasil pengujian yang muncul. Saya juga tidak langsung mengikuti semua saran, tetapi mencoba memahami terlebih dahulu bagian mana yang perlu diperbaiki.
- Satu hal yang saya pahami lebih baik sekarang: Saya jadi lebih paham tentang konsep overriding di Java. Saya juga belajar bahwa ketika method pada kelas induk di-override, validasi dari kelas induk tidak otomatis dijalankan. Jadi, validasi perlu dipanggil kembali di method subclass jika memang dibutuhkan.