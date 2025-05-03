
import subprocess
import os

def extract_frames(video_path: str, frame_rate: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    output_pattern = os.path.join(output_dir, "frame_%04d.png")
    subprocess.run([
        "ffmpeg", "-i", video_path, "-r", frame_rate, output_pattern
    ], check=True)

