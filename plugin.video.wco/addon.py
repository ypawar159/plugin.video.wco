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
        {"label": "Search", "path": plugin.url_for("search")},
        {"label": "Genres", "path": plugin.url_for("genre")},
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
    pass

# ToDO Create function to play video and point latest to that
@plugin.route("/last")
def last():
    animes = wco.get_latest()
    items = []
    for anime in animes:
        items.append({"label": anime["title"], "path": plugin.url_for("episodes", anime_url = anime["src"])})
    return items
    pass


@plugin.route("/cartoon")
def cartoon():
    pass


@plugin.route("/movie")
def movie():
    pass


@plugin.route("/ova")
def ova():
    pass


@plugin.route("/popular")
def popular():
    pass


@plugin.route("/todays")
def todays():
    pass


@plugin.route("/search")
def search():
    pass


@plugin.route("/genre")
def genre():
    pass


@plugin.route("/episodes/<anime_url>")
def episodes(anime_url):
    # plugin.log.info(anime_url)
    links = wco.get_episodes(anime_url)
    # plugin.log.info(links)


if __name__ == '__main__':
    plugin.run()
