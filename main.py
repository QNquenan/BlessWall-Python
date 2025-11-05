import tkinter as tk
import random
import json
import sys
import os

def get_color():
    high_value = 200 + random.randint(0, 55)
    min_value = 100 + random.randint(0, 155)
    high_channel = random.randint(0, 2)

    if high_channel == 0:
        r = high_value
        g = min_value
        b = 100 + random.randint(0, 155)
    elif high_channel == 1:
        r = 100 + random.randint(0, 155)
        g = high_value
        b = min_value
    else:
        r = min_value
        g = 100 + random.randint(0, 155)
        b = high_value

    r = max(r, 100)
    g = max(g, 100)
    b = max(b, 100)

    return f"#{r:02x}{g:02x}{b:02x}"

def load_bless():
    # 获取资源文件路径的函数
    def json_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        else:
            return os.path.join(os.path.abspath("."), relative_path)
    
    bless_path = json_path('Blessing.json')
    with open(bless_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_window(root, blessing, x, y, bg_color):
    window = tk.Toplevel(root)
    window.geometry(f"250x100+{x}+{y}")
    window.title("温馨提示")
    window.configure(bg=bg_color)
    window.resizable(False, False)
    window.pack_propagate(False)
    
    label = tk.Label(window, text=blessing,
                    wraplength=230,
                    bg=bg_color,
                    fg="black")
    label.pack(expand=True, padx=10, pady=10)
    
    return window

def get_all_windows(root):
    blessings = load_bless()

    windows = []
    window_width = 250
    window_height = 100
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_configs = []
    for i, blessing in enumerate(blessings):
        x = random.randint(0, screen_width - window_width)
        y = random.randint(0, screen_height - window_height)
        bg_color = get_color()
        
        window_configs.append({
            'blessing': blessing,
            'x': x,
            'y': y,
            'bg_color': bg_color
        })
    
    def get_next_window(index=0):
        if index < len(window_configs):
            config = window_configs[index]
            window = get_window(
                root, 
                config['blessing'], 
                config['x'], 
                config['y'], 
                config['bg_color']
            )
            windows.append(window)
            root.after(50, lambda: get_next_window(index + 1))
    
    get_next_window()
    
    return windows

def main():
    root = tk.Tk()
    root.withdraw()
    get_all_windows(root)
    root.mainloop()

if __name__ == "__main__":
    main()