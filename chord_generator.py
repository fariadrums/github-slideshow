import argparse

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

CHORD_TYPES = {
    'major': [0, 4, 7],
    'minor': [0, 3, 7],
    'dim': [0, 3, 6],
    'aug': [0, 4, 8],
    'major7': [0, 4, 7, 11],
    'minor7': [0, 3, 7, 10],
    'dominant7': [0, 4, 7, 10],
    'sus2': [0, 2, 7],
    'sus4': [0, 5, 7]
}

NOTE_ALIASES = {
    'Db': 'C#',
    'Eb': 'D#',
    'Gb': 'F#',
    'Ab': 'G#',
    'Bb': 'A#'
}


def normalize(note: str) -> str:
    note = note.strip().capitalize()
    return NOTE_ALIASES.get(note, note)


def chord(root: str, chord_type: str):
    root = normalize(root)
    if root not in NOTES:
        raise ValueError(f"Invalid root note: {root}")
    if chord_type not in CHORD_TYPES:
        raise ValueError(f"Invalid chord type: {chord_type}")
    intervals = CHORD_TYPES[chord_type]
    root_idx = NOTES.index(root)
    notes = [NOTES[(root_idx + i) % len(NOTES)] for i in intervals]
    return notes


def main():
    parser = argparse.ArgumentParser(description='Generate piano chord notes')
    parser.add_argument('root', help='Root note (e.g. C, D#, Bb)')
    parser.add_argument('type', choices=sorted(CHORD_TYPES.keys()), help='Chord type')
    args = parser.parse_args()
    notes = chord(args.root, args.type)
    print(' '.join(notes))


if __name__ == '__main__':
    main()
