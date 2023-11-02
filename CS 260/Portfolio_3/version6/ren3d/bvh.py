# bvh.py

def make_BVH(surfaces, axis=0):
    assert len(surfaces) > 0
    if len(surfaces) == 1:
        return surfaces[0]
    else:
        return BVH(surfaces, axis)

class BVH:

    def __init__(self, surfaces, axis):
        n = len(surfaces)
        assert n > 1
        def keyfn(s): return s.bbox.midpoint[axis]
        surfaces.sort(key=keyfn)
        m = n//2
        next_axis = (axis + 1) % 3
        self.left = make_BVH(surfaces[:m], next_axis)
        self.right = make_BVH(surfaces[m:], next_axis)
        self.bbox = self.left.bbox.combine(self.right.bbox)
        self.surfaces = surfaces

    def intersect(self, ray, interval, info):
        if not self.bbox.hit(ray, interval):
            return False
        hit = False
        if self.left.intersect(ray, interval, info):
            hit = True
            interval.high = info.t
        if self.right.intersect(ray, interval, info):
            hit = True
            interval.high = info.t
        return hit

    def iter_polygons(self):
        for s in self.surfaces:
            for r in s.iter_polygons():
                yield r
