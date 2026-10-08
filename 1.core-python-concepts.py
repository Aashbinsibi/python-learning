# =====================================================================
# PYTHON FOR ABSOLUTE BEGINNERS
# Topics: Statements, Multiple Lines, and Strings
# =====================================================================
# Welcome to Python!
# In programming, you give instructions for the computer to follow.
#
# Here are the three most basic building blocks:
#   1. Statements     -> Giving Python an instruction
#   2. Multiple Lines -> Writing long instructions or text across lines
#   3. Strings        -> Working with words and text
# =====================================================================


# =====================================================================
# 1. WHAT IS A STATEMENT?
# =====================================================================
# Think of a statement like a single step in a cooking recipe.
# It is one complete command telling Python to DO something.

print("--- 1. STATEMENTS ---")

# Step 1: Tell Python to remember some text (a variable)
pet = "Cat"

# Step 2: Tell Python to remember a number
age = 3

# Step 3: Tell Python to do simple math
next_year_age = age + 1

# Step 4: Tell Python to show (print) the result on your screen
print("My pet is a:", pet)
print("Next year, my pet will be:", next_year_age)

# Golden Rule for Beginners:
# Put each instruction on its own line!
# Python reads your program from top to bottom, one line at a time.


# =====================================================================
# 2. WRITING ON MULTIPLE LINES
# =====================================================================
# Usually, one instruction lives on one single line.
# But what if an instruction is long and you want to split it up so
# it is easy to read?

print("\n--- 2. MULTIPLE LINES ---")

# Way 1: Use Parentheses ( )
# When you wrap a calculation inside ( ), Python knows it continues on the next line.
total_score = (
    10
    + 20
    + 30
    + 40
)
print("Total score is:", total_score)

# You can also split long print messages using ( ):
print(
    "Line 1: You can break long messages",
    "Line 2: into multiple lines",
    "Line 3: to keep your code clean and readable."
)

# Adding Notes for Humans (Comments):
# Any line starting with '#' is ignored by Python.
# It is just a note for YOU to read!
# Tip 1: Take your time when learning to code.
# Tip 2: Writing clean code makes things easy.


# =====================================================================
# 3. STRINGS (WORKING WITH TEXT)
# =====================================================================
# In Python, "string" is simply the word for plain text.
# Whenever you want words, sentences, or letters, put them in quotes: " " or ' '

print("\n--- 3. STRINGS ---")

# You can use single quotes or double quotes:
fruit = 'Apple'
city = "London"
print("Fruit:", fruit)
print("City:", city)

# If your sentence has an apostrophe (like "It's"), wrap it in double quotes:
sentence = "It's very easy to learn Python!"
print(sentence)

# --- Multi-line Strings (Triple Quotes) ---
# What if you want to write a message with multiple lines?
# Use three double quotes """ at the start and at the end:
story = """Once upon a time,
a learner started writing Python.
Step by step, line by line,
it started to make complete sense!"""

print("\nMulti-line story:")
print(story)

# --- Gluing Strings Together (Joining) ---
# You can use the '+' sign to glue words together:
first_word = "Hello"
second_word = "World"
full_greeting = first_word + " " + second_word
print("\nGlued text:", full_greeting)

# --- Repeating Text ---
# You can repeat text using the '*' sign:
cheer = "Yay! " * 3
print("Repeated text:", cheer)

# --- f-Strings: The Easiest Way to Put Variables in Text ---
# Put an 'f' before the opening quote.
# Then put any variable inside {curly brackets}:
user_name = "Alex"
score = 100
announcement = f"Great job {user_name}! Your score is {score}."
print("\nf-string announcement:")
print(announcement)

# --- Simple String Tools (Changing Case) ---
# Python has handy built-in tools to transform text:
book = "python for beginners"

print("\nSimple text tools:")
print("Make it ALL CAPS:    ", book.upper())
print("Make it lowercase:   ", book.lower())
print("Capitalize Each Word:", book.title())


# =====================================================================
# SUMMARY
# =====================================================================
print("\n" + "=" * 55)
print("Congratulations! You learned the basics:")
print("  1. Statements     -> One instruction per line")
print("  2. Multiple Lines -> Splitting code using ( ) or \"\"\"")
print("  3. Strings        -> Plain text inside quotes")
print("=" * 55)
