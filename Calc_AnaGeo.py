from math import *
import BasicMath
import sys


# Converter Plane
def conv_pl_par_norm(support, dr1, dr2):
    out_support = support
    out_normal = basic_vc_unit(basic_vc_vector_product(dr1, dr2))
    return [out_support, out_normal]


def conv_pl_par_coord(support, dr1, dr2):
    help_pl = conv_pl_par_norm(support, dr1, dr2)
    return conv_pl_norm_coord(help_pl[0], help_pl[1])


def conv_pl_norm_par(support, normal):
    out_support = support
    base_x = Vector(1, 0, 0)
    base_y = Vector(0, 1, 0)
    base_z = Vector(0, 0, 1)
    d1 = basic_vc_vector_product(normal, base_x)
    d2 = basic_vc_vector_product(normal, base_y)
    d3 = basic_vc_vector_product(normal, base_z)
    if d1.full_zero:
        dr1 = basic_vc_unit(d2)
        dr2 = basic_vc_unit(d3)
    elif d2.full_zero:
        dr1 = basic_vc_unit(d1)
        dr2 = basic_vc_unit(d3)
    elif d2.full_zero:
        dr1 = basic_vc_unit(d1)
        dr2 = basic_vc_unit(d2)
    elif basic_vc_lin_dep(d1, d2):
        dr1 = basic_vc_unit(d2)
        dr2 = basic_vc_unit(d3)
    else:
        dr1 = basic_vc_unit(d1)
        dr2 = basic_vc_unit(d2)
    return [out_support, dr1, dr2]


def conv_pl_norm_coord(support, normal):
    a = normal.x
    b = normal.y
    c = normal.z
    d = -1 * basic_vc_scalar_product(normal, basic_vc_scalar_multi(support, -1))
    return [a, b, c, d]


def conv_pl_coord_norm(a, b, c, d):
    normal = basic_vc_unit(Vector(a, b, c))
    if a != 0:
        support = Vector(d / a, 0, 0)
    elif b != 0:
        support = Vector(0, d / b, 0)
    else:
        support = Vector(0, 0, d / c)
    return [support, normal]


def conv_pl_coord_par(a, b, c, d):
    help_pl = conv_pl_coord_norm(a, b, c, d)
    return conv_pl_norm_par(help_pl[0], help_pl[1])


def conv_pl_pt_par(pt_a, pt_b, pt_c):
    dr1 = basic_vc_minus(pt_b.ov, pt_a.ov)
    dr2 = basic_vc_minus(pt_c.ov, pt_a.ov)
    support = pt_a
    return [support, dr1, dr2]


def conv_pl_pt_norm(pt_a, pt_b, pt_c):
    help_pl = conv_pl_pt_par(pt_a, pt_b, pt_c)
    return conv_pl_par_norm(help_pl[0], help_pl[1], help_pl[2])


def conv_pl_pt_coord(pt_a, pt_b, pt_c):
    help_pl = conv_pl_pt_par(pt_a, pt_b, pt_c)
    return conv_pl_par_coord(help_pl[0], help_pl[1], help_pl[2])


# Converter Line
def conv_ln_pt_par(pt_a, pt_b):
    support = pt_a.ov
    direction = basic_vc_minus(pt_b.ov, pt_a.ov)
    return [support, direction]


# Converter LGS
def conv_lgs_pl_mtx(pl_a, pl_b, pl_c):
    out_mtx = Matrix(pl_a.a, pl_a.b, pl_a.c, pl_b.a, pl_b.b, pl_b.c, pl_c.a, pl_c.b, pl_c.c)
    out_vc = Vector(pl_a.d, pl_b.d, pl_c.d)
    return [out_mtx, out_vc]


# Converter Point
def vc2pt(vc):
    return Point(vc.x, vc.y, vc.z)


# Basic Vector
def basic_vc_plus(vc_a, vc_b):
    return Vector(vc_a.x + vc_b.x, vc_a.y + vc_b.y, vc_a.z + vc_b.z)


def basic_vc_minus(vc_a, vc_b):
    return Vector(vc_a.x - vc_b.x, vc_a.y - vc_b.y, vc_a.z - vc_b.z)


