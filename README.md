# **Telegram Auto-Translator Userbot**  

A simple **auto-translator** for Telegram using **Telethon** and **Google Translate API.**  

---

## **🚀 Setup & Installation**  

### **1️⃣ Clone the Repository**  
Run the following command to clone the project:  
```bash
git clone https://github.com/ankit-chaubey/telegram-translator-userbot.git
cd telegram-translator-userbot
```

#### 2️⃣ Install Dependencies

```
pip install telethon googletrans==4.0.0-rc1
```

#### 3️⃣ Get API Credentials

1. Visit [my.telegram.org](https://my.telegram.org) and log in.
2. Click on API Development Tools.
3. Create a new app and save your `API ID`, `API HASH`


#### 4️⃣ Configure & Run the Userbot

Open `nano translate.py` and replace:

```
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
```

Run the script:
```
python translate.py
```

Log in with your phone number and Telegram login code (only for the first time).



---

### **📌 Command Guide for Telegram Auto-Translator Userbot**  

## **🔹 Basic Commands**  

| Command | Description | Example | Output |
|---------|------------|---------|--------|
| `.t-lang text` | Auto-detect source language & translate to `lang` | `.t-en नमस्ते` | `Hello` |
| `.t-from:to text` | Translate from `from` language to `to` language | `.t-hi:en मेरा नाम अंकित है` | `My name is Ankit` |
| `.t-fr How are you?` | Translate to French | `.t-fr How are you?` | `Comment ça va ?` |
| `.t-es I love programming` | Translate to Spanish | `.t-es I love programming` | `Me encanta programar` |

---

## **🔹 Explanation**  

- **`.t-lang text`** → Automatically detects the language of `text` and translates it to `lang`.  
- **`.t-from:to text`** → Translates `text` from `from` language to `to` language.  
- **Language Codes:**  
  - `en` → English  
  - `hi` → Hindi  
  - `fr` → French  
  - `es` → Spanish  
  - **[Full list of supported languages](https://cloud.google.com/translate/docs/languages)**  

🚀 **Now you can translate messages instantly on Telegram!**

---

### 💡 Usage

🔹 Auto-Detect Language & Translate

```
.t-en नमस्ते

Output:

Hello

```
🔹 Translate from a Specific Language
```
.t-hi:en मेरा नाम अंकित चौबे है

Output:

My name is Ankit Chaubey
```

🔹 Translate to Other Languages

```
.t-fr How are you?

Output:

Comment ça va ?

.t-es I love programming

Output:

Me encanta programar
```


---

### 🎯 Supported Languages

Use language codes (en for English, hi for Hindi, fr for French, etc.).
Full list: [Google Translate Language Codes](https://cloud.google.com/translate/docs/languages)


---

### 🛠️ Features

✅ Auto-detects language
✅ Works in private & group chats
✅ Lightweight & fast
✅ Easy setup with Telethon


---

### 📌 Notes

Must be logged in as a Telegram user (not a bot).

Works with any language supported by Google Translate.

Restart the script if you face issues.



---

## **👨‍💻 Creator**  
This project is built by **[Ankit Chaubey](https://github.com/ankit-chaubey)**
- 📬 **Telegram:** [@ankify](https://t.me/ankify)
- 📧 **Email:** [📨📨📨📨](mailto:m.ankitchaubey@gmail.com)

---

🚀 Now your Telegram userbot can automatically translate messages!


