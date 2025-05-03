# jpfashionista 👘🎥  
> A machine learning tool that auto-detects outfit segments in fashion influencer videos — blending my love for ML, MLOps, and Japanese streetwear.

## 📌 Overview
jpfashionista is a video summarization prototype that processes fashion-focused video content (e.g. Japanese vlogs) and detects segments where outfit changes or styling moments occur. It’s designed as a creator-focused tool — to automate boring editing tasks and enhance discoverability.

This project reflects my dual passion for fashion and machine learning, and is part of my exploration into MLOps workflows in the context of media-focused ML systems.

## 🚀 Features
- 🎯 Basic scene segmentation using frame difference + face/pose detection
- 🧵 Visual summary (thumbnail grid of detected outfits)
- 🎧 Audio-based filtering (removes talking heads / static scenes)
- 🔄 Deployed using a minimal MLOps pipeline: preprocessing, inference, result visualization

## 🛠 Tech Stack
- Python, OpenCV, Numpy
- YOLOv8 (for optional pose/body detection)
- ffmpeg for video processing
- Streamlit (or CLI for MVP)
- GitHub Actions (for pipeline automation)
- Docker + Makefile (containerized run)

## 📂 Folder Structure

