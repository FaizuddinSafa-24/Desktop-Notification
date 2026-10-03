# 🖥️ Desktop Notification (Python)

A lightweight Python automation project that sends a desktop health reminder using native system notifications.

This repository demonstrates my ability to build clean, practical automation scripts with:
- Python scripting fundamentals
- third-party package integration (`plyer`)
- exception handling for reliability
- simple UX-focused productivity tooling

---

## ✨ What this project does

The script sends a notification with:
- a **custom title**
- a **custom message**
- a **custom app icon**
- a configurable **timeout**

Use case: quick personal reminder automation (health, study, meeting, or break alerts).

---

## 🧰 Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3 |
| Notification API | `plyer.notification` |
| Runtime behavior | `time.sleep` scheduling |

---

## 📂 Project Structure

```text
Desktop-Notification-/
├── notifi.py               # Main notification script
├── daily-health-app.ico    # Notification icon
├── LICENSE
└── README.md
```

---

## ⚙️ Setup

1. Clone the repository
2. Install dependency:

```bash
pip install plyer
```

3. Run the script:

```bash
python notifi.py
```

---

## 🧪 Current Behavior

When executed, the script:
1. Triggers a desktop notification
2. Waits for 60 minutes before exiting (`time.sleep(60*60)`)

---

## 🔧 Customization

In `notifi.py`, you can easily customize:
- `title` → Notification heading
- `message` → Notification body
- `app_icon` → `.ico` file path
- `timeout` → Notification display duration

This makes the script reusable for multiple reminder workflows.

---

## 💡 Professional Skills Highlighted

- Writing concise and maintainable Python automation scripts
- Integrating external libraries with clear, readable code
- Applying defensive programming (`try/except`)
- Building user-centered utility tools with practical real-world value

---

## 📜 License

This project is licensed under the MIT License.
