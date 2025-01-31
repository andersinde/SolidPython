from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/vnf.scad'}", use_not_include=False)

EMPTY_VNF = _OpenSCADConstant('EMPTY_VNF')
_vnf_validate_errs = _OpenSCADConstant('_vnf_validate_errs')
class vnf_vertex_array(_Bosl2Base):
    def __init__(self, points=None, caps=None, cap1=None, cap2=None, col_wrap=None, row_wrap=None, reverse=None, style=None, **kwargs):
       super().__init__("vnf_vertex_array", {"points" : points, "caps" : caps, "cap1" : cap1, "cap2" : cap2, "col_wrap" : col_wrap, "row_wrap" : row_wrap, "reverse" : reverse, "style" : style, **kwargs})

class vnf_tri_array(_Bosl2Base):
    def __init__(self, points=None, row_wrap=None, reverse=None, **kwargs):
       super().__init__("vnf_tri_array", {"points" : points, "row_wrap" : row_wrap, "reverse" : reverse, **kwargs})

class vnf_join(_Bosl2Base):
    def __init__(self, vnfs=None, **kwargs):
       super().__init__("vnf_join", {"vnfs" : vnfs, **kwargs})

class vnf_from_polygons(_Bosl2Base):
    def __init__(self, polygons=None, **kwargs):
       super().__init__("vnf_from_polygons", {"polygons" : polygons, **kwargs})

class _path_path_closest_vertices(_Bosl2Base):
    def __init__(self, path1=None, path2=None, **kwargs):
       super().__init__("_path_path_closest_vertices", {"path1" : path1, "path2" : path2, **kwargs})

class _join_paths_at_vertices(_Bosl2Base):
    def __init__(self, path1=None, path2=None, v1=None, v2=None, **kwargs):
       super().__init__("_join_paths_at_vertices", {"path1" : path1, "path2" : path2, "v1" : v1, "v2" : v2, **kwargs})

class _cleave_connected_region(_Bosl2Base):
    def __init__(self, region=None, eps=None, **kwargs):
       super().__init__("_cleave_connected_region", {"region" : region, "eps" : eps, **kwargs})

class _polyHoles(_Bosl2Base):
    def __init__(self, outer=None, holes=None, extremes=None, eps=None, n=None, **kwargs):
       super().__init__("_polyHoles", {"outer" : outer, "holes" : holes, "extremes" : extremes, "eps" : eps, "n" : n, **kwargs})

class _bridge(_Bosl2Base):
    def __init__(self, pt=None, outer=None, eps=None, **kwargs):
       super().__init__("_bridge", {"pt" : pt, "outer" : outer, "eps" : eps, **kwargs})

class vnf_from_region(_Bosl2Base):
    def __init__(self, region=None, transform=None, reverse=None, **kwargs):
       super().__init__("vnf_from_region", {"region" : region, "transform" : transform, "reverse" : reverse, **kwargs})

class is_vnf(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_vnf", {"x" : x, **kwargs})

class is_vnf_list(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_vnf_list", {"x" : x, **kwargs})

class vnf_vertices(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_vertices", {"vnf" : vnf, **kwargs})

class vnf_faces(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_faces", {"vnf" : vnf, **kwargs})

class vnf_reverse_faces(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_reverse_faces", {"vnf" : vnf, **kwargs})

class vnf_quantize(_Bosl2Base):
    def __init__(self, vnf=None, q=None, **kwargs):
       super().__init__("vnf_quantize", {"vnf" : vnf, "q" : q, **kwargs})

class vnf_merge_points(_Bosl2Base):
    def __init__(self, vnf=None, eps=None, **kwargs):
       super().__init__("vnf_merge_points", {"vnf" : vnf, "eps" : eps, **kwargs})

class vnf_drop_unused_points(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_drop_unused_points", {"vnf" : vnf, **kwargs})

class _link_indicator(_Bosl2Base):
    def __init__(self, l=None, imin=None, imax=None, **kwargs):
       super().__init__("_link_indicator", {"l" : l, "imin" : imin, "imax" : imax, **kwargs})

class vnf_triangulate(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_triangulate", {"vnf" : vnf, **kwargs})

class _vnf_sort_vertices(_Bosl2Base):
    def __init__(self, vnf=None, idx=None, **kwargs):
       super().__init__("_vnf_sort_vertices", {"vnf" : vnf, "idx" : idx, **kwargs})

class vnf_slice(_Bosl2Base):
    def __init__(self, vnf=None, dir=None, cuts=None, **kwargs):
       super().__init__("vnf_slice", {"vnf" : vnf, "dir" : dir, "cuts" : cuts, **kwargs})

class _shift_cut_plane(_Bosl2Base):
    def __init__(self, vnf=None, dir=None, cut=None, off=None, **kwargs):
       super().__init__("_shift_cut_plane", {"vnf" : vnf, "dir" : dir, "cut" : cut, "off" : off, **kwargs})

class _split_polygon_at_x(_Bosl2Base):
    def __init__(self, poly=None, x=None, **kwargs):
       super().__init__("_split_polygon_at_x", {"poly" : poly, "x" : x, **kwargs})

class _split_2dpolygons_at_each_x(_Bosl2Base):
    def __init__(self, polys=None, xs=None, _i=None, **kwargs):
       super().__init__("_split_2dpolygons_at_each_x", {"polys" : polys, "xs" : xs, "_i" : _i, **kwargs})

class _slice_3dpolygons(_Bosl2Base):
    def __init__(self, polys=None, dir=None, cuts=None, **kwargs):
       super().__init__("_slice_3dpolygons", {"polys" : polys, "dir" : dir, "cuts" : cuts, **kwargs})

class vnf_volume(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_volume", {"vnf" : vnf, **kwargs})

class vnf_area(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_area", {"vnf" : vnf, **kwargs})

class _vnf_centroid(_Bosl2Base):
    def __init__(self, vnf=None, eps=None, **kwargs):
       super().__init__("_vnf_centroid", {"vnf" : vnf, "eps" : eps, **kwargs})

class vnf_halfspace(_Bosl2Base):
    def __init__(self, plane=None, vnf=None, closed=None, boundary=None, **kwargs):
       super().__init__("vnf_halfspace", {"plane" : plane, "vnf" : vnf, "closed" : closed, "boundary" : boundary, **kwargs})

class _assemble_paths(_Bosl2Base):
    def __init__(self, vertices=None, edges=None, paths=None, i=None, **kwargs):
       super().__init__("_assemble_paths", {"vertices" : vertices, "edges" : edges, "paths" : paths, "i" : i, **kwargs})

class _vnfcut(_Bosl2Base):
    def __init__(self, plane=None, vertices=None, vertexmap=None, inside=None, faces=None, vertcount=None, newfaces=None, newedges=None, newvertices=None, i=None, **kwargs):
       super().__init__("_vnfcut", {"plane" : plane, "vertices" : vertices, "vertexmap" : vertexmap, "inside" : inside, "faces" : faces, "vertcount" : vertcount, "newfaces" : newfaces, "newedges" : newedges, "newvertices" : newvertices, "i" : i, **kwargs})

class _triangulate_planar_convex_polygons(_Bosl2Base):
    def __init__(self, polys=None, **kwargs):
       super().__init__("_triangulate_planar_convex_polygons", {"polys" : polys, **kwargs})

class vnf_bend(_Bosl2Base):
    def __init__(self, vnf=None, r=None, d=None, axis=None, **kwargs):
       super().__init__("vnf_bend", {"vnf" : vnf, "r" : r, "d" : d, "axis" : axis, **kwargs})

class _vnf_validate(_Bosl2Base):
    def __init__(self, vnf=None, show_warns=None, check_isects=None, **kwargs):
       super().__init__("_vnf_validate", {"vnf" : vnf, "show_warns" : show_warns, "check_isects" : check_isects, **kwargs})

class _vnf_validate_err(_Bosl2Base):
    def __init__(self, name=None, extra=None, **kwargs):
       super().__init__("_vnf_validate_err", {"name" : name, "extra" : extra, **kwargs})

class _pts_not_reported(_Bosl2Base):
    def __init__(self, pts=None, varr=None, reports=None, **kwargs):
       super().__init__("_pts_not_reported", {"pts" : pts, "varr" : varr, "reports" : reports, **kwargs})

class _edge_not_reported(_Bosl2Base):
    def __init__(self, edge=None, varr=None, reports=None, **kwargs):
       super().__init__("_edge_not_reported", {"edge" : edge, "varr" : varr, "reports" : reports, **kwargs})

class vnf_polyhedron(_Bosl2Base):
    def __init__(self, vnf=None, convexity=None, extent=None, cp=None, anchor=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("vnf_polyhedron", {"vnf" : vnf, "convexity" : convexity, "extent" : extent, "cp" : cp, "anchor" : anchor, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class vnf_wireframe(_Bosl2Base):
    def __init__(self, vnf=None, width=None, **kwargs):
       super().__init__("vnf_wireframe", {"vnf" : vnf, "width" : width, **kwargs})

class _show_vertices(_Bosl2Base):
    def __init__(self, vertices=None, size=None, filter=None, **kwargs):
       super().__init__("_show_vertices", {"vertices" : vertices, "size" : size, "filter" : filter, **kwargs})

class _show_faces(_Bosl2Base):
    def __init__(self, vertices=None, faces=None, size=None, filter=None, **kwargs):
       super().__init__("_show_faces", {"vertices" : vertices, "faces" : faces, "size" : size, "filter" : filter, **kwargs})

class debug_vnf(_Bosl2Base):
    def __init__(self, vnf=None, faces=None, vertices=None, opacity=None, size=None, convexity=None, filter=None, **kwargs):
       super().__init__("debug_vnf", {"vnf" : vnf, "faces" : faces, "vertices" : vertices, "opacity" : opacity, "size" : size, "convexity" : convexity, "filter" : filter, **kwargs})

class vnf_validate(_Bosl2Base):
    def __init__(self, vnf=None, size=None, show_warns=None, check_isects=None, opacity=None, adjacent=None, label_verts=None, label_faces=None, wireframe=None, **kwargs):
       super().__init__("vnf_validate", {"vnf" : vnf, "size" : size, "show_warns" : show_warns, "check_isects" : check_isects, "opacity" : opacity, "adjacent" : adjacent, "label_verts" : label_verts, "label_faces" : label_faces, "wireframe" : wireframe, **kwargs})

