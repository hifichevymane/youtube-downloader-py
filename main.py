import os
import utils

def main():
    # Downloading video
    download_option = int(input('What do you wanna download? 1 - only video, 2 - audio from video, 3 - video and audio: '))
    video_url = input('Enter youtube video url: ')

    try:
        # Creating all needed folders
        DOWNLOADS_FOLDER = 'downloads'

        if not os.path.exists(DOWNLOADS_FOLDER):
            os.makedirs(DOWNLOADS_FOLDER)

        # If we download a playlist
        if 'playlist?' in video_url:
            utils.download_playlist(video_url, DOWNLOADS_FOLDER, download_option=download_option)

        else:
            path = utils.download_video(video_url, DOWNLOADS_FOLDER)

        # If we wanna download mp3        
        if download_option == 2:
            utils.convert_mp4_to_mp3(path_to_video=path[0], name_of_file=path[1], delete_video=True)

        elif download_option == 3:
            utils.convert_mp4_to_mp3(path_to_video=path[0], name_of_file=path[1])

    except Exception as e:
        print("We couldn't download the video", str(e))


if __name__ == '__main__':
    main()
    print("Congrats! You've downloaded a file!")
