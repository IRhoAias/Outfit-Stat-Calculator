import customtkinter as ctk

class StatCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Outfit Stat Calculator. For SPN Beta2")
        self.geometry("355x264")
        self.resizable(False, False)  # Evitar redimensionamiento
        
        # Variables
        self.str_base = ctk.StringVar()
        self.agi_base = ctk.StringVar()
        self.sta_base = ctk.StringVar()
        self.str_isv_min = ctk.StringVar()
        self.agi_isv_min = ctk.StringVar()
        self.sta_isv_min = ctk.StringVar()
        self.level = ctk.StringVar(value="1")  # Valor inicial del nivel
        
        # Entradas
        self.create_label_entry("Str:", self.str_base, 0, 0)
        self.create_label_entry("ISV:", self.str_isv_min, 0, 1)
        
        self.create_label_entry("Agi:", self.agi_base, 1, 0)
        self.create_label_entry("ISV:", self.agi_isv_min, 1, 1)
        
        self.create_label_entry("Sta:", self.sta_base, 2, 0)
        self.create_label_entry("ISV:", self.sta_isv_min, 2, 1)
        
        # Menú desplegable para el nivel
        level_options = [str(i) for i in range(1, 33)]  # Niveles del 1 al 32
        level_menu = ctk.CTkOptionMenu(self, variable=self.level, values=level_options)
        level_menu.grid(row=3, column=1, padx=10, pady=5)

        level_label = ctk.CTkLabel(self, text="Level (Máx. 32):")
        level_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        # Cuadro de texto para resultados (solo visualización)
        self.result_text = ctk.CTkTextbox(self, height=100, width=354)
        self.result_text.configure(font=("Arial", 14))
        self.result_text.grid(row=4, column=0, columnspan=3, pady=10)
        self.result_text.configure(state="disabled")  # Deshabilitar la entrada de texto
        
        # Vincular cambios
        for var in [
            self.str_base, self.agi_base, self.sta_base,
            self.str_isv_min,
            self.agi_isv_min,
            self.sta_isv_min,
            self.level
        ]:
            var.trace_add("write", self.update_stats)

    def create_label_entry(self, text, variable, row, column):
        label = ctk.CTkLabel(self, text=text)
        label.grid(row=row, column=column * 1, padx=10, pady=5, sticky="w")
        
        # Crear un Entry con un tamaño reducido
        entry = ctk.CTkEntry(self, textvariable=variable, width=40)  # Reducir a la mitad
        entry.grid(row=row, column=column * 1, padx=10, pady=5)

    def update_stats(self, *args):
        try:
            str_base = int(self.str_base.get() or 0)
            agi_base = int(self.agi_base.get() or 0)
            sta_base = int(self.sta_base.get() or 0)
            str_isv_min = float(self.str_isv_min.get() or 0)
            agi_isv_min = float(self.agi_isv_min.get() or 0)
            sta_isv_min = float(self.sta_isv_min.get() or 0)
            level = min(int(self.level.get() or 0), 32)  # Limite de Level en 32
            
            str_final = str_base + int(8 * str_isv_min * level)
            agi_final = agi_base + int(8 * agi_isv_min * level)
            sta_final = sta_base + int(8 * sta_isv_min * level)
            
            result = f"Str Final: {str_final}\nAgi Final: {agi_final}\nSta Final: {sta_final}"
            self.result_text.configure(state="normal")  # Habilitar para insertar texto
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", result)
            self.result_text.configure(state="disabled")  # Deshabilitar después de insertar texto
        except ValueError:
            pass

if __name__ == "__main__":
    app = StatCalculator()
    app.mainloop()
