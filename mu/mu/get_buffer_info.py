import supriya
import os


server = supriya.Server.default().boot()

file_paths = []
frames = []

directory = '/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files'
folders = os.listdir(directory)
for folder in folders:
    if folder == ".DS_Store":
        continue
    else:
        folder_name = '/Users/evansdsg2/supercollider_scores/supriya_scores/mu/mu/buffer_files/' + folder
        files = os.listdir(folder_name)
        for file in files:
            name = folder_name + "/" + file
            if file == ".DS_Store":
                continue
            else:
                file_paths.append(name)
                buffer_one = supriya.realtime.Buffer().allocate_from_file(
                    name
                    )
                frames.append(buffer_one.frame_count)
                buffer_one.free()

pairs = [(x, y) for x, y in zip(file_paths, frames)]
print(pairs)

server.quit()
