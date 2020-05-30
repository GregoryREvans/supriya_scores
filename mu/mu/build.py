import supriya
from mu.session_setup import session
from mu.synth_defs import (
    multiband_compressor,
    limiter,
    )
from mu.composite_patterns import (
    part_1_pattern_0,
    part_1_pattern_1,
    part_1_pattern_2,
    part_1_pattern_3,
    part_1_pattern_4,
    part_1_pattern_5,
    part_1_pattern_6,
    part_2_pattern_0,
    part_2_pattern_1,
    part_2_pattern_2,
    part_2_pattern_3,
    part_2_pattern_4,
    part_2_pattern_5,
    part_2_pattern_6,
    part_3_pattern_0,
    part_3_pattern_1,
    part_3_pattern_2,
    part_3_pattern_3,
    part_3_pattern_4,
    part_3_pattern_5,
    part_3_pattern_6,
    )

### PART 1 ###
with session.at(0):
    for i in range(5):
        session.inscribe(part_1_pattern_0, duration=180, seed=(i+4))
    session.add_synth(
        add_action=supriya.AddAction.ADD_TO_TAIL,
        synthdef=multiband_compressor,
        )
    session.add_synth(
        add_action=supriya.AddAction.ADD_TO_TAIL,
        synthdef=limiter,
        )

with session.at(0):
    for i in range(6):
        session.inscribe(part_1_pattern_1, duration=240, seed=(i+5))

with session.at(215):
    for i in range(7):
        session.inscribe(part_1_pattern_2, duration=360, seed=(i+6))

with session.at(570):
    for i in range(6):
        session.inscribe(part_1_pattern_3, duration=300, seed=(i+7))

with session.at(867):
    for i in range(5):
        session.inscribe(part_1_pattern_4, duration=420, seed=(i+8))

with session.at(1285):
    for i in range(4):
        session.inscribe(part_1_pattern_5, duration=120, seed=(i+9))

with session.at(1400):
    for i in range(3):
        session.inscribe(part_1_pattern_6, duration=180, seed=(i+10))

### PART 2 ###
with session.at(1450):
    for i in range(2):
        session.inscribe(part_2_pattern_6, duration=240, seed=(i+11))

with session.at(1450):
    for i in range(3):
        session.inscribe(part_2_pattern_5, duration=300, seed=(i+12))

with session.at(1695):
    for i in range(4):
        session.inscribe(part_2_pattern_4, duration=395, seed=(i+13))

with session.at(2055):
    for i in range(3):
        session.inscribe(part_2_pattern_3, duration=320, seed=(i+14))

with session.at(2337):
    for i in range(4):
        session.inscribe(part_2_pattern_2, duration=455, seed=(i+15))

with session.at(2775):
    for i in range(5):
        session.inscribe(part_2_pattern_1, duration=132, seed=(i+16))

with session.at(2800):
    for i in range(6):
        session.inscribe(part_2_pattern_0, duration=286, seed=(i+17))

### PART 3 ###
with session.at(3000):
    for i in range(7):
        session.inscribe(part_3_pattern_0, duration=180, seed=(i+18))

with session.at(3000):
    for i in range(6):
        session.inscribe(part_3_pattern_1, duration=240, seed=(i+19))

with session.at(3215):
    for i in range(5):
        session.inscribe(part_3_pattern_2, duration=360, seed=(i+20))

with session.at(3570):
    for i in range(6):
        session.inscribe(part_3_pattern_3, duration=300, seed=(i+21))

with session.at(3867):
    for i in range(5):
        session.inscribe(part_3_pattern_4, duration=420, seed=(i+22))

with session.at(4285):
    for i in range(4):
        session.inscribe(part_3_pattern_5, duration=120, seed=(i+23))

with session.at(4400):
    for i in range(3):
        session.inscribe(part_3_pattern_6, duration=180, seed=(i+24))

supriya.render(session, output_file_path='/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/renders/mu.aiff', memory_size=8192 * 16)
