# Catatan Minggu 05:  Abstraction

## Yang saya kerjakan
Pada minggu ini saya mengerjakan materi abstraksi dan penerapan aturan denda pada sistem Aset-Pinjam. Saya mengubah kelas Aset menjadi abstract, membuat metode bisaDipinjam(), serta mengimplementasikan perhitungan denda pada kelas Ruang, Laptop, dan AlatLab. Saya juga mengerjakan DendaFlat dan DendaProgresif serta menjalankan pengujian untuk memastikan kode berjalan dengan benar.

## Keputusan desain
Saya menggunakan kelas abstract pada Aset agar setiap jenis aset memiliki perhitungan denda masing-masing. Untuk denda, saya menggunakan aturan flat sesuai tarif dasar setiap aset dan aturan progresif yang membuat denda semakin besar jika keterlambatan semakin lama. Saya juga menambahkan validasi agar jumlah hari keterlambatan tidak boleh negatif.

## Kendala
Kendala yang saya alami adalah beberapa pengujian masih gagal karena ada metode yang belum memiliki validasi hari negatif. Selain itu, saya sempat mengalami masalah saat menyimpan perubahan kode di VS Code. Saya mengatasinya dengan memeriksa isi file melalui PowerShell, memperbaiki kode yang belum sesuai, lalu menjalankan pengujian kembali.

## Penggunaan AI
- Alat yang dipakai: chatgpt
- Bagian yang dibantu AI: (kelas/metode)
- Prompt utama:Saya meminta bantuan AI untuk memahami dan memperbaiki kode Java yang mengalami error, mencari penyebab pengujian Maven yang gagal, serta menjelaskan cara menambahkan validasi pada perhitungan denda.
- Yang saya ubah atau tolak dari saran AI, dan alasannya:Saya menyesuaikan kode berdasarkan  perintah yang sudah ada dan hasil pengujian agar tidak mengubah bagian yang sebenarnya sudah benar.
- Satu hal yang saya pahami lebih baik sekarang:Saya lebih memahami penggunaan abstract class, overriding, aturan perhitungan denda, validasi input, serta cara membaca error saat menjalankan pengujian Maven, tapi kadang juga masih bingung sih
