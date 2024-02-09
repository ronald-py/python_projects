import matplotlib.pyplot as plot

fig, ax = plot.subplots()
frutas = ['manzana', 'moras', 'cerezas', 'naranjas']
ventas = [29, 130, 83, 47]
etiquetas_barras = ['red', 'blue', 'green', 'orange']
color_barras = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(frutas, ventas, label=etiquetas_barras, color=color_barras)

ax.set_ylabel('ventas totales')
ax.set_xlabel('frutas vendidas')
ax.legend(title= 'Barra x fruta')

plot.show()