from pytube import YouTube, Playlist
import os
import subprocess
from random import randint

# Download video
def download_video(url: str, folder_to_download: str):
    yt = YouTube(url)

    video = yt.streams.get_highest_resolution()

    video_title = f'youtube-downloader-py_{randint(1, 100000)}'
    output_folder = os.path.join(folder_to_download, video_title)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Downloading
    video.download(output_path=output_folder, filename=f'{video_title}.mp4')

    return [output_folder, video_title]


# Converting a mp4 to mp3
def convert_mp4_to_mp3(path_to_video, name_of_file, delete_video=False):
    # Convert mp4 to mp3
    mp4_file = os.path.join(path_to_video, f'{name_of_file}.mp4')
    mp3_file = os.path.join(path_to_video, f'{name_of_file}.mp3')

    cmd = f'ffmpeg -i "{mp4_file}" -vn -ab 320k "{mp3_file}"'

    subprocess.call(cmd, shell=True)

    if delete_video:
        os.remove(mp4_file)


# Download playlist
def download_playlist(url: str, folder_to_download: str, download_option=1):
    playlist = Playlist(url)

    playlist_folder = os.path.join(folder_to_download, 'playlists')
    folder_name = 'playlist ' + str(randint(100000, 1000000))
    output_folder = os.path.join(playlist_folder, folder_name)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    count_videos = 1

    if download_option == 1:
        for video in playlist.videos:
            playlist_video = video.streams.get_highest_resolution()
            playlist_video.download(output_path=output_folder)
            print(f'Video {count_videos} has been downloaded!')
            count_videos += 1

    elif download_option == 2:
        for video in playlist.videos:
            playlist_video = video.streams.get_highest_resolution()

            video_title = video.title

            playlist_video.download(output_path=output_folder)
            convert_mp4_to_mp3(output_folder, video_title)
            
            print(f'Video {count_videos} has been downloaded!')
            count_videos += 1
