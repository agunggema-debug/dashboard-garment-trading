# 👕 IT Asset Management Dashboard
### Garment & Trading Division

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Dashboard interaktif yang dirancang khusus untuk memantau dan mengelola aset IT pada bisnis **Garment & Trading**. Solusi ini memberikan visibilitas real-time terhadap status mesin, perangkat gudang, dan inventaris kantor.

---
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b622749d-e210-4b93-9b3c-6ad9ce8d80bb" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5313be29-6138-4a77-a12a-c5b75d85f0b3" />


## ✨ Fitur Utama
* **📊 Real-time Metrics:** Pantau total nilai aset dan status operasional secara instan.
* **🔍 Advanced Search:** Pencarian cepat berdasarkan ID Aset, Kategori, atau Lokasi.
* **📈 Visualisasi Dinamis:** Grafik distribusi kategori dan status aset menggunakan Plotly.
* **📥 Export Data:** Unduh laporan inventaris langsung ke format CSV.
* **📱 Responsive Design:** Tampilan elegan dengan Header & Footer kustom yang nyaman di berbagai perangkat.

---

## 🛠️ Teknologi yang Digunakan
* **Python** - Bahasa pemrograman utama.
* **Streamlit** - Framework untuk antarmuka dashboard.
* **Pandas** - Manipulasi dan pemrosesan data aset.
* **Plotly** - Pembuatan grafik interaktif.

---

## 🚀 Cara Menjalankan Secara Lokal

1. **Clone Repository**
   ```bash
   git clone [https://github.com/username/it-asset-management.git](https://github.com/username/it-asset-management.git)
   cd it-asset-management
   ```
2. **Install Dependensi Pastikan Anda sudah menginstal Python, lalu jalankan:**
   ```
   pip install -r requirements.txt
   ```
3. **Jalankan Aplikasi**
   ```
    streamlit run app.py
   ```

## 📁 Struktur Proyek
   ``` 
    ├── app.py              # File utama aplikasi Streamlit
    ├── requirements.txt    # Daftar pustaka yang dibutuhkan
    ├── data/               # (Opsional) Tempat penyimpanan dataset
    └── README.md           # Dokumentasi proyek
   ```
 
## 🌐 Publikasi (Deployment)
   Aplikasi ini dioptimalkan untuk dideploy ke Streamlit Cloud. Cukup hubungkan repository GitHub Anda, dan aplikasi akan aktif secara otomatis di URL *.streamlit.app.
