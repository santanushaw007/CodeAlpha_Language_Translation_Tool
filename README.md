# CodeAlpha_Language_Translation_Tool

# 🌐 GlobalSpeak: Multi-Language Translator

A lightweight, modern, and interactive full-featured language translator built with **Python**, **Streamlit**, and **Google Translate API**. Translate text seamlessly across 100+ global languages instantly!

---

## ✨ Features

- **🌐 100+ Languages Supported**: Translate text to and from English, Spanish, French, German, Hindi, Mandarin, Arabic, and many more.
- **⚡ Instant Translation**: Fast real-time translation powered by the Google Translate API.
- **🎨 Minimal & Elegant UI**: Built with Streamlit for a clean, user-friendly, responsive interface.
- **📝 High Capacity Input**: Large text area with custom placeholder guide for long sentences or paragraphs.

---

## 🛠️ Technology Stack

- **Frontend & UI**: [Streamlit](https://streamlit.io/) (Python Web App Framework)
- **Translation Engine**: [Googletrans](https://pytrident.github.io/googletrans/) (Google Translate API Wrapper)
- **Language**: Python 3.8+

---

## 🚀 Quick Start Guide

Follow these simple steps to set up and run the translator application on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.8 or higher** installed on your system. You can verify this by running:
```bash
python --version
```

### 2. Install Dependencies
You need to install `streamlit` and the correct pre-release version of `googletrans` (version `4.0.0rc1` is highly recommended to avoid API changes/limitations of the older stable build).

Run the following command in your terminal/command prompt:
```bash
pip install streamlit googletrans==4.0.0-rc1
```

### 3. Run the Application
Navigate to the project folder containing the `LT.py` file and run:
```bash
streamlit run LT.py
```

Once executed, a local web server will spin up and open automatically in your default browser at:
👉 **`http://localhost:8501`**

---

## 📝 How to Use

1. **Enter Text**: Type or paste the text you want to translate in the **"Source Text"** text area.
2. **Select Target Language**: Choose your desired target language from the dropdown menu (Defaults to **English**).
3. **Translate**: Click the blue **"Translate"** button.
4. **View Output**: The translated text will appear instantly right below the translation button.

---

## 💡 Troubleshooting

* **Issue: `googletrans` raises `AttributeError: 'NoneType' object has no attribute 'group'`**
  * **Solution**: This is a known issue with the older `googletrans` package version `3.0.0`. Run `pip install googletrans==4.0.0-rc1` to install the updated version which resolves this issue completely.

* **Issue: Streamlit command not found**
  * **Solution**: Ensure your Python scripts folder is added to your system's Environment PATH, or run it using `python -m streamlit run LT.py`.

---

**Made with ❤️ for AI Project - 4th Semester**
