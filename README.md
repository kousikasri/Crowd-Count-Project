# Crowd Count Project 🚶‍♂️📊

A real-time crowd monitoring and analytics system using **YOLO-based people detection**, **zone-wise counting**, **alerts**, and an **admin dashboard**.  
This project is designed for **public safety monitoring**, **crowd management**, and **smart surveillance applications**.

---

## 🔥 Features

### 🎥 Real-Time People Detection
- YOLOv8-based person detection from video feeds
- Supports multiple camera inputs
- Live camera preview in admin dashboard

### 🗺️ Zone Management
- Draw zones directly on live camera feed
- Name zones (Entry, Exit, Waiting Area, etc.)
- Edit and delete zones dynamically
- Store zone coordinates for analytics

### 📊 Analytics Dashboard
- Zone-wise people count (Bar Chart)
- Time-based people count trends (Line Chart)
- Real-time analytics updates
- Historical data storage

### 🚨 Alert & Threshold System
- Admin-controlled threshold settings per zone
- On-screen alert notifications
- Siren sound alert on threshold breach
- Acknowledge alerts to prevent duplicates

### 👥 User Management
- View users, roles, status, and last login
- Enable / disable user accounts
- Change user roles (Admin ↔ User)
- Delete users (admin protected)

### 📤 Data Export
- Store historical crowd data
- Export analytics as CSV / PDF
- Data includes:
  - Timestamp
  - Camera ID
  - Zone ID
  - People Count

---

## 🛠️ Technology Stack

### Backend
- Python
- Flask
- OpenCV
- YOLOv8
- SQLite (for analytics history)

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Tools
- GitHub
- GitHub Releases
- Git LFS (optional)

---

## 📁 Project Structure

