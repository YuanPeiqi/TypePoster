import os

from flask import jsonify


def json2lay(json):
    lay_path = ''
    return lay_path


def lay2json(lay):
    return {}


class Blender:
    def __init__(self, layout1, layout2):
        self.layout1 = layout1
        self.layout2 = layout2
        self.result_layouts = []

    def blending(self):
        path1 = json2lay(self.layout1)
        path2 = json2lay(self.layout2)
        os.system(f"out.exe {path1} {path2}")
        return jsonify(self.result_layouts)
