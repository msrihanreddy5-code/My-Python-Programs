mood_colors = {
    "happy": "#FFD700",
    "sad": "#1E90FF",
    "angry": "#FF4500",
    "calm": "#98FB98",
    "stressed": "#8B0000"
}

mood = input("Enter your mood: ").lower()

if mood in mood_colors:
    print("Your color is:", mood_colors[mood])
else:
    print("Mood not found!")
