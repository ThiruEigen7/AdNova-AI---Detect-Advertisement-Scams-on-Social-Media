import instaloader
from PIL import Image
import requests as re
import io


def url_loader(url):
    ig = instaloader.Instaloader()
    pst = instaloader.Post.from_shortcode(ig.context, url.split("/")[-2])
    img_url = pst.url
    r = re.get(img_url,stream=True)
    img = Image.open(io.BytesIO((r.content)))
    lks = pst.likes
    cmts1 = pst.comments
    user = pst.owner_username
    caption = pst.caption
    
    return [user , img, lks, cmts1, caption]


