# NotPixTod

Auto paint and claim for N\*t P\*xel

The English version of the Readme is available at [README_EN.md](README_EN.md)

# Daftar Isi
- [NotPixTod](#notpixtod)
- [Daftar Isi](#daftar-isi)
- [Pendaftaran](#pendaftaran)
- [Fitur](#fitur)
- [Dukung saya](#dukung-saya)
- [Peringatan](#peringatan)
- [Cara Penggunaan](#cara-penggunaan)
  - [Tentang Config.json](#tentang-configjson)
  - [Opsi Command Line / Argument Command Line](#opsi-command-line--argument-command-line)
  - [Tentang Proxy](#tentang-proxy)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Terima kasih](#terima-kasih)

# Pendaftaran

Ikuti tautan berikut untuk mendaftar : [https://t.me/notpixel/app?startapp=f629438076](https://t.me/notpixel/app?startapp=f629438076)

# Fitur

- [x] Otomatis Melakukan Paint
- [x] Otomatis Klaim Mining
- [x] Otomatis Upgrade Boost
- [x] Mendukung Penggunaan Proxy
- [x] Menggunakan fake useragent
- [x] Mengikuti event saldo x3

# Dukung saya

Jika anda suka dengan hasil pekerjaan saya anda bisa mendukung saya melakui tautan dibawah

- [Indonesia] https://s.id/nusanqr (QRIS)
- [Indonesia] https://trakteer.id/fawwazthoerif/tip
- [Global] https://sociabuzz.com/fawwazthoerif/tribe
- Jika anda ingin mengirim dalam bentuk lain, anda bisa menghubungi saya melalui telegram.

# Peringatan

Program ini menggunakan library pihak ke-3 untuk masuk ke akun telegram.

Menurut TOS Telegram, semua akun yang mendaftar atau masuk menggunakan klien API Telegram yang tidak resmi secara otomatis akan diawasi untuk menghindari pelanggaran terhadap Ketentuan Layanan.

Jadi berhati-hatilah, semoga akun Anda tidak diblokir.

Semua risiko ditanggung oleh pengguna !

# Cara Penggunaan

## Tentang Config.json

Berikut penjelasan untuk tentang isi config.json

| Kata kunci        | Deskripsi                                                                                                                                                                                                                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_id            | untuk mengisi kunci ini bisa mendaftar terlebih dahulu di my.telegram.org/apps, ini tidak wajib anda bisa menggunakan milik saya yang sudah tersimpan di file `config.json.example`                                                                                                                                          |
| api_hash          | untuk mengisi kunci ini bisa mendaftar terlebih dahulu di my.telegram.org/apps, ini tidak wajib anda bisa menggunakan milik saya yang sudah tersimpan di file `config.json.example`                                                                                                                                          |
| referral_code     | pada kunci ini diisi kode undangan akun utama kalian                                                                                                                                                                                                                                                                         |
| colors            | pada kunci ini diisi daftar warna yang ingin di terapkan ke kanvas kalian bisa mendapatkan kode warna (hexcode) didalam bot telegramnya (ikut format yang ada). Anda bisa menonton video berikut untuk mengetahui bagaimana cara mendapatkan hex color dari bot [https://youtu.be/r7qhx95gwVw](https://youtu.be/r7qhx95gwVw) |
| auto_upgrade      | kunci ini untuk mengaktifkan fitur auto upgrade, didalamnya terdapat beberapa key/kunci lagi berikan value/isi `true` untuk mengaktifkannya dan beri value/isi `false` untuk menonaktifkannya                                                                                                                                |
| countdown         | kunci ini untuk memberikan seberapa lama waktu tunggu untuk mengisi energi, kunci ini diisi dengan nilai positif (satuan detik)                                                                                                                                                                                              |
| time_before_start | kunci ini digunakan untuk membuat waktu muncur secara acak sebelum memulai menjalankan script, kunci memiliki 2 nilai yang perlu diisi \[kecil,besar\], contoh seperti tertera di config itu sendiri (satuan : detik)                                                                                                        |

## Opsi Command Line / Argument Command Line

Script / program ini juga mendukung beberapa argument parameter yang bisa dipakai, berikut adalah penjelasan argument 

<!-- `--data` / `-D` bisa digunakan ketika anda mempunyai nama file yang berbeda untuk menyimpan data akun. Secara bawaan nama file yang digunakan oleh script / program ini untuk menyimpan data akun adalah `data.txt`, semisal anda mempunyai file bernama `query.txt` sebagai file yang menyimpan data akun maka tinggal jalankan `bot.py` dengan menambahkan argumetn `--data` / `-D`. Contoh `python bot.py --data query.txt` -->

`--proxy` / `-P` bisa digunakan ketika anda mempunyai nama file yang berbeda untuk menyimpan list proxy. Nama file yang digunakan oleh script / program ini untuk menyimpan daftar proxy adalah `proxies.txt`, semisal anda mempunyai file bernama `prox.txt` sebagai file yang menyimpan daftar proxy, anda hanya tinggal menambahkan argument parameter `--proxy` / `-P` untuk dapat menggunakan file proxy anda. Contoh `python bot.py --proxy prox.txt`

`--worker` / `-W` argument ini berfungsi untuk melakukan kustomisasi jumlah thread / worker yang digunakan ketika script bot ini berjalan. Secara bawaan script / software ini jumlah worker nya adalah (total core cpu / 2), semisal cpu anda memiliki core 6 maka jumlah worker yang digunakan adalah 3. Anda bisa melakukan kustomisasi untuk jumlah worker ini menggunakan argument ini. Contohnya anda ingin membuat jumlah worker nya menjadi 100 maka jalankan `bot.py` dengan argument seperti ini `python bot.py --worker 100`. Dan jika anda tidak suka menggunakan worker / thread / multiprocessing maka anda bisa melakukan kustomisasi worker menjadi 1, contoh `python bot.py --worker 1`.

`--action` / `-A` argument ini berfungsi untuk langsung masuk ke kemu yang dituju, misal dalam script bot ini ada 5 menu jika anda tidak ingin melakukan input secara manual anda bisa menggunakan argument ini untuk langsung masuk ke menu yang dituju. Contoh : `python bot.py --action 5` dalalm contoh tersebut berarti anda akan langsung masuk ke menu nomor 5. Argument ini berguna jika kalian menggunakan docker / pm2 untuk menjalankan script bot di proses background.

## Tentang Proxy

Daftar di Website Berikut untuk Mendapatkan Proxy Gratis : [Here](https://www.webshare.io/?referral_code=dwj0m9cdi4mp)

Website dengan harga proxy termurah $1/GB [Here](https://dataimpulse.com/?aff=48082)

Anda bisa menambahkan daftar proxy di file `proxies.txt` dan format proxynya seprti berikut :

Jika terdapat autentikasi :

Format : 

```
protocol://user:password@hostname:port
```

Contoh :

```
http://admin:admin@69.69.69.69:6969
```

Jika tidak ada autentikasi :

Format :

```
protocol://hostname:port
```

Contoh :

```
http://69.69.69.69:6969
```

Tolong diperhatikan dengan saksama apakah proxy yang anda gunakan itu harus menggunakan autentikasi atau tidak, karena banyak orang yang DM saya bertanya cara penggunaan proxy.

Berikut cara penggunaan dibeberapa operasi sistem

## Windows

1. Pastikan komputer anda sudah terinstall python dan git, jika belum anda bisa menginstallnya terlebih dahulu

    Saran versi python adalah 3.10

    Unduh python : [https://python.org](https://python.org)

    Unduh Git : [https://git-scm.com](https://git-scm.com/)

2. Buka Terminal / CMD

3. Kloning repository ini
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

4. Masuk ke folder NotPixTod
   ```shell
   cd NotPixTod
   ```

5. Install library yang dibutuhkan
   ```shell
   python -m pip install -r requirements.txt
   ```

6. Salin file `config.json.example` ke `config.json` atau kalian juga bisa melakukan penamaan ulang pada file `config.json.example` menjadi `config.json`. Kemudian sesuaikan config sesuai keinginnan kalian, kalian bisa melihat [Tentang Config.json](#tentang-configjson) untuk penjelasannya.

   Ikuti salah satu perintah dibawah dan sesuaikan dengan os kalian:
   
   Windows CMD / Powershell
   
   ```shell
   copy config.json.example config.json
   ```
   
   Linux/Unix
   
   ```shell
   cp config.json.example config.json
   ```
   
7. Jalankan/ eksekusi file utama 
   ```shell
   python bot.py
   ```

## Linux

1. Pastikan komputer anda sudah terinstall python dan git, jika belum anda bisa menginstallnya terlebih dahulu

    Perintah linux untuk melakukan installasi python dan git

    ```shell
    sudo apt install python3 python3-venv python3-pip git -y
    ```

2. Kloning repository ini
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

3. Masuk ke folder NotPixTod
   ```shell
   cd NotPixTod
   ```

4. Buat virtual environment dan mengaktifkannya.
   
   ```shell
   python3 -m venv env && source env/bin/activate
   ```

5. Install library yang dibutuhkan
   ```shell
   python -m pip install -r requirements.txt
   ```

6. Salin file `config.json.example` ke `config.json` atau kalian juga bisa melakukan penamaan ulang pada file `config.json.example` menjadi `config.json`. Kemudian sesuaikan config sesuai keinginnan kalian, kalian bisa melihat [Tentang Config.json](#tentang-configjson) untuk penjelasannya.

   Ikuti salah satu perintah dibawah dan sesuaikan dengan os kalian:

   Windows CMD / Powershell

   ```shell
   copy config.json.example config.json
   ```

   Linux/Unix

   ```shell
   cp config.json.example config.json
   ```
   
7. Jalankan/ eksekusi file utama 
   ```shell
   python bot.py
   ```

## Termux

1. Pastikan di aplikasi termux anda sudah terinstall python dan git, jika belum anda bisa menginstallnya terlebih dahulu
   
   ```shell
   pkg update -y && pkg upgrade -y && pkg install python git -y
   ```

2. Kloning repository ini
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

3. Masuk ke folder NotPixTod
   ```shell
   cd NotPixTod
   ```

4. Install library yang dibutuhkan
   ```shell
   python -m pip install -r requirements.txt
   ```

5. Salin file `config.json.example` ke `config.json` atau kalian juga bisa melakukan penamaan ulang pada file `config.json.example` menjadi `config.json`. Kemudian sesuaikan config sesuai keinginnan kalian, kalian bisa melihat [Tentang Config.json](#tentang-configjson) untuk penjelasannya.

   Ikuti salah satu perintah dibawah dan sesuaikan dengan os kalian:

   Windows CMD / Powershell

   ```shell
   copy config.json.example config.json
   ```

   Linux/Unix

   ```shell
   cp config.json.example config.json
   ```
   
6. Jalankan/ eksekusi file utama 
   ```shell
   python bot.py
   ```

# Terima kasih