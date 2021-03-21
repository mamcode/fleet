# Copyright 2021 - TODAY, Marcel Savegnago - Escodoo
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import re


def get_video_embed_code(video_url):
    """Computes the valid iframe from given URL that can be embedded
    (or False in case of invalid URL).
    """

    if not video_url:
        return False

    # To detect if we have a valid URL or not
    validURLRegex = (
        r"^(http:\/\/|https:\/\/|\/\/)[a-z0-9]+"
        r"([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"
    )

    # Regex for few of the widely used video hosting services
    ytRegex = (
        r"^(?:(?:https?:)?\/\/)?(?:www\.)?(?:youtu\.be\/|"
        r"youtube(-nocookie)?\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))"
        r"((?:\w|-){11})(?:\S+)?$"
    )
    vimeoRegex = r"\/\/(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*"
    dmRegex = r".+dailymotion.com\/(video|hub|embed)\/([^_?]+)[^#]*(#video=([^_&]+))?"
    igRegex = r"(.*)instagram.com\/p\/(.[a-zA-Z0-9]*)"
    ykuRegex = r"(.*).youku\.com\/(v_show\/id_|embed\/)(.+)"

    if not re.search(validURLRegex, video_url):
        return False
    else:
        embedUrl = False
        ytMatch = re.search(ytRegex, video_url)
        vimeoMatch = re.search(vimeoRegex, video_url)
        dmMatch = re.search(dmRegex, video_url)
        igMatch = re.search(igRegex, video_url)
        ykuMatch = re.search(ykuRegex, video_url)

        if ytMatch and len(ytMatch.groups()[1]) == 11:
            embedUrl = "//www.youtube{}.com/embed/{}?rel=0".format(
                ytMatch.groups()[0] or "",
                ytMatch.groups()[1],
            )
        elif vimeoMatch:
            embedUrl = "//player.vimeo.com/video/%s" % (vimeoMatch.groups()[2])
        elif dmMatch:
            embedUrl = "//www.dailymotion.com/embed/video/%s" % (dmMatch.groups()[1])
        elif igMatch:
            embedUrl = "//www.instagram.com/p/%s/embed/" % (igMatch.groups()[1])
        elif ykuMatch:
            ykuLink = ykuMatch.groups()[2]
            if ".html?" in ykuLink:
                ykuLink = ykuLink.split(".html?")[0]
            embedUrl = "//player.youku.com/embed/%s" % (ykuLink)
        else:
            # We directly use the provided URL as it is
            embedUrl = video_url
        return (
            '<iframe class="embed-responsive-item"'
            'src="%s" allowFullScreen="true" frameborder="0"></iframe>' % embedUrl
        )
