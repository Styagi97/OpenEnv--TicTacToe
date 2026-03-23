# 🎮 TicTacToe API

This project implements a simple **TicTacToe game environment** using **FastAPI**.  
It exposes REST endpoints so you can reset the game, make moves, and check the current state.  
The app is containerized with Docker and ready to deploy on Hugging Face Spaces or any server.

---

## 🚀 Features
- FastAPI backend with `/reset`, `/step`, and `/state` endpoints
- Dockerized for easy deployment
- Lightweight and beginner‑friendly project structure

---

## 📂 Project Structure
TicTacToe/
├── app.py              # FastAPI entrypoint (defines routes)
├── environment.py      # Core TicTacToe game logic
├── models.py           # Pydantic models (MoveAction, GameState)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker setup for deployment
├── README.md           # Documentation
