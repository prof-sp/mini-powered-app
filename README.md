# 🍅 AI-Powered Food Quality & Safety Monitoring System

An intelligent, non-invasive solution to detect food spoilage and contamination using computer vision and deep learning. Designed to reduce food waste, improve safety, and empower stakeholders across the supply chain—from farm to consumer.

---

## 🌍 SDG Alignment

This project directly supports:

* **SDG 2: Zero Hunger** – Reduces food waste and improves supply chain efficiency.
* **SDG 3: Good Health & Well-being** – Prevents foodborne illness through early detection.
* **SDG 11 & 13 (Extensions)** – Adaptable for smart waste sorting and environmental monitoring.

---

## 🚀 Features & Modules

### 👨‍🌾 Farmer Mobile App (Flutter)

* Scan produce using smartphone camera
* Instant spoilage classification (Fresh / Spoiled / Contaminated)
* Optional **offline-first model inference (TFLite)**

### 🏢 Warehouse Dashboard (React)

* Live camera feeds with spoilage alerts
* Batch tracking and severity tagging
* Automated reporting via REST API

### 🛒 Retailer Interface

* QR code scan for incoming shipments
* Shelf-life prediction and acceptance recommendations
* Inventory logging

### 📊 Central Dashboard

* Analytics on spoilage trends and waste reduction
* Compliance reporting for regulators
* Map view of flagged locations

---

## 🧰 Tech Stack

| Layer       | Technology Used                                    |
| ----------- | -------------------------------------------------- |
| Frontend    | **Flutter (mobile)**, **React (web)**              |
| Backend     | **FastAPI**, **Python**                            |
| ML Models   | **TensorFlow** / PyTorch (CNN + anomaly detection) |
| Database    | **PostgreSQL**                                     |
| Cloud       | AWS / GCP (Docker, S3, Lambda)                     |
| Integration | REST APIs, IoT camera feeds, ERP/SCM systems       |

---

## 📦 Code Architecture

```
ai-food-quality-monitoring/
├─ backend/ (FastAPI backend)
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ models.py
│  │  ├─ schemas.py
│  │  ├─ crud.py
│  │  ├─ ml_inference.py
│  │  ├─ database.py
│  │  └─ config.py
│  ├─ Dockerfile
│  └─ requirements.txt
├─ ml/ (Training + TFLite export)
│  ├─ train.py
│  ├─ export_tflite.py
│  └─ saved_models/
├─ frontend/
│  ├─ dashboard/ (React)
│  │  └─ src/
├─ mobile/
│  └─ flutter_app/
│     ├─ lib/
│     └─ pubspec.yaml
├─ docker-compose.yml
└─ README.md
```

---

## ⚙️ Key Code Components

### **1. Machine Learning (TensorFlow)**

* **EfficientNetB0 transfer learning** for fresh/spoiled/contaminated classification.
* `train.py` trains the CNN.
* `export_tflite.py` converts the trained model to **TFLite** for mobile offline inference.

### **2. Backend API (FastAPI)**

Core endpoints:

* `POST /inspect` — Upload image → receive classification + confidence.
* `GET /inspections` — Fetch inspection history.
* Auto-saves inspections to **PostgreSQL**.

ML inference powered by:

* `ml_inference.py` (image preprocessing + TF model prediction)

### **3. React Warehouse Dashboard**

* Displays real-time inspection logs.
* Table view includes batch, label, confidence, timestamp.
* Polls backend every 5 seconds.

### **4. Flutter Farmer App**

* Captures images via camera.
* Uploads to backend OR performs on-device TFLite inference.
* Simple result display.

### **5. Docker & Compose**

`docker-compose.yml` includes:

* **PostgreSQL** database
* **Backend FastAPI**
* Mounted model files & uploads

---

## 🔧 Installation & Setup

### **Clone the Repository**

```bash
git clone https://github.com/your-username/ai-food-quality-monitoring.git
cd ai-food-quality-monitoring
```

---

## 🧠 ML Model Setup

### **Train the model**

```bash
cd ml
python train.py
```

### **Export TFLite model**

```bash
python export_tflite.py
```

---

## 🖥 Backend Setup (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API available at: `http://localhost:8000`

---

## 🌐 Frontend Setup (React Dashboard)

```bash
cd frontend/dashboard
npm install
npm start
```

---

## 📱 Mobile App Setup (Flutter)

```bash
cd mobile/flutter_app
flutter pub get
flutter run
```

---

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

Services:

* Backend → `localhost:8000`
* Postgres → `localhost:5432`

---

## 🔗 Deployment

Live deployment link (coming soon):

```
https://your-deployment-url.com
```

---

## 📽️ Pitch Deck

Full presentation:

```
https://www.canva.com/design/DAG4UmhjPsY/IU3LDRmUhG-kVRreeaoXkw/edit
```

---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch:

```bash
git checkout -b feature/your-feature
```

3. Commit your changes:

```bash
git commit -m 'Add new feature'
```

4. Push to your branch:

```bash
git push origin feature/your-feature
```

5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## ✔️ What’s Next?

* Add on-device TFLite inference example for mobile
* Integrate real camera streams for warehouse monitoring
* Add auth (JWT) + user roles
* Add analytics & dashboards (charts + GIS maps)

If you want, I can generate **badges, diagrams, or a more polished README styling**.

