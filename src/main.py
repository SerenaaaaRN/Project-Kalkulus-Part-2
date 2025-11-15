import tkinter as tk
from src.gui_component import buatJendelaUtama, setupGaya
from src.event_handlers import ikatEvent


if __name__ == "__main__":
    """Fungsi utama untuk menjalankan aplikasi"""
    root = tk.Tk()
    root.title("Solver Persamaan Diferensial Linear Orde 1")
    root.geometry("1400x900")
    root.configure(bg="#f0f0f0")
    
    # Setup gaya
    setupGaya()
    
    # Buat komponen jendela utama
    widgetDict = buatJendelaUtama(root)
    
    # Ikat event
    ikatEvent(widgetDict)
    
    # Update status
    widgetDict['barStatus'].config(text="Ready - Masukkan persamaan diferensial Anda")
    
    root.mainloop()