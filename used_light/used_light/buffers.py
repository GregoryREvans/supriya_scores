import supriya
import os
from used_light.session_setup import session


frames = [
    441747,
    623450,
    470216,
    1321452,
    329144,
    348409,
    268083,
    472055,
    460499,
    905105,
    762703,
    1280343,
    476186,
    398297,
    1068087,
    335799,
    251906,
    815353,
    519797,
    328600,
    349635,
    376479,
    388664,
    302978,
    682105,
    645858,
    275857,
    287019,
    303441,
]

lights = []
directory = '/Users/evansdsg2/supercollider_scores/used_light/used_light/buffer_files'
files = os.listdir(directory)
for file, frame in zip(files, frames):
    name = '/Users/evansdsg2/supercollider_scores/used_light/used_light/buffer_files/' + file
    if file == ".DS_Store":
        continue
    else:
        lights.append((name, frame))

buffers = []
with session.at(0):
    for pair in lights:
        buffer_ = session.add_buffer(channel_count=1, frame_count=pair[1], file_path=pair[0])
        buffers.append(buffer_)
