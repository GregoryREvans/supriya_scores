#! /usr/bin/env python
from supriya import (
    AddAction, DoneAction, Say, Session, SynthDefBuilder,
    patterns, play, synthdefs, ugens
    )

### SESSION SETUP ###

channel_count = 2

session = Session(0, channel_count)

### BUFFERS ###

says = []
for voice in ['Daniel', 'Fiona', 'Victoria', 'Tessa', 'Karen', 'Thomas']:
    for text in [
        'I must not fear.', 'Fear is the mind-killer.',
        'Fear is the little-death that brings total obliteration.',
        'I will face my fear.', 'I will permit it to pass over me and through me.',
        'And when it has gone past I will turn the inner eye to see its path.',
        'Where the fear has gone there will be nothing.',
        'Only I will remain.',
        ]:
        says.append(Say(text, voice=voice))

buffers = []
with session.at(0):
    for say in says:
        buffer_ = session.add_buffer(channel_count=1, file_path=say)
        buffers.append(buffer_)

### WARP BUFFER PLAYER ###

with SynthDefBuilder(
    buffer_id=0,
    gain=0,
    out=0,
    overlaps=32,
    rate=1,
    transpose=0,
    window_size=0.5,
    ) as builder:
    line = ugens.Line.kr(
        done_action=2,
        duration=ugens.BufDur.kr(builder['buffer_id']) * builder['rate'],
        )
    window = line.hanning_window()
    pointer_scrub = ugens.LFNoise2.kr(
        frequency=[0.01, 0.01],
        ) * window * 0.1
    warps = ugens.Warp1.ar(
        buffer_id=builder['buffer_id'],
        channel_count=1,
        frequency_scaling=builder['transpose'].semitones_to_ratio(),
        interpolation=2,
        overlaps=builder['overlaps'].as_int(),
        pointer=line + pointer_scrub,
        window_rand_ratio=0.001,
        window_size=ugens.LFNoise2.kr(
            frequency=0.01,
            ).scale(-1, 1, 0.125, 0.375),
        )
    source = ugens.XFade2.ar(
        in_a=ugens.Pan2.ar(
            source=warps[0],
            position=ugens.LFNoise2.kr(frequency=0.05),
            ),
        in_b=ugens.Pan2.ar(
            source=warps[1],
            position=ugens.LFNoise2.kr(frequency=0.05),
            ),
        pan=ugens.LFNoise2.kr(frequency=0.05),
        )
    source = source * window * builder['gain'].db_to_amplitude()
    ugens.Out.ar(
        bus=builder['out'],
        source=source,
        )

warp_buffer_player_synthdef = builder.build()

warp_buffer_player_pattern = patterns.Pbind(
    add_action=AddAction.ADD_TO_HEAD,
    buffer_id=patterns.Prand(buffers, repetitions=None),
    delta=patterns.Pwhite(0.0, 16.0),
    duration=0,
    gain=patterns.Pwhite(-24, -12),
    overlaps=patterns.Prand([16, 32], repetitions=None),
    pan=patterns.Pwhite(-1.0, 1.0),
    rate=patterns.Pwhite(20, 80),
    synthdef=warp_buffer_player_synthdef,
    transpose=patterns.Pwhite(-12.0, 12.0),
    window_size=0.25,
    )

### CHORUS ###

with SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    ) as builder:
    window = ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    in_ = ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source = in_ * window
    source = source[0] + source[1]
    source += ugens.LocalIn.ar(channel_count=1)
    allpasses = []
    allpass_count = 16
    maximum_delay_time = 0.01
    for _ in range(allpass_count):
        allpass = ugens.AllpassC.ar(
            decay_time=ugens.LFDNoise3.kr(
                frequency=ugens.ExpRand.ir(0.1, 5),
                ).scale(-1, 1, 0., 0.1),
            delay_time=ugens.LFDNoise3.kr(
                frequency=ugens.ExpRand.ir(0.1, 5),
                ).scale(-1, 1, 0., maximum_delay_time),
            maximum_delay_time=maximum_delay_time,
            source=source,
            )
        allpasses.append(allpass)
    source = ugens.Mix.new(allpasses) / allpass_count
    source = ugens.LeakDC.ar(source=source)
    source = ugens.Limiter.ar(source=source)
    ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=[source, source],
        )
    ugens.LocalOut.ar(
        source=source * -0.9 * abs(ugens.LFDNoise1.kr(frequency=0.1))
        )
    ugens.DetectSilence.kr(
        done_action=DoneAction.FREE_SYNTH,
        source=ugens.Mix.new(tuple(in_) + tuple(source)),
        )

durated_chorus = builder.build()

chorus_pattern = patterns.Pbind(
    add_action=AddAction.ADD_TO_TAIL,
    synthdef=durated_chorus,
    delta=patterns.Pwhite(5, 45),
    duration=patterns.Pwhite(15, 30),
    level=patterns.Pwhite(),
    )

### ALLPASS ###

with SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    ) as builder:
    window = ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source += ugens.LocalIn.ar(channel_count=channel_count)
    source *= ugens.Line.kr(duration=0.1)
    allpasses = []
    maximum_delay = ugens.Rand.ir(0.1, 1)
    for output in source:
        for _ in range(3):
            output = ugens.AllpassC.ar(
                decay_time=ugens.LFDNoise3.kr(
                    frequency=ugens.ExpRand.ir(0.01, 0.1),
                    ).scale(-1, 1, 0.001, 1),
                delay_time=ugens.LFDNoise3.kr(
                    frequency=ugens.ExpRand.ir(0.01, 0.1),
                    ).scale(-1, 1, 0.001, 1) * maximum_delay,
                maximum_delay_time=maximum_delay,
                source=output,
                )
        allpasses.append(output)
    source = synthdefs.UGenArray(allpasses)
    source = ugens.LeakDC.ar(source=source)
    source = ugens.Limiter.ar(source=source)
    ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window,
        source=source * builder['level'],
        )
    ugens.LocalOut.ar(
        source=source * -0.9 * ugens.LFDNoise1.kr(frequency=0.1)
        )
    ugens.DetectSilence.kr(
        done_action=DoneAction.FREE_SYNTH,
        source=ugens.Mix.new(source),
        )

durated_allpass = builder.build()

allpass_pattern = patterns.Pbind(
    add_action=AddAction.ADD_TO_TAIL,
    synthdef=durated_allpass,
    delta=patterns.Pwhite(5, 45),
    duration=patterns.Pwhite(15, 30),
    level=patterns.Pwhite(0., 0.5),
    )

### FREEVERB ###

with SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    damping=0.5,
    room_size=0.5,
    ) as builder:
    window = ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    #source = in_ * window
    source = ugens.FreeVerb.ar(
        source=source,
        damping=builder['damping'],
        room_size=builder['room_size'],
        mix=1.0,
        )
    source = ugens.LeakDC.ar(source=source)
    source = (source * 1.5).tanh()
    source = ugens.Limiter.ar(source=source)
    ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=source,
        )
    ugens.DetectSilence.kr(
        done_action=DoneAction.FREE_SYNTH,
        source=ugens.Mix.new(source),
        )

durated_freeverb = builder.build()

freeverb_pattern = patterns.Pbind(
    add_action=AddAction.ADD_TO_TAIL,
    synthdef=durated_freeverb,
    damping=patterns.Pwhite(),
    delta=patterns.Pwhite(5, 45),
    duration=patterns.Pwhite(15, 30),
    level=patterns.Pwhite(0.25, 1.),
    room_size=patterns.Pwhite(),
    )

### PITCHSHIFT ###

with SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    pitch_shift=0.,
    pitch_dispersion=0,
    time_dispersion=0,
    window_size=0.5,
    ) as builder:
    window = ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source += ugens.LocalIn.ar(channel_count=channel_count)
    source = ugens.PitchShift.ar(
        source=source,
        pitch_dispersion=builder['pitch_dispersion'],
        pitch_ratio=builder['pitch_shift'].semitones_to_ratio(),
        time_dispersion=builder['time_dispersion'] * builder['window_size'],
        window_size=builder['window_size'],
        )
    source = ugens.LeakDC.ar(source=source)
    source = (source * 1.5).tanh()
    source = ugens.Limiter.ar(source=source)
    ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=source,
        )
    ugens.LocalOut.ar(
        source=[
            source[1] * -0.9 * ugens.LFDNoise1.kr(frequency=0.1),
            source[0] * -0.9 * ugens.LFDNoise1.kr(frequency=0.1),
            ],
        )
    ugens.DetectSilence.kr(
        done_action=DoneAction.FREE_SYNTH,
        source=ugens.Mix.new(source),
        )

durated_pitchshift = builder.build()

pitchshift_pattern = patterns.Pbind(
    add_action=AddAction.ADD_TO_TAIL,
    synthdef=durated_pitchshift,
    delta=patterns.Pwhite(5, 45),
    duration=patterns.Pwhite(15, 30),
    level=patterns.Pwhite(),
    pitch_dispersion=patterns.Pwhite(0., 0.1),
    pitch_shift=patterns.Pwhite(-12.0, 12.0),
    time_dispersion=patterns.Pwhite(),
    window_size=patterns.Pwhite(0.1, 2.0),
    )

### FREQSHIFT ###

with SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    ) as builder:
    window = ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source = ugens.FreqShift.ar(
        source=source,
        frequency=ugens.LFDNoise3.kr(frequency=0.01) * 2000,
        phase=ugens.LFNoise2.kr(frequency=0.01),
        )
    source = ugens.LeakDC.ar(source=source)
    source = (source * 1.5).tanh()
    source = ugens.Limiter.ar(source=source)
    ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=source,
        )
    ugens.DetectSilence.kr(
        done_action=DoneAction.FREE_SYNTH,
        source=ugens.Mix.new(source),
        )

durated_freqshift = builder.build()

freqshift_pattern = patterns.Pbind(
    add_action=AddAction.ADD_TO_TAIL,
    synthdef=durated_freqshift,
    delta=patterns.Pwhite(5, 45),
    duration=patterns.Pwhite(15, 30),
    level=patterns.Pwhite(0., 0.5),
    )

### LIMITER ###

with SynthDefBuilder(
    out=0,
    ) as builder:
    source = ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source = ugens.LeakDC.ar(source=source)
    source = ugens.Limiter.ar(source=source)
    ugens.ReplaceOut.ar(
        bus=builder['out'],
        source=source,
        )

limiter = builder.build()

### MULTIBAND COMPRESSOR ###

with SynthDefBuilder(
    frequency_1=200,
    frequency_2=2000,
    frequency_3=5000,
    band_1_clamp_time=0.01,
    band_1_postgain=1,
    band_1_pregain=1,
    band_1_relax_time=0.1,
    band_1_slope_above=0.5,
    band_1_slope_below=1.0,
    band_1_threshold=0.9,
    band_2_clamp_time=0.01,
    band_2_postgain=1,
    band_2_pregain=1,
    band_2_relax_time=0.1,
    band_2_slope_above=0.5,
    band_2_slope_below=1.0,
    band_2_threshold=0.9,
    band_3_clamp_time=0.01,
    band_3_postgain=1,
    band_3_pregain=1,
    band_3_relax_time=0.1,
    band_3_slope_above=0.5,
    band_3_slope_below=1.0,
    band_3_threshold=0.9,
    band_4_clamp_time=0.01,
    band_4_postgain=1,
    band_4_pregain=1,
    band_4_relax_time=0.1,
    band_4_slope_above=0.5,
    band_4_slope_below=1.0,
    band_4_threshold=0.9,
    in_=0,
    out=0,
    ) as builder:
    source = ugens.In.ar(
        bus=builder['in_'],
        channel_count=channel_count,
        )
    band_1 = ugens.LPF.ar(
        frequency=builder['frequency_1'],
        source=source,
        )
    band_4 = ugens.HPF.ar(
        frequency=builder['frequency_3'],
        source=source,
        )
    center = source - band_1 - band_4
    band_2 = ugens.LPF.ar(
        frequency=builder['frequency_2'],
        source=center,
        )
    band_3 = ugens.HPF.ar(
        frequency=builder['frequency_2'],
        source=center,
        )
    band_1 = ugens.CompanderD.ar(
        clamp_time=builder['band_1_clamp_time'],
        relax_time=builder['band_1_relax_time'],
        slope_above=builder['band_1_slope_above'],
        slope_below=builder['band_1_slope_below'],
        source=band_1 * builder['band_1_pregain'].db_to_amplitude(),
        threshold=builder['band_1_threshold'].db_to_amplitude(),
        )
    band_2 = ugens.CompanderD.ar(
        clamp_time=builder['band_2_clamp_time'],
        relax_time=builder['band_2_relax_time'],
        slope_above=builder['band_2_slope_above'],
        slope_below=builder['band_2_slope_below'],
        source=band_2 * builder['band_2_pregain'].db_to_amplitude(),
        threshold=builder['band_2_threshold'].db_to_amplitude(),
        )
    band_3 = ugens.CompanderD.ar(
        clamp_time=builder['band_3_clamp_time'],
        relax_time=builder['band_3_relax_time'],
        slope_above=builder['band_3_slope_above'],
        slope_below=builder['band_3_slope_below'],
        source=band_3 * builder['band_3_pregain'].db_to_amplitude(),
        threshold=builder['band_3_threshold'].db_to_amplitude(),
        )
    band_4 = ugens.CompanderD.ar(
        clamp_time=builder['band_4_clamp_time'],
        relax_time=builder['band_4_relax_time'],
        slope_above=builder['band_4_slope_above'],
        slope_below=builder['band_4_slope_below'],
        source=band_4 * builder['band_4_pregain'].db_to_amplitude(),
        threshold=builder['band_4_threshold'].db_to_amplitude(),
        )
    band_1 *= builder['band_1_postgain'].db_to_amplitude()
    band_2 *= builder['band_2_postgain'].db_to_amplitude()
    band_3 *= builder['band_3_postgain'].db_to_amplitude()
    band_4 *= builder['band_4_postgain'].db_to_amplitude()
    source = ugens.Sum4.new(
        input_one=band_1,
        input_two=band_2,
        input_three=band_3,
        input_four=band_4,
        )
    ugens.ReplaceOut.ar(bus=builder['out'], source=source)

multiband_compressor = builder.build()

### RENDER ###

pattern = patterns.Pbus(
    patterns.Ppar([
        warp_buffer_player_pattern,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

with session.at(0):
    for i in range(3):
        session.inscribe(pattern, duration=60 * 7, seed=i)
    session.add_synth(
        add_action=AddAction.ADD_TO_TAIL,
        synthdef=multiband_compressor,
        )
    session.add_synth(
        add_action=AddAction.ADD_TO_TAIL,
        synthdef=limiter,
        )

play(session, memory_size=8192 * 16)
