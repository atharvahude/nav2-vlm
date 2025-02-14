# nav2-vlm

# 🤖  Ros2 Navigation2 with Vision-Language Models


*A Vision-Language Model (VLM) powered system for waypoint generation and intelligent navigation using ROS2, Nav2, and TurtleBot3.*


# This project is in active development. 
# Base Results (Youtube Demo) : https://youtu.be/9UGKGdawtN0?si=5kDADisyX7LLFk6V
---

## 🚀 Project Overview
This project integrates **Vision-Language Models (VLMs)** with **ROS2 Nav2** to enhance **TurtleBot3’s navigation** in complex environments.  
- The system **analyzes cost maps and occupancy grids**.
- It generates **intelligent waypoints** using **GPT-4V (Vision)**.
- Converts **pixel coordinates** to **real-world waypoints** for TurtleBot3.
- Executes **autonomous navigation** while avoiding obstacles dynamically.

---

## 🎯 Features
✅ **AI-Powered Path Planning** – Generates waypoints intelligently.  
✅ **Cost Map & Occupancy Grid Analysis** – Extracts spatial insights.  
✅ **Pixel-to-World Coordinate Conversion** – Ensures real-world accuracy.  
✅ **ROS2 Nav2 Integration** – Executes AI-generated waypoints.  
✅ **Gazebo Simulation & RViz Visualization** – Test before real-world deployment.  

---


---

## 🔧 Installation & Setup
### **1️ Prerequisites**
- ROS2 **Humble**  
- **Nav2** (Navigation Stack)  
- **Gazebo** (for simulation)  
- **OpenAI API Key** (for GPT-4 Vision)  
- Python libraries: `numpy`, `opencv-python`, `PIL`, `requests`

### **2 Clone 
git clone https://github.com/atharvahude/nav2-vlm.git
cd nav2-vlm

### **3 Setup the simulation
- Can use the world files that I have made or use your own

### **4 Capture the map with Lidar SLAM using the Cartographer and SLAM toolkit

### **5 Convert the map image .pgm to png and rename it as input.png

### **6 Start the cartographer to visualize the Global and Local Planner 

### **7 run the nav2_test.py



