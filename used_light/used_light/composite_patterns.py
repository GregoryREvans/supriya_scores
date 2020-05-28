import supriya
from used_light.patterns import (
    bufnoise_pattern_1,
    bufnoise_pattern_2,
    allpass_pattern,
    freqshift_pattern,
    freeverb_pattern,
    chorus_pattern,
    pitchshift_pattern,
    warp_buffer_player_pattern_1,
    warp_buffer_player_pattern_2,
    warp_buffer_player_pattern_3,
    warp_buffer_player_pattern_4,
    warp_buffer_player_pattern_5,
    warp_buffer_player_pattern_6,
    )


pattern_0 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

pattern_1 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        warp_buffer_player_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

pattern_2 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        warp_buffer_player_pattern_2,
        bufnoise_pattern_2,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

pattern_3 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        warp_buffer_player_pattern_3,
        bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

pattern_4 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        warp_buffer_player_pattern_4,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

pattern_5 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        warp_buffer_player_pattern_5,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

pattern_6 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        warp_buffer_player_pattern_6,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )
