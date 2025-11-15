import threading
from tkinter import messagebox
from src.solver import selesaikanPersamaanDiferensial
from src.output_display import bersihkanSemuaOutput

def ikatEvent(widgetDict):
    """Bind semua event handlers ke widgets"""
    widgetDict['tombolDict']['solve'].config(
        command=lambda: padaKlikSolve(widgetDict)
    )
    
    widgetDict['tombolDict']['clear'].config(
        command=lambda: padaKlikClear(widgetDict)
    )

def padaKlikSolve(widgetDict):
    """Handler untuk tombol SOLVE"""
    # Disable button
    widgetDict['tombolDict']['solve'].config(state='disabled')
    updateStatus(widgetDict, "Menghitung solusi...")
    
    # Run di thread terpisah
    thread = threading.Thread(target=threadSolve, args=(widgetDict,))
    thread.daemon = True
    thread.start()

def padaKlikClear(widgetDict):
    """Handler untuk tombol CLEAR"""
    # Reset semua entry ke default
    widgetDict['entryDict']['px'].delete(0, 'end')
    widgetDict['entryDict']['px'].insert(0, "1")
    
    widgetDict['entryDict']['qx'].delete(0, 'end')
    widgetDict['entryDict']['qx'].insert(0, "x")
    
    widgetDict['entryDict']['x0'].delete(0, 'end')
    widgetDict['entryDict']['x0'].insert(0, "0")
    
    widgetDict['entryDict']['y0'].delete(0, 'end')
    widgetDict['entryDict']['y0'].insert(0, "1")
    
    widgetDict['entryDict']['xAkhir'].delete(0, 'end')
    widgetDict['entryDict']['xAkhir'].insert(0, "2")
    
    widgetDict['entryDict']['stepSize'].delete(0, 'end')
    widgetDict['entryDict']['stepSize'].insert(0, "0.1")
    
    # Bersihkan output
    bersihkanSemuaOutput(widgetDict)
    
    updateStatus(widgetDict, "Semua input dan output telah dibersihkan")

def threadSolve(widgetDict):
    """Thread function untuk solving equation"""
    try:
        # Ambil input
        ekspresiP = widgetDict['entryDict']['px'].get().strip()
        ekspresiQ = widgetDict['entryDict']['qx'].get().strip()
        x0 = float(widgetDict['entryDict']['x0'].get().strip())
        y0 = float(widgetDict['entryDict']['y0'].get().strip())
        xAkhir = float(widgetDict['entryDict']['xAkhir'].get().strip())
        stepSize = float(widgetDict['entryDict']['stepSize'].get().strip())
        
        # Selesaikan persamaan
        hasil = selesaikanPersamaanDiferensial(
            ekspresiP, ekspresiQ, x0, y0, xAkhir, stepSize, widgetDict
        )
        
        if hasil['sukses']:
            widgetDict['root'].after(0, lambda: updateStatus(
                widgetDict, "✅ Solusi berhasil dihitung!"
            ))
        else:
            widgetDict['root'].after(0, lambda: messagebox.showerror(
                "Error", hasil['error']
            ))
            widgetDict['root'].after(0, lambda: updateStatus(
                widgetDict, "❌ Terjadi error"
            ))
            
    except Exception as e:
        pesanError = f"❌ Error: {str(e)}\n\nPastikan input menggunakan sintaks yang benar!"
        widgetDict['root'].after(0, lambda: messagebox.showerror("Error", pesanError))
        widgetDict['root'].after(0, lambda: updateStatus(widgetDict, "❌ Terjadi error"))
        
    finally:
        widgetDict['root'].after(0, lambda: widgetDict['tombolDict']['solve'].config(state='normal'))

def updateStatus(widgetDict, pesan):
    """Update status bar message"""
    widgetDict['barStatus'].config(text=pesan)
    widgetDict['root'].update_idletasks()