def basic_vc_scalar_multi(vc, c):
    if (type(vc) == int or type(type(vc) == float)) and type(c) == Vector:
        temp = vc
        vc = c
        c = temp
    return Vector(vc.x*c, vc.y*c, vc.z*c)


def basic_vc_scalar_product(vc_a, vc_b):
    return vc_a.x*vc_b.x + vc_a.y*vc_b.y + vc_a.z*vc_b.z


def basic_vc_vector_product(vc_a, vc_b):
    output_x = vc_a.y * vc_b.z - vc_a.z * vc_b.y
    output_y = vc_a.z * vc_b.x - vc_a.x * vc_b.z
    output_z = vc_a.x * vc_b.y - vc_a.y * vc_b.x
    return Vector(output_x, output_y, output_z)


def basic_vc_spar_product(vc_a, vc_b, vc_c):
    return abs(basic_vc_scalar_product(basic_vc_vector_product(vc_a, vc_b), vc_c))


def basic_vc_unit(vc):
    return basic_vc_scalar_multi(vc, 1/vc.length)


def basic_vc_lin_dep(vc_a, vc_b):
    if vc_a.full_zero != vc_b.full_zero:
        return True
    elif vc_a.full_zero:
        return False
    else:
        # check for inequality
        if vc_a.zero_x != vc_b.zero_x:
            return False
        if vc_a.zero_y != vc_b.zero_y:
            return False
        if vc_a.zero_z != vc_b.zero_z:
            return False

        # if no 0
        if not vc_a.con_zero and not vc_b.con_zero:
            a = BasicMath.constant_round((vc_a.x / vc_b.x), 8)
            b = BasicMath.constant_round((vc_a.y / vc_b.y), 8)
            c = BasicMath.constant_round((vc_a.z / vc_b.z), 8)
            if a == b and a == c:
                return True
            else:
                return False

        if vc_a.zero_x:
            if vc_a.zero_y or vc_a.zero_z:
                return True
            else:
                b = BasicMath.constant_round((vc_a.y / vc_b.y), 8)
                c = BasicMath.constant_round((vc_a.z / vc_b.z), 8)
                if b == c:
                    return True
                else:
                    return False
        elif vc_a.zero_y:
            if vc_a.zero_z:
                return True
            else:
                a = BasicMath.constant_round((vc_a.x / vc_b.x), 8)
                c = BasicMath.constant_round((vc_a.z / vc_b.z), 8)
                if a == c:
                    return True
                else:
                    return False
        else:
            a = BasicMath.constant_round((vc_a.x / vc_b.x), 8)
            b = BasicMath.constant_round((vc_a.y / vc_b.y), 8)
            if a == b:
                return True
            else:
                return False


# Basic LGS
def basic_lgs_det(lgs):
    sum1 = lgs.a11 * lgs.a22 * lgs.a33
    sum2 = lgs.a12 * lgs.a23 * lgs.a31
    sum3 = lgs.a13 * lgs.a21 * lgs.a32
    min1 = lgs.a31 * lgs.a22 * lgs.a13
    min2 = lgs.a32 * lgs.a23 * lgs.a11
    min3 = lgs.a33 * lgs.a21 * lgs.a12
    return (sum1 + sum2 + sum3) - (min1 + min2 + min3)


def basic_lgs_solve(lgs):
    if basic_lgs_det(lgs) == 0:
        sys.exit("Das Gleichungssystem hat keine eindeutige Lösung.")
    help1 = Matrix(lgs.b1, lgs.a12, lgs.a13, lgs.b2, lgs.a22, lgs.a23, lgs.b3, lgs.a32, lgs.a33)
    help2 = Matrix(lgs.a11, lgs.b1, lgs.a13, lgs.a21, lgs.b2, lgs.a23, lgs.a31, lgs.b3, lgs.a33)
    help3 = Matrix(lgs.a11, lgs.a12, lgs.b1, lgs.a21, lgs.a22, lgs.b2, lgs.a31, lgs.a32, lgs.b3)
    ox = (basic_lgs_det(help1) / basic_lgs_det(lgs.mtx))
    oy = (basic_lgs_det(help2) / basic_lgs_det(lgs.mtx))
    oz = (basic_lgs_det(help3) / basic_lgs_det(lgs.mtx))
    return Vector(ox, oy, oz)


