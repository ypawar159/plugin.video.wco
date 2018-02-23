from xbmcswift2 import Plugin
from resources.lib import wco_browser as wco

plugin = Plugin()


@plugin.route('/')
def index():
    wco.get_latest()
    item = {
        'label': 'Hello XBMC!',
        'path': 'http://s3.amazonaws.com/KA-youtube-converted/JwO_25S_eWE.mp4/JwO_25S_eWE.mp4',
        'is_playable': True
    }
    return [item]


if __name__ == '__main__':
    plugin.run()
