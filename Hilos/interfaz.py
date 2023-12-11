import PySimpleGUI as pg
#pg.theme("Topanga")

layout = [
[pg.Text("Mi primera ventana")],
[pg.Button("Botón 1"), pg.Button("Botón 2")],
[pg.InputText(key="num_1"), pg.InputText(key="num_2")],
[pg.Slider((0, 10), orientation="horizontal")],
[pg.Output(size=(45, 19))]
]

ventana = pg.Window("Mi aplicación", layout)

def sumar(*args):
    return sum(args)

while True:
    evento, valor = ventana.read()
    if evento == pg.WIN_CLOSED:
        ventana.close()
        break
    if evento == "Botón 1":
        print(sumar(int(valor["num_1"]), int(valor["num_2"])))
    if evento == "Botón 2":
        print("B2")