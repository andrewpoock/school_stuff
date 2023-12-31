# render_ray.py
#    Ray tracing rendering algorithms

from ren3d.ray3d import Interval, Point
from ren3d.models import Record


def raytrace(scene, img, updatefn=None):
    """basic raytracing algorithm to render scene into img
    """
    w, h = img.size
    camera = scene.camera
    camera.set_resolution(w, h)
    for j in range(h):
        for i in range(w):
            ray = camera.ij_ray(i, j)
            color = raycolor(scene, ray, Interval())
            img[(i, j)] = color.quantize(255)
        if updatefn:
            updatefn()


def raycolor(scene, ray, interval):
    """returns the color of ray in the scene
    """
    record = Record()
    if scene.objects.intersect(ray, interval, record):
        lvec = (scene.light-ray.point_at(interval.high)).normalized()
        norm = record.normal
        lambert = max(0, lvec.dot(norm))
        color = lambert*record.color
        return color
    else:
        return scene.background
