# render_ray.py
#    Ray tracing rendering algorithms
# by: John Zelle

from ren3d.ray3d import Interval, Point
from ren3d.models import Record
from ren3d.rgb import RGB
from ren3d.ray3d import Ray

# switch scene.objects to scene.surface
def raytrace(scene, img, updatefn=None):
    """basic raytracing algorithm to render scene into img
    """
    camera = scene.camera
    w, h = img.size
    camera.set_resolution(w, h)
    for j in range(h):
        for i in range(w):
            ray = camera.ij_ray(i, j)
            color = raycolor(scene, ray, Interval(), scene.reflections)
            img[i, j] = color.quantize(255)
        if updatefn:
            updatefn()


def raycolor(scene, ray, interval, reflections):
    """returns the color of ray in the scene
    """

    hit_info = Record()
    if scene.surface.intersect(ray, interval, hit_info):
        hitpt = hit_info.point
        ambient = scene.ambient
        k = hit_info.color
        n = hit_info.normal
        color = k.ambient*scene.ambient
        if scene.textures and hit_info.texture is not None:
            uvn = hit_info.texture(hit_info.uvn)
            k.diffuse, k.ambient = uvn, uvn
        for i in range(len(scene.lights)):
            lpos, lcolor = scene.lights[i]
            shadowray = Ray(hitpt, lpos-hitpt)
            if scene.surface.intersect(shadowray, Interval(.001, 1), Record()) == False:
                lvec = (lpos-hitpt).normalized()
                lambert = max(0, lvec.dot(n))
                color += k.diffuse * lambert
                vvec = -ray.dir.normalized()
                h = (lvec + vvec).normalized()
                color += k.specular*lcolor*max(0, h.dot(n))**k.shininess
        if k.reflect and reflections > 0:
            reflray = Ray(hitpt, ray.dir.reflect(n))
            rcolor = raycolor(scene, reflray, Interval(.001, 1), reflections-1)
            color += rcolor*k.reflect
        return color
    else:
        return scene.background
