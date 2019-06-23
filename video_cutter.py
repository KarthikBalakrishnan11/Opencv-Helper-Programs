from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ffmpeg_extract_subclip("sample.mp4", 1320, 1440, targetname="cut.mp4")