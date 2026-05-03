import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class BookTracker:
    """Приложение для отслеживания прочитанных книг"""
    
    def __init__(self):
        # Создаём главное окно
        self.window = tk.Tk()
        self.window.title("📚 Book Tracker — Трекер прочитанных книг")
        self.window.geometry("900x600")
        self.window.resizable(False, False)
        self.window.configure(bg="#2c3e50")
        
        # Загрузка данных
        self.books = []
        self.load_data()
        
        # Создание интерфейса
        self.create_widgets()
        
        # Обновление таблицы
        self.update_table()
        
        # Запуск приложения
        self.window.mainloop()
    
    # ==================== РАБОТА С JSON ====================
    def load_data(self):
        """Загружает данные из JSON-файла"""
        if os.path.exists("books.json"):
            try:
                with open("books.json", "r", encoding="utf-8") as file:
                    self.books = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                self.books = []
    
    def save_data(self):
        """Сохраняет данные в JSON-файл"""
        with open("books.json", "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)
    
    # ==================== СОЗДАНИЕ ИНТЕРФЕЙСА ====================
    def create_widgets(self):
        """Создаёт все элементы интерфейса"""
        
        # Заголовок
        title_label = tk.Label(
            self.window,
            text="📚 BOOK TRACKER — Трекер прочитанных книг",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=15)
        
        # === ЛЕВАЯ ПАНЕЛЬ — ФОРМА ДОБАВЛЕНИЯ ===
        left_frame = tk.Frame(
            self.window,
            bg="#34495e",
            relief="groove",
            bd=2,
            width=300
        )
        left_frame.pack(side="left", fill="y", padx=10, pady=10)
        left_frame.pack_propagate(False)
        
        # Заголовок формы
        tk.Label(
            left_frame,
            text="➕ ДОБАВИТЬ КНИГУ",
            font=("Arial", 14, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        ).pack(pady=15)
        
        # Поле для названия
        tk.Label(
            left_frame,
            text="Название книги:",
            font=("Arial", 11),
            bg="#34495e",
            fg="#ecf0f1"
        ).pack(anchor="w", padx=20, pady=(10, 5))
        
        self.title_entry = tk.Entry(
            left_frame,
            font=("Arial", 11),
            width=25,
            relief="solid",
            bd=1
        )
        self.title_entry.pack(padx=20, pady=(0, 10))
        
        # Поле для автора
        tk.Label(
            left_frame,
            text="Автор:",
            font=("Arial", 11),
            bg="#34495e",
            fg="#ecf0f1"
        ).pack(anchor="w", padx=20, pady=(5, 5))
        
        self.author_entry = tk.Entry(
            left_frame,
            font=("Arial", 11),
            width=25,
            relief="solid",
            bd=1
        )
        self.author_entry.pack(padx=20, pady=(0, 10))
        
        # Поле для жанра
        tk.Label(
            left_frame,
            text="Жанр:",
            font=("Arial", 11),
            bg="#34495e",
            fg="#ecf0f1"
        ).pack(anchor="w", padx=20, pady=(5, 5))
        
        self.genre_entry = tk.Entry(
            left_frame,
            font=("Arial", 11),
            width=25,
            relief="solid",
            bd=1
        )
        self.genre_entry.pack(padx=20, pady=(0, 10))
        
        # Поле для количества страниц
        tk.Label(
            left_frame,
            text="Количество страниц:",
            font=("Arial", 11),
            bg="#34495e",
            fg="#ecf0f1"
        ).pack(anchor="w", padx=20, pady=(5, 5))
        
        self.pages_entry = tk.Entry(
            left_frame,
            font=("Arial", 11),
            width=25,
            relief="solid",
            bd=1
        )
        self.pages_entry.pack(padx=20, pady=(0, 15))
        
        # Кнопка "Добавить книгу"
        add_button = tk.Button(
            left_frame,
            text="📖 ДОБАВИТЬ КНИГУ",
            command=self.add_book,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            cursor="hand2",
            width=20,
            height=2,
            activebackground="#45a049",
            relief="raised",
            bd=2
        )
        add_button.pack(pady=10)
        
        # Информационная метка
        tk.Label(
            left_frame,
            text="💡 Совет: Все поля обязательны\nдля заполнения",
            font=("Arial", 9),
            bg="#34495e",
            fg="#7f8c8d",
            justify="center"
        ).pack(side="bottom", pady=20)
        
        # === ПРАВАЯ ПАНЕЛЬ — ТАБЛИЦА И ФИЛЬТРЫ ===
        right_frame = tk.Frame(self.window, bg="#2c3e50")
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # === ФИЛЬТРАЦИЯ ===
        filter_frame = tk.LabelFrame(
            right_frame,
            text="🔍 ФИЛЬТРАЦИЯ КНИГ",
            font=("Arial", 11, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief="groove",
            bd=2
        )
        filter_frame.pack(fill="x", pady=(0, 10))
        
        # Фильтр по жанру
        tk.Label(
            filter_frame,
            text="Жанр:",
            font=("Arial", 10),
            bg="#ecf0f1"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.genre_filter = tk.Entry(
            filter_frame,
            font=("Arial", 10),
            width=15,
            relief="solid",
            bd=1
        )
        self.genre_filter.grid(row=0, column=1, padx=10, pady=10)
        
        # Фильтр по страницам
        tk.Label(
            filter_frame,
            text="Страниц больше:",
            font=("Arial", 10),
            bg="#ecf0f1"
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        
        self.pages_filter = tk.Entry(
            filter_frame,
            font=("Arial", 10),
            width=10,
            relief="solid",
            bd=1
        )
        self.pages_filter.grid(row=0, column=3, padx=10, pady=10)
        
        # Кнопка применения фильтра
        filter_button = tk.Button(
            filter_frame,
            text="🔍 ПРИМЕНИТЬ",
            command=self.apply_filter,
            font=("Arial", 9, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2",
            width=10,
            relief="raised",
            bd=1
        )
        filter_button.grid(row=0, column=4, padx=5, pady=10)
        
        # Кнопка сброса фильтра
        reset_button = tk.Button(
            filter_frame,
            text="🔄 СБРОСИТЬ",
            command=self.reset_filter,
            font=("Arial", 9, "bold"),
            bg="#9E9E9E",
            fg="white",
            cursor="hand2",
            width=10,
            relief="raised",
            bd=1
        )
        reset_button.grid(row=0, column=5, padx=5, pady=10)
        
        # === ТАБЛИЦА С КНИГАМИ ===
        # Создаём фрейм для таблицы и скроллбара
        table_frame = tk.Frame(right_frame, bg="#2c3e50")
        table_frame.pack(fill="both", expand=True)
        
        # Создаём скроллбар
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side="right", fill="y")
        
        # Создаём таблицу (Treeview)
        columns = ("Название", "Автор", "Жанр", "Страницы")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=18
        )
        
        # Настраиваем колонки
        self.tree.heading("Название", text="📖 Название книги")
        self.tree.heading("Автор", text="✍️ Автор")
        self.tree.heading("Жанр", text="🎭 Жанр")
        self.tree.heading("Страницы", text="📄 Страницы")
        
        self.tree.column("Название", width=250, anchor="w")
        self.tree.column("Автор", width=180, anchor="w")
        self.tree.column("Жанр", width=150, anchor="w")
        self.tree.column("Страницы", width=100, anchor="center")
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # === КНОПКА УДАЛЕНИЯ ===
        delete_button = tk.Button(
            right_frame,
            text="🗑 УДАЛИТЬ ВЫБРАННУЮ КНИГУ",
            command=self.delete_book,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            width=25,
            height=1,
            activebackground="#d32f2f",
            relief="raised",
            bd=2
        )
        delete_button.pack(pady=10)
        
        # Статусная строка
        self.status_label = tk.Label(
            right_frame,
            text="",
            font=("Arial", 9),
            bg="#2c3e50",
            fg="#7f8c8d"
        )
        self.status_label.pack()
    
    # ==================== ЛОГИКА ПРОГРАММЫ ====================
    def add_book(self):
        """Добавляет новую книгу после проверки данных"""
        # Получаем данные из полей ввода
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        genre = self.genre_entry.get().strip()
        pages_str = self.pages_entry.get().strip()
        
        # Проверка на пустые поля
        if not title or not author or not genre or not pages_str:
            messagebox.showwarning(
                "Ошибка ввода",
                "❌ Все поля должны быть заполнены!"
            )
            return
        
        # Проверка, что количество страниц — число
        try:
            pages = int(pages_str)
            if pages <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Ошибка ввода",
                "❌ Количество страниц должно быть положительным целым числом!"
            )
            return
        
        # Проверка на дубликаты (опционально)
        for book in self.books:
            if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
                if messagebox.askyesno(
                    "Подтверждение",
                    f"Книга «{title}» автора {author} уже существует.\nДобавить всё равно?"
                ):
                    break
                else:
                    return
        
        # Добавляем книгу в список
        new_book = {
            "title": title,
            "author": author,
            "genre": genre,
            "pages": pages
        }
        self.books.append(new_book)
        
        # Сохраняем в JSON
        self.save_data()
        
        # Обновляем таблицу
        self.update_table()
        
        # Очищаем поля ввода
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.pages_entry.delete(0, tk.END)
        
        # Статус
        self.status_label.config(
            text=f"✅ Книга «{title}» добавлена! Всего книг: {len(self.books)}",
            fg="#2ecc71"
        )
        
        # Сбрасываем статус через 3 секунды
        self.window.after(3000, lambda: self.status_label.config(text="", fg="#7f8c8d"))
    
    def delete_book(self):
        """Удаляет выбранную книгу из таблицы"""
        selected = self.tree.selection()
        
        if not selected:
            messagebox.showwarning(
                "Удаление",
                "❌ Выберите книгу для удаления!"
            )
            return
        
        # Получаем данные выбранной книги
        item = self.tree.item(selected[0])
        title = item["values"][0]
        author = item["values"][1]
        
        # Подтверждение удаления
        if messagebox.askyesno(
            "Подтверждение",
            f"Вы уверены, что хотите удалить книгу:\n«{title}» - {author}?"
        ):
            # Удаляем из списка
            self.books = [b for b in self.books if not (b["title"] == title and b["author"] == author)]
            
            # Сохраняем в JSON
            self.save_data()
            
            # Обновляем таблицу
            self.update_table()
            
            # Статус
            self.status_label.config(
                text=f"🗑 Книга «{title}» удалена! Осталось книг: {len(self.books)}",
                fg="#e74c3c"
            )
            self.window.after(3000, lambda: self.status_label.config(text="", fg="#7f8c8d"))
    
    def apply_filter(self):
        """Применяет фильтры и обновляет таблицу"""
        genre_filter = self.genre_filter.get().strip().lower()
        pages_filter_str = self.pages_filter.get().strip()
        
        # Преобразуем в число, если введено
        pages_filter = None
        if pages_filter_str:
            try:
                pages_filter = int(pages_filter_str)
                if pages_filter < 0:
                    pages_filter = 0
            except ValueError:
                messagebox.showwarning(
                    "Ошибка фильтрации",
                    "Количество страниц должно быть числом!"
                )
                return
        
        # Очищаем таблицу
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Фильтруем и отображаем книги
        filtered_count = 0
        for book in self.books:
            # Фильтр по жанру
            if genre_filter and genre_filter not in book["genre"].lower():
                continue
            
            # Фильтр по страницам
            if pages_filter is not None and book["pages"] <= pages_filter:
                continue
            
            # Добавляем в таблицу
            self.tree.insert("", tk.END, values=(
                book["title"],
                book["author"],
                book["genre"],
                book["pages"]
            ))
            filtered_count += 1
        
        # Обновляем статус
        self.status_label.config(
            text=f"🔍 Найдено книг: {filtered_count} из {len(self.books)}",
            fg="#3498db"
        )
        self.window.after(3000, lambda: self.status_label.config(text="", fg="#7f8c8d"))
    
    def reset_filter(self):
        """Сбрасывает фильтры и показывает все книги"""
        self.genre_filter.delete(0, tk.END)
        self.pages_filter.delete(0, tk.END)
        self.update_table()
        
        self.status_label.config(
            text=f"🔄 Фильтры сброшены. Всего книг: {len(self.books)}",
            fg="#f39c12"
        )
        self.window.after(3000, lambda: self.status_label.config(text="", fg="#7f8c8d"))
    
    def update_table(self):
        """Обновляет таблицу со всеми книгами"""
        # Очищаем таблицу
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Добавляем все книги
        for book in self.books:
            self.tree.insert("", tk.END, values=(
                book["title"],
                book["author"],
                book["genre"],
                book["pages"]
            ))

# ===== ЗАПУСК ПРОГРАММЫ =====
if __name__ == "__main__":
    app = BookTracker()