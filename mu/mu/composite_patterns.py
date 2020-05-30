import supriya
from mu.patterns import (
    part_1_bufnoise_pattern_1,
    part_1_bufnoise_pattern_2,
    part_2_bufnoise_pattern_1,
    part_2_bufnoise_pattern_2,
    part_3_bufnoise_pattern_1,
    part_3_bufnoise_pattern_2,
    allpass_pattern,
    freqshift_pattern,
    freeverb_pattern,
    chorus_pattern,
    pitchshift_pattern,
    part_1_warp_buffer_player_pattern_1,
    part_1_warp_buffer_player_pattern_2,
    part_1_warp_buffer_player_pattern_3,
    part_1_warp_buffer_player_pattern_4,
    part_1_warp_buffer_player_pattern_5,
    part_1_warp_buffer_player_pattern_6,
    part_2_warp_buffer_player_pattern_1,
    part_2_warp_buffer_player_pattern_2,
    part_2_warp_buffer_player_pattern_3,
    part_2_warp_buffer_player_pattern_4,
    part_2_warp_buffer_player_pattern_5,
    part_2_warp_buffer_player_pattern_6,
    part_3_warp_buffer_player_pattern_1,
    part_3_warp_buffer_player_pattern_2,
    part_3_warp_buffer_player_pattern_3,
    part_3_warp_buffer_player_pattern_4,
    part_3_warp_buffer_player_pattern_5,
    part_3_warp_buffer_player_pattern_6,
    )


### PART 1 ###

part_1_pattern_0 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_1_bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_1_pattern_1 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_1_warp_buffer_player_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_1_pattern_2 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_1_warp_buffer_player_pattern_2,
        part_1_bufnoise_pattern_2,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_1_pattern_3 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_1_warp_buffer_player_pattern_3,
        part_1_bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_1_pattern_4 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_1_warp_buffer_player_pattern_4,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_1_pattern_5 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_1_warp_buffer_player_pattern_5,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_1_pattern_6 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_1_warp_buffer_player_pattern_6,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

### PART 2 ###

part_2_pattern_0 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_2_bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_2_pattern_1 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_2_warp_buffer_player_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_2_pattern_2 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_2_warp_buffer_player_pattern_2,
        part_2_bufnoise_pattern_2,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_2_pattern_3 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_2_warp_buffer_player_pattern_3,
        part_2_bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_2_pattern_4 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_2_warp_buffer_player_pattern_4,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_2_pattern_5 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_2_warp_buffer_player_pattern_5,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_2_pattern_6 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_2_warp_buffer_player_pattern_6,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

### PART 3 ###

part_3_pattern_0 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_3_bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_3_pattern_1 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_3_warp_buffer_player_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_3_pattern_2 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_3_warp_buffer_player_pattern_2,
        part_3_bufnoise_pattern_2,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_3_pattern_3 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_3_warp_buffer_player_pattern_3,
        part_3_bufnoise_pattern_1,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_3_pattern_4 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_3_warp_buffer_player_pattern_4,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_3_pattern_5 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_3_warp_buffer_player_pattern_5,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )

part_3_pattern_6 = supriya.patterns.Pbus(
    supriya.patterns.Ppar([
        part_3_warp_buffer_player_pattern_6,
        allpass_pattern,
        freqshift_pattern,
        freeverb_pattern,
        chorus_pattern,
        pitchshift_pattern,
        ]),
    release_time=30.0,
    )
