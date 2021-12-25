import PySimpleGUI as sg

sg.theme("DarkAmber")

map = [
    "#############",
    "#...........#",
    "###A#C#B#D###",
    "  #D#C#B#A#  ",
    "  #D#B#A#C#  ",
    "  #B#A#D#C#  ",
    "  #########  ",
]

layout = [
    [
        sg.Text("Score: 0", key="score", font=("Helvetica", 40)),
        sg.Button(
            "Reset",
            key="reset",
            size=(10, 2),
            font=("Helvetica", 15),
        ),
    ],
    *[
        [
            sg.Button(
                f"{map[row][col]}",
                key=f"button_{row},{col}",
                size=(2, 2),
                font=("Helvetica", 15),
                button_color="gray" if map[row][col] in [" ", "#"] else "yellow",
                disabled=map[row][col] in [" ", "#"],
            )
            for col in range(len(map[0]))
        ]
        for row in range(len(map))
    ],
]

score = 0
score_delta = dict(A=1, B=10, C=100, D=1000)
window = sg.Window("Window Title", layout)
previous = None
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    event = str(event)
    if event == "reset":
        score = 0
        score_text: sg.Text = window["score"]
        score_text.update(value="Score: 0")
        for row in range(len(map)):
            for col in range(len(map[0])):
                button: sg.Button = window[f"button_{row},{col}"]
                button.update(button_color="gray" if map[row][col] in [" ", "#"] else "yellow", text=map[row][col])

    if event.startswith("button_"):
        current_button: sg.Button = window[event]
        score_text: sg.Text = window["score"]
        [current_i, current_j] = [int(coord) for coord in event.replace("button_", "").split(",")]
        if current_button.get_text() in (" ", "#"):
            continue
        if previous is None:
            if current_button.get_text() == ".":
                continue
            previous = (current_i, current_j)
            current_button.update(button_color="green")
            continue

        previous_button = window[f"button_{previous[0]},{previous[1]}"]

        if current_button.get_text() != ".":
            previous = (current_i, current_j)
            current_button.update(button_color="green")
            previous_button.update(button_color="yellow")
            continue

        if previous in [
            (current_i - 1, current_j),
            (current_i, current_j + 1),
            (current_i + 1, current_j),
            (current_i, current_j - 1),
        ]:
            score += score_delta[previous_button.get_text()]
            score_text.update(value=f"Score: {score}")
            current_button.update(text=previous_button.get_text())
            previous_button.update(text=".")
            previous = None
            previous_button.update(button_color="yellow")
        else:
            continue


window.close()
