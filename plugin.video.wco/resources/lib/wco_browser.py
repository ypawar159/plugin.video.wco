import requests
from bs4 import BeautifulSoup as bs
from xbmcswift2 import plugin
import re
import base64

_base_url = "https://www.watchcartoononline.io"
last_50_url = "/last-50-recent-release"
_dubbed_anime_url = "/dubbed-anime-list"
_subbed_anime_url = "/subbed-anime-list"
_cartoons_url = "/cartoon-list"
_movies_url = "/movie-list"
_ova_series_url = "/ova-list"
_search_url = "/search"
_search_genre_url = "/search-by-genre"


def get_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return None
    except Exception as e:
        # TODO: log errors to kodi logs
        # print(e)
        plugin.log.error(e)


def post_url(url, data):
    try:
        r = requests.post(url, data)
        # print r.text
        if r.status_code == 200:
            return r.text
        else:
            return None
    except Exception as e:
        # TODO: log errors to kodi logs
        # print(e)
        plugin.log.error(e)


def get_latest():
    url = _base_url + last_50_url
    print(url)
    r = get_url(url)
    anime_list = []
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find("div", class_="menulaststyle")
        # print(animes)
        urls = animes.find_all('a')
        for url in urls:
            # print urls[0]["href"]
            # print(urls[0].text.strip())
            anime_list.append({"src": url["href"], "title": url.text.strip()})
        return anime_list


def get_dub():
    url = _base_url + _dubbed_anime_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find("div", id="ddmcc_container")
        # print(animes)
        urls = animes.find_all('a')
        anime_list = []
        for url in urls:
            if url.has_attr("href"):
                # print url["href"], url.text
                anime_list.append({"src": url["href"], "title": url.text.strip()})
        return anime_list


def get_sub():
    url = _base_url + _subbed_anime_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find("div", id="ddmcc_container")
        # print(animes)
        urls = animes.find_all('a')
        for url in urls:
            if url.has_attr("href"):
                print url["href"], url.text


def get_cartoon():
    url = _base_url + _cartoons_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find("div", id="ddmcc_container")
        # print(animes)
        urls = animes.find_all('a')
        for url in urls:
            if url.has_attr("href"):
                print url["href"], url.text


def get_movie():
    url = _base_url + _movies_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find("div", id="ddmcc_container")
        # print(animes)
        urls = animes.find_all('a')
        for url in urls:
            if url.has_attr("href"):
                print url["href"], url.text


def get_ova():
    url = _base_url + _ova_series_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find("div", id="ddmcc_container")
        # print(animes)
        urls = animes.find_all('a')
        for url in urls:
            if url.has_attr("href"):
                print url["href"], url.text


def get_popular():
    url = _base_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find_all("div", class_="menustyle")[1]
        urls = animes.find_all('a')
        for url in urls:
            if url.has_attr("href"):
                print url["href"], url.text


def get_todays():
    url = _base_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find_all("div", class_="menustyle")[0]
        urls = animes.find_all('a')
        for url in urls:
            if url.has_attr("href"):
                print url["href"], url.text


def search_anime(query):
    url = _base_url + _search_url
    print(url)
    data = {'catara': query, 'konuara': 'series'}
    r = post_url(url, data)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find_all("div", class_="iccerceve")
        for anime in animes:
            print(anime.find_all("a")[-1])


def get_genres():
    url = _base_url + _search_genre_url
    print(url)
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        animes = sp.find("div", id="ddmcc_container")
        # print(animes)
        urls = animes.find_all('a')
        for url in urls:
            if url.has_attr("href"):
                print url["href"], url.text


def get_episodes(url):
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        episodes = sp.find("div", id="catlist-listview")
        urls = episodes.find_all("a")
        episodes_list = []
        for url in urls:
            if url.has_attr("href"):
                # print url["href"], url.text
                episodes_list.append({"src": url["href"], "title": url.text})
        return episodes_list


def get_episode(url):
    r = get_url(url)
    if r:
        sp = bs(r, 'html.parser')
        script_blocks = sp.find_all("script")
        for i, script in enumerate(script_blocks):
            if "decodeURIComponent" in script.text:
                # print i, script
                s = script.text
                start = s.find("[") + 1
                end = s.find("]")
                # print(start)
                # print(end)
                encoded_data = s[start:end]
                encoded_data = encoded_data.replace('"', "").split(",")
                # Remove all non-digit characters
                value = int(re.sub("\D", "", s[end:]))
                # print(encoded_data)
                # print(value)
                doc = ""
                for d in encoded_data:
                    doc += chr(int(re.sub("\D", "", base64.b64decode(d))) - value)
                # print(doc)
                video_sources = _base_url + doc.split(" ")[2][5:-1]
                # print video_sources
                r = get_url(video_sources)
                if r:
                    #     sp = bs(r, 'html.parser')
                    #     script_blocks = sp.find_all("script")
                    #     for script in script_blocks:
                    #         if "file" in script.text:
                    #             print(script)
                    sources = url = re.findall(r'file:.*?"(.*?)"', r)
                    # print(sources)
                    # break
                    return sources[0]
    return None


if __name__ == "__main__":
    # print get_latest()
    print get_dub()
    # get_sub()
    # get_cartoon()
    # get_movie()
    # get_ova()
    # get_popular()
    # get_todays()
    # search_anime("naruto")
    # get_genres()
    # print get_episodes("https://www.watchcartoononline.io/anime/6teen")
    # print(get_episode("https://www.watchcartoononline.io/6teen-season-4-episode-13-bye-bye-nikki-part-2"))
    pass
