# 🐍 Snake Game - SHLOKGAMES

A classic Snake game built with Python and Turtle graphics, featuring modern enhancements and special gameplay mechanics.

## 🎮 Features

## 🎮 Game Modes

### 🎮 Normal Mode
- **Classic Gameplay**: Traditional snake game experience
- **Consistent Speed**: Snake moves at steady pace throughout
- **Endless Play**: No level restrictions, play as long as you can survive
- **Focus on Score**: Pure score-based challenge

### 🚀 Career Mode  
- **50 Progressive Levels**: Start easy, get increasingly challenging
- **Dynamic Difficulty**: Snake speed increases with each level
- **Level Progression**: Advance every 50 points scored
- **Speed Challenge**: From 100ms delay (Level 1) to 22ms delay (Level 50)
- **Color-Coded Levels**:
  - 🟢 Levels 1-10: Easy (Green)
  - 🟠 Levels 11-25: Medium (Orange) 
  - 🔴 Levels 26-40: Hard (Red-Orange)
  - 🔥 Levels 41-50: Extreme (Pink-Red)

### Enhanced Visual Features
- **Realistic Snake Design**: 3D-styled snake with gradient body segments
- **Stylish Head**: Distinctive snake head with forest green color
- **Gradient Body**: Body segments with alternating shades and size variation
- **Professional UI**: Dark theme with glowing text effects
- **Animated Loading Screen**: SHLOKGAMES branding with emojis
- **Enhanced Game Over**: Stylish game over screen with background effects

### Audio Features
- **Sound Effects**: Eating sounds, special food sounds, and game over audio
- **Audio Feedback**: Different sounds for regular and special food

### Gameplay Features
- **Dual Game Modes**: Normal (classic) and Career (50 levels) modes
- **Progressive Difficulty**: Career mode increases speed every level
- **Score System**: Track current score and high score with golden styling
- **Special Green Food**: Appears every 10 seconds, worth 20 points
- **Visual Score Card**: Mode-specific display with level tracking
- **Level Progression**: Visual level indicator with color-coded difficulty
- **Game Over Screen**: Shows final score and restart option

## 🎯 How to Play

1. **Start the Game**: Run `python snake.py`
2. **Choose Mode**: 
   - Press **N** for Normal Mode (classic gameplay)
   - Press **C** for Career Mode (50 levels with increasing difficulty)
3. **Controls**: 
   - ↑ Arrow Key: Move Up
   - ↓ Arrow Key: Move Down
   - ← Arrow Key: Move Left
   - → Arrow Key: Move Right
   - SPACE: Restart game (when game over)

4. **Scoring**:
   - Red Food: 10 points
   - Green Special Food: 20 points (appears every 10 seconds)

5. **Objective**: 
   - **Normal Mode**: Eat food to grow and increase your score
   - **Career Mode**: Progress through all 50 levels while achieving high scores

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Turtle graphics (included with Python)
- Pygame (for sound effects)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/shloksathe18-dotcom/SnakeGame.git
cd SnakeGame
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python snake.py
```

## 🎨 Game Screenshots

- **Mode Selection**: Choose between Normal and Career modes with stylish UI
- **Loading Screen**: Features SHLOKGAMES branding with emojis and glow effects
- **Normal Mode**: Classic gameplay with realistic 3D snake, orange food, bright green special food
- **Career Mode**: Progressive difficulty with level display and speed indicators
- **Score Display**: Mode-specific score card with level tracking (Career mode only)
- **Game Over**: Stylish game over screen with red background and emoji effects

## 🔧 Technical Details

- **Language**: Python 3
- **Graphics**: Turtle Graphics Library
- **Audio**: Pygame Mixer for sound effects
- **Game Loop**: Timer-based movement system
- **Special Food Timer**: 10-second intervals
- **Screen Size**: 500x500 pixels
- **Game Speed**: 100ms delay between moves
- **Visual Style**: 3D gradient snake with realistic head design

## 🏆 Game Mechanics

### Mode Selection System
- Interactive mode selection screen with visual options
- Normal mode for classic snake experience
- Career mode for progressive challenge

### Career Mode Progression
- 50 levels of increasing difficulty
- Level advancement every 50 points
- Speed increases from 100ms to 22ms delay
- Color-coded difficulty indicators

### Special Food System
- Green special food spawns every 10 seconds
- Stays visible for 5 seconds before disappearing
- Worth double points (20 vs 10)
- Adds strategic gameplay element

### Score System
- Current score displayed in real-time
- High score persistence during game session
- New high score celebration
- Mode-specific score card design

## 🎯 Future Enhancements

- [ ] Persistent high score storage
- [ ] Multiple difficulty levels
- [ ] Sound effects
- [ ] Power-ups and obstacles
- [ ] Multiplayer mode

## 📝 Credits

**Developer**: Shlok Sathe (@iishlok23)
**Brand**: SHLOKGAMES
**Repository**: https://github.com/shloksathe18-dotcom/SnakeGame

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📞 Contact

- **GitHub**: [@shloksathe18-dotcom](https://github.com/shloksathe18-dotcom)
- **Project Link**: https://github.com/shloksathe18-dotcom/SnakeGame

---

**Enjoy the game! 🎮🐍**

*Made with ❤️ by Shlok - SHLOKGAMES*
