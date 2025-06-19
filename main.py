import os
import customtkinter as ctk
from tkinter import scrolledtext,PhotoImage
import time
from text_generator import generate_fake_paragraph

# Theme Configuration
THEME_COLOR = "#F7A44C"
BG_COLOR = "#323437"
FRAME_BG = "#2B2B2B"
BUTTON_HOVER = "#E8943D"
TEXT_COLOR = "#FFFFFF"
CORRECT_COLOR = "#4CAF50"
INCORRECT_COLOR = "#F44336"
DEFAULT_COLOR = "#B0B0B0"

# Global Variables
STARTED = False
START_TIME = None
TIME = 30
MISTAKES = 0
WORDS = 0
AFTER_ID = None
FONT = ("Courier New", 16, "bold")
TEST_COMPLETED = False



TARGET_TEXT = generate_fake_paragraph(20)


def change_time():
    global TIME
    TIME = time_var.get()
    restart()


def set_focus_after_start():
    entry.place(x=-1000, y=-1000)
    entry.focus_set()


def refresh_display():
    """Force refresh the display to show clean state"""
    text_display.config(state="normal")
    text_display.delete("1.0", "end")
    text_display.insert("1.0", TARGET_TEXT, "default")
    text_display.config(state="disabled")


def restart():
    global MISTAKES, WORDS, STARTED, START_TIME, AFTER_ID, TEST_COMPLETED
    if AFTER_ID:
        app.after_cancel(AFTER_ID)

    # Reset all variables first
    MISTAKES = 0
    WORDS = 0
    STARTED = False
    START_TIME = None
    TEST_COMPLETED = False

    # Clear results
    results_frame.grid_forget()

    # Clear and reset entry field completely
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.icursor(0)  # Reset cursor position

    # Reset text display with proper clearing of all tags
    text_display.config(state="normal")
    text_display.delete("1.0", "end")
    # Clear all existing tags
    for tag in text_display.tag_names():
        if tag not in ["sel", "disabled"]:
            text_display.tag_delete(tag)
    # Re-configure tags
    text_display.tag_configure("correct", foreground=CORRECT_COLOR)
    text_display.tag_configure("incorrect", foreground=INCORRECT_COLOR, background="#4A1A1A")
    text_display.tag_configure("default", foreground=DEFAULT_COLOR)
    # Insert fresh text with default tag
    text_display.insert("1.0", TARGET_TEXT, "default")
    text_display.config(state="disabled")

    # Reset timer display
    timer_label.configure(text=f"Time: {TIME}s")

    # Force focus and ensure entry is ready
    app.after(50, lambda: entry.focus_set())

    # Trigger display update to show clean state
    app.after(100, lambda: refresh_display())


def change_font_size(value):
    global FONT
    font_size = int(value)
    FONT = ("Courier New", font_size, "bold")
    text_display.config(font=FONT)
    entry.configure(font=("Consolas", font_size))


def show_results():
    global WORDS, START_TIME, TEST_COMPLETED

    # Check if test is actually running
    if START_TIME is None or TEST_COMPLETED:
        return

    TEST_COMPLETED = True
    entry.configure(state="disabled")

    elapsed_seconds = time.time() - START_TIME
    typed = entry.get()
    elapsed_minutes = elapsed_seconds / 60
    total_chars = len(typed)
    correct_chars = total_chars - MISTAKES
    gross_wpm = total_chars / 5 / elapsed_minutes if elapsed_minutes > 0 else 0
    net_wpm = max(0, (total_chars / 5 - MISTAKES) / elapsed_minutes) if elapsed_minutes > 0 else 0
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0

    # Count words correctly
    words_typed = len(typed.split())

    # Display results in the app
    results_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    wpm_label.configure(text=f"WPM: {net_wpm:.1f}")
    accuracy_label.configure(text=f"Accuracy: {accuracy:.1f}%")
    time_label.configure(text=f"Time: {elapsed_seconds:.1f}s")
    chars_label.configure(text=f"Characters: {total_chars}")
    mistakes_label.configure(text=f"Mistakes: {MISTAKES}")
    words_label.configure(text=f"Words: {words_typed}")


def update_timer():
    global STARTED, START_TIME, AFTER_ID
    if STARTED and not TEST_COMPLETED:
        elapsed = time.time() - START_TIME
        remaining = max(0, TIME - elapsed)
        timer_label.configure(text=f"Time: {remaining:.1f}s")

        if remaining <= 0:
            show_results()
            return

        AFTER_ID = app.after(100, update_timer)


