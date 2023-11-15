import tkinter as tk
from tkinter import messagebox, ttk
import browser_cookie3

class CookieGetter:
    def __init__(self):
        self.cookies = []
        self.filtered_cookies = []
        self.domain = ""

        # 初始化用户界面
        self.initialize_ui()

    def initialize_ui(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("Cookie Getter")
        self.root.geometry("1024x768")

        # 创建顶部输入控件
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)

        self.domain_label = ttk.Label(self.input_frame, text="Domain:")
        self.domain_label.pack(side=tk.LEFT)

        self.domain_entry = ttk.Entry(self.input_frame)
        self.domain_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)

        self.get_button = ttk.Button(self.input_frame, text="Get Cookies", command=self.get_cookies)
        self.get_button.pack(side=tk.RIGHT)

        # 添加浏览器选择单选按钮
        self.browser_frame = ttk.Frame(self.input_frame)
        self.browser_frame.pack(side=tk.LEFT, padx=10)

        self.browser_label = ttk.Label(self.browser_frame, text="Browser:")
        self.browser_label.pack(side=tk.LEFT)

        self.browser_var = tk.StringVar()

        self.firefox_radio = ttk.Radiobutton(self.browser_frame, text="Firefox", variable=self.browser_var, value="firefox")
        self.firefox_radio.pack(side=tk.LEFT)

        self.chrome_radio = ttk.Radiobutton(self.browser_frame, text="Chrome", variable=self.browser_var, value="chrome")
        self.chrome_radio.pack(side=tk.LEFT)

        self.browser_var.set("firefox")  # 默认值设为Firefox

        # 创建中间列表控件
        self.list_frame = ttk.Frame(self.root)
        self.list_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        self.filter_frame = ttk.Frame(self.list_frame)
        self.filter_label = ttk.Label(self.filter_frame, text="Filter:")
        self.filter_label.pack(side=tk.LEFT)

        self.filter_entry = ttk.Entry(self.filter_frame)
        self.filter_entry.bind("<KeyRelease>", self.filter_cookies)
        self.filter_entry.pack(side=tk.LEFT)

        self.filter_frame.pack()

        self.listbox = tk.Listbox(self.list_frame)
        self.listbox.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)

    def get_cookies(self):
        try:
            self.domain = self.domain_entry.get()
            if self.browser_var.get() == "firefox":
                self.cookies = browser_cookie3.firefox()
            elif self.browser_var.get() == "chrome":
                self.cookies = browser_cookie3.chrome()
            self.filtered_cookies = self.cookies
            self.update_listbox()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get cookies: {e}")

    def filter_cookies(self, event):
        filter_text = self.filter_entry.get().lower()
        self.filtered_cookies = [cookie for cookie in self.cookies if filter_text in cookie.name.lower()]
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for cookie in self.filtered_cookies:
            self.listbox.insert(tk.END, f"{cookie.name}={cookie.value}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CookieGetter()
    app.run()
