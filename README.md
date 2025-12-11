# 📘 Self-Note Organizer

**Self-Note Organizer** is a simple and efficient CLI-based note-management tool that helps you store, view, search, delete, and manage personal notes.
You can also save all data in a JSON file for persistence and easy portability.

---

## ✨ Features

### 1️⃣ Add Full User Details

Add a complete entry containing:

* **Name**
* **Email**
* **Contact Number**
* **Notes**

### 2️⃣ Add Notes Separately

If a user already exists or if you just want to add standalone notes, you can add notes without entering other details.

### 3️⃣ View All Notes

Display all stored notes or user entries in a structured and readable format.

### 4️⃣ Search Notes

Search through notes using keywords, names, or any matching text to quickly find what you need.

### 5️⃣ Delete Notes

Remove any note or user entry safely from the system.

### 6️⃣ Save All Data to JSON

Export all stored information to a **JSON file**, allowing:

* Persistent storage
* Easy backup
* Integration with other systems

---

## 📂 Project Structure (example)

```
/self-note-organizer
│── main.py
│── note.json
│── README.md
│── stored_in_json.py
```

---

## 🚀 How to Use

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Choose an operation from the menu:**

   * Add full details
   * Add only notes
   * View notes
   * Search notes
   * Delete notes
   * Save to JSON

3. **Follow the on-screen instructions** to complete your action.

---

## 🧾 Example JSON Structure

Data is saved in the following format:

```json
{"name": "Vishal",
 "email": "vishal@gmail.com",
 "contact": "+91888888888",
 "notes": [
          {"11/12/2025 10:45:56": "This is my first note"},
          {"11/12/2025 10:46:03": "Thisis my"}
]
}
```

---

## 🛠 Requirements

* Python 3.x
* No external dependencies (unless your project adds some)

---

## 📌 Future Enhancements (Optional Ideas)

* Add password protection
* Add categories/tags for easier filtering
* Add GUI interface
* Sync with cloud storage

---

## 📄 License

This project is open-source and free to use.

---


