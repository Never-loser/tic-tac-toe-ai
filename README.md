# 🎯 Unbeatable Tic-Tac-Toe AI

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Minimax-red.svg)](https://en.wikipedia.org/wiki/Minimax)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **An AI that never loses.** Built with the Minimax algorithm, this Tic-Tac-Toe engine guarantees perfect gameplay — the best you can achieve is a draw.

## 🎮 Demo


| O | X | O |
| X | O | X |
| O | X | X |

## ✨ Features

- 🤖 **Unbeatable AI** – Uses Minimax algorithm to evaluate all possible moves
- ♾️ **Perfect Gameplay** – AI always chooses the optimal move
- 🎯 **Zero Dependencies** – Pure Python, no external libraries
- 🖥️ **Clean Console Interface** – Simple and intuitive gameplay
- 📊 **Game Tree Evaluation** – Recursively analyzes up to 362,880 possible game states

## 🧠 How It Works

The AI uses the **Minimax algorithm** with depth-based scoring:

| Outcome | Score |
|---------|-------|
| AI Wins | `+10 - depth` |
| Human Wins | `-10 + depth` |
| Draw | `0` |

The algorithm:
1. Recursively simulates all possible moves
2. Assigns scores to terminal states (win/loss/draw)
3. AI maximizes its score while human minimizes
4. Selects the move with the highest guaranteed outcome

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/Never-loser/tic-tac-toe-ai.git

# Navigate to project directory
cd tic-tac-toe-ai

# Run the game
python tic_tac_toe.py
```
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9

1. Enter a number (1-9) to place your mark X
2. AI responds with O
3. Try to win — but you can't!

### 📁 Project Structure
tic-tac-toe-ai/
├── tic_tac_toe.py    # Main game file
├── README.md         # Documentation
└── LICENSE           # MIT License


### 🔬 Technical Deep Dive
## Minimax Implementation
```
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 10 - depth
    elif check_winner(board, HUMAN):
        return -10 + depth
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -inf
        for move in get_empty_cells(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        # Minimizing logic...
```

## Complexity Analysis
+ Time Complexity: O(9!) = 362,880 maximum recursive calls

+ Space Complexity: O(9) recursion depth

+ Optimal Strategy: Perfect play guarantees at least a draw

## 🎯 Why This Implementation?

| Approach | Pros | Cons |
|----------|------|------|
| **Rule-Based** | Fast, simple | Hard-coded, not perfect |
| **Machine Learning** | Adaptive | Requires training data |
| **Minimax** ✅ | Perfect play, provable optimal | Recursive overhead |

___________________________________________________________________________________________________________________
### 🧪 Testing
Test the AI's unbeatable nature:

```
# Run multiple games automatically
for _ in range(100):
    result = play_game(autoplay=True)
    assert result != 'human_win'  # AI never loses
```

### 📈 Future Improvements
+ Alpha-beta pruning for faster evaluation

+ GUI interface with Pygame or Tkinter

+ Web version using Flask + JavaScript

+ Different difficulty levels

+ 4x4 board support

### 🤝 Contributing
Contributions are welcome!

Fork the repository

Create a feature branch (git checkout -b feature/amazing)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing)

Open a Pull Request

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

## 📧 Contact
- @neverloser - your.ilia95081@gmail.com

Project Link: https://github.com/Never-loser/tic-tac-toe-ai

## ⭐ Show Your Support
If this project helped you understand the Minimax algorithm, give it a ⭐!

## 💼 Why I Built This

This project demonstrates:
- Understanding of recursive algorithms
- Game theory implementation
- Clean, maintainable Python code
- Technical documentation skills
