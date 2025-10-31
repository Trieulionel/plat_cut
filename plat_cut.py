import tkinter as tk
from tkinter import ttk, messagebox

def calculate_depth():
    try:
        diameter = float(entry_diameter.get())
    except ValueError:
        messagebox.showerror("入力エラー", "有効な直径の数値を入力してください。")
        return
    
    type_selected = type_var.get()
    depth = None
    
    if type_selected == "スペーサ・ホルダー":
        # スペーサ・ホルダーの場合
        if diameter < 70:
            depth = 0.5
        elif diameter < 200:
            depth = 1
        else:
            depth = 2
    elif type_selected == "ピン":
        # ピンの場合
        if diameter < 10:
            depth = 0.2
        elif diameter < 25:
            depth = 0.5
        else:
            depth = 1
    else:
        messagebox.showerror("エラー", "スペーサ・ホルダーかピンを選択してください。")
        return
    
    # 結果表示用Textをクリアしてから結果を表示
    text_result.config(state=tk.NORMAL)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, f"平カット深さ (A): {depth}\n")
    text_result.config(state=tk.DISABLED)

# メインウィンドウ作成
root = tk.Tk()
root.title("平カット深さ計算アプリ")

# 直径入力ラベル・エントリー
tk.Label(root, text="直径を入力してください (φD):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_diameter = tk.Entry(root)
entry_diameter.grid(row=0, column=1, padx=10, pady=10)

# 種類選択ラベル・ラジオボタン
type_var = tk.StringVar(value="スペーサ・ホルダー")
tk.Label(root, text="種類を選択してください:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
frame_radio = tk.Frame(root)
frame_radio.grid(row=1, column=1, padx=10, pady=10)
ttk.Radiobutton(frame_radio, text="スペーサ・ホルダー", variable=type_var, value="スペーサ・ホルダー").pack(side="left", padx=5)
ttk.Radiobutton(frame_radio, text="ピン", variable=type_var, value="ピン").pack(side="left", padx=5)

# 計算ボタン
btn_calculate = tk.Button(root, text="計算する", command=calculate_depth)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

# 結果表示用Textウィジェット
text_result = tk.Text(root, height=2, width=30, borderwidth=2, relief="sunken", font=("Arial", 14))
text_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
text_result.config(state=tk.DISABLED)  # 編集不可に設定

root.mainloop()
