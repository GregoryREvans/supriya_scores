import supriya
import os
from orchestrion.session_setup import session


frames = [
    3749028,
    3329550,
    6108539,
    6712548,
    3007665,
]

lights = []
directory = '/Users/evansdsg2/supercollider_scores/orchestrion/orchestrion/buffer_files'
files = os.listdir(directory)
for file, frame in zip(files, frames):
    name = '/Users/evansdsg2/supercollider_scores/orchestrion/orchestrion/buffer_files/' + file
    if file == ".DS_Store":
        continue
    else:
        lights.append((name, frame))

buffers = []
with session.at(0):
    for pair in lights:
        buffer_ = session.add_buffer(channel_count=2, frame_count=pair[1], file_path=pair[0])
        buffers.append(buffer_)
