n = int(input())
xs = input().split()

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
count = 12

scales = {}
for i in range(12):
    scales[notes[i]] = [
        notes[(i + 0) % 12], notes[(i + 2) % 12], notes[(i + 4) % 12], notes[(i + 5) % 12],
        notes[(i + 7) % 12], notes[(i + 9) % 12], notes[(i + 11) % 12], notes[(i + 12) % 12]
    ]
out = []
for note in notes:
    scale = scales[note]
    if all(x in scale for x in xs):
        out.append(note)
if len(out):
    print(*out)
else:
    print("none")
