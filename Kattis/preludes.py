d = {
    "A#": "Bb",
    "Bb": "A#",
    "C#": "Db",
    "Db": "C#",
    "D#": "Eb",
    "Eb": "D#",
    "F#": "Gb",
    "Gb": "F#",
    "G#": "Ab",
    "Ab": "G#"
}
i = 1
while True:
    try:
        k, m = raw_input().split()
        if k in d: r = d[k] + " " + m
        else: r = "UNIQUE"
        print "Case %d: %s" % (i, r)
        i += 1
    except:
        break
