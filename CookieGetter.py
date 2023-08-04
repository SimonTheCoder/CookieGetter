import tkinter as tk
import browser_cookie3


class CookieGetter:
    def __init__(self):
        self.cookies = []
        self.filtered_cookies = []
        self.domain = ""

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("Cookie Getter")
        
        # set to 1024 * 768
        self.root.geometry("1024x768")


        # 创建顶部输入控件
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)

        self.domain_label = tk.Label(self.input_frame, text="Domain:")
        self.domain_label.pack(side=tk.LEFT)

        self.domain_entry = tk.Entry(self.input_frame)
        self.domain_entry.pack(fill=tk.X, padx=5, expand=True)

        self.get_button = tk.Button(self.input_frame, text="Get Cookies", command=self.get_cookies)
        self.get_button.pack(side=tk.RIGHT)

        # 创建中间列表控件
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        self.filter_label = tk.Label(self.list_frame, text="Filter:")
        self.filter_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.filter_entry = tk.Entry(self.list_frame)
        self.filter_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.filter_entry.bind("<KeyRelease>", self.filter_cookies)

        self.listbox = tk.Listbox(self.list_frame)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

        # 自动填充空白区域
        self.list_frame.columnconfigure(0, weight=1)
        self.list_frame.columnconfigure(1, weight=1)
        self.list_frame.rowconfigure(1, weight=1)

    def get_cookies(self):
        self.domain = self.domain_entry.get()
        self.cookies = browser_cookie3.load(self.domain)
        self.filtered_cookies = self.cookies
        self.update_listbox()

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
