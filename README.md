<div align="center">

# 💊 Medical Management System & Billing

### *Your Complete Pharmacy Solution*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*A powerful, user-friendly pharmacy management system built with Python to streamline your medical store operations*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

---

</div>

## 🌟 Features

### 📦 **Inventory Management**
- ✅ Add, update, and delete medicine records with ease
- 🔍 Advanced search by medicine name or symptoms
- 📊 Real-time stock tracking and monitoring
- ⚠️ Expiry date management
- 🏷️ Comprehensive medicine information (dosage, side effects, precautions)

### 💳 **Smart Billing System**
- 🧾 Auto-generated unique bill numbers
- 🛒 Interactive shopping cart functionality
- 💰 Automatic price calculation
- 💾 Save and retrieve bills
- 📧 Customer information management

### 🔐 **User Management**
- 👤 Secure employee login system
- 📝 Customer registration portal
- 🎯 Role-based access control
- 🏢 Multi-branch support ready

### 🎨 **Modern Interface**
- 🖼️ Clean, intuitive GUI design
- 📱 Organized layouts with multiple frames
- 🎭 Visual feedback with images and icons
- 📜 Scrollable data tables

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8 or higher
MySQL Server 5.7+
```

### Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/medical-management-system.git
cd medical-management-system
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install pillow mysql-connector-python
```

3️⃣ **Set up the database**
```sql
CREATE DATABASE medical;
USE medical;

-- Medicine reference table
CREATE TABLE med (
    RefName VARCHAR(50) PRIMARY KEY,
    MedName VARCHAR(100) NOT NULL
);

-- Main pharmacy inventory table
CREATE TABLE pharmacy (
    RefName VARCHAR(50) PRIMARY KEY,
    companyname VARCHAR(100),
    TypeMed VARCHAR(50),
    MedicineName VARCHAR(100),
    LotNo VARCHAR(50),
    IssueDate VARCHAR(20),
    ExpDate VARCHAR(20),
    Symptom VARCHAR(200),
    SideEff VARCHAR(200),
    Precaution VARCHAR(200),
    Dosage VARCHAR(100),
    price DECIMAL(10,2),
    ProductQt INT
);
```

4️⃣ **Configure database connection**

Edit the connection details in the Python files:
```python
conn = mysql.connector.connect(
    host="localhost",
    username="your_username",      # Change this
    password="your_password",      # Change this
    database="medical"
)
```

5️⃣ **Create required directories**
```bash
mkdir Bills
mkdir Images
```

6️⃣ **Add images** (Update paths in code accordingly)
- Place your logo and UI images in the `Images` folder

---

## 💻 Usage

### Launch Main Application
```bash
python medicalmangement.py
```

### Launch Billing System Only
```bash
python Billing.py
```

### Launch Login Portal
```bash
python main.py
```

---

## 📸 Screenshots

<div align="center">

### 🏠 Main Dashboard
![Dashboard](path/to/screenshot1.png)

### 💊 Medicine Management
![Medicine Management](path/to/screenshot2.png)

### 🧾 Billing Interface
![Billing](path/to/screenshot3.png)

</div>

---

## 🗂️ Project Structure

```
medical-management-system/
│
├── 📄 medicalmangement.py    # Main inventory management application
├── 📄 Billing.py              # Standalone billing system
├── 📄 main.py                 # Authentication & menu system
├── 📄 requirements.txt        # Python dependencies
├── 📁 Bills/                  # Generated bills storage
├── 📁 Images/                 # UI images and assets
│   ├── logo.jpg
│   ├── Med.jpg
│   ├── Capsule.jpg
│   └── ...
├── 📄 README.md
└── 📄 LICENSE
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Core Programming Language |
| ![Tkinter](https://img.shields.io/badge/-Tkinter-green?style=flat) | GUI Framework |
| ![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat&logo=mysql&logoColor=white) | Database Management |
| ![Pillow](https://img.shields.io/badge/-Pillow-yellow?style=flat) | Image Processing |

---

## 📋 Medicine Types Supported

- 💊 **Tablets**
- 💧 **Liquids**
- ⚪ **Capsules**
- 💉 **Injections**
- 🧴 **Creams**
- 💧 **Drops**

---

## 🎯 Key Functionalities

### Inventory Operations

| Operation | Description | Status |
|-----------|-------------|--------|
| ➕ Add Medicine | Insert new records | ✅ Working |
| ✏️ Update | Modify existing data | ✅ Working |
| 🗑️ Delete | Remove records | ✅ Working |
| 🔍 Search | Find by name/symptom | ✅ Working |
| 🔄 Reset | Clear input fields | ✅ Working |

### Billing Operations

| Operation | Description | Status |
|-----------|-------------|--------|
| 🛒 Add to Cart | Add items with quantity | ✅ Working |
| 🧾 Generate Bill | Create formatted invoice | ✅ Working |
| 💾 Save Bill | Store as text file | ✅ Working |
| 🚪 Exit | Close application | ✅ Working |

---

## ⚙️ Configuration

### Database Settings

Create a `config.py` file (recommended):

```python
# config.py
DB_CONFIG = {
    'host': 'localhost',
    'username': 'your_username',
    'password': 'your_password',
    'database': 'medical'
}
```

### Image Paths

Update image paths in the code to match your directory structure:

```python
# Instead of hardcoded paths
img1 = Image.open("./Images/logo.jpg")
```

---

## 🚧 Roadmap

- [ ] 🔐 Enhanced authentication with password encryption
- [ ] 📊 Sales analytics and reporting dashboard
- [ ] 📱 Responsive design for different screen sizes
- [ ] 🔔 Low stock alerts and notifications
- [ ] 📈 Expiry date warnings
- [ ] 🖨️ Print functionality for bills
- [ ] 📧 Email receipt feature
- [ ] 🌐 Multi-language support
- [ ] ☁️ Cloud database integration
- [ ] 📱 Mobile app version

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

1. 🍴 Fork the Project
2. 🌿 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

---

## 🐛 Known Issues

- ⚠️ Image paths are hardcoded - need configuration file
- ⚠️ Database credentials exposed in code
- ⚠️ Limited error handling in some modules
- ⚠️ SQL injection vulnerability in search function

**Working on fixes! Contributions welcome!**

---

## 👨‍💻 Authors

**Your Name**
- GitHub: nikhilbhoir0808
- Email: nikhilbhoir710@gmail.com

---

## 🙏 Acknowledgments

- Inspired by real-world pharmacy needs
- Built with ❤️ using Python

---

<div align="center">

### ⭐ If you find this project useful, please consider giving it a star!

**Made with 💊 for pharmacies worldwide**

[Report Bug](https://github.com/yourusername/medical-management-system/issues) • [Request Feature](https://github.com/yourusername/medical-management-system/issues)

</div>
