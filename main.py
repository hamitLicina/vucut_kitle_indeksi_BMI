import tkinter as tk
from tkinter import messagebox

# Pencereyi oluşturma
window = tk.Tk()
window.title("BMI (Vücut Kitle Endeksi) Hesaplayıcı")

# Boy giriş etiketi ve alanı
tk.Label(window, text="Boy (metre ya da santimetre):").grid(row=0, column=0, padx=10, pady=10)
entry_height = tk.Entry(window)
entry_height.grid(row=0, column=1, padx=10, pady=10)

# Kilo giriş etiketi ve alanı
tk.Label(window, text="Kilo (kg):").grid(row=1, column=0, padx=10, pady=10)
entry_weight = tk.Entry(window)
entry_weight.grid(row=1, column=1, padx=10, pady=10)


# BMI hesaplama fonksiyonu
def calculate_bmi():
    try:
        # Girişlerin boş olup olmadığını kontrol et
        if not entry_height.get() or not entry_weight.get():
            messagebox.showerror("Hata", "Lütfen boy ve kilo değerlerini girin!")
            return

        # Boyu al ve ondalıklı sayıya çevir
        height = float(entry_height.get())
        # Kiloyu al ve ondalıklı sayıya çevir
        weight = float(entry_weight.get())

        # Boy 3'ten küçükse metre olarak hesapla, aksi takdirde santimetre olarak kabul et
        if height > 3:
            height = height / 100  # Santimetreyi metreye çeviriyoruz

        if height > 0 and weight > 0:
            bmi = weight / (height ** 2)  # BMI hesaplama
            show_bmi_result(bmi)
        else:
            messagebox.showerror("Hata", "Lütfen geçerli bir boy ve kilo girin!")

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")


def show_bmi_result(bmi):
    # BMI sonucunu kullanıcıya göster
    if bmi < 18.5:
        result = f"BMI: {bmi:.2f} (Zayıf)"
    elif 18.5 <= bmi < 24.9:
        result = f"BMI: {bmi:.2f} (Normal)"
    elif 25 <= bmi < 29.9:
        result = f"BMI: {bmi:.2f} (Fazla Kilolu)"
    else:
        result = f"BMI: {bmi:.2f} (Obez)"

    messagebox.showinfo("BMI Sonucu", result)


# Hesapla butonu
button_calculate = tk.Button(window, text="Hesapla", command=calculate_bmi)
button_calculate.grid(row=2, column=0, columnspan=2, pady=10)

# Pencereyi açık tutma
window.mainloop()