# Basic Angle
def basic_angle(obj_a, obj_b):
    if (type(obj_a) == Vector and obj_a.length == 0) or (type(obj_b) == Vector and obj_b.length == 0):
        sys.exit("Der Vektor hat keine Richtung.")
    # calculate
    output = 0
    if type(obj_a) == Vector:
        if type(obj_b) == Vector:
            output = degrees(acos(basic_vc_scalar_product(obj_a, obj_b) / (obj_a.length * obj_b.length)))
        elif type(obj_b) == Line:
            output = degrees(acos(basic_vc_scalar_product(obj_a, obj_b.dr) / (obj_a.length * obj_b.dr.length)))
        elif type(obj_b) == Plane:
            output = degrees(asin(basic_vc_scalar_product(obj_a, obj_b.normal) / (obj_a.length * obj_b.normal.length)))
    elif type(obj_a) == Line:
        if type(obj_b) == Vector:
            output = degrees(acos(basic_vc_scalar_product(obj_a.dr, obj_b) / (obj_a.dr.length * obj_b.length)))
        elif type(obj_b) == Line:
            if con_line2(obj_a, obj_b) != 3:
                sys.exit("Es gibt keinen eindeutigen Schnittpunkt zwischen den beiden Geraden.")
            output = degrees(acos(basic_vc_scalar_product(obj_a.dr, obj_b.dr) /
                                  (obj_a.dr.length * obj_b.dr.length)))
        elif type(obj_b) == Plane:
            if not (con_line_plane(obj_a, obj_b) == 1 or con_line_plane(obj_a, obj_b) == 3):
                sys.exit("Es gibt keinen eindeutigen Schnittpunkt zwischen den beiden Objekten.")
            output = degrees(asin(basic_vc_scalar_product(obj_a.dr, obj_b.normal) /
                                  (obj_a.dr.length * obj_b.normal.length)))
    elif type(obj_a) == Plane:
        if type(obj_b) == Vector:
            output = degrees(asin(basic_vc_scalar_product(obj_a.normal, obj_b) /
                                  (obj_a.normal.length * obj_b.length)))
        elif type(obj_b) == Line:
            if not (con_line_plane(obj_a, obj_b) == 1 or con_line_plane(obj_a, obj_b) == 3):
                sys.exit("Es gibt keinen eindeutigen Schnittpunkt zwischen den beiden Objekten.")
            output = degrees(asin(basic_vc_scalar_product(obj_a.normal, obj_b.dr) /
                                  (obj_a.normal.length * obj_b.dr.length)))
        elif type(obj_b) == Plane:
            if not (con_plane2(obj_a, obj_b) == 1 or con_plane2(obj_a, obj_b) == 3):
                sys.exit("Es gibt keine eindeutige Schnittgerade zwischen den beiden Ebenen.")
            output = degrees(acos(basic_vc_scalar_product(obj_a.normal, obj_b.normal) /
                                  (obj_a.normal.length * obj_b.normal.length)))
    return Angle(abs(output))


# Objects
class Angle:
    def __init__(self, ang_deg):
        self.ang_degree = ang_deg
        self.ang_radian = radians(ang_deg)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        length = sqrt(x * x + y * y + z * z)
        self.length = length
        full_zero = False
        if length == 0:
            full_zero = True
        self.full_zero = full_zero
        zero_x = False
        zero_y = False
        zero_z = False
        con_zero = False
        if x == 0:
            zero_x = True
            con_zero = True
        if y == 0:
            zero_y = True
            con_zero = True
        if z == 0:
            zero_z = True
            con_zero = True
        self.zero_x = zero_x
        self.zero_y = zero_y
        self.zero_z = zero_z
        self.con_zero = con_zero


class Point:
    def __init__(self, x, y, z):
        self.x = BasicMath.constant_round(x, 8)
        self.y = BasicMath.constant_round(y, 8)
        self.z = BasicMath.constant_round(z, 8)
        ov = Vector(x, y, z)
        self.ov = ov


