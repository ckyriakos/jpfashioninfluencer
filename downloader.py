from pytube import YouTube
import os

def download_youtube_video(url, output_path="videos", filename=None, resolution="720p"):
    yt = YouTube(url)
    
    # Filter progressive streams (video + audio) and choose resolution
    stream = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()
    
    if not stream:
        print(f"No {resolution} stream available. Trying highest resolution instead.")
        stream = yt.streams.get_highest_resolution()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Set filename or default to video title
    filename = filename or yt.title.replace(" ", "_").replace("/", "_") + ".mp4"

    print(f"Downloading: {yt.title} to {output_path}/{filename}")
    stream.download(output_path=output_path, filename=filename)

    return os.path.join(output_path, filename)

# Example usage
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=your_video_id"
    download_youtube_video(video_url)

