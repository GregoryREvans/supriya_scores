import supriya
import os
from mu.session_setup import session

###

wolf_paths = [
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/bark.wav', 1044416),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/fox_bark.wav', 93892),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/fox_chirp.wav', 98816),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/fox_hiss.wav', 323585),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/fox_sex.wav', 1433250),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/jackal.wav', 27199),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/man.wav', 10510848),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/saw.wav', 837900),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/small_pack.wav', 7306561),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/1canines/wolf_pack.wav', 1468530),
    ]
wolves = []
with session.at(0):
    for pair in wolf_paths:
        buffer_ = session.add_buffer(channel_count=2, frame_count=pair[1], file_path=pair[0])
        wolves.append(buffer_)

###

tree_paths = [
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/aspen.wav', 5051330),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/branch.wav', 950272),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/crash.wav', 255669),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/creaking.wav', 326707),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/fall.wav', 199321),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/falling.wav', 418950),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/rain.wav', 3470063),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/rotten.wav', 326245),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/tree1.wav', 481281),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/tree_wind.wav', 3272704),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/treehouse.wav', 32289408),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/2trees/twig.wav', 912000),
     ]
trees = []
with session.at(0):
    for pair in tree_paths:
        buffer_ = session.add_buffer(channel_count=2, frame_count=pair[1], file_path=pair[0])
        trees.append(buffer_)

###

insect_paths = [
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/3bugs/bees.wav', 2583528),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/3bugs/bees2.wav', 12188222),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/3bugs/chirp.wav', 2023701),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/3bugs/chorus.wav', 2647216),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/3bugs/frogs.wav', 5328163),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/3bugs/frogs2.wav', 5613753),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/3bugs/night.wav', 2693602),
    ]
insects = []
with session.at(0):
    for pair in insect_paths:
        buffer_ = session.add_buffer(channel_count=2, frame_count=pair[1], file_path=pair[0])
        insects.append(buffer_)

###

paper_paths = [
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/4paper/crumple.wav', 538942),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/4paper/crumple_2.wav', 168133),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/4paper/drop.wav', 147840),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/4paper/flip.wav', 39488),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/4paper/rip.wav', 67275),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/4paper/rumple.wav', 516387),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/4paper/writing.wav', 560128),
    ]
paper = []
with session.at(0):
    for pair in paper_paths:
        buffer_ = session.add_buffer(channel_count=2, frame_count=pair[1], file_path=pair[0])
        paper.append(buffer_)

###

gear_paths = [
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/5gears/bad_clock.wav', 383029),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/5gears/clock.wav', 1148099),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/5gears/gear.wav', 469625),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/5gears/mechanism.wav', 984000),
    ('/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/5gears/water_gear.wav', 1937176),
    ]
gears = []
with session.at(0):
    for pair in gear_paths:
        buffer_ = session.add_buffer(channel_count=2, frame_count=pair[1], file_path=pair[0])
        gears.append(buffer_)

###

wolves_and_trees = wolves + trees
trees_and_insects = trees + insects
insects_and_paper = insects + paper
paper_and_gears = paper + gears
wolf_pack_howls = wolves[8]
