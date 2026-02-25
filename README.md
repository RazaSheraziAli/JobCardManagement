Here is a professional, standalone **README.md** specifically for your Job Card Manager. It is designed to look like a high-end GitHub repository for **TechProServices**.

---

# 📋 TechPro Job Manager

> **A Cross-Platform, Cloud-Synced Repair Tracking System for TechProServices (PTY) LTD.**

The **TechPro Job Manager** is a professional tool built to streamline the intake and management of computer and laptop repairs. Designed for the modern technician, it replaces paper-based workflows with a secure, digital dashboard that works seamlessly on Windows, macOS, and Android.


## ✨ Key Features

* **Unified Intake Form:** Quickly capture client names, device models (Dell, HP, Lenovo, etc.), and detailed issue descriptions.
* **Dual-Layer Storage:** * **Local:** Uses `SQLite` for instant data retention on your laptop.
* **Cloud:** Integrates with `Supabase` (PostgreSQL) for real-time synchronization across multiple devices.
* **Adaptive UI:** Built with `Flet` (Flutter for Python), offering a responsive design that looks native on both desktop and mobile.
* **Status Tracking:** Manage the lifecycle of a repair from "Pending" to "In Progress" to "Completed."
* **Searchable Database:** Instantly retrieve past job cards to review repair history for recurring clients.

---

## 🏗️ Technical Stack

* **Language:** Python 3.10+
* **UI Framework:** [Flet](https://flet.dev/) (Flutter-based)
* **Local Database:** SQLite

---

## 🚀 Getting Started

### Prerequisites

1. Python installed from [python.org](https://www.python.org/).


### Installation

1. **Clone the project:**
```bash
git clone https://github.com/RazaSheraziAli/JobCardManagement/.git
cd techpro-job-manager

```


### Running the App

```bash
python main.py

```

---

## 📱 Mobile Deployment

To run this on your Android device for on-site call-outs:

1. Install the **Flet** app from the Google Play Store.
2. Run the following command on your laptop (ensuring both are on the same Wi-Fi):
```bash
flet run --android

```



---

## 🛠️ Roadmap

* [ ] **PDF Generation:** Automatically generate and email PDF job cards to clients.
* [ ] **WhatsApp Integration:** Send status updates directly to clients' phones.
* [ ] **Inventory Link:** Track parts used (SSDs, RAM) from a built-in inventory list.

---

## 👤 Author

**Sherazi Ali** Founder & Lead Developer, **TechProServices (PTY) LTD** *ICT Specialist | Reservoir Hills, Durban, ZA*

---
