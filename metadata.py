import json
import os

def generate_metadata(video_path: str, frame_dir: str, output_file: str, frame_rate: int):
    metadata = {}
    video_name = os.path.basename(video_path)
    frames = sorted(f for f in os.listdir(frame_dir) if f.endswith(".png"))

    for i, frame in enumerate(frames):
        timestamp = i / frame_rate  # in seconds
        metadata[frame] = {
            "video": video_name,
            "timestamp_sec": round(timestamp, 2),
            "path": os.path.abspath(os.path.join(frame_dir, frame))
        }

    with open(output_file, "w") as f:
        json.dump(metadata, f, indent=2)

