<div align="center">

# 🗺️ Map Gamer: The Arab World Challenge 🌍
### *Where Python Graphics Meet Geographical Mastery* 🎯✨

<img src="https://raw.githubusercontent.com/abhisheknaiidu/abhisheknaiidu/master/raw/giticons/python.svg" width="50" height="50" alt="Python" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
<img src="https://img.shields.io/badge/Turtle_GUI-🐍-green?style=for-the-badge" alt="Turtle GUI" />

---

> *"Interactive real-time plotting of geographic data. Test your regional knowledge coordinate-by-coordinate!"* 📍

<img width="913" height="528" alt="Map Game" src="https://github.com/user-attachments/assets/80a1c950-8334-4b66-a392-361f1edefedd" />

<img src="gameplay.gif" alt="Map Gamer Gameplay" width="75%"/>

*🍿 Live Gameplay Demo: Guessing Arab countries and plotting coordinates in real-time!*

</div>

---

## 🌟 About The Game
**Map Gamer: The Arab World Challenge** is a dynamic Python application that blends interactive graphical interfaces with clean data extraction. Players test their knowledge of the Arab World map by guessing countries. When guessed correctly, the app dynamically extracts the exact `x` and `y` coordinates from a dataset and plots the country name directly on the graphical screen!

---

## 🚀 Key Features

| Feature | Description | Status |
| :--- | :--- | :---: |
| 📍 **Real-Time Coordinate Plotting** | Dynamically locates and writes correctly guessed countries onto the interactive map. | ✅ Active |
| 🧠 **Interactive Text Input Prompt** | Tracks correct score progress (e.g., `0/22 guessed`) out of the total target countries in real-time. | ✅ Active |
| 💾 **Automated Missed-Country Tracker** | Generates a custom `Missing_Countries.csv` file upon exiting so players can review what they missed. | ✅ Active |

---

## 🎮 How to Play

1. Run `main.py`.
2. Type the name of an Arab country in the pop-up text prompt (e.g., "Egypt", "Saudi Arabia") and hit **Enter**.
3. If correct, the country name will automatically be plotted on the map!
4. Type **`Exit`** at any time to close the game and automatically save a list of countries you missed in `Missing_Countries.csv`.

---

## 🌟 The Evolution of This Project (A Learning Journey)
> *"Combining GUI interaction with real-world Data Analysis!"* 🚀

Here is how this project was designed step-by-step:

| Phase | Core Mechanism | What I Built & Learned | Status |
| :--- | :--- | :--- | :---: |
| 🎨 **Step 1: Graphical Setup** | *Turtle Module* | Configured the interactive canvas screen, custom background map image (of the Arab World), and input dialog mechanics. | ✅ Done |
| 📊 **Step 2: Data Extraction** | *Pandas DataFrames* | Sliced `coordinates.csv` using Pandas to query `x` and `y` positions dynamically based on player input. | ✅ Done |
| 📝 **Step 3: Learning Retention** | *File I/O Automation* | Implemented custom File I/O logic to cross-reference missed countries and save them into a printable review file. | ✅ Level Up! |

*💡 Summary: Gamifying learning is one of the most effective ways to master Python data structures!*

---

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3 🐍
* **GUI Engine:** Python `turtle` Library
* **Data Processing:** `pandas` (for CSV parsing and coordinate indexing)

---

<div align="center">

### 💡 Let's Connect!
Crafted with ❤️ and precision by **Engy Magdy**  
*Computer Science & Mathematics Student* 🎓

</div>
