import tkinter as tk
from tkinter import ttk, scrolledtext

def setupGaya():
    """Setup styling untuk ttk widgets"""
    gaya = ttk.Style()
    gaya.theme_use('clam')
    gaya.configure('Title.TLabel', font=('Arial', 16, 'bold'), 
                    background='#2c3e50', foreground='white')
    gaya.configure('Header.TLabel', font=('Arial', 11, 'bold'), 
                    background='#34495e', foreground='white')
    gaya.configure('Custom.TButton', font=('Arial', 10, 'bold'), padding=10)
    gaya.configure('TEntry', font=('Arial', 10))
    gaya.configure('TLabel', font=('Arial', 10), background='#ecf0f1')

def buatHeader(induk):
    """Membuat header frame"""
    frameHeader = tk.Frame(induk, bg='#2c3e50', height=60)
    frameHeader.pack(fill='x', pady=(0, 10))
    frameHeader.pack_propagate(False)
    
    labelJudul = ttk.Label(frameHeader, 
                            text="🔬 Solver Persamaan Diferensial Linear Orde 1", 
                            style='Title.TLabel')
    labelJudul.pack(pady=15)
    
    return frameHeader

def buatPanelInput(induk):
    """Membuat panel input di sebelah kiri"""
    panelKiri = tk.Frame(induk, bg='#ecf0f1', relief='raised', bd=2)
    panelKiri.pack(side='left', fill='both', padx=(0, 5), pady=5)
    
    # Header Input Section
    headerInput = tk.Frame(panelKiri, bg='#34495e', height=40)
    headerInput.pack(fill='x')
    headerInput.pack_propagate(False)
    ttk.Label(headerInput, text="📝 INPUT PARAMETER", 
              style='Header.TLabel').pack(pady=8)
    
    isiInput = tk.Frame(panelKiri, bg='#ecf0f1')
    isiInput.pack(fill='both', expand=True, padx=15, pady=15)
    
    # Info persamaan
    framePersamaan = tk.LabelFrame(isiInput, text="Persamaan: dy/dx + P(x)y = Q(x)", 
                             font=('Arial', 10, 'bold'), bg='#ecf0f1', fg='#2c3e50')
    framePersamaan.pack(fill='x', pady=(0, 15))
    
    labelInfo = tk.Label(framePersamaan, 
                         text="Contoh: 2*x, x**2, sin(x), cos(x), exp(x), 1/x, sqrt(x)", 
                         font=('Arial', 9, 'italic'), bg='#ecf0f1', fg='#7f8c8d')
    labelInfo.pack(pady=5)
    
    # Dictionary untuk input fields
    entryDict = {}
    
    # Input P(x)
    entryDict['px'] = buatFieldInput(isiInput, "P(x):", "1")
    
    # Input Q(x)
    entryDict['qx'] = buatFieldInput(isiInput, "Q(x):", "x")
    
    # Separator
    ttk.Separator(isiInput, orient='horizontal').pack(fill='x', pady=15)
    
    # Label kondisi awal
    labelKondisiAwal = tk.Label(isiInput, text="Kondisi Awal & Parameter:", 
                       font=('Arial', 10, 'bold'), bg='#ecf0f1', fg='#2c3e50')
    labelKondisiAwal.pack(anchor='w', pady=(0, 10))
    
    # Parameter numerik
    entryDict['x0'] = buatFieldInput(isiInput, "x₀ (awal):", "0")
    entryDict['y0'] = buatFieldInput(isiInput, "y₀ (awal):", "1")
    entryDict['xAkhir'] = buatFieldInput(isiInput, "x (akhir):", "2")
    entryDict['stepSize'] = buatFieldInput(isiInput, "Step size (h):", "0.1")
    
    # Tombol-tombol
    tombolDict = buatTombol(isiInput)
    
    return panelKiri, entryDict, tombolDict

def buatFieldInput(induk, teksLabel, nilaiDefault):
    """Membuat input field dengan label"""
    frame = tk.Frame(induk, bg='#ecf0f1')
    frame.pack(fill='x', pady=5)
    
    tk.Label(frame, text=teksLabel, font=('Arial', 10, 'bold'), 
             bg='#ecf0f1', width=15, anchor='w').pack(side='left')
    
    entry = ttk.Entry(frame, font=('Arial', 10))
    entry.pack(side='left', fill='x', expand=True)
    entry.insert(0, nilaiDefault)
    
    return entry

