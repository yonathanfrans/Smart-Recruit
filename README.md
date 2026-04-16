# Smart Recruit

Smart Recruit adalah sebuah website berbasis Artificial Intelligence yang dirancang untuk membantu proses pencarian kandidat profesi Teknologi Informasi (TI) secara lebih cepat dan akurat. Sistem ini mengintegrasikan model Machine Learning menggunakan algoritma Naive Bayes untuk mengklasifikasikan kandidat, serta chatbot AI sebagai asisten interaktif bagi recruiter.

🔗 **Live Demo**: 

---

## 📚 Table of Contents

- [Features](#features)
- [Modules](#modules)
- [Tech Stack](#tech-stack)
- [Machine Learning Model](#machine-learning-model)
- [Installation](#installation)
- [Usage](#usage)
- [Design](#design)
- [Contact](#contact)

---

## ✨ Features

- **Machine Learning Classification**  
  Mengklasifikasikan kandidat ke dalam profesi:
  - Data Scientist
  - AI Engineer
  - Cybersecurity Engineer

- **Candidate Profile Input**  
  Kandidat dapat mengisi data seperti skills, education, experience, dan projects.

- **Automatic Job Role Prediction**  
  Sistem secara otomatis menentukan job role berdasarkan data kandidat.

- **Candidate Filtering**  
  Recruiter dapat memfilter kandidat berdasarkan:
  - Job Role
  - Gender

- **AI Chatbot (Your Assistant)**  
  Chatbot membantu recruiter mencari kandidat berdasarkan kebutuhan tertentu.

- **Authentication System**  
  Fitur login dan register untuk kandidat dan recruiter.

- **File Upload**  
  Upload CV dan sertifikat kandidat.

---

## 🧩 Modules

Website ini terdiri dari beberapa modul utama:

- **Authentication (Login & Register)**  
  Sistem autentikasi untuk kandidat dan recruiter.

- **Profile Kandidat**  
  Input dan update data kandidat.

- **Job Role Classification**  
  Implementasi model Machine Learning untuk menentukan profesi kandidat.

- **Candidate Page (Recruiter)**  
  Menampilkan daftar kandidat dengan fitur filter.

- **Your Assistant (Chatbot)**  
  Asisten AI untuk membantu pencarian kandidat.

---

## 🛠️ Tech Stack

- **Backend**:
  - ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white)
  - ![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-323330?style=for-the-badge&logo=sqlalchemy&logoColor=CE563D)
- **Machine Learning**:
  - ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
  - ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas) ![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
- **Frontend**:
  - ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  - ![Tailwind CSS](https://img.shields.io/badge/tailwindcss-0F172A?&logo=tailwindcss)
- **Database**:
  - ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white)
- **AI Chatbot**:
  - Flowise AI
  - ![Ollama](https://img.shields.io/badge/-Ollama-000000?style=flat&logo=ollama&logoColor=white)
- **Tools**:
  - Visual Studio Code
  - Git & GitHub
  - Ngrok (Testing)

---

## 🤖 Machine Learning Model

Model yang digunakan adalah **Naive Bayes Classifier** untuk mengklasifikasikan kandidat berdasarkan data berikut:
- Skills (TF-IDF)
- Certifications (TF-IDF)
- Education (Encoded)
- Experience (Years)
- Projects Count

Model menghasilkan prediksi job role:
- Data Scientist
- AI Engineer
- Cybersecurity Engineer

---

## 🎨 Design 
Desain website ini dapat dilihat di Figma melalui tautan berikut: 
- [Link Figma](https://www.figma.com/design/VlfFhMOIZpdMc7RsapMER7/Ma-Job?node-id=0-1&t=ZQeoF1hTS0BFj2Wr-1)

---

## ⚙️ Installation

Ikuti langkah berikut untuk menjalankan project secara lokal:

1. Clone repository
```bash
git clone https://github.com/username/smart-recruit.git
cd smart-recruit
```
2. Buat virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Konfigurasi environment
4. Jalankan Aplikasi
```bash
python app.py
```

---

## 🚀 Usage
Kandidat:
1. Register akun
2. Login
3. isi data profil (skills, education, dll.)
4. Lihat hasil job role otomatis

Recruiter:
1. Login
2. Akses halaman Candidate
3. Gunakan filter kandidat
4. Akses halaman Your Assistant
5. Gunakan chatbot untuk mencari kandidat cepat

---

## 📬 Contact 
Untuk informasi lebih lanjut, Anda dapat menghubungi saya melalui: 
- **Email**: [yonatanfrans07@gmail.com](mailto:yonatanfrans07@gmail.com)
- **Instagram**: [@yonathanfrans_](https://www.instagram.com/yonathanfrans_)

--- 

## 🙏 Acknowledgement 
Terima kasih telah menggunakan Smart Recruit!
