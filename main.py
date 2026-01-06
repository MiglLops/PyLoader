import instaloader, os
from pytubefix import YouTube # https://www.youtube.com/watch?v=dQw4w9WgXcQ  # https://youtu.be/VlCJUjEoT44?si=0RlOCcQCdW805qWH   # https://youtube.com/playlist?list=PLTP0-W-US2Svy_jW2V61s6RhDXioHJrSu
from pytubefix.cli import on_progress, Playlist  # https://www.instagram.com/reel/DOqLVVVCnIQ/?id=3722837886497354256_48594204151

n = 0
substring_ig, substring_pl = "instagram", "playlist"
substring_yt = "youtu"
lista_titulo, lista_url = [], []

L = instaloader.Instaloader(
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    post_metadata_txt_pattern="",
    download_video_thumbnails=False
)

def lista():
    global n
    if playlist == True:
        lista_titulo.append(pl.title)
    elif youtube == True:
        lista_titulo.append(yt.title)
    elif instagram == True:
        n += 1
        lista_titulo.append(f"Instagram video n° {n}")
    lista_url.append(url)


def download():
    global url
    os.system('cls')
    lista()
    link = "https://"
    print(f"Titulo dos videos/playlist >> {lista_titulo}"); print(f"URL dos videos >> {lista_url}")
    print("Voce pode inserir mais url`s")
    print("Digite o numero da forma de download:")
    print("1 - MP3    2 - MP4")
    escolha = input("> ")
    if link in escolha: # + urls
        url = escolha
        config()
    elif escolha == "1": # audio
        for i in lista_url:
            if substring_ig in i:
                shortcode = url.split("/")[-2]
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                print("...")
                L.download_post(post, target="Downloads instaloader")

            elif substring_pl in i:
                for video in pl.videos:
                    video.streams.get_audio_only().download()
                    print(f"{video.title} | ok\n")

            elif substring_yt in i:
                video = YouTube(i, on_progress_callback=on_progress)
                video.streams.get_audio_only().download()
                try:
                    print(f"{video.title} | ok \n")
                except:
                    print(f"{yt.title} | ok \n")   

    elif escolha == "2": # video
        for i in lista_url:
            if substring_ig in i:
                shortcode = url.split("/")[-2]
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                print("...")
                L.download_post(post, target="Downloads instaloader")

            if substring_pl in i:
                for video in pl.videos:
                    video.streams.get_highest_resolution().download()
                    print(f"{video.title} | ok\n")

            elif substring_yt in i:
                video = YouTube(i, on_progress_callback=on_progress)
                video.streams.get_highest_resolution().download()
                try:
                    print(f"{video.title} | ok \n")
                except:
                    print(f"{yt.title} | ok \n")   

def config():
    global url, yt, substring_yt, substring_pl, substring_pl, youtube, instagram, playlist, pl
    youtube, playlist, instagram = False, False, False

    if substring_pl in url:
        playlist = True
        pl = Playlist(url)
        download()
    elif substring_yt in url:
        youtube = True
        yt = YouTube(url)
        download()
    elif substring_ig in url:
        instagram = True
        print("ig")
        download()
    else:
        print("insira uma url correta.")
        url = input("URL > ")
        config()

url = input("URL > ")
config()