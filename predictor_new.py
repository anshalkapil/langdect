import tkinter as tk
import pickle
from tkinter import messagebox

# Load the classification model from a pickle file
with open('twitter_new.pkl', 'rb') as f:
    cv = pickle.load(f)
    rf = pickle.load(f)

# Define the function to classify the text
def classify_text():
    text = input_box.get('1.0', 'end-1c') # Get the text from the input box
    text_counts = cv.transform([text])
    result = rf.predict(text_counts)
    if result == 0:
        tk.messagebox.showinfo('Result', 'The text is classified as Hate Speech.')
    elif result == 1:
        tk.messagebox.showinfo('Result', 'The text is classified as Inappropriate Text.')
    elif result == 2:
        tk.messagebox.showinfo('Result', 'The text is classified as Normal Text.')

# Create the main window
root = tk.Tk()
root.title('Text Classification')

# Create the input box and the detect button
input_box = tk.Text(root, height=5, width=50)
detect_button = tk.Button(root, text='Detect', command=classify_text)

# Place the input box and the detect button in the main window
input_box.pack()
detect_button.pack()

# Start the main loop
root.mainloop()