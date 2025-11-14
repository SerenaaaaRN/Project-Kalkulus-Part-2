import numpy as np
import sympy as sp
from output_display import tampilkanLangkahSolusi, tampilkanTabel, tampilkanPlot

def selesaikanPersamaanDiferensial(ekspresiP, ekspresiQ, x0, y0, xAkhir, stepSize, widgetDict):
    try:
        x = sp.Symbol('x')
        simbolP = sp.sympify(ekspresiP)
        simbolQ = sp.sympify(ekspresiQ)
        
        # Generate dan tampilkan langkah solusi
        langkahSolusi = generateLangkahSolusi(simbolP, simbolQ, x0, y0, x)
        widgetDict['root'].after(0, lambda: tampilkanLangkahSolusi(widgetDict, langkahSolusi))
        
        # Update status
        widgetDict['root'].after(0, lambda: widgetDict['barStatus'].config(
            text="Menghitung solusi eksak..."
        ))
        
        # Selesaikan dengan SymPy
        y = sp.Function('y')
        persamaanDif = sp.Eq(y(x).diff(x) + simbolP * y(x), simbolQ)
        solusiEksak = sp.dsolve(persamaanDif, y(x), ics={y(x0): y0})
        
        # Generate nilai x
        jumlahLangkah = int((xAkhir - x0) / stepSize) + 1
        nilaiX = np.linspace(x0, xAkhir, jumlahLangkah)
        
        # Hitung nilai y
        fungsiYEksak = sp.lambdify(x, solusiEksak.rhs, 'numpy')
        nilaiYEksak = fungsiYEksak(nilaiX)
        
        # Tampilkan hasil
        widgetDict['root'].after(0, lambda: tampilkanTabel(widgetDict, nilaiX, nilaiYEksak))
        widgetDict['root'].after(0, lambda: tampilkanPlot(
            widgetDict, nilaiX, nilaiYEksak, ekspresiP, ekspresiQ
        ))
        
        return {
            'sukses': True,
            'nilaiX': nilaiX,
            'nilaiY': nilaiYEksak,
            'solusi': solusiEksak
        }
        
    except Exception as e:
        return {
            'sukses': False,
            'error': f"❌ Error: {str(e)}\n\nPastikan input menggunakan sintaks yang benar!"
        }

def generateLangkahSolusi(simbolP, simbolQ, x0, y0, x):
    """Generate step-by-step solution text"""
    langkah = "="*80 + "\n"
    langkah += " SOLUSI MANUAL (METODE FAKTOR INTEGRASI)\n"
    langkah += "="*80 + "\n\n"
    
    langkah += "📌 Langkah 1: Persamaan Diferensial Linear Orde 1\n"
    langkah += "   dy/dx + P(x)y = Q(x)\n"
    langkah += f"   dy/dx + ({simbolP})y = {simbolQ}\n\n"
    
    langkah += "📌 Langkah 2: Menentukan Faktor Integrasi\n"
    langkah += "   μ(x) = e^(∫P(x)dx)\n"
    
    try:
        integralP = sp.integrate(simbolP, x)
        langkah += f"   ∫P(x)dx = ∫({simbolP})dx = {integralP}\n"
        
        faktorIntegrasi = sp.exp(integralP)
        faktorIntegrasiSederhana = sp.simplify(faktorIntegrasi)
        langkah += f"   μ(x) = e^({integralP}) = {faktorIntegrasiSederhana}\n\n"
        
        langkah += "📌 Langkah 3: Kalikan persamaan dengan faktor integrasi μ(x)\n"
        langkah += "   μ(x)·dy/dx + μ(x)·P(x)·y = μ(x)·Q(x)\n\n"
        
        langkah += "📌 Langkah 4: Persamaan menjadi turunan dari μ(x)·y\n"
        langkah += "   d/dx[μ(x)·y] = μ(x)·Q(x)\n"
        
        ruasKanan = faktorIntegrasiSederhana * simbolQ
        langkah += f"   d/dx[{faktorIntegrasiSederhana}·y] = {ruasKanan}\n\n"
        
        langkah += "📌 Langkah 5: Integralkan kedua ruas terhadap x\n"
        
        try:
            integralRuasKanan = sp.integrate(ruasKanan, x)
            langkah += f"   {faktorIntegrasiSederhana}·y = {integralRuasKanan} + C\n\n"
            
            langkah += "📌 Langkah 6: Solusi Umum\n"
            konstantaC = sp.Symbol('C')
            solusiUmum = (integralRuasKanan + konstantaC) / faktorIntegrasiSederhana
            solusiUmumSederhana = sp.simplify(solusiUmum)
            langkah += f"   y = ({integralRuasKanan} + C) / {faktorIntegrasiSederhana}\n"
            langkah += f"   y = {solusiUmumSederhana}\n\n"
            
            langkah += "📌 Langkah 7: Terapkan Kondisi Awal\n"
            langkah += f"   y({x0}) = {y0}\n"
            
            try:
                nilaiYdiX0 = solusiUmumSederhana.subs(x, x0)
                persamaanC = sp.Eq(nilaiYdiX0, y0)
                nilaiC = sp.solve(persamaanC, konstantaC)[0]
                langkah += f"   C = {nilaiC}\n\n"
                
                langkah += "📌 Langkah 8: Solusi Khusus (Particular Solution)\n"
                solusiKhusus = solusiUmumSederhana.subs(konstantaC, nilaiC)
                solusiKhususSederhana = sp.simplify(solusiKhusus)
                langkah += f"   y(x) = {solusiKhususSederhana}\n"
                
            except:
                langkah += "   ⚠ Tidak dapat menentukan konstanta C secara simbolik\n"
        except:
            langkah += "   ⚠ Integral ruas kanan terlalu kompleks\n"
            
    except Exception as e:
        langkah += f"   ⚠ Error: {e}\n"
        
    return langkah