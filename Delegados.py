import tkinter as tk
from tkinter import messagebox

# Lista de candidatos fijos
candidatos = ["Delegado 1 (Amira)", "Delegado 2 (Sabrina)" , "Delegado 3 (Dario)" , "Delegado 4 (Kata)"]
votos = {c: 0 for c in candidatos}

def postularse():
    nombre = entry_nombre.get()
    if nombre and nombre not in candidatos:
        candidatos.append(nombre)
        votos[nombre] = 0
        actualizar_lista()
        messagebox.showinfo("Postulación", f"{nombre} se postuló correctamente")
    elif nombre in candidatos:
        messagebox.showwarning("Aviso", "Ese nombre ya está en la lista")

def votar():
    seleccion = lista.curselection()
    if seleccion:
        candidato = lista.get(seleccion)
        votos[candidato] += 1
        messagebox.showinfo("Voto registrado", f"Votaste a {candidato}")
    else:
        messagebox.showwarning("Atención", "Selecciona un candidato para votar")

def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        candidato = lista.get(seleccion)
        if "fijo" in candidato:
            messagebox.showwarning("Aviso", "No se pueden eliminar los delegados fijos")
        else:
            candidatos.remove(candidato)
            votos.pop(candidato)
            actualizar_lista()
            messagebox.showinfo("Eliminado", f"{candidato} fue eliminado")
    else:
        messagebox.showwarning("Atención", "Selecciona un candidato para eliminar")

def mostrar_resultados():
    resultados = "\n".join([f"{c}: {votos[c]} votos" for c in candidatos])
    messagebox.showinfo("Resultados", resultados)

def actualizar_lista():
    lista.delete(0, tk.END)
    for c in candidatos:
        lista.insert(tk.END, c)

# Ventana principal
ventana = tk.Tk()
ventana.title("Elección de Delegados")

# Instrucciones
label_info = tk.Label(ventana, text="Postúlate si querés ser candidato")
label_info.pack()

# Campo para ingresar nombre
label = tk.Label(ventana, text="Tu nombre:")
label.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Botón para postularse
boton_postular = tk.Button(ventana, text="Postularme", command=postularse)
boton_postular.pack()

# Lista de candidatos
label_lista = tk.Label(ventana, text="Selecciona un candidato y vota a quien gustes")
label_lista.pack()
lista = tk.Listbox(ventana, width=40)
lista.pack()
actualizar_lista()

# Botones de acción
boton_votar = tk.Button(ventana, text="Votar", command=votar)
boton_votar.pack()

boton_eliminar = tk.Button(ventana, text="Eliminar candidato", command=eliminar)
boton_eliminar.pack()

boton_resultados = tk.Button(ventana, text="Ver resultados", command=mostrar_resultados)
boton_resultados.pack()

ventana.mainloop()
