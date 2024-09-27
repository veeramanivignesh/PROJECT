import tkinter as tk
from tkinter import ttk

conversion_rates = {
    'USD_INR': 82.50,
    'USD_EUR': 0.85,
    'EUR_INR': 96.50,
    'EUR_USD': 1.18,
    'INR_USD': 0.012,
    'INR_EUR': 0.010,
}
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()
        conversion_key = f"{from_currency}_{to_currency}"

        if conversion_key in conversion_rates:
            conversion_rate = conversion_rates[conversion_key]
            converted_amount = amount * conversion_rate
            result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            result_label.config(text="Conversion rate not available")
    except ValueError:
        result_label.config(text="Invalid amount entered")

root = tk.Tk()
root.title("Currency Converter ")
root.geometry("400x350")

amount_label = tk.Label(root, text="Enter Amount:")
amount_label.pack(pady=10)

amount_entry = tk.Entry(root)
amount_entry.pack(pady=10)

side=tk.Label(root,text="SELECT FROM CURRENCY AND TO CURRENCY",fg="blue")
side.pack(pady=10)

currency_options = ["USD", "EUR", "INR"]

from_currency_combo = ttk.Combobox(root, values=currency_options)
from_currency_combo.set("USD")  
from_currency_combo.pack(pady=10)

to_currency_combo = ttk.Combobox(root, values=currency_options)
to_currency_combo.set("INR")  
to_currency_combo.pack(pady=10)

convert_button = tk.Button(root, text="Convert",fg="green",command=convert_currency)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)


exit_button = tk.Button(root, text="Exit",fg="red",command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
