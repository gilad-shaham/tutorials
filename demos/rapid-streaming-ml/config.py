from os import getenv, path
import urllib.parse
import posixpath
import v3io.dataplane

V3IO_ACCESS_KEY = getenv('V3IO_ACCESS_KEY')
V3IO_USERNAME = getenv('V3IO_USERNAME')
CONTAINER = 'users'
PROJECT_NAME = 'rapid-streaming-ml'
DATA_PATH = path.join('demos', PROJECT_NAME, 'data')
ENDPOINT = 'http://v3io-webapi:8081'

STREAM_CONFIGS = {'generated-stream': {
                        'path': path.join(V3IO_USERNAME, DATA_PATH, 'generated-stream'),
                        'stream_url': urllib.parse.urljoin(ENDPOINT, posixpath.join('users', V3IO_USERNAME, DATA_PATH, 'generated-stream')),
                        'shard_count': 8},
                  'incoming-events-stream': {
                        'path': path.join(V3IO_USERNAME, DATA_PATH, 'incoming-events-stream'),
                        'stream_url': urllib.parse.urljoin(ENDPOINT, posixpath.join('users', V3IO_USERNAME, DATA_PATH, 'incoming-events-stream')),
                        'shard_count': 8
                  },
                  'enriched-events-stream': {
                        'path': path.join(V3IO_USERNAME, DATA_PATH, 'enriched-events-stream'),
                        'stream_url': urllib.parse.urljoin(ENDPOINT, posixpath.join('users', V3IO_USERNAME, DATA_PATH, 'enriched-events-stream')),
                        'shard_count': 8
                  },
                  'serving-stream': {
                        'path': path.join(V3IO_USERNAME, DATA_PATH, 'serving-stream'),
                        'stream_url': urllib.parse.urljoin(ENDPOINT, posixpath.join('users', V3IO_USERNAME, DATA_PATH, 'serving-stream')),
                        'shard_count': 8
                  },
                  'inference-stream': {
                        'path': path.join(V3IO_USERNAME, DATA_PATH, 'inference-stream'),
                        'stream_url': urllib.parse.urljoin(ENDPOINT, posixpath.join('users', V3IO_USERNAME, DATA_PATH, 'inference-stream')),
                        'shard_count': 8
                  }
                 }

v3io_client = v3io.dataplane.Client(endpoint=ENDPOINT, access_key=V3IO_ACCESS_KEY)

