import turtle
import random
import time
import pygame

# Initialize pygame mixer for sound
try:
    pygame.mixer.init()
    # Create simple sound effects
    eat_sound = None
    special_eat_sound = None
    game_over_sound = None
except:
    eat_sound = None
    special_eat_sound = None
    game_over_sound = None

# Game constants
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
BASE_DELAY = 100
DELAY = 100

# Game variables
score = 0
high_score = 0
level = 1
max_level = 50
game_running = False
special_food_timer = 0
special_food_active = False
game_mode = None
mode_selected = False

# Snake variables
snake = []
snake_direction = "up"
food_pos = [0, 0]

# Movement offsets
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def play_sound(sound):
    """Play sound effect safely"""
    try:
        if sound:
            sound.play()
    except:
        pass

def show_loading_screen():
    """Display attractive animated loading screen"""
    screen.clear()
    screen.bgcolor("#0a0a23")  # Deep dark blue
    
    loading_pen = turtle.Turtle()
    loading_pen.hideturtle()
    loading_pen.penup()
    loading_pen.speed(0)
    
    # Create animated background stars
    create_background_stars()
    
    # Main title with glow effect
    loading_pen.goto(2, 102)  # Shadow
    loading_pen.color("#001a4d")
    loading_pen.write("SHLOKGAMES", align="center", font=("Arial", 28, "bold"))
    loading_pen.goto(0, 100)  # Main text
    loading_pen.color("#00ffff")
    loading_pen.write("SHLOKGAMES", align="center", font=("Arial", 28, "bold"))
    
    # Subtitle with snake emoji animation
    loading_pen.goto(0, 60)
    loading_pen.color("#32cd32")
    loading_pen.write("🐍", align="center", font=("Arial", 24, "normal"))
    
    loading_pen.goto(0, 30)
    loading_pen.color("#ffffff")
    loading_pen.write("SNAKE GAME", align="center", font=("Arial", 20, "bold"))
    
    loading_pen.goto(0, 10)
    loading_pen.color("#32cd32")
    loading_pen.write("🐍", align="center", font=("Arial", 24, "normal"))
    
    # Version info
    loading_pen.goto(0, -20)
    loading_pen.color("#888888")
    loading_pen.write("Version 2.0 - Enhanced Edition", align="center", font=("Arial", 10, "normal"))
    
    # Loading animation
    loading_pen.goto(0, -60)
    loading_pen.color("#ffff00")
    loading_pen.write("Loading", align="center", font=("Arial", 16, "bold"))
    
    screen.update()
    
    # Animated loading dots
    for i in range(3):
        time.sleep(0.5)
        loading_pen.goto(50 + i*15, -60)
        loading_pen.color("#ffff00")
        loading_pen.write(".", align="center", font=("Arial", 20, "bold"))
        screen.update()
    
    time.sleep(0.5)
    
    # Success message
    loading_pen.goto(0, -100)
    loading_pen.color("#00ff88")
    loading_pen.write("🎮 Ready to Play! 🎮", align="center", font=("Arial", 14, "bold"))
    
    # Developer credit
    loading_pen.goto(0, -130)
    loading_pen.color("#666699")
    loading_pen.write("Developed by Shlok", align="center", font=("Arial", 10, "italic"))
    
    screen.update()
    time.sleep(1)
    loading_pen.clear()