class Line:
    def __init__(self, support, dr):
        if dr.full_zero:
            sys.exit("Die Gerade konnte nicht entstehen. Der Richtungsvektor gleicht dem Nullvektor.")
        self.support = support
        self.dr = dr
        s_point = Point(support.x, support.y, support.z)
        self.s_point = s_point
        base_x = Vector(1, 0, 0)
        base_y = Vector(0, 1, 0)
        base_z = Vector(0, 0, 1)
        n1 = basic_vc_vector_product(dr, base_x)
        n2 = basic_vc_vector_product(dr, base_y)
        n3 = basic_vc_vector_product(dr, base_z)
        if n1.full_zero:
            pl_help1 = conv_pl_norm_par(support, n2)
            pl_help2 = conv_pl_norm_par(support, n3)
        elif n2.full_zero:
            pl_help1 = conv_pl_norm_par(support, n1)
            pl_help2 = conv_pl_norm_par(support, n3)
        elif n3.full_zero:
            pl_help1 = conv_pl_norm_par(support, n1)
            pl_help2 = conv_pl_norm_par(support, n2)
        elif basic_vc_lin_dep(n1, n2):
            pl_help1 = conv_pl_norm_par(support, n2)
            pl_help2 = conv_pl_norm_par(support, n3)
        else:
            pl_help1 = conv_pl_norm_par(support, n1)
            pl_help2 = conv_pl_norm_par(support, n2)
        plane1 = Plane(pl_help1[0], pl_help1[1], pl_help1[2])
        plane2 = Plane(pl_help2[0], pl_help2[1], pl_help2[2])
        self.plane1 = plane1
        self.plane2 = plane2


class Plane:
    def __init__(self, support, dr1, dr2):
        if basic_vc_lin_dep(dr1, dr2):
            sys.exit("Ebene konnte nicht entstehen. Die Spannvektoren sind linear abhängig.")
        elif dr1.full_zero or dr2.full_zero:
            sys.exit("Ebene konnte nicht entstehen. Ein Spannvektor gleicht dem Nullvektor.")

        self.support = support
        s_point = Point(support.x, support.y, support.z)
        self.s_point = s_point
        self.dr1 = dr1
        self.dr2 = dr2
        normal = conv_pl_par_norm(support, dr1, dr2)[1]
        self.normal = normal
        coord = conv_pl_par_coord(support, dr1, dr2)
        a = coord[0]
        b = coord[1]
        c = coord[2]
        d = coord[3]
        self.a = BasicMath.constant_round(a, 8)
        self.b = BasicMath.constant_round(b, 8)
        self.c = BasicMath.constant_round(c, 8)
        self.d = BasicMath.constant_round(d, 8)


class Matrix:
    def __init__(self, a11, a12, a13, a21, a22, a23, a31, a32, a33):
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33


class LGS:
    def __init__(self, mtx, vc):
        self.mtx = mtx
        self.vc = vc
        self.a11 = mtx.a11
        self.a12 = mtx.a12
        self.a13 = mtx.a13
        self.a21 = mtx.a21
        self.a22 = mtx.a22
        self.a23 = mtx.a23
        self.a31 = mtx.a31
        self.a32 = mtx.a32
        self.a33 = mtx.a33
        self.b1 = vc.x
        self.b2 = vc.y
        self.b3 = vc.z


# Base Units
x_axis = Line(Vector(0, 0, 0), Vector(1, 0, 0))
y_axis = Line(Vector(0, 0, 0), Vector(0, 1, 0))
z_axis = Line(Vector(0, 0, 0), Vector(0, 0, 1))

wall_x1 = Plane(conv_pl_coord_par(1, 0, 0, 0)[0], conv_pl_coord_par(1, 0, 0, 0)[1], conv_pl_coord_par(1, 0, 0, 0)[2])
wall_x2 = Plane(conv_pl_coord_par(1, 0, 0, 1)[0], conv_pl_coord_par(1, 0, 0, 1)[1], conv_pl_coord_par(1, 0, 0, 1)[2])
wall_y1 = Plane(conv_pl_coord_par(0, 1, 0, 0)[0], conv_pl_coord_par(0, 1, 0, 0)[1], conv_pl_coord_par(0, 1, 0, 0)[2])
wall_y2 = Plane(conv_pl_coord_par(0, 1, 0, 1)[0], conv_pl_coord_par(0, 1, 0, 1)[1], conv_pl_coord_par(0, 1, 0, 1)[2])
wall_z1 = Plane(conv_pl_coord_par(0, 0, 1, 0)[0], conv_pl_coord_par(0, 0, 1, 0)[1], conv_pl_coord_par(0, 0, 1, 0)[2])
wall_z2 = Plane(conv_pl_coord_par(0, 0, 1, 1)[0], conv_pl_coord_par(0, 0, 1, 1)[1], conv_pl_coord_par(0, 0, 1, 1)[2])

