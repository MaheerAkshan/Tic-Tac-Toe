# Tic-Tac-Toe# Tic-Tac-Toe AI {#tic-tac-toe-ai}

## 1. Project Overview {#overview}
An implementation of the classic Tic-Tac-Toe game featuring an unbeatable AI opponent using the Minimax algorithm with Alpha-Beta pruning. This project demonstrates fundamental concepts in game theory and search algorithms.

## 2. Features {#features}
- 🎮 Human vs AI gameplay
- 🤖 Unbeatable AI using Minimax algorithm
- ⚡ Optimized with Alpha-Beta Pruning
- 📊 Score tracking
- 🔄 Option to play first or second
- 🖥️ Clean console-based interface

## 3. Algorithms {#algorithms}
### Minimax Implementation:
```python
def minimax(board, depth, is_maximizing):
    # Base cases
    if check_win(board, AI_MARKER):
        return 1
    if check_win(board, HUMAN_MARKER):
        return -1
    if check_tie(board):
        return 0
    
    # Recursive case
    if is_maximizing:
        best_score = -float('inf')
        for move in available_moves(board):
            make_move(board, move, AI_MARKER)
            score = minimax(board, depth+1, False)
            undo_move(board, move)
            best_score = max(score, best_score)
        return best_score
    else:
        # Minimizing player logic...
def alphabeta(board, depth, alpha, beta, is_maximizing):
    # Similar structure with pruning
    if is_maximizing:
        for move in available_moves(board):
            # ...
            alpha = max(alpha, score)
            if alpha >= beta:
                break
            # ...
    else:
        # ...
```
# Tic-Tac-Toe AI

## 4. Getting Started
1. Download the Python files
2. Run `tictactoe.py`
3. Follow on-screen instructions

## 5. How to Play
Select positions 1-9 corresponding to
The AI will automatically respond with perfect moves.

## 6. Technical Details
- **Language**: Python 3
- **Dependencies**: None
- **Algorithm Complexity**:
  - Minimax: O(bᵈ)
  - Alpha-Beta: O(√bᵈ)
  (b = branching factor, d = depth)

## 7. Project Structure
- `tictactoe.py` - Main game logic
- `ai.py` - AI implementation
- `tests/` - Unit tests

## 8. Future Improvements
- Graphical user interface
- Adjustable difficulty
- Multiplayer support
- Machine learning version

## 9. Contributing
Contributions welcome! Please:
1. Fork the project
2. Create a feature branch
3. Submit a pull request

## 10. License
MIT License