def create_background_stars():
    """Create animated background stars"""
    star_pen = turtle.Turtle()
    star_pen.hideturtle()
    star_pen.penup()
    star_pen.speed(0)
    
    # Create random stars
    star_positions = []
    for _ in range(15):
        x = random.randint(-WIDTH//2, WIDTH//2)
        y = random.randint(-HEIGHT//2, HEIGHT//2)
        star_positions.append((x, y))
    
    # Draw twinkling stars
    colors = ["#ffffff", "#ffff99", "#99ffff", "#ff99ff"]
    for i, (x, y) in enumerate(star_positions):
        star_pen.goto(x, y)
        star_pen.color(random.choice(colors))
        star_pen.write("✦", align="center", font=("Arial", random.randint(8, 12), "normal"))
    
    screen.update()

def show_mode_selection():
    """Display attractive mode selection screen"""
    screen.clear()
    screen.bgcolor("#0a0a23")  # Deep dark blue
    
    mode_pen = turtle.Turtle()
    mode_pen.hideturtle()
    mode_pen.penup()
    mode_pen.speed(0)
    
    # Create background stars again
    create_background_stars()
    
    # Main title with glow effect
    mode_pen.goto(1, 151)  # Shadow
    mode_pen.color("#001a4d")
    mode_pen.write("🐍 SHLOKGAMES SNAKE 🐍", align="center", font=("Arial", 22, "bold"))
    mode_pen.goto(0, 150)  # Main text
    mode_pen.color("#00ffff")
    mode_pen.write("🐍 SHLOKGAMES SNAKE 🐍", align="center", font=("Arial", 22, "bold"))
    
    # Mode selection title
    mode_pen.goto(0, 100)
    mode_pen.color("#ffffff")
    mode_pen.write("SELECT GAME MODE", align="center", font=("Arial", 18, "bold"))
    
    # Decorative line
    mode_pen.goto(-100, 80)
    mode_pen.color("#32cd32")
    mode_pen.write("═" * 20, align="center", font=("Arial", 12, "normal"))
    
    # Normal Mode - Enhanced box
    mode_pen.goto(-150, 40)
    mode_pen.color("#2a4d3a")  # Dark green background
    mode_pen.begin_fill()
    for _ in range(2):
        mode_pen.forward(140)
        mode_pen.right(90)
        mode_pen.forward(100)
        mode_pen.right(90)
    mode_pen.end_fill()
    
    # Normal mode border
    mode_pen.goto(-152, 42)
    mode_pen.color("#00ff88")
    mode_pen.pensize(3)
    mode_pen.pendown()
    for _ in range(2):
        mode_pen.forward(144)
        mode_pen.right(90)
        mode_pen.forward(104)
        mode_pen.right(90)
    mode_pen.penup()
    mode_pen.pensize(1)
    
    mode_pen.goto(-80, 15)
    mode_pen.color("#00ff88")
    mode_pen.write("🎮 NORMAL", align="center", font=("Arial", 16, "bold"))
    mode_pen.goto(-80, -5)
    mode_pen.color("#ffffff")
    mode_pen.write("Classic Snake", align="center", font=("Arial", 11, "normal"))
    mode_pen.goto(-80, -20)
    mode_pen.color("#cccccc")
    mode_pen.write("Steady Speed", align="center", font=("Arial", 9, "normal"))
    mode_pen.goto(-80, -35)
    mode_pen.color("#ffff00")
    mode_pen.write("Press 'N'", align="center", font=("Arial", 12, "bold"))
    
    # Career Mode - Enhanced box
    mode_pen.goto(10, 40)
    mode_pen.color("#4d2a2a")  # Dark red background
    mode_pen.begin_fill()
    for _ in range(2):
        mode_pen.forward(140)
        mode_pen.right(90)
        mode_pen.forward(100)
        mode_pen.right(90)
    mode_pen.end_fill()
    
    # Career mode border
    mode_pen.goto(8, 42)
    mode_pen.color("#ff6b35")
    mode_pen.pensize(3)
    mode_pen.pendown()
    for _ in range(2):
        mode_pen.forward(144)
        mode_pen.right(90)
        mode_pen.forward(104)
        mode_pen.right(90)
    mode_pen.penup()
    mode_pen.pensize(1)
    
    mode_pen.goto(80, 15)
    mode_pen.color("#ff6b35")
    mode_pen.write("🚀 CAREER", align="center", font=("Arial", 16, "bold"))
    mode_pen.goto(80, -5)
    mode_pen.color("#ffffff")
    mode_pen.write("50 Levels", align="center", font=("Arial", 11, "normal"))
    mode_pen.goto(80, -20)
    mode_pen.color("#cccccc")
    mode_pen.write("Increasing Speed", align="center", font=("Arial", 9, "normal"))
    mode_pen.goto(80, -35)
    mode_pen.color("#ffff00")
    mode_pen.write("Press 'C'", align="center", font=("Arial", 12, "bold"))
    
    # Instructions with animation effect
    mode_pen.goto(0, -80)
    mode_pen.color("#32cd32")
    mode_pen.write("🎯 Choose your adventure! 🎯", align="center", font=("Arial", 14, "bold"))
    
    # Footer with developer info
    mode_pen.goto(0, -120)
    mode_pen.color("#666699")
    mode_pen.write("🎮 SHLOKGAMES - Premium Snake Experience", align="center", font=("Arial", 10, "normal"))
    
    mode_pen.goto(0, -140)
    mode_pen.color("#444466")
    mode_pen.write("Developed with ❤️ by Shlok", align="center", font=("Arial", 8, "italic"))
    
    screen.update()

def select_normal_mode():
    """Select normal mode"""
    global game_mode, mode_selected
    if not mode_selected:
        game_mode = "normal"
        mode_selected = True
        start_game()

def select_career_mode():
    """Select career mode"""
    global game_mode, mode_selected
    if not mode_selected:
        game_mode = "career"
        mode_selected = True
        start_game()

def start_game():
    """Start the game"""
    screen.clear()
    screen.bgcolor("#001122")
    screen.tracer(0)
    
    # Setup game objects
    setup_game_objects()
    
    # Register controls
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(restart_game, "space")
    
    # Reset and start
    reset_game()

def setup_game_objects():
    """Setup all game objects"""
    global pen, food, special_food, score_pen
    
    # Snake pen
    pen = turtle.Turtle()
    pen.shape("square")
    pen.color("#32CD32")  # Lime green
    pen.penup()
    pen.speed(0)
    
    # Food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("#FF4500")  # Orange red
    food.penup()
    food.speed(0)
    
    # Special food
    special_food = turtle.Turtle()
    special_food.shape("circle")
    special_food.color("#00FF00")  # Bright green
    special_food.penup()
    special_food.speed(0)
    special_food.hideturtle()
    
    # Score display
    score_pen = turtle.Turtle()
    score_pen.hideturtle()
    score_pen.penup()
    score_pen.color("white")
    score_pen.speed(0)

def update_score_display():
    """Update score display"""
    score_pen.clear()
    
    # Mode indicator
    mode_text = "CAREER" if game_mode == "career" else "NORMAL"
    mode_icon = "🚀" if game_mode == "career" else "🎮"
    
    score_pen.goto(-WIDTH//2 + 10, HEIGHT//2 - 30)
    score_pen.color("#00d4ff")
    score_pen.write(f"{mode_icon} {mode_text} MODE", align="left", font=("Arial", 12, "bold"))
    
    # Current score
    score_pen.goto(-WIDTH//2 + 10, HEIGHT//2 - 50)
    score_pen.color("#FFFFFF")
    score_pen.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))
    
    # High score
    score_pen.goto(-WIDTH//2 + 10, HEIGHT//2 - 70)
    score_pen.color("#FFD700")
    score_pen.write(f"High Score: {high_score}", align="left", font=("Arial", 14, "normal"))
    
    # Level (only in career mode)
    if game_mode == "career":
        score_pen.goto(-WIDTH//2 + 10, HEIGHT//2 - 90)
        score_pen.color("#FF6B35")
        score_pen.write(f"Level: {level}/{max_level}", align="left", font=("Arial", 14, "normal"))

def get_random_food_pos():
    """Get random food position"""
    x = random.randint(-WIDTH//2 + 20, WIDTH//2 - 20)
    y = random.randint(-HEIGHT//2 + 20, HEIGHT//2 - 20)
    return [x, y]

def get_distance(pos1, pos2):
    """Calculate distance between two points"""
    return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

def reset_game():
    """Reset game state"""
    global snake, snake_direction, food_pos, score, level, DELAY, game_running
    global special_food_timer, special_food_active
    
    # Reset snake
    snake = [[0, 0], [0, 20], [0, 40], [0, 60]]
    snake_direction = "up"
    
    # Reset game state
    score = 0
    level = 1
    DELAY = BASE_DELAY
    game_running = True
    special_food_timer = 0
    special_food_active = False
    
    # Position food
    food_pos = get_random_food_pos()
    food.goto(food_pos[0], food_pos[1])
    
    # Hide special food
    special_food.hideturtle()
    
    # Clear screen and update display
    pen.clearstamps()
    update_score_display()
    
    # Draw initial snake
    draw_snake()
    
    # Start movement
    move_snake()

def draw_snake():
    """Draw the snake"""
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

def move_snake():
    """Move the snake"""
    global snake_direction, high_score, special_food_timer, special_food_active
    
    if not game_running:
        return
    
    # Handle special food timer
    special_food_timer += 1
    if special_food_timer >= 100:  # 10 seconds
        if not special_food_active:
            spawn_special_food()
        special_food_timer = 0
    
    # Calculate new head position
    head = snake[-1].copy()
    head[0] += offsets[snake_direction][0]
    head[1] += offsets[snake_direction][1]
    
    # Screen wrapping
    if head[0] > WIDTH//2:
        head[0] = -WIDTH//2
    elif head[0] < -WIDTH//2:
        head[0] = WIDTH//2
    elif head[1] > HEIGHT//2:
        head[1] = -HEIGHT//2
    elif head[1] < -HEIGHT//2:
        head[1] = HEIGHT//2
    
    # Check self collision
    if head in snake:
        game_over()
        return
    
    # Add new head
    snake.append(head)
    
    # Check food collision
    if check_food_collision():
        # Grow snake (don't remove tail)
        pass
    else:
        # Remove tail
        snake.pop(0)
    
    # Draw snake
    draw_snake()
    
    # Update screen
    screen.update()
    
    # Schedule next move
    turtle.ontimer(move_snake, DELAY)

def check_food_collision():
    """Check if snake ate food"""
    global score, food_pos, special_food_active
    
    head = snake[-1]
    
    # Check regular food
    if get_distance(head, food_pos) < 20:
        play_sound(eat_sound)
        score += 10
        food_pos = get_random_food_pos()
        food.goto(food_pos[0], food_pos[1])
        
        # Level up in career mode
        if game_mode == "career":
            calculate_level()
        
        update_score_display()
        return True
    
    # Check special food
    if special_food_active and get_distance(head, [special_food.xcor(), special_food.ycor()]) < 20:
        play_sound(special_eat_sound)
        score += 20
        special_food.hideturtle()
        special_food_active = False
        
        # Level up in career mode
        if game_mode == "career":
            calculate_level()
        
        update_score_display()
        return True
    
    return False

def calculate_level():
    """Calculate level in career mode"""
    global level, DELAY
    
    if game_mode != "career":
        return
    
    new_level = min((score // 50) + 1, max_level)
    if new_level != level:
        level = new_level
        DELAY = max(BASE_DELAY - (level - 1) * 1.6, 22)
        DELAY = int(DELAY)

def spawn_special_food():
    """Spawn special food"""
    global special_food_active
    if not special_food_active:
        pos = get_random_food_pos()
        special_food.goto(pos[0], pos[1])
        special_food.showturtle()
        special_food_active = True
        turtle.ontimer(hide_special_food, 5000)

def hide_special_food():
    """Hide special food"""
    global special_food_active
    special_food.hideturtle()
    special_food_active = False

def game_over():
    """Handle game over with attractive screen"""
    global game_running, high_score
    
    game_running = False
    
    if score > high_score:
        high_score = score
    
    play_sound(game_over_sound)
    
    # Show attractive game over screen
    game_over_pen = turtle.Turtle()
    game_over_pen.hideturtle()
    game_over_pen.penup()
    game_over_pen.speed(0)
    
    # Background overlay
    game_over_pen.goto(-200, 150)
    game_over_pen.color("#1a0000")  # Dark red background
    game_over_pen.begin_fill()
    for _ in range(2):
        game_over_pen.forward(400)
        game_over_pen.right(90)
        game_over_pen.forward(300)
        game_over_pen.right(90)
    game_over_pen.end_fill()
    
    # Border with glow effect
    game_over_pen.goto(-202, 152)
    game_over_pen.color("#660000")
    game_over_pen.pensize(4)
    game_over_pen.pendown()
    for _ in range(2):
        game_over_pen.forward(404)
        game_over_pen.right(90)
        game_over_pen.forward(304)
        game_over_pen.right(90)
    game_over_pen.penup()
    game_over_pen.pensize(1)
    
    # Game over title with shadow effect
    game_over_pen.goto(2, 82)  # Shadow
    game_over_pen.color("#330000")
    game_over_pen.write("💀 GAME OVER 💀", align="center", font=("Arial", 24, "bold"))
    game_over_pen.goto(0, 80)  # Main text
    game_over_pen.color("#ff3333")
    game_over_pen.write("💀 GAME OVER 💀", align="center", font=("Arial", 24, "bold"))
    
    # Score section with styling
    game_over_pen.goto(0, 40)
    game_over_pen.color("#ffffff")
    game_over_pen.write("FINAL SCORE", align="center", font=("Arial", 14, "normal"))
    
    game_over_pen.goto(0, 15)
    game_over_pen.color("#00ff88")
    game_over_pen.write(f"🏆 {score:,} Points", align="center", font=("Arial", 20, "bold"))
    
    # High score celebration
    if score == high_score and score > 0:
        game_over_pen.goto(0, -15)
        game_over_pen.color("#ffd700")
        game_over_pen.write("🌟 NEW HIGH SCORE! 🌟", align="center", font=("Arial", 16, "bold"))
        game_over_pen.goto(0, -35)
        game_over_pen.color("#ffaa00")
        game_over_pen.write("🎉 CONGRATULATIONS! 🎉", align="center", font=("Arial", 12, "normal"))
        restart_y = -65
    else:
        game_over_pen.goto(0, -15)
        game_over_pen.color("#ffaa00")
        game_over_pen.write(f"Best Score: {high_score:,}", align="center", font=("Arial", 14, "normal"))
        restart_y = -45
    
    # Mode info
    mode_text = "Career Mode" if game_mode == "career" else "Normal Mode"
    if game_mode == "career":
        game_over_pen.goto(0, restart_y - 20)
        game_over_pen.color("#ff6b35")
        game_over_pen.write(f"🚀 {mode_text} - Level {level}", align="center", font=("Arial", 12, "normal"))
        restart_y -= 20
    
    # Restart instruction with animation
    game_over_pen.goto(0, restart_y - 20)
    game_over_pen.color("#00d4ff")
    game_over_pen.write("⌨️ Press SPACE to play again", align="center", font=("Arial", 14, "bold"))
    
    # Footer
    game_over_pen.goto(0, restart_y - 45)
    game_over_pen.color("#666699")
    game_over_pen.write("Thanks for playing SHLOKGAMES Snake!", align="center", font=("Arial", 10, "normal"))
    
    screen.update()

def restart_game():
    """Restart the game"""
    global mode_selected
    if not game_running:
        mode_selected = False
        show_mode_selection()
        screen.listen()
        screen.onkey(select_normal_mode, "n")
        screen.onkey(select_career_mode, "c")

# Control functions
def go_up():
    global snake_direction
    if game_running and snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if game_running and snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if game_running and snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if game_running and snake_direction != "right":
        snake_direction = "left"

# Main game setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game - SHLOKGAMES")

# Start the game
show_loading_screen()
show_mode_selection()

# Register mode selection
screen.listen()
screen.onkey(select_normal_mode, "n")
screen.onkey(select_career_mode, "c")

turtle.done()
