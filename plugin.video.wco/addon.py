from xbmcswift2 import Plugin
from resources.lib import wco_browser as wco

plugin = Plugin()


@plugin.route('/')
def index():
    menu = [
        {"label": "Dubbed Anime", "path": plugin.url_for("dub")},
        {"label": "Subbed Anime", "path": plugin.url_for("sub")},
        {"label": "Last 50 Recent Release", "path": plugin.url_for("last")},
        {"label": "Cartoons", "path": plugin.url_for("cartoon")},
        {"label": "Movies", "path": plugin.url_for("movie")},
        {"label": "OVA Series", "path": plugin.url_for("ova")},
        {"label": "Popular & Ongoing Series", "path": plugin.url_for("popular")},
        {"label": "Today's Anime List", "path": plugin.url_for("todays")},
        {"label": "Genres", "path": plugin.url_for("genre", gid='a')},
        {"label": "Search", "path": plugin.url_for("search")},
        {"label": "Addon Setting", "path": plugin.url_for("setting")},
    ]
    return menu
    pass


@plugin.route("/dub")
def dub():
    animes = wco.get_dub()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url=anime["src"])})
    return items
    pass


@plugin.route("/sub")
def sub():
    animes = wco.get_sub()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url=anime["src"])})
    return items
    pass


# ToDO Create function to play video and point latest to that
@plugin.route("/last")
def last():
    animes = wco.get_latest()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episode", episode_url=anime["src"])})
    return items
    pass


@plugin.route("/cartoon")
def cartoon():
    animes = wco.get_cartoon()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url=anime["src"])})
    return items
    pass


@plugin.route("/movie")
def movie():
    animes = wco.get_movie()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episode", episode_url=anime["src"])})
    return items
    pass


@plugin.route("/ova")
def ova():
    animes = wco.get_ova()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episode", episode_url=anime["src"])})
    return items
    pass


@plugin.route("/popular")
def popular():
    animes = wco.get_popular()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url=anime["src"])})
    return items
    pass


@plugin.route("/todays")
def todays():
    animes = wco.get_todays()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url=anime["src"])})
    return items
    pass


@plugin.route("/genre/<gid>")
def genre(gid):
    if gid == 'a':
        gid = None
    animes = wco.get_genres(gid)
    items = []
    for anime in animes:
        if gid:
            items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url=anime["src"])})
        else:
            items.append({"label": anime["title"], "path": plugin.url_for("genre", gid=anime["src"].split("/")[-1])})
    return items
    pass


@plugin.route("/search")
def search():
    keyword = plugin.keyboard()
    if keyword:
        animes = wco.search_anime(keyword)
        items = []
        for anime in animes:
            items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url=anime["src"])})
        return items
    pass


@plugin.route("/episodes/<anime_url>")
def episodes(anime_url):
    episode_list = wco.get_episodes(anime_url)
    items = []
    for epsd in episode_list:
        items.append({"label": epsd["title"], "path": plugin.url_for("episode", episode_url=epsd["src"])})
    return items


@plugin.route("/episode/<episode_url>")
def episode(episode_url):
    video_link = wco.get_episode(episode_url)
    if video_link:
        plugin.log.info(video_link)
        plugin.set_resolved_url(video_link)
    pass


@plugin.route("/setting")
def setting():
    plugin.open_settings()


if __name__ == '__main__':
    plugin.run()
