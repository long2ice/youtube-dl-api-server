import logging

import youtube_dl
from fastapi import FastAPI
from starlette.requests import Request
from youtube_dl.version import __version__ as youtube_dl_version

import settings

api = FastAPI(
    title='API接口文档',
    debug=settings.DEBUG
)


@api.get('/info')
async def info(request: Request, url: str):
    ydl_params = {
        'format': 'best',
        'cachedir': False,
        'logger': logging.getLogger(__name__),
        'proxy': settings.PROXY
    }
    with youtube_dl.YoutubeDL(ydl_params) as ydl:
        result = ydl.extract_info(url, download=False)
    return {
        'url': url,
        'info': result
    }


@api.get('/version')
async def version():
    return {
        'youtube-dl': youtube_dl_version,
        'youtube-dl-api-server': settings.VERSION,
    }


@api.get('/extractors')
async def extractors():
    ie_list = [{
        'name': ie.IE_NAME,
        'working': ie.working(),
    } for ie in youtube_dl.gen_extractors()]
    return dict(extractors=ie_list)
