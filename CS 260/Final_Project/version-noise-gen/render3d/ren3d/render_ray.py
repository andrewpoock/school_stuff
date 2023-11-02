# render_ray.py
#    Ray tracing rendering algorithms

from ren3d.ray3d import Ray, Interval
from ren3d.models import Record


def raytrace_chunk(scene, img_size, inc, start, updatefn=None):
    w, h = img_size
    bgc = scene.background.quantize(255)
    color = [[bgc for _ in range(w)] for _ in range(start, h, inc)]
    for j in range(start, h, inc):
        for i in range(w):
            ray = scene.camera.ij_ray(i, j)
            color[j//inc][i] = raycolor(scene, ray, Interval(), scene.reflections).quantize(255)
        if updatefn:
            updatefn()
    return color


def raytrace(scene, img, updatefn=None):
    """basic raytracing algorithm to render scene into img"""
    img.clear(scene.background.quantize(255))
    w, h = img.size
    scene.camera.set_resolution(w, h)

    for j in range(h):
        for i in range(w):
            ray = scene.camera.ij_ray(i, j)
            color = raycolor(scene, ray, Interval(), scene.reflections)
            img[(i, j)] = color.quantize(255)
        if updatefn:
            updatefn()


def raycolor(scene, ray, interval, nreflect):
    """returns the color of ray in the scene"""
    info = Record()
    info.color, info.normal, info.point, info.texture, info.uvn = [None] * 5
    if scene.surface.intersect(ray, interval, info):
        k = info.color
        hitpt = info.point
        n = info.normal
        if scene.textures and info.texture:
            k.diffuse = info.texture(info.uvn)
            k.ambient = info.texture(info.uvn)  # we need to set ambient too

        # ambient
        color = k.ambient * scene.ambient

        for light in scene.lights:
            lpos, lcolor = light

            lvec = (lpos-hitpt)
            if not (scene.shadows and scene.surface.intersect(Ray(hitpt, lvec), Interval(0.0001, 1), Record())):
                lvec = lvec.normalized()
                lambert = max(0.0, lvec.dot(n))
                # diffuse
                color += k.diffuse * lambert
                vvec = -ray.dir.normalized()
                # vvec = (scene.camera.eye - hitpt).normalized()
                h = (lvec + vvec).normalized()
                # specular
                color += k.specular * lcolor * max(0.0, h.dot(n)) ** k.shininess

        if k.reflect and nreflect > 0:
            rcolor = raycolor(scene, Ray(hitpt, ray.dir.reflect(n)), Interval(low=0.0001), nreflect-1)
            color += rcolor * k.reflect

    else:
        color = scene.background

    return color