zero = Point(0, 0, 0)


# Containment
def con_point2(pt_a, pt_b):
    if pt_a.x == pt_b.x and pt_a.y == pt_b.y and pt_a.z == pt_b.z:
        return True
    else:
        return False


def con_line2(ln_a, ln_b):  # 1 = identical, 2 = parallel, 3 = cross point, 4 = skewed
    support = basic_vc_minus(ln_b.support, ln_a.support)
    direction1 = basic_vc_scalar_multi(ln_a.dr, -1)
    direction2 = ln_b.dr
    if basic_vc_lin_dep(ln_a.dr, ln_b.dr):
        if con_point_line(ln_a.s_point, ln_b):
            return 1
        else:
            return 2
    else:
        help_pl = Plane(support, direction1, direction2)
        if help_pl.d == 0:
            return 3
        else:
            return 4


def con_plane2(pl_a, pl_b):  # 1 = identical, 2 = parallel, 3 = cross line
    if basic_vc_lin_dep(pl_a.normal, pl_b.normal):
        if con_point_plane(pl_a.s_point, pl_b):
            return 1
        else:
            return 2
    else:
        return 3


def con_line_plane(ln, pl):  # 1 = identical, 2 = parallel, 3 = cross point
    if type(ln) == Plane and type(pl) == Line:
        temp = ln
        ln = pl
        pl = temp
    if basic_vc_scalar_product(ln.dr, pl.normal) == 0:
        if con_point_plane(ln.s_point, pl):
            return 1
        else:
            return 2
    else:
        return 3


def con_point_plane(pt, pl):
    if type(pt) == Plane and type(pl) == Point:
        temp = pt
        pt = pl
        pl = temp
    if BasicMath.constant_round((pt.x * pl.a + pt.y * pl.b + pt.z * pl.c), 6) == BasicMath.constant_round(pl.d, 6):
        return True
    else:
        return False


def con_point_line(pt, ln):
    if type(pt) == Line and type(ln) == Point:
        temp = pt
        pt = ln
        ln = temp
    help_vc = basic_vc_minus(pt.ov, ln.support)
    return basic_vc_lin_dep(help_vc, ln.dr)


# Distance
def dis_point2(pt_a, pt_b):
    return basic_vc_minus(pt_a.ov, pt_b.ov).length


def dis_line2(ln_a, ln_b):
    support = basic_vc_minus(ln_b.support, ln_a.support)
    dire1 = basic_vc_scalar_multi(ln_a.dr, -1)
    dire2 = ln_b.dr
    if con_line2(ln_a, ln_b) == 1 or con_line2(ln_a, ln_b) == 3:
        return 0
    elif con_line2(ln_a, ln_b) == 2:
        return abs(dis_point_line(ln_a.s_point, ln_b))
    else:
        help_pl = Plane(support, dire1, dire2)
        return abs(dis_point_plane(zero, help_pl))


def dis_plane2(pl_a, pl_b):
    if con_plane2(pl_a, pl_b) == 1 or con_plane2(pl_a, pl_b) == 3:
        return 0
    else:
        return abs(dis_point_plane(pl_a.s_point, pl_b))


def dis_line_plane(ln, pl):
    if type(ln) == Plane and type(pl) == Line:
        temp = ln
        ln = pl
        pl = temp
    if con_line_plane(ln, pl) == 1 or con_line_plane(ln, pl) == 3:
        return 0
    else:
        return abs(dis_point_plane(ln.s_point, pl))


def dis_point_plane(pt, pl):
    if type(pt) == Plane and type(pl) == Point:
        temp = pt
        pt = pl
        pl = temp
    return abs(BasicMath.constant_round((pt.x * pl.a + pt.y * pl.b + pt.z * pl.c - pl.d), 8))


def dis_point_line(pt, ln):
    if type(pt) == Line and type(ln) == Point:
        temp = pt
        pt = ln
        ln = temp
    hh = conv_pl_norm_par(pt.ov, ln.dr)
    help_pl = Plane(hh[0], hh[1], hh[2])
    root = cross_line_plane(ln, help_pl)
    return abs(dis_point2(pt, root))


# Cross Area
def cross_line2(ln_a, ln_b):
    if con_line2(ln_a, ln_b) != 3:
        sys.exit("Es gibt keinen eindeutigen Schnittpunkt zwischen den beiden Geraden.")
    help1 = LGS(conv_lgs_pl_mtx(ln_a.plane1, ln_a.plane2, ln_b.plane1)[0],
                conv_lgs_pl_mtx(ln_a.plane1, ln_a.plane2, ln_b.plane1)[1])
    help2 = LGS(conv_lgs_pl_mtx(ln_a.plane1, ln_a.plane2, ln_b.plane2)[0],
                conv_lgs_pl_mtx(ln_a.plane1, ln_a.plane2, ln_b.plane2)[1])
    if basic_lgs_det(help1.mtx) == 0:
        help_lgs = help2
    else:
        help_lgs = help1
    return vc2pt(basic_lgs_solve(help_lgs))


def cross_line_plane(ln, pl):
    if type(ln) == Plane and type(pl) == Line:
        temp = ln
        ln = pl
        pl = temp
    if con_line_plane(ln, pl) != 3:
        sys.exit("Es gibt keinen eindeutigen Schnittpunkt zwischen der Gerade und der Ebene.")
    help_lgs = LGS(conv_lgs_pl_mtx(ln.plane1, ln.plane2, pl)[0], conv_lgs_pl_mtx(ln.plane1, ln.plane2, pl)[1])
    return vc2pt(basic_lgs_solve(help_lgs))


def cross_plane2(pl_a, pl_b):
    if con_plane2(pl_a, pl_b) != 3:
        sys.exit("Die beiden Ebenen haben keine eindeutige Schnittgerade.")
    lgs1 = LGS(conv_lgs_pl_mtx(pl_a, pl_b, wall_x1)[0], conv_lgs_pl_mtx(pl_a, pl_b, wall_x1)[1])
    lgs2 = LGS(conv_lgs_pl_mtx(pl_a, pl_b, wall_x2)[0], conv_lgs_pl_mtx(pl_a, pl_b, wall_x2)[1])
    lgs3 = LGS(conv_lgs_pl_mtx(pl_a, pl_b, wall_y1)[0], conv_lgs_pl_mtx(pl_a, pl_b, wall_y1)[1])
    lgs4 = LGS(conv_lgs_pl_mtx(pl_a, pl_b, wall_y2)[0], conv_lgs_pl_mtx(pl_a, pl_b, wall_y2)[1])
    lgs5 = LGS(conv_lgs_pl_mtx(pl_a, pl_b, wall_z1)[0], conv_lgs_pl_mtx(pl_a, pl_b, wall_z1)[1])
    lgs6 = LGS(conv_lgs_pl_mtx(pl_a, pl_b, wall_z2)[0], conv_lgs_pl_mtx(pl_a, pl_b, wall_z2)[1])
    if basic_lgs_det(lgs1) != 0 and basic_lgs_det(lgs2) != 0:
        out_1 = vc2pt(basic_lgs_solve(lgs1))
        out_2 = vc2pt(basic_lgs_solve(lgs2))
        return Line(conv_ln_pt_par(out_1, out_2)[0], conv_ln_pt_par(out_1, out_2)[1])
    elif basic_lgs_det(lgs3) != 0 and basic_lgs_det(lgs4) != 0:
        out_1 = vc2pt(basic_lgs_solve(lgs3))
        out_2 = vc2pt(basic_lgs_solve(lgs4))
        return Line(conv_ln_pt_par(out_1, out_2)[0], conv_ln_pt_par(out_1, out_2)[1])
    else:
        out_1 = vc2pt(basic_lgs_solve(lgs5))
        out_2 = vc2pt(basic_lgs_solve(lgs6))
        return Line(conv_ln_pt_par(out_1, out_2)[0], conv_ln_pt_par(out_1, out_2)[1])


def track_point_pl(pl):
    axes = [x_axis, y_axis, z_axis]
    points = []
    for axis in axes:
        if basic_vc_scalar_product(pl.normal, axis.dr) != 0:
            cross_point = [cross_line_plane(axis, pl), axes.index(axis)]
            if not con_point2(cross_point[0], zero):
                points.append(cross_point)
    return points
