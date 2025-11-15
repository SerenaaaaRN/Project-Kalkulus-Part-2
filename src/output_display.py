import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def tampilkanLangkahSolusi(widgetDict, teksLangkah):
    """Display solution steps in text widget"""
    widgetDict['teksLangkah'].delete(1.0, tk.END)
    widgetDict['teksLangkah'].insert(1.0, teksLangkah)

def tampilkanTabel(widgetDict, nilaiX, nilaiY):
    """Display table of x and y values"""
    tabel = "="*60 + "\n"
    tabel += " TABEL HASIL SOLUSI EKSAK\n"
    tabel += "="*60 + "\n\n"
    tabel += f"{'x':>15}  {'y_Eksak':>20}\n"
    tabel += "-"*60 + "\n"
    
    titikTampil = min(20, len(nilaiX))
    for i in range(titikTampil):
        tabel += f"{nilaiX[i]:>15.6f}  {nilaiY[i]:>20.10f}\n"
        
    if len(nilaiX) > 20:
        tabel += "   ...\n"
        tabel += f"{nilaiX[-1]:>15.6f}  {nilaiY[-1]:>20.10f}\n"
        
    tabel += "\n" + "="*60 + "\n"
    tabel += f"Total titik: {len(nilaiX)}\n"
    
    widgetDict['teksTabel'].delete(1.0, tk.END)
    widgetDict['teksTabel'].insert(1.0, tabel)

def tampilkanPlot(widgetDict, nilaiX, nilaiY, ekspresiP, ekspresiQ):
    """Display plot of solution"""
    # Bersihkan plot sebelumnya
    for widget in widgetDict['frameGrafik'].winfo_children():
        widget.destroy()
        
    # Buat plot baru
    fig = Figure(figsize=(10, 6), dpi=100)
    ax = fig.add_subplot(111)
    
    ax.plot(nilaiX, nilaiY, 'r-', label='Solusi Eksak', linewidth=2.5, alpha=0.8)
    ax.set_xlabel('x', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_title(f'Solusi: dy/dx + ({ekspresiP})y = {ekspresiQ}', 
                 fontsize=13, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.4)
    
    # Embed plot ke tkinter
    canvas = FigureCanvasTkAgg(fig, master=widgetDict['frameGrafik'])
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True, padx=5, pady=5)

def bersihkanSemuaOutput(widgetDict):
    """Clear all output displays"""
    widgetDict['teksLangkah'].delete(1.0, tk.END)
    widgetDict['teksTabel'].delete(1.0, tk.END)
    
    for widget in widgetDict['frameGrafik'].winfo_children():
        widget.destroy()