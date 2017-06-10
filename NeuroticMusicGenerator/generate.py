"""classes to provider easier format for notes compatible with 
MIDITime 1.1.3"""


class MyMidiNote:
    def __init__(self, note=0, note_start_time=0, note_duration_in_beats=1, velocity=127):
        self.note = note
        self.note_start_time = note_start_time
        self.note_duration_in_beats = note_duration_in_beats
        self.velocity = velocity

    def randomise_note(self, note_start_time):
        from random import randint
        self.note = randint(10, 110)
        self.note_start_time = note_start_time
        self.note_duration_in_beats = randint(1, 16)/4
        self.velocity = randint(100, 127)

    def __len__(self):
        return 4

    def __getitem__(self, item):
        if item == 0:
            return self.note_start_time
        elif item == 1:
            return self.note
        elif item == 2:
            return self.velocity
        elif item == 3:
            return self.note_duration_in_beats


class MyMidiNoteGenerator:
    @staticmethod
    def gen(fun, fun_cycle_len, start_time, duration, beat_duration, cycle_number):
        from random import randint
        notes_list = []
        nodes_iterator = 0
        nodes_number = duration / beat_duration
        nodes_per_cycle = nodes_number / cycle_number
        delta = fun_cycle_len / nodes_per_cycle
        time = start_time
        for i in range(1, round(nodes_number - 1)):
            pitch = int(round((fun(nodes_iterator))*60))
            nodes_iterator += delta
            notes_list.append(MyMidiNote(pitch, time, randint(1, 16)/4, randint(50, 127)))
            # notes_list.append([time, pitch, random.randint(100, 127),
            #                   random.randint(1, 4)/2])
            time += beat_duration
        return notes_list