import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import numpy as np

# Load model and movie list
with open('movie_list.pkl', 'rb') as file:
    movie_list = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)


# Function to recommend movies
def recommend_movies(movie_name):
    try:
        movie_name = movie_name.lower().strip()
        movie_titles = movie_list['title'].str.lower().str.strip()

        if movie_name not in movie_titles.values:
            return ["Movie not found! Please try another title."]

        movie_index = movie_titles[movie_titles == movie_name].index[0]
        distances = similarity[movie_index]

        movie_indices = sorted(
            list(enumerate(distances)), key=lambda x: x[1], reverse=True
        )[1:6]
        recommendations = [movie_list.iloc[i[0]]['title'] for i in movie_indices]
        return recommendations
    except Exception as e:
        return [f"An error occurred: {e}"]


# Function to handle the recommend button 
def on_recommend():
    movie_name = movie_input.get()
    if not movie_name.strip():
        messagebox.showwarning("Input Error", "Please enter a movie name!")
        return

    recommendations = recommend_movies(movie_name)
    recommendations_label.configure(state="normal")
    recommendations_label.delete("1.0", tk.END)
    recommendations_label.insert(tk.END, "\n".join(recommendations))
    recommendations_label.configure(state="disabled")


# Create the main Tkinter window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("500x400")
root.resizable(False, False)

# Set a gradient background
def set_gradient(canvas, colors=("white", "#e0e0e0")):
    width, height = 500, 400
    canvas.create_rectangle(0, 0, width, height, fill=colors[0], outline="")
    canvas.create_rectangle(0, height//2, width, height, fill=colors[1], outline="")


gradient_canvas = tk.Canvas(root, width=500, height=400)
gradient_canvas.pack(fill=tk.BOTH, expand=True)
set_gradient(gradient_canvas)

# Main Frame
frame = ttk.Frame(root, padding=20, relief="flat", style="TFrame")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = tk.Label(frame, text="🎬 Movie Recommendation System 🎥", font=("Helvetica", 18, "bold"),
                       bg="#e0e0e0", fg="#333")
title_label.pack(pady=10)

# Input Field
movie_input_label = tk.Label(frame, text="Enter a Movie Name:", font=("Helvetica", 12), bg="#e0e0e0", fg="#555")
movie_input_label.pack(anchor="w", pady=5)
movie_input = ttk.Entry(frame, width=35)
movie_input.pack(pady=5)

# Recommend Button
recommend_button = tk.Button(frame, text="Recommend", command=on_recommend, bg="#0078d7", fg="white",
                              font=("Helvetica", 12, "bold"), activebackground="#005bb5", activeforeground="white",
                              relief="flat", padx=10, pady=5)
recommend_button.pack(pady=10)

# Recommendations Label
recommendations_label = tk.Text(frame, width=50, height=8, font=("Helvetica", 12), wrap="word", state="disabled",
                                bg="#f4f4f4", fg="#333", bd=1, relief="solid", highlightthickness=0)
recommendations_label.pack(pady=10)

# Footer Label
footer_label = tk.Label(root, text="Powered by Movie Recommender", font=("Helvetica", 10, "italic"),
                        bg="#f0f0f0", fg="#777")
footer_label.pack(side="bottom", pady=5)

# Run the Tkinter event loop
root.mainloop()
