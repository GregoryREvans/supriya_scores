import supriya
from used_light.session_setup import channel_count


### BUF NOISE ###

with supriya.SynthDefBuilder(
    name="bufnoise",
    amp=1,
    out=0,
    buffer_id=0,
    start=0,
    end=1,
    freq=1,
    atk=0,
    sus=0,
    rel=3,
    c1=1.0,
    c2=-1.0,
    pan=0,
    ) as builder:
    env = supriya.ugens.EnvGen.kr(
        envelope=supriya.synthdefs.Envelope(
            amplitudes=(0,1,1,0),
            durations=(
                builder['atk'],
                builder['sus'],
                builder['rel'],
                ),
            curves=(
                builder['c1'],
                0,
                builder['c2'],
                )
            ),
        done_action=2
        )
    ptr = supriya.ugens.LFNoise1.ar(frequency=builder['freq']).range(minimum=builder['start'], maximum=builder['end'])
    sig = supriya.ugens.BufRd.ar(channel_count=1, buffer_id=builder['buffer_id'], phase=ptr)
    sig = sig * env
    sig = supriya.ugens.Pan2.ar(source=sig, position=supriya.ugens.LFNoise2.kr(frequency=0.05), level=builder['amp'])
    sig = supriya.ugens.PanAz.ar(
        channel_count=channel_count,
        amplitude=1,
        orientation=0.5,
        position=builder['pan'],
        source=sig,
        width=2,
        )
    supriya.ugens.Out.ar(bus=builder['out'], source=sig)

bufnoise_synthdef = builder.build()

### CHORUS ###

with supriya.SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    ) as builder:
    window = supriya.ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    in_ = supriya.ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source = in_ * window
    source = source[0] + source[1]
    source += supriya.ugens.LocalIn.ar(channel_count=1)
    allpasses = []
    allpass_count = 16
    maximum_delay_time = 0.01
    for _ in range(allpass_count):
        allpass = supriya.ugens.AllpassC.ar(
            decay_time=supriya.ugens.LFDNoise3.kr(
                frequency=supriya.ugens.ExpRand.ir(0.1, 5),
                ).scale(-1, 1, 0., 0.1),
            delay_time=supriya.ugens.LFDNoise3.kr(
                frequency=supriya.ugens.ExpRand.ir(0.1, 5),
                ).scale(-1, 1, 0., maximum_delay_time),
            maximum_delay_time=maximum_delay_time,
            source=source,
            )
        allpasses.append(allpass)
    source = supriya.ugens.Mix.new(allpasses) / allpass_count
    source = supriya.ugens.LeakDC.ar(source=source)
    source = supriya.ugens.Limiter.ar(source=source)
    supriya.ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=[source, source],
        )
    supriya.ugens.LocalOut.ar(
        source=source * -0.9 * abs(supriya.ugens.LFDNoise1.kr(frequency=0.1))
        )
    supriya.ugens.DetectSilence.kr(
        done_action=supriya.DoneAction.FREE_SYNTH,
        source=supriya.ugens.Mix.new(tuple(in_) + tuple(source)),
        )

durated_chorus = builder.build()

### ALLPASS ###

with supriya.SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    ) as builder:
    window = supriya.ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = supriya.ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source += supriya.ugens.LocalIn.ar(channel_count=channel_count)
    source *= supriya.ugens.Line.kr(duration=0.1)
    allpasses = []
    maximum_delay = supriya.ugens.Rand.ir(0.1, 1)
    for output in source:
        for _ in range(3):
            output = supriya.ugens.AllpassC.ar(
                decay_time=supriya.ugens.LFDNoise3.kr(
                    frequency=supriya.ugens.ExpRand.ir(0.01, 0.1),
                    ).scale(-1, 1, 0.001, 1),
                delay_time=supriya.ugens.LFDNoise3.kr(
                    frequency=supriya.ugens.ExpRand.ir(0.01, 0.1),
                    ).scale(-1, 1, 0.001, 1) * maximum_delay,
                maximum_delay_time=maximum_delay,
                source=output,
                )
        allpasses.append(output)
    source = supriya.synthdefs.UGenArray(allpasses)
    source = supriya.ugens.LeakDC.ar(source=source)
    source = supriya.ugens.Limiter.ar(source=source)
    supriya.ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window,
        source=source * builder['level'],
        )
    supriya.ugens.LocalOut.ar(
        source=source * -0.9 * supriya.ugens.LFDNoise1.kr(frequency=0.1)
        )
    supriya.ugens.DetectSilence.kr(
        done_action=supriya.DoneAction.FREE_SYNTH,
        source=supriya.ugens.Mix.new(source),
        )

