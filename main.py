import customtkinter as ctk

def main():
  app = ctk.CTk()
  app.title("hello world")
  app.geometry("1000x600")
  label = ctk.CTkLabel(app, text="hello world").place(relx=0.5,rely=0.5, anchor="center")


if __name__ == __main__:
  app.mainloop()
  main()
