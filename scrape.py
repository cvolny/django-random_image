import fileinput
import codecs
import json
import os
import re
import sys
from collections import defaultdict
from urllib import request, parse


if "__main__" == __name__:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")
import django
from random_image.models import Image


reader = codecs.getreader("utf-8")


def build_api_query(dicts, glue):
    """
    Build a query dict from collection of dicts with values joined on glue
    """
    q = defaultdict(list)
    for d in dicts:
        for k, v in d.items():
            q[k].append(v)
    return {k: glue.join(v) for k, v in q.items()}


def query_mediawiki(apiurl, link):
    title = link.split('/')[-1]
    glue = "|"
    headers = {'Content-Type': 'application/json'}
    base_query = {'action': 'query', 'continue': '', 'format': 'json'}
    ex_query = {'prop': 'extracts', 'exintro': '', 'explaintext': ''}
    pi_query = {'prop': 'pageimages', 'piprop': 'name'}
    ii_query = {'prop': 'imageinfo', 'iiprop': 'url'}

    query_data = build_api_query([ex_query, pi_query], glue)
    query_data.update(base_query)
    query_data.update({'titles': title})
    query_url = "{}?{}".format(apiurl, parse.urlencode(query_data))
    print(query_url, file=sys.stderr)
    response = request.urlopen(request.Request(query_url, headers=headers))
    data = json.load(reader(response))

    pages = data["query"]["pages"]
    for key, page in pages.items():
        title = page["title"]
        body = "".join(re.split("([!?\.]) ", page["extract"], maxsplit=1)[:2])
        pageimage = page["pageimage"]
        break

    if pageimage:
        query_data = ii_query
        query_data.update(base_query)
        query_data.update({'titles': "File:{}".format(pageimage)})
        query_url = "{}?{}".format(apiurl, parse.urlencode(query_data))
        print(query_url, file=sys.stderr)
        response = request.urlopen(request.Request(query_url, headers=headers))
        data = json.load(reader(response))
        pages = data["query"]["pages"]
        for key, page in pages.items():
            for image in page["imageinfo"]:
                image = image["url"]
                break
            break

    return {
        'cite': link,
        'title': title,
        'body': body,
        'image': image,
        'user_id': 1,
    }


def main():
    apiurl = "http://en.wikipedia.org/w/api.php"
    print(sys.argv[1:])
    for line in fileinput.input():
        line = line.strip()
        if 0 < len(line):
            print("Query: '{}'...".format(line))
            d = query_mediawiki(apiurl, line)
            print("Results: {}".format("".join([key for key, value in d.items() if value])))
            img = Image(**d)
            img.save()
            print("ID: {}".format(img.id))


if "__main__" == __name__:
    django.setup()
    main()