def buatTombol(induk):
    """Membuat tombol-tombol aksi"""
    frameTombol = tk.Frame(induk, bg='#ecf0f1')
    frameTombol.pack(fill='x', pady=20)
    
    tombolSolve = tk.Button(frameTombol, text="🚀 SOLVE",
                         font=('Arial', 11, 'bold'), bg='#27ae60', fg='white',
                         activebackground='#229954', cursor='hand2', pady=10)
    tombolSolve.pack(fill='x', pady=5)
    
    tombolClear = tk.Button(frameTombol, text="🔄 CLEAR",
                         font=('Arial', 11, 'bold'), bg='#e74c3c', fg='white',
                         activebackground='#c0392b', cursor='hand2', pady=10)
    tombolClear.pack(fill='x', pady=5)
    
    return {'solve': tombolSolve, 'clear': tombolClear}

def buatPanelOutput(induk):
    """Membuat panel output di sebelah kanan"""
    panelKanan = tk.Frame(induk, bg='#ecf0f1', relief='raised', bd=2)
    panelKanan.pack(side='right', fill='both', expand=True, padx=(5, 0), pady=5)
    
    # Header Output Section
    headerOutput = tk.Frame(panelKanan, bg='#34495e', height=40)
    headerOutput.pack(fill='x')
    headerOutput.pack_propagate(False)
    ttk.Label(headerOutput, text="📊 HASIL & VISUALISASI", 
              style='Header.TLabel').pack(pady=8)
    
    # Notebook untuk tabs
    notebook = ttk.Notebook(panelKanan)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Tab 1: Langkah Solusi
    frameLangkah = tk.Frame(notebook, bg='white')
    notebook.add(frameLangkah, text='📝 Langkah Solusi')
    
    teksLangkah = scrolledtext.ScrolledText(frameLangkah, wrap=tk.WORD, 
                                           font=('Courier New', 9), bg='#fdfefe')
    teksLangkah.pack(fill='both', expand=True, padx=5, pady=5)
    
    # Tab 2: Grafik
    frameGrafik = tk.Frame(notebook, bg='white')
    notebook.add(frameGrafik, text='📈 Grafik')
    
    # Tab 3: Tabel
    frameTabel = tk.Frame(notebook, bg='white')
    notebook.add(frameTabel, text='📋 Tabel Nilai')
    
    teksTabel = scrolledtext.ScrolledText(frameTabel, wrap=tk.WORD, 
                                           font=('Courier New', 9), bg='#fdfefe')
    teksTabel.pack(fill='both', expand=True, padx=5, pady=5)
    
    return panelKanan, notebook, teksLangkah, frameGrafik, teksTabel

def buatBarStatus(induk):
    """Membuat status bar di bagian bawah"""
    barStatus = tk.Label(induk, text="Ready", bd=1, relief=tk.SUNKEN, 
                         anchor=tk.W, font=('Arial', 9), bg='#34495e', fg='white')
    barStatus.pack(side=tk.BOTTOM, fill=tk.X)
    return barStatus

def buatJendelaUtama(root):
    """Membuat semua komponen window dan mengembalikan dictionary widgets"""
    # Buat header
    header = buatHeader(root)
    
    # Container utama
    containerUtama = tk.Frame(root, bg='#f0f0f0')
    containerUtama.pack(fill='both', expand=True, padx=10, pady=5)
    
    # Buat panel input
    panelKiri, entryDict, tombolDict = buatPanelInput(containerUtama)
    
    # Buat panel output
    panelKanan, notebook, teksLangkah, frameGrafik, teksTabel = buatPanelOutput(containerUtama)
    
    # Buat status bar
    barStatus = buatBarStatus(root)
    
    # Return semua widgets sebagai dictionary
    widgetDict = {
        'root': root,
        'header': header,
        'containerUtama': containerUtama,
        'panelKiri': panelKiri,
        'panelKanan': panelKanan,
        'entryDict': entryDict,
        'tombolDict': tombolDict,
        'notebook': notebook,
        'teksLangkah': teksLangkah,
        'frameGrafik': frameGrafik,
        'teksTabel': teksTabel,
        'barStatus': barStatus
    }
    
    return widgetDict