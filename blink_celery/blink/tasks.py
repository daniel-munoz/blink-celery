import io
import uu
from .. import app
from .utils import connect


@app.task
def list_videos():
    b = connect()
    return b.videos()


@app.task
def get_video_content(address):
    b = connect()
    content = b.download_video_by_address(address)
    out = io.BytesIO()
    uu.encode(io.BytesIO(content), out, name='address')
    return out.getvalue().decode('ascii')
