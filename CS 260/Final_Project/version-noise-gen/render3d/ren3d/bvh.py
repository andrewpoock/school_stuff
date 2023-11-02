# bvh.py


def make_BVH(surfaces, axis=0):
    """ Build BVH from list of surfaces """
    assert len(surfaces) > 0
    if len(surfaces) == 1:
        return surfaces[0]
    return BVH(surfaces, axis)


class BVH:

    def __init__(self, surfaces, axis=0):
        n = len(surfaces)
        assert n > 1
        # store surfaces for iter_polygons
        self.surfaces = surfaces
        # sort objects by "midpt" along axis
        surfaces.sort(key=lambda s: s.bbox.midpoint[axis])
        # split into 2 halfs
        m = n//2
        self.left = make_BVH(surfaces[:m], (axis+1) % 3)
        # left objects into left BVH, right objects into right BVH
        self.right = make_BVH(surfaces[m:], (axis+1) % 3)
        # then build combined bounding box
        self.bbox = self.left.bbox.combine(self.right.bbox)

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
            for rec in s.iter_polygons():
                yield rec
