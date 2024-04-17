import tkinter as tk    #Importar la libreria y declarle un alias
root = tk.Tk()  #llamar a la libreria puede ser cualquier variable

root.title("Ejemplo")   #titulo de la ventana
root.geometry("600x400+600+200")    #tamaño de la ventana lo que sigue despues determinara la ubicacion donde abrira la ventana
root.resizable(True,True) #linea que permite agrandar o minimizar la ventana

boton_salir = tk.Button(root, text="Salir", command=lambda: root.quit())    #funciones del boton
boton_salir.pack(ipadx=20,ipady=10,expand=True)     #Tamaño del boton

root.mainloop()