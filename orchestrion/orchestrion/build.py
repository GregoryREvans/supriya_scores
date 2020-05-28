import supriya
from orchestrion.session_setup import session
from orchestrion.synth_defs import (
    multiband_compressor,
    limiter,
    )
from orchestrion.composite_patterns import (
    pattern_0,
    pattern_1,
    pattern_2,
    pattern_3,
    pattern_4,
    pattern_5,
    pattern_6,
    )

with session.at(0):
    for i in range(5):
        session.inscribe(pattern_0, duration=60 * 3, seed=(i+2))
    session.add_synth(
        add_action=supriya.AddAction.ADD_TO_TAIL,
        synthdef=multiband_compressor,
        )
    session.add_synth(
        add_action=supriya.AddAction.ADD_TO_TAIL,
        synthdef=limiter,
        )

with session.at(0):
    for i in range(4):
        session.inscribe(pattern_1, duration=60 * 4, seed=(i+2))
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=multiband_compressor,
    #     )
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=limiter,
    #     )

with session.at(215):
    for i in range(5):
        session.inscribe(pattern_2, duration=60 * 6, seed=(i+2))
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=multiband_compressor,
    #     )
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=limiter,
    #     )

with session.at(570):
    for i in range(2):
        session.inscribe(pattern_3, duration=60 * 5, seed=(i+2))
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=multiband_compressor,
    #     )
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=limiter,
    #     )

with session.at(867):
    for i in range(3):
        session.inscribe(pattern_4, duration=60 * 7, seed=(i+2))
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=multiband_compressor,
    #     )
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=limiter,
    #     )

with session.at(1285):
    for i in range(4):
        session.inscribe(pattern_5, duration=60 * 2, seed=(i+2))
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=multiband_compressor,
    #     )
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=limiter,
    #     )

with session.at(1400):
    for i in range(3):
        session.inscribe(pattern_6, duration=60 * 3, seed=(i+2))
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=multiband_compressor,
    #     )
    # session.add_synth(
    #     add_action=AddAction.ADD_TO_TAIL,
    #     synthdef=limiter,
    #     )

supriya.render(session, output_file_path='/Users/evansdsg2/supercollider_scores/orchestrion/orchestrion/renders', memory_size=8192 * 16)
