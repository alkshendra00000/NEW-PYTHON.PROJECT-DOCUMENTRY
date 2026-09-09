import random
import tkinter as tk


WIDTH = 720
HEIGHT = 520
BASKET_WIDTH = 110
BASKET_HEIGHT = 22
STAR_SIZE = 18


class CatchTheStars:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Stars")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg="#08152e",
            highlightthickness=0,
        )
        self.canvas.pack()
        self.canvas.focus_set()
        self.canvas.bind("<Left>", self.move_left)
        self.canvas.bind("<Right>", self.move_right)
        self.canvas.bind("<KeyPress-a>", self.move_left)
        self.canvas.bind("<KeyPress-d>", self.move_right)
        self.canvas.bind("<KeyPress-r>", self.restart)

        self.reset_game()
        self.update_game()

    def reset_game(self):
        self.canvas.delete("all")
        self.score = 0
        self.lives = 3
        self.running = True
        self.basket_x = WIDTH // 2
        self.star_x = random.randint(30, WIDTH - 30)
        self.star_y = -STAR_SIZE
        self.star_speed = 5
        self.draw_scene()

    def draw_scene(self):
        self.canvas.create_text(
            20,
            20,
            anchor="nw",
            text="CATCH THE STARS",
            fill="#ffe28a",
            font=("Georgia", 22, "bold"),
        )
        self.score_text = self.canvas.create_text(
            WIDTH - 20,
            22,
            anchor="ne",
            text="Score: 0   Lives: 3",
            fill="#e8f1ff",
            font=("Arial", 14, "bold"),
        )
        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT - 16,
            text="Move: Left/Right or A/D    Restart: R",
            fill="#8fa9d6",
            font=("Arial", 11),
        )
        self.basket = self.canvas.create_rectangle(
            self.basket_x - BASKET_WIDTH // 2,
            HEIGHT - 58,
            self.basket_x + BASKET_WIDTH // 2,
            HEIGHT - 58 + BASKET_HEIGHT,
            fill="#45d6c4",
            outline="#b6fff4",
            width=2,
        )
        self.star = self.canvas.create_oval(
            self.star_x - STAR_SIZE // 2,
            self.star_y - STAR_SIZE // 2,
            self.star_x + STAR_SIZE // 2,
            self.star_y + STAR_SIZE // 2,
            fill="#ffd166",
            outline="#fff1ad",
            width=2,
        )

    def move_left(self, _event=None):
        if self.running:
            self.basket_x = max(BASKET_WIDTH // 2, self.basket_x - 32)
            self.update_basket()

    def move_right(self, _event=None):
        if self.running:
            self.basket_x = min(WIDTH - BASKET_WIDTH // 2, self.basket_x + 32)
            self.update_basket()

    def update_basket(self):
        self.canvas.coords(
            self.basket,
            self.basket_x - BASKET_WIDTH // 2,
            HEIGHT - 58,
            self.basket_x + BASKET_WIDTH // 2,
            HEIGHT - 58 + BASKET_HEIGHT,
        )

    def update_game(self):
        if not self.running:
            return

        self.star_y += self.star_speed
        self.canvas.coords(
            self.star,
            self.star_x - STAR_SIZE // 2,
            self.star_y - STAR_SIZE // 2,
            self.star_x + STAR_SIZE // 2,
            self.star_y + STAR_SIZE // 2,
        )

        basket_top = HEIGHT - 58
        if basket_top - STAR_SIZE // 2 <= self.star_y <= basket_top + BASKET_HEIGHT:
            if abs(self.star_x - self.basket_x) <= BASKET_WIDTH // 2:
                self.score += 1
                self.star_speed = min(13, 5 + self.score * 0.35)
                self.reset_star()

        if self.star_y > HEIGHT + STAR_SIZE:
            self.lives -= 1
            self.reset_star()
            if self.lives <= 0:
                self.end_game()

        self.canvas.itemconfig(
            self.score_text,
            text=f"Score: {self.score}   Lives: {self.lives}",
        )
        self.root.after(25, self.update_game)

    def reset_star(self):
        self.star_x = random.randint(30, WIDTH - 30)
        self.star_y = -STAR_SIZE

    def end_game(self):
        self.running = False
        self.canvas.create_rectangle(
            150,
            180,
            WIDTH - 150,
            340,
            fill="#102754",
            outline="#ffd166",
            width=3,
        )
        self.canvas.create_text(
            WIDTH // 2,
            225,
            text="GAME OVER",
            fill="#ffd166",
            font=("Georgia", 34, "bold"),
        )
        self.canvas.create_text(
            WIDTH // 2,
            275,
            text=f"Final score: {self.score}",
            fill="#e8f1ff",
            font=("Arial", 18),
        )
        self.canvas.create_text(
            WIDTH // 2,
            315,
            text="Press R to play again",
            fill="#8fa9d6",
            font=("Arial", 14),
        )

    def restart(self, _event=None):
        self.reset_game()
        self.update_game()


if __name__ == "__main__":
    window = tk.Tk()
    CatchTheStars(window)
    window.mainloop()
