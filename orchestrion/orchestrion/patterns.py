import supriya
from orchestrion.buffers import (
    buffers,
    )
from orchestrion.synth_defs import (
    bufnoise_synthdef,
    durated_chorus,
    durated_allpass,
    durated_freeverb,
    durated_pitchshift,
    durated_freqshift,
    warp_buffer_player_synthdef,
    )

### BUF NOISE ###

bufnoise_pattern_1 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Pseq([_ for _ in buffers], repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 7),
    duration=supriya.patterns.Pwhite(1, 6),
    amp=supriya.patterns.Pwhite(0.2, 0.7),
    start=0,
    end=supriya.patterns.Pseq([_.frame_count for _ in buffers], repetitions=None),
    freq=supriya.patterns.Pwhite(1, 10),
    atk=supriya.patterns.Pwhite(1, 3),
    sus=supriya.patterns.Pwhite(1, 3),
    rel=supriya.patterns.Pwhite(1, 3),
    c1=1,
    c2=-1,
    # pan=supriya.patterns.Pwhite(-1, 1),
    synthdef=bufnoise_synthdef,
    )

bufnoise_pattern_2 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Prand([_ for _ in buffers], repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 9),
    duration=supriya.patterns.Pwhite(2, 9),
    amp=supriya.patterns.Pwhite(0.1, 0.5),
    start=0,
    freq=supriya.patterns.Pwhite(0.25, 1.5),
    atk=supriya.patterns.Pwhite(1, 3),
    sus=supriya.patterns.Pwhite(1, 3),
    rel=supriya.patterns.Pwhite(1, 3),
    c1=1,
    c2=-1,
    # pan=supriya.patterns.Pwhite(-1, 1),
    synthdef=bufnoise_synthdef,
    )

### CHORUS ###

chorus_pattern = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_TAIL,
    synthdef=durated_chorus,
    delta=supriya.patterns.Pwhite(5, 45),
    duration=supriya.patterns.Pwhite(15, 30),
    level=supriya.patterns.Pwhite(),
    )

### ALLPASS ###

allpass_pattern = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_TAIL,
    synthdef=durated_allpass,
    delta=supriya.patterns.Pwhite(5, 45),
    duration=supriya.patterns.Pwhite(15, 30),
    level=supriya.patterns.Pwhite(0., 0.5),
    )

### FREEVERB ###

freeverb_pattern = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_TAIL,
    synthdef=durated_freeverb,
    damping=supriya.patterns.Pwhite(),
    delta=supriya.patterns.Pwhite(5, 45),
    duration=supriya.patterns.Pwhite(15, 30),
    level=supriya.patterns.Pwhite(0.25, 1.),
    room_size=supriya.patterns.Pwhite(),
    )

### PITCHSHIFT ###

pitchshift_pattern = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_TAIL,
    synthdef=durated_pitchshift,
    delta=supriya.patterns.Pwhite(5, 45),
    duration=supriya.patterns.Pwhite(15, 30),
    level=supriya.patterns.Pwhite(),
    pitch_dispersion=supriya.patterns.Pwhite(0., 0.1),
    pitch_shift=supriya.patterns.Pwhite(-12.0, 12.0),
    time_dispersion=supriya.patterns.Pwhite(),
    window_size=supriya.patterns.Pwhite(0.1, 2.0),
    )

### FREQSHIFT ###

freqshift_pattern = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_TAIL,
    synthdef=durated_freqshift,
    delta=supriya.patterns.Pwhite(5, 45),
    duration=supriya.patterns.Pwhite(15, 30),
    level=supriya.patterns.Pwhite(0., 0.5),
    )

###WARP BUFFER PLAYER###

warp_buffer_player_pattern_1 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Prand(buffers, repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 16.0),
    duration=0,
    gain=supriya.patterns.Pwhite(-20, -6),
    overlaps=supriya.patterns.Prand([16, 32], repetitions=None),
    # pan=supriya.patterns.Pwhite(-1.0, 2.0),
    rate=supriya.patterns.Pwhite(0.0625, 6),
    synthdef=warp_buffer_player_synthdef,
    transpose=supriya.patterns.Pwhite(-30.0, -3.0),
    window_size=0.25,
    )

warp_buffer_player_pattern_2 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Prand(buffers, repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 16.0),
    duration=0,
    gain=supriya.patterns.Pwhite(-10, -3),
    overlaps=supriya.patterns.Prand([10, 25], repetitions=None),
    # pan=supriya.patterns.Pwhite(-1.0, 2.0),
    rate=supriya.patterns.Pwhite(20, 50),
    synthdef=warp_buffer_player_synthdef,
    transpose=supriya.patterns.Pwhite(-70.0, -10.0),
    window_size=0.15,
    )

warp_buffer_player_pattern_3 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Prand(buffers, repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 16.0),
    duration=0,
    gain=supriya.patterns.Pwhite(-11, -4),
    overlaps=supriya.patterns.Prand([30, 42], repetitions=None),
    # pan=supriya.patterns.Pwhite(-1.0, 2.0),
    rate=supriya.patterns.Pwhite(27, 83),
    synthdef=warp_buffer_player_synthdef,
    transpose=supriya.patterns.Pwhite(-50.0, -9.0),
    window_size=0.25,
    )

warp_buffer_player_pattern_4 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Prand(buffers, repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 16.0),
    duration=0,
    gain=supriya.patterns.Pwhite(-17, -6),
    overlaps=supriya.patterns.Prand([16, 32], repetitions=None),
    # pan=supriya.patterns.Pwhite(-1.0, 2.0),
    rate=supriya.patterns.Pwhite(0.5, 2.25),
    synthdef=warp_buffer_player_synthdef,
    transpose=supriya.patterns.Pwhite(-60.0, -4.25),
    window_size=0.25,
    )

warp_buffer_player_pattern_5 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Prand(buffers, repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 16.0),
    duration=0,
    gain=supriya.patterns.Pwhite(-10, -4),
    overlaps=supriya.patterns.Prand([60, 74], repetitions=None),
    # pan=supriya.patterns.Pwhite(-1.0, 2.0),
    rate=supriya.patterns.Pwhite(40, 90),
    synthdef=warp_buffer_player_synthdef,
    transpose=supriya.patterns.Pwhite(-80.0, -3.5),
    window_size=0.25,
    )

warp_buffer_player_pattern_6 = supriya.patterns.Pbind(
    add_action=supriya.AddAction.ADD_TO_HEAD,
    buffer_id=supriya.patterns.Prand(buffers, repetitions=None),
    delta=supriya.patterns.Pwhite(0.0, 16.0),
    duration=0,
    gain=supriya.patterns.Pwhite(-15, -6),
    overlaps=supriya.patterns.Prand([35, 52], repetitions=None),
    # pan=supriya.patterns.Pwhite(-1.0, 2.0),
    rate=supriya.patterns.Pwhite(0.015625, 0.25),
    synthdef=warp_buffer_player_synthdef,
    transpose=supriya.patterns.Pwhite(-50.0, 1.0),
    window_size=0.25,
    )