def start_timer(event):
    global STARTED, START_TIME
    if not STARTED and not TEST_COMPLETED:
        STARTED = True
        START_TIME = time.time()
        update_timer()


def on_keypress(event):
    global MISTAKES, WORDS

    if TEST_COMPLETED:
        return

    user_input = entry.get()

    # Ensure we have valid input to work with
    if user_input is None:
        user_input = ""

    text_display.config(state="normal")
    text_display.delete("1.0", "end")

    mistake_count = 0

    for i, char in enumerate(TARGET_TEXT):
        if i < len(user_input):
            if user_input[i] == char:
                text_display.insert("end", char, "correct")
            else:
                text_display.insert("end", char, "incorrect")
                mistake_count += 1
        else:
            text_display.insert("end", char, "default")

    MISTAKES = mistake_count

    # Check if test is complete (only if test has started)
    if STARTED and len(user_input) >= len(TARGET_TEXT):
        show_results()

    text_display.config(state="disabled")


def get_custom_text():
    text_display.grid_forget()
    text_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    text_entry.focus()


def add_custom_text(event):
    global TARGET_TEXT
    text = text_entry.get()
    if text.strip():
        text_entry.grid_forget()
        TARGET_TEXT = text
        text_display.config(state="normal")
        text_display.delete("1.0", "end")
        # Clear all existing tags
        for tag in text_display.tag_names():
            if tag not in ["sel", "disabled"]:
                text_display.tag_delete(tag)
        # Re-configure tags
        text_display.tag_configure("correct", foreground=CORRECT_COLOR)
        text_display.tag_configure("incorrect", foreground=INCORRECT_COLOR, background="#4A1A1A")
        text_display.tag_configure("default", foreground=DEFAULT_COLOR)
        text_display.insert("1.0", TARGET_TEXT, "default")
        text_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        text_display.config(state="disabled")
        restart()


# Initialize App
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.minsize(1000, 800)
app.title("KeySprint - Typing Speed Test")
app.configure(fg_color=BG_COLOR)

if os.path.exists("icon.ico"):
    try:
        app.iconbitmap("icon.ico")
    except Exception:
        pass

# Configure grid weights
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=3)
app.grid_rowconfigure(2, weight=1)

# Title
title_label = ctk.CTkLabel(
    app,
    text="KeySprint",
    font=("Impact", 48, "bold"),
    text_color=THEME_COLOR
)
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Timer Display
timer_label = ctk.CTkLabel(
    app,
    text=f"Time: {TIME}s",
    font=("Arial", 20, "bold"),
    text_color=THEME_COLOR
)
timer_label.grid(row=1, column=0, columnspan=2, pady=10)

# Options Frame
options_frame = ctk.CTkFrame(app, fg_color=FRAME_BG)
options_frame.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="ew")
options_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

# Restart Button
restart_button = ctk.CTkButton(
    options_frame,
    text="Restart",
    command=restart,
    fg_color=THEME_COLOR,
    hover_color=BUTTON_HOVER,
    font=("Arial", 14, "bold")
)
restart_button.grid(row=0, column=0, padx=5, pady=10)

# Custom Text Button
custom_button = ctk.CTkButton(
    options_frame,
    text="Custom Text",
    command=get_custom_text,
    fg_color=THEME_COLOR,
    hover_color=BUTTON_HOVER,
    font=("Arial", 14, "bold")
)
custom_button.grid(row=0, column=1, padx=5, pady=10)

# Time Selection
time_var = ctk.IntVar(value=30)
time_30 = ctk.CTkRadioButton(
    options_frame,
    text="30s",
    command=change_time,
    variable=time_var,
    value=30,
    fg_color=THEME_COLOR,
    font=("Arial", 12, "bold")
)
time_30.grid(row=0, column=2, padx=5, pady=10)

time_60 = ctk.CTkRadioButton(
    options_frame,
    text="60s",
    command=change_time,
    variable=time_var,
    value=60,
    fg_color=THEME_COLOR,
    font=("Arial", 12, "bold")
)
time_60.grid(row=0, column=3, padx=5, pady=10)

time_120 = ctk.CTkRadioButton(
    options_frame,
    text="120s",
    command=change_time,
    variable=time_var,
    value=120,
    fg_color=THEME_COLOR,
    font=("Arial", 12, "bold")
)
time_120.grid(row=0, column=4, padx=5, pady=10)

# Font Size Controls
font_label = ctk.CTkLabel(
    options_frame,
    text="Font Size",
    font=("Arial", 12, "bold"),
    text_color=TEXT_COLOR
)
font_label.grid(row=0, column=5, padx=5, pady=10)

font_size_slider = ctk.CTkSlider(
    options_frame,
    from_=10,
    to=24,
    number_of_steps=14,
    command=change_font_size,
    fg_color=THEME_COLOR,
    progress_color=BUTTON_HOVER,
    button_color=THEME_COLOR,
    button_hover_color=BUTTON_HOVER
)
font_size_slider.set(16)
font_size_slider.grid(row=0, column=6, padx=5, pady=10, sticky="ew")

# Text Frame with Scrollbar
text_frame = ctk.CTkFrame(app, fg_color=FRAME_BG)
text_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
text_frame.grid_rowconfigure(0, weight=1)
text_frame.grid_columnconfigure(0, weight=1)

# Scrolled Text Display
text_display = scrolledtext.ScrolledText(
    text_frame,
    font=FONT,
    state="normal",
    wrap="word",
    bg=FRAME_BG,
    fg=DEFAULT_COLOR,
    insertbackground=THEME_COLOR,
    selectbackground=THEME_COLOR,
    selectforeground="white",
    highlightcolor=THEME_COLOR,
    highlightbackground=FRAME_BG,
    relief="flat",
    borderwidth=0
)

text_display.insert("1.0", TARGET_TEXT, "default")
text_display.config(state="disabled")
text_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configure text tags
text_display.tag_configure("correct", foreground=CORRECT_COLOR)
text_display.tag_configure("incorrect", foreground=INCORRECT_COLOR, background="#4A1A1A")
text_display.tag_configure("default", foreground=DEFAULT_COLOR)

# Hidden Entry for Input
entry = ctk.CTkEntry(
    app,
    font=("Consolas", 16),
    width=200,
    fg_color=FRAME_BG,
    text_color=TEXT_COLOR,
    border_color=THEME_COLOR
)

# Custom Text Entry (initially hidden)
text_entry = ctk.CTkEntry(
    text_frame,
    placeholder_text="Enter your custom text here and press Enter...",
    font=("Arial", 14),
    fg_color=FRAME_BG,
    text_color=TEXT_COLOR,
    border_color=THEME_COLOR
)
text_entry.bind("<Return>", add_custom_text)

# Results Frame
results_frame = ctk.CTkFrame(app, fg_color=FRAME_BG)
results_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

# Result Labels
wpm_label = ctk.CTkLabel(
    results_frame,
    text="WPM: 0",
    font=("Arial", 18, "bold"),
    text_color=THEME_COLOR
)
wpm_label.grid(row=0, column=0, padx=10, pady=15)

accuracy_label = ctk.CTkLabel(
    results_frame,
    text="Accuracy: 0%",
    font=("Arial", 18, "bold"),
    text_color=CORRECT_COLOR
)
accuracy_label.grid(row=0, column=1, padx=10, pady=15)

time_label = ctk.CTkLabel(
    results_frame,
    text="Time: 0s",
    font=("Arial", 18, "bold"),
    text_color=TEXT_COLOR
)
time_label.grid(row=0, column=2, padx=10, pady=15)

chars_label = ctk.CTkLabel(
    results_frame,
    text="Characters: 0",
    font=("Arial", 18, "bold"),
    text_color=TEXT_COLOR
)
chars_label.grid(row=0, column=3, padx=10, pady=15)

mistakes_label = ctk.CTkLabel(
    results_frame,
    text="Mistakes: 0",
    font=("Arial", 18, "bold"),
    text_color=INCORRECT_COLOR
)
mistakes_label.grid(row=0, column=4, padx=10, pady=15)

words_label = ctk.CTkLabel(
    results_frame,
    text="Words: 0",
    font=("Arial", 18, "bold"),
    text_color=TEXT_COLOR
)
words_label.grid(row=0, column=5, padx=10, pady=15)

# Initialize
app.after(100, set_focus_after_start)
entry.bind("<KeyRelease>", on_keypress)
entry.bind("<KeyRelease>", start_timer, add="+")

# Show initial clean text
refresh_display()

if __name__ == "__main__":
    app.mainloop()