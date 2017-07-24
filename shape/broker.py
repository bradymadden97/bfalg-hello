# Copyright 2017, RadiantBlue Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib2 import urlopen
import urllib
import uuid
import io
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000


def get_image_from_url(url):
    u = url.rstrip("\"").lstrip("\"")
    fn = str(uuid.uuid4()) + "-" + url.split("/")[-1]
    urllib.urlretrieve(u, fn)
    img = Image.open(fn)
    img_size = img.size
    return fn, img_size


def get_image_from_file(filename):
    img = Image.open(filename)
    img_size = img.size
    return filename, img_size
