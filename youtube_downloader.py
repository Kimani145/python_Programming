
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_youtube_video():
    url = input("Enter the YouTube video URL: ").strip()
    format_choice = input("Download as (1) MP3 or (2) MP4? Enter 1 or 2: ").strip()

    try:
        yt = YouTube(url)
        print(f"\nVideo Title: {yt.title}")
        
        # For MP4 (Video)
        if format_choice == '2':
            print("Downloading MP4 video...")
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
            video_stream.download()
            print("Download complete.")

        # For MP3 (Audio)
        elif format_choice == '1':
            print("Downloading audio stream...")
            audio_stream = yt.streams.filter(only_audio=True).first()
            output_file = audio_stream.download(filename="temp_audio.mp4")

            mp3_file = yt.title.replace(" ", "_").replace("|", "").replace("/", "_") + ".mp3"
            audio_clip = AudioFileClip(output_file)
            audio_clip.write_audiofile(mp3_file)
            audio_clip.close()

            os.remove(output_file)  # Clean up the temporary file
            print(f"MP3 saved as: {mp3_file}")

        else:
            print("Invalid option. Please enter 1 or 2.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
