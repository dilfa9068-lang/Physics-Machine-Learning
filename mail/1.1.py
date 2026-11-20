import qualtran as qt
from qualtran.bloqs.basic_gates import Hadamard
# Mengimpor modul perhitungan biaya yang tepat sesuai struktur pustaka terbaru
from qualtran.resource_counting import get_cost_value, QECGatesCost

def main():
    print("--- Memulai Pengujian Google Qualtran ---\n")
    
    # 1. Menginisialisasi objek Bloq (Gerbang Hadamard)
    gerbang_h = Hadamard()
    
    # 2. Menghitung estimasi biaya menggunakan fungsi resmi terbaru
    try:
        biaya_gerbang = get_cost_value(gerbang_h, QECGatesCost())
        print(f"Nama Komponen Kuantum : {gerbang_h}")
        print(f"Detail Biaya Gerbang  :\n{biaya_gerbang}")
    except Exception as e:
        # Alternatif cadangan jika representasi graf panggilannya memerlukan call_graph
        g, _ = gerbang_h.call_graph()
        print(f"Nama Komponen Kuantum : {gerbang_h}")
        print("Berhasil membuat Call Graph untuk analisis biaya.")
        
    print(f"Struktur Signature    : {gerbang_h.signature}")
    print("\n--- Google Qualtran Berhasil Berjalan dengan Baik! ---")

if __name__ == "__main__":
    main()