durated_allpass = builder.build()

### FREEVERB ###

with supriya.SynthDefBuilder(
    duration=3.0,
    level=1.0,
    out=0,
    damping=0.5,
    room_size=0.5,
    ) as builder:
    window = supriya.ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = supriya.ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source = supriya.ugens.FreeVerb.ar(
        source=source,
        damping=builder['damping'],
        room_size=builder['room_size'],
        mix=1.0,
        )
    source = supriya.ugens.LeakDC.ar(source=source)
    source = (source * 1.5).tanh()
    source = supriya.ugens.Limiter.ar(source=source)
    supriya.ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=source,
        )
    supriya.ugens.DetectSilence.kr(
        done_action=supriya.DoneAction.FREE_SYNTH,
        source=supriya.ugens.Mix.new(source),
        )

durated_freeverb = builder.build()

### PITCHSHIFT ###

with supriya.SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    pitch_shift=0.,
    pitch_dispersion=0,
    time_dispersion=0,
    window_size=0.5,
    ) as builder:
    window = supriya.ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = supriya.ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source += supriya.ugens.LocalIn.ar(channel_count=channel_count)
    source = supriya.ugens.PitchShift.ar(
        source=source,
        pitch_dispersion=builder['pitch_dispersion'],
        pitch_ratio=builder['pitch_shift'].semitones_to_ratio(),
        time_dispersion=builder['time_dispersion'] * builder['window_size'],
        window_size=builder['window_size'],
        )
    source = supriya.ugens.LeakDC.ar(source=source)
    source = (source * 1.5).tanh()
    source = supriya.ugens.Limiter.ar(source=source)
    supriya.ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=source,
        )
    supriya.ugens.LocalOut.ar(
        source=[
            source[1] * -0.9 * supriya.ugens.LFDNoise1.kr(frequency=0.1),
            source[0] * -0.9 * supriya.ugens.LFDNoise1.kr(frequency=0.1),
            ],
        )
    supriya.ugens.DetectSilence.kr(
        done_action=supriya.DoneAction.FREE_SYNTH,
        source=supriya.ugens.Mix.new(source),
        )

durated_pitchshift = builder.build()

### FREQSHIFT ###

with supriya.SynthDefBuilder(
    duration=1.0,
    level=1.0,
    out=0,
    ) as builder:
    window = supriya.ugens.Line.kr(
        done_action=2,
        duration=builder['duration'],
        ).hanning_window()
    source = supriya.ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source = supriya.ugens.FreqShift.ar(
        source=source,
        frequency=supriya.ugens.LFDNoise3.kr(frequency=0.01) * 2000,
        phase=supriya.ugens.LFNoise2.kr(frequency=0.01),
        )
    source = supriya.ugens.LeakDC.ar(source=source)
    source = (source * 1.5).tanh()
    source = supriya.ugens.Limiter.ar(source=source)
    supriya.ugens.XOut.ar(
        bus=builder['out'],
        crossfade=window * builder['level'],
        source=source,
        )
    supriya.ugens.DetectSilence.kr(
        done_action=supriya.DoneAction.FREE_SYNTH,
        source=supriya.ugens.Mix.new(source),
        )

durated_freqshift = builder.build()

### LIMITER ###

with supriya.SynthDefBuilder(
    out=0,
    ) as builder:
    source = supriya.ugens.In.ar(
        bus=builder['out'],
        channel_count=channel_count,
        )
    source = supriya.ugens.LeakDC.ar(source=source)
    source = supriya.ugens.Limiter.ar(source=source)
    supriya.ugens.ReplaceOut.ar(
        bus=builder['out'],
        source=source,
        )

limiter = builder.build()

### MULTIBAND COMPRESSOR ###

with supriya.SynthDefBuilder(
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
    source = supriya.ugens.In.ar(
        bus=builder['in_'],
        channel_count=channel_count,
        )
    band_1 = supriya.ugens.LPF.ar(
        frequency=builder['frequency_1'],
        source=source,
        )
    band_4 = supriya.ugens.HPF.ar(
        frequency=builder['frequency_3'],
        source=source,
        )
    center = source - band_1 - band_4
    band_2 = supriya.ugens.LPF.ar(
        frequency=builder['frequency_2'],
        source=center,
        )
    band_3 = supriya.ugens.HPF.ar(
        frequency=builder['frequency_2'],
        source=center,
        )
    band_1 = supriya.ugens.CompanderD.ar(
        clamp_time=builder['band_1_clamp_time'],
        relax_time=builder['band_1_relax_time'],
        slope_above=builder['band_1_slope_above'],
        slope_below=builder['band_1_slope_below'],
        source=band_1 * builder['band_1_pregain'].db_to_amplitude(),
        threshold=builder['band_1_threshold'].db_to_amplitude(),
        )
    band_2 = supriya.ugens.CompanderD.ar(
        clamp_time=builder['band_2_clamp_time'],
        relax_time=builder['band_2_relax_time'],
        slope_above=builder['band_2_slope_above'],
        slope_below=builder['band_2_slope_below'],
        source=band_2 * builder['band_2_pregain'].db_to_amplitude(),
        threshold=builder['band_2_threshold'].db_to_amplitude(),
        )
    band_3 = supriya.ugens.CompanderD.ar(
        clamp_time=builder['band_3_clamp_time'],
        relax_time=builder['band_3_relax_time'],
        slope_above=builder['band_3_slope_above'],
        slope_below=builder['band_3_slope_below'],
        source=band_3 * builder['band_3_pregain'].db_to_amplitude(),
        threshold=builder['band_3_threshold'].db_to_amplitude(),
        )
    band_4 = supriya.ugens.CompanderD.ar(
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
    source = supriya.ugens.Sum4.new(
        input_one=band_1,
        input_two=band_2,
        input_three=band_3,
        input_four=band_4,
        )
    supriya.ugens.ReplaceOut.ar(bus=builder['out'], source=source)

multiband_compressor = builder.build()

### WARP BUFFER PLAYER ###

with supriya.SynthDefBuilder(
    buffer_id=0,
    gain=0,
    out=0,
    overlaps=32,
    pan=0,
    rate=1,
    transpose=0,
    window_size=0.5,
    ) as builder:
    line = supriya.ugens.Line.kr(
        done_action=2,
        duration=supriya.ugens.BufDur.kr(builder['buffer_id']) * builder['rate'],
        )
    window = line.hanning_window()
    pointer_scrub = supriya.ugens.LFNoise2.kr(
        frequency=[0.01, 0.01],
        ) * window * 0.1
    warps = supriya.ugens.Warp1.ar(
        buffer_id=builder['buffer_id'],
        channel_count=1,
        frequency_scaling=builder['transpose'].semitones_to_ratio(),
        interpolation=2,
        overlaps=builder['overlaps'].as_int(),
        pointer=line + pointer_scrub,
        window_rand_ratio=0.001,
        window_size=supriya.ugens.LFNoise2.kr(
            frequency=0.01,
            ).scale(-1, 1, 0.125, 0.375),
        )
    source = supriya.ugens.XFade2.ar(
        in_a=supriya.ugens.Pan2.ar(
            source=warps[0],
            position=supriya.ugens.LFNoise2.kr(frequency=0.05),
            ),
        in_b=supriya.ugens.Pan2.ar(
            source=warps[1],
            position=supriya.ugens.LFNoise2.kr(frequency=0.05),
            ),
        pan=supriya.ugens.LFNoise2.kr(frequency=0.05),
        )
    source = supriya.ugens.PanAz.ar(
        channel_count=channel_count,
        amplitude=1,
        orientation=0.5,
        position=builder['pan'],
        source=source,
        width=2,
        )
    source = source * window * builder['gain'].db_to_amplitude()
    supriya.ugens.Out.ar(
        bus=builder['out'],
        source=source,
        )

warp_buffer_player_synthdef = builder.build()
