# 🎮 Game Jump

Game Jump adalah game platformer vertikal sederhana mirip *Doodle Jump*, dibuat dengan **Python** dan **Pygame**. Pemain melompat dari platform ke platform sambil menghindari musuh/batu yang jatuh dari atas.

---

## 📌 Fitur Utama

* Gerakan kiri / kanan (A / D atau ← / →)
* Lompat dengan tombol SPACE
* Sistem gravitasi dan physics sederhana
* Platform acak yang bisa diinjak
* Musuh/batu yang jatuh dari atas (hindari!)
* Platform baru muncul saat pemain naik
* Layar Game Over dengan efek fade
* Dua sprite karakter (menghadap kanan dan kiri)

---

## 📁 Struktur Project

```
Game Jump/
│
├── game.py          # Main loop & logika game
├── player.py        # Kelas Player (gerak, lompat, sprite kiri/kanan)
├── platfroms.py     # Kelas Platform
├── enemy.py         # Kelas Enemy (batu/musuh jatuh dari atas)
├── settings.py      # Konfigurasi (WIDTH, HEIGHT, asset paths)
├── README.md        # Dokumen ini
│
├── images/          # Folder asset gambar
│   ├── background.png
│   ├── anjay.png       # sprite menghadap kanan
│   ├── anjay2.png      # sprite menghadap kiri
│   ├── platform.png
│   └── enemy.png (opsional)
```

---


## ▶ Cara Bermain

| Aksi        | Tombol |
| ----------- | ------ |
| Lompat      | SPACE  |
| Gerak Kiri  | A / ←  |
| Gerak Kanan | D / →  |

* Hindari musuh/batu yang jatuh dari atas.
* Jangan jatuh melewati batas bawah layar.
* Lompat ke platform untuk terus naik dan dapat skor.

---

## 🧩 Penjelasan File Singkat

* **game.py**: file utama. Menginisialisasi game, memproses input, meng-handle spawn platform & musuh, serta render.
* **player.py**: logika pemain — kecepatan, gravitasi, jump, deteksi collision dengan platform, penggantian sprite kanan/kiri.
* **platfroms.py**: kelas Platform (gambar, posisi, update saat layar "bergerak").
* **enemy.py**: kelas Enemy (spawn dari atas, bergerak turun, hilang saat keluar layar).
* **settings.py**: konfigurasi global seperti `WIDTH`, `HEIGHT`, dan path gambar.

---

## ♻️ Cara Menambah Fitur (Saran)

* Tambahkan sistem skor dan highscore
* Tambahkan power-ups (double jump temporer, shield)
* Animasi berjalan / spritesheet
* Platform bergerak atau rapuh
* Level atau difficulty scaling (musuh lebih sering/cepat saat skor tinggi)


