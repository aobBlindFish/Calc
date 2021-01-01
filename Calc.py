from math import *
import sys
# Converter


class Conv:
    class Pl:
        class Par:
            def norm(support, dr1, dr2):
                OutSupport = support
                OutNormal = Basic.Vc.unit(Basic.Vc.vproduct(dr1, dr2))
                Output = [OutSupport, OutNormal]
                return Output
            def coord(support, dr1, dr2):
                help = Conv.Pl.Par.norm(support, dr1, dr2)
                Output = Conv.Pl.Norm.coord(help[0], help[1])
                return Output
        class Norm:
            def par(support, normal):
                OutSupport = support
                basex = Vector(1, 0, 0)
                basey = Vector(0, 1, 0)
                basez = Vector(0, 0, 1)
                d1 = Basic.Vc.vproduct(normal, basex)
                d2 = Basic.Vc.vproduct(normal, basey)
                d3 = Basic.Vc.vproduct(normal, basez)
                if d1.fullzero == True:
                    dr1 = Basic.Vc.unit(d2)
                    dr2 = Basic.Vc.unit(d3)
                elif d2.fullzero == True:
                    dr1 = Basic.Vc.unit(d1)
                    dr2 = Basic.Vc.unit(d3)
                elif d2.fullzero == True:
                    dr1 = Basic.Vc.unit(d1)
                    dr2 = Basic.Vc.unit(d2)
                elif Basic.Vc.lindep(d1, d2) == True:
                    dr1 = Basic.Vc.unit(d2)
                    dr2 = Basic.Vc.unit(d3)
                else:
                    dr1 = Basic.Vc.unit(d1)
                    dr2 = Basic.Vc.unit(d2)
                Output = [OutSupport, dr1, dr2]
                return Output
            def coord(support, normal):
                a = normal.x
                b = normal.y
                c = normal.z
                d = -1 * Basic.Vc.sproduct(normal, Basic.Vc.smulti(support, -1))
                Output = [a, b, c, d]
                return Output
        class Coord:
            def norm(a, b, c, d):
                normal = Basic.Vc.unit(Vector(a, b, c))
                if a != 0:
                    support = Vector(d / a, 0, 0)
                elif b != 0:
                    support = Vector(0, d / b, 0)
                else:
                    support = Vector(0, 0, d / c)
                Output = [support, normal]
                return Output
            def par(a, b, c, d):
                help = Conv.Pl.Coord.norm(a, b, c, d)
                Output = Conv.Pl.Norm.par(help[0], help[1])
                return Output
        class Pt:
            def par(aa,bb,cc):
                dr1 = Basic.Vc.minus(bb.ov, aa.ov)
                dr2 = Basic.Vc.minus(cc.ov, aa.ov)
                support = aa
                Output = [support,dr1,dr2]
                return Output
            def norm(aa,bb,cc):
                help = Conv.Pl.Pt.par(aa,bb,cc)
                Output = Conv.Pl.Par.norm(help[0],help[1],help[2])
            def coord(aa,bb,cc):
                help = Conv.Pl.Pt.par(aa,bb,cc)
                Output = Conv.Pl.Par.coord(help[0],help[1],help[2])
        class Fxy:
            def par(aa):
                help = Conv.Pl.Fxy.coord(aa)
                Output = Conv.Pl.Coord.par(help[0],help[1],help[2],help[3])
                return Output
            def norm(aa):
                help = Conv.Pl.Fxy.coord(aa)
                Output = Conv.Pl.Coord.norm(help[0],help[1],help[2],help[3])
                return Output
            def coord(aa):
                if aa[0] != 0:
                    a = aa[1];
                    b = aa[2];
                    c = -1*aa[0];
                    d = -1*aa[3];
                    Output = [a,b,c,d]
                    return Output
                else:
                    sys.exit("Die Nullgleichung ist keine Ebene.")
    class Ln:
        class Pt:
            def par(aa,bb):
                support = aa.ov
                direction = Basic.Vc.minus(bb.ov,aa.ov)
                Output = [support,direction]
                return Output
    class LGS:
        class Pl:
            def mtx(aa,bb,cc):
                OutMtx = Matrix(aa.a,aa.b,aa.c,bb.a,bb.b,bb.c,cc.a,cc.b,cc.c)
                OutVec = Vector(aa.d,bb.d,cc.d)
                Output = [OutMtx,OutVec]
                return Output
    def pt2vc(aa):
        Output = Vector(aa.x,aa.y,aa.z)
        return Output
    def vc2pt(aa):
        Output = Point(aa.x,aa.y,aa.z)
        return Output
### Basics
class Basic:
    class Vc:
        def plus(aa,bb):
            Output = Vector(aa.x + bb.x, aa.y + bb.y, aa.z + bb.z)
            return Output
        def minus(aa,bb):
            Output = Vector(aa.x - bb.x, aa.y - bb.y, aa.z - bb.z)
            return Output
        def smulti(aa,c):
            Output = Vector(aa.x*c, aa.y*c, aa.z*c)
            return Output
        def sproduct(aa,bb):
            Output = aa.x*bb.x + aa.y*bb.y + aa.z*bb.z
            return Output
        def vproduct(aa,bb):
            Outx = aa.y*bb.z - aa.z*bb.y
            Outy = aa.z*bb.x - aa.x*bb.z
            Outz = aa.x * bb.y - aa.y * bb.x
            Output = Vector(Outx,Outy,Outz)
            return Output
        def unit(aa):
            Output = Basic.Vc.smulti(aa,1/aa.l)
            return Output
        def lindep(aa,bb):
            Output = False
            if (aa.fullzero == True and bb.fullzero != True) or (aa.fullzero != True and bb.fullzero == True):
                Output = True
                return Output
            if aa.fullzero == True or bb.fullzero == True:
                return Output
            if aa.zerox != bb.zerox:
                return Output
            if aa.zeroy != bb.zeroy:
                return Output
            if aa.zeroz != bb.zeroz:
                return Output
            if aa.czero == False and bb.czero == False:
                a = round(1000000000000*(aa.x / bb.x))
                b = round(1000000000000*(aa.y / bb.y))
                c = round(1000000000000*(aa.z / bb.z))
                if a == b and a == c:
                    Output = True
                    return Output
                else:
                    Output = False
                    return Output
            if aa.zerox == True:
                if aa.zeroy == True or aa.zeroz == True:
                    Output = True
                    return Output
                else:
                    b = round(1000000000000*(aa.y / bb.y))
                    c = round(1000000000000*(aa.z / bb.z))
                    if b == c:
                        Output = True
                        return Output
                    else:
                        Output = False
                        return Output
            if aa.zeroy == True:
                if aa.zeroz == True:
                    Output = True
                    return Output
                else:
                    a = round(1000000000000*(aa.x / bb.x))
                    c = round(1000000000000*(aa.z / bb.z))
                    if a == c:
                        Output = True
                        return Output
                    else:
                        Output = False
                        return Output
            if aa.zeroz == True:
                a = round(1000000000000*(aa.x / bb.x))
                b = round(1000000000000*(aa.y / bb.y))
                if a == b:
                    Output = True
                    return Output
                else:
                    Output = False
                    return Output
            return Output
    class LGS:
        def det(aa):
            Output = 0
            Sum1 = aa.a11*aa.a22*aa.a33
            Sum2 = aa.a12*aa.a23*aa.a31
            Sum3 = aa.a13*aa.a21*aa.a32
            Min1 = aa.a31*aa.a22*aa.a13
            Min2 = aa.a32*aa.a23*aa.a11
            Min3 = aa.a33*aa.a21*aa.a12
            Output = (Sum1 + Sum2 + Sum3) - (Min1 + Min2 + Min3)
            return Output
        def solve(aa):
            if Basic.LGS.det(aa) == 0:
                sys.exit("Das Gleichungssystem hat keine eindeutige Lösung.")
            help1 = Matrix(aa.b1, aa.a12, aa.a13, aa.b2, aa.a22, aa.a23, aa.b3, aa.a32, aa.a33)
            help2 = Matrix(aa.a11, aa.b1, aa.a13, aa.a21, aa.b2, aa.a23, aa.a31, aa.b3, aa.a33)
            help3 = Matrix(aa.a11, aa.a12, aa.b1, aa.a21, aa.a22, aa.b2, aa.a31, aa.a32, aa.b3)
            ox = round(1000000000000*(Basic.LGS.det(help1) / Basic.LGS.det(aa.Mtx)))/1000000000000 #Auf 9. Nachkommastelle genau
            oy = round(1000000000000*(Basic.LGS.det(help2) / Basic.LGS.det(aa.Mtx)))/1000000000000 #Auf 9. Nachkommastelle genau
            oz = round(1000000000000*(Basic.LGS.det(help3) / Basic.LGS.det(aa.Mtx)))/1000000000000 #Auf 9. Nachkommastelle genau
            Output = Vector(ox,oy,oz)
            return Output
### Objects
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        l = sqrt(x*x + y*y + z*z); self.l = l
        fullzero = False
        if l == 0:
            fullzero = True
        self.fullzero = fullzero
        zerox = False; zeroy = False; zeroz = False; czero = False
        if x == 0:
            zerox = True
            czero = True
        if y == 0:
            zeroy = True
            czero = True
        if z == 0:
            zeroz = True
            czero = True
        self.zerox = zerox
        self.zeroy = zeroy
        self.zeroz = zeroz
        self.czero = czero
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        pt = (x,y,z); self.pt = pt
        ov = Vector(x,y,z); self.ov = ov
class Line:
    def __init__(self,support,dr):
        if dr.fullzero == True:
            sys.exit("Die Gerade konnte nicht enstehen. Der Richtungsvektor gleicht dem Nullvektor.")
        self.support = support
        self.dr = dr
        sPoint = Point(support.x, support.y, support.z); self.sPoint = sPoint
        basex = Vector(1, 0, 0)
        basey = Vector(0, 1, 0)
        basez = Vector(0, 0, 1)
        n1 = Basic.Vc.vproduct(dr, basex)
        n2 = Basic.Vc.vproduct(dr, basey)
        n3 = Basic.Vc.vproduct(dr, basez)
        if n1.fullzero == True:
            phelp1 = Conv.Pl.Norm.par(support, n2)
            phelp2 = Conv.Pl.Norm.par(support, n3)
        elif n2.fullzero == True:
            phelp1 = Conv.Pl.Norm.par(support, n1)
            phelp2 = Conv.Pl.Norm.par(support, n3)
        elif n3.fullzero == True:
            phelp1 = Conv.Pl.Norm.par(support, n1)
            phelp2 = Conv.Pl.Norm.par(support, n2)
        elif Basic.Vc.lindep(n1, n2) == True:
            phelp1 = Conv.Pl.Norm.par(support, n2)
            phelp2 = Conv.Pl.Norm.par(support, n3)
        else:
            phelp1 = Conv.Pl.Norm.par(support, n1)
            phelp2 = Conv.Pl.Norm.par(support, n2)
        plane1 = Plane(phelp1[0], phelp1[1], phelp1[2])
        plane2 = Plane(phelp2[0], phelp2[1], phelp2[2])
        self.plane1 = plane1
        self.plane2 = plane2
class Plane:
    def __init__(self,support,dr1,dr2):
        if Basic.Vc.lindep(dr1,dr2) == True:
            sys.exit("Ebene konnte nicht enstehen. Die Spannvektoren sind linear abhängig.")
        elif dr1.fullzero == True or dr2.fullzero == True:
            sys.exit("Ebene konnte nicht enstehen. Ein Spannvektor gleicht dem Nullvektor.")
        self.support = support
        sPoint = Point(support.x,support.y,support.z)
        self.sPoint = sPoint
        self.dr1 = dr1
        self.dr2 = dr2
        normal = Conv.Pl.Par.norm(support,dr1,dr2)[1]
        self.normal = normal
        coord = Conv.Pl.Par.coord(support,dr1,dr2)
        a = coord[0]; self.a = a
        b = coord[1]; self.b = b
        c = coord[2]; self.c = c
        d = coord[3]; self.d = d
        fxy = [0,0,0,0]
        if c != 0:
            fxy[0] = 1;
            fxy[1] = -a / c;
            fxy[2] = -b / c;
            fxy[3] = d / c;
        self.fxy = fxy
class Matrix:
    def __init__(self,a11,a12,a13,a21,a22,a23,a31,a32,a33):
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
    def __init__(self,Mtx,Vec):
        self.Mtx = Mtx
        self.Vec = Vec
        self.a11 = Mtx.a11
        self.a12 = Mtx.a12
        self.a13 = Mtx.a13
        self.a21 = Mtx.a21
        self.a22 = Mtx.a22
        self.a23 = Mtx.a23
        self.a31 = Mtx.a31
        self.a32 = Mtx.a32
        self.a33 = Mtx.a33
        self.b1 = Vec.x
        self.b2 = Vec.y
        self.b3 = Vec.z
### Containment
class Con:
    def point2(aa,bb):
        Output = True
        if aa.x == bb.x and aa.y == bb.y and aa.z == bb.z:
            Output == True
            return Output
        else:
            Output = False
            return Output
    def line2(aa,bb):#0 = error, 1 = identical, 2 = parallel, 3 = crosspoint, 4 = skewed
        Output = 0
        Zero = Point(0,0,0)
        Supp = Basic.Vc.minus(bb.support,aa.support)
        dire1 = Basic.Vc.smulti(aa.dr,-1)
        dire2 = bb.dr
        if Basic.Vc.lindep(aa.dr,bb.dr) == True:
            if Con.pointline(aa.sPoint,bb) == True:
                Output = 1
                return Output
            else:
                Output = 2
                return Output
        else:
            OutHelp = Plane(Supp, dire1, dire2)
            if OutHelp.d == 0:
                Output = 3
                return Output
            else:
                Output = 4
                return Output
    def plane2(aa,bb):#0 = error, 1 = identical, 2 = parallel, 3 = crossline
        Output = 0
        if Basic.Vc.lindep(aa.normal,bb.normal) == True:
            if Con.pointplane(aa.sPoint,bb) == True:
                Output = 1
                return Output
            else:
                Output = 2
                return Output
        else:
            Output = 3
            return Output
    def lineplane(ln,pl):#0 = error, 1 = identical, 2 = parallel, 3 = crosspoint
        Output = 0
        if Basic.Vc.sproduct(ln.dr,pl.normal) == 0:
            if Con.pointplane(ln.sPoint,pl) == True:
                Output = 1
                return Output
            else:
                Output = 2
                return Output
        else:
            Output = 3
            return Output
    def pointplane(pt,pl):
        Output = True
        if (round(1000000000000*(pt.x * pl.a + pt.y * pl.b + pt.z * pl.c)) == round(1000000000000*pl.d)):#Auf 9. Nachkommastelle genau
            Output = True
            return Output
        else:
            Output = False
            return Output
    def pointline(pt,ln):
        help = Basic.Vc.minus(pt.ov,ln.support)
        Output = Basic.Vc.lindep(help,ln.dr)
        return Output
### Distance
class Dis:
    def point2(aa,bb):
        Output = Basic.Vc.minus(aa,bb).l
        return Output
    def line2(aa,bb):
        Output = 0
        Zero = Point(0, 0, 0)
        Supp = Basic.Vc.minus(bb.support, aa.support)
        dire1 = Basic.Vc.smulti(aa.dr, -1)
        dire2 = bb.dr
        if Con.line2(aa,bb) == 1 or Con.line2(aa,bb) == 3:
            Output = 0
            return Output
        elif Con.line2(aa,bb) == 2:
            Output = abs(Dis.pointline(aa.sPoint,bb))
            return Output
        else:
            OutHelp = Plane(Supp, dire1, dire2)
            Output = abs(Dis.pointplane(Zero,OutHelp))
            return Output
    def plane2(aa,bb):
        Output = 0
        if Con.plane2(aa,bb) == 1 or Con.plane2(aa,bb) == 3:
            Output = 0
            return Output
        else:
            Output = abs(Dis.pointplane(aa.sPoint,bb))
            return Output
    def lineplane(ln,pl):
        Output = 0
        if Con.lineplane(ln,pl) == 1 or Con.lineplane(ln,pl) == 3:
            Output = 0
            return Output
        else:
            Output = abs(Dis.pointplane(ln.sPoint,pl))
            return Output
    def pointplane(pt,pl):
        Output = abs(round(1000000000000*(pt.x * pl.a + pt.y * pl.b + pt.z * pl.c - pl.d))/1000000000000) #Auf 9. Nachkommastelle genau
        return Output
    def pointline(pt,ln):
        hh = Conv.Pl.Norm.par(pt.ov,ln.dr)
        Help = Plane(hh[0],hh[1],hh[2])
        Root = Cross.lineplane(ln,Help)
        Output = abs(Dis.point2(pt,Root))
        return Output
#Crossarea
class Cross:
    def line2(aa,bb):
        Output = Point(0,0,0)
        if Con.line2(aa,bb) != 3:
            sys.exit("Es gibt keinen eindeutigen Schnittpunkt zwischen den beiden Geraden.")
        help1 = LGS(Conv.LGS.Pl.mtx(aa.plane1, aa.plane2, bb.plane1)[0], Conv.LGS.Pl.mtx(aa.plane1, aa.plane2, bb.plane1)[1])
        help2 = LGS(Conv.LGS.Pl.mtx(aa.plane1, aa.plane2, bb.plane2)[0], Conv.LGS.Pl.mtx(aa.plane1, aa.plane2, bb.plane2)[1])
        if Basic.LGS.det(help1.Mtx) == 0:
            Out = help2
        else:
            Out = help1
        Output = Conv.vc2pt(Basic.LGS.solve(Out))
        return Output
    def lineplane(ln,pl):
        if Con.lineplane(ln,pl) != 3:
            sys.exit("Es gibt keinen eindeutigen Schnittpunkt zwischen der Gerade und der Ebene.")
        help = LGS(Conv.LGS.Pl.mtx(ln.plane1, ln.plane2, pl)[0], Conv.LGS.Pl.mtx(ln.plane1, ln.plane2, pl)[1])
        Output = Conv.vc2pt(Basic.LGS.solve(help))
        return Output
    def plane2(aa,bb):
        if Con.plane2(aa,bb) != 3:
            sys.exit("Die beiden Ebenen haben keine eindeutige Schnittgerade.")
        Wallx1 = Plane(Conv.Pl.Coord.par(1, 0, 0, 0)[0], Conv.Pl.Coord.par(1, 0, 0, 0)[1], Conv.Pl.Coord.par(1, 0, 0, 0)[2])
        Wallx2 = Plane(Conv.Pl.Coord.par(1, 0, 0, 1)[0], Conv.Pl.Coord.par(1, 0, 0, 1)[1], Conv.Pl.Coord.par(1, 0, 0, 1)[2])
        Wally1 = Plane(Conv.Pl.Coord.par(0, 1, 0, 0)[0], Conv.Pl.Coord.par(0, 1, 0, 0)[1], Conv.Pl.Coord.par(0, 1, 0, 0)[2])
        Wally2 = Plane(Conv.Pl.Coord.par(0, 1, 0, 1)[0], Conv.Pl.Coord.par(0, 1, 0, 1)[1], Conv.Pl.Coord.par(0, 1, 0, 1)[2])
        Wallz1 = Plane(Conv.Pl.Coord.par(0, 0, 1, 0)[0], Conv.Pl.Coord.par(0, 0, 1, 0)[1], Conv.Pl.Coord.par(0, 0, 1, 0)[2])
        Wallz2 = Plane(Conv.Pl.Coord.par(0, 0, 1, 1)[0], Conv.Pl.Coord.par(0, 0, 1, 1)[1], Conv.Pl.Coord.par(0, 0, 1, 1)[2])
        lgs1 = LGS(Conv.LGS.Pl.mtx(aa, bb, Wallx1)[0], Conv.LGS.Pl.mtx(aa, bb, Wallx1)[1])
        lgs2 = LGS(Conv.LGS.Pl.mtx(aa, bb, Wallx2)[0], Conv.LGS.Pl.mtx(aa, bb, Wallx2)[1])
        lgs3 = LGS(Conv.LGS.Pl.mtx(aa, bb, Wally1)[0], Conv.LGS.Pl.mtx(aa, bb, Wally1)[1])
        lgs4 = LGS(Conv.LGS.Pl.mtx(aa, bb, Wally2)[0], Conv.LGS.Pl.mtx(aa, bb, Wally2)[1])
        lgs5 = LGS(Conv.LGS.Pl.mtx(aa, bb, Wallz1)[0], Conv.LGS.Pl.mtx(aa, bb, Wallz1)[1])
        lgs6 = LGS(Conv.LGS.Pl.mtx(aa, bb, Wallz2)[0], Conv.LGS.Pl.mtx(aa, bb, Wallz2)[1])
        if Basic.LGS.det(lgs1) != 0 and Basic.LGS.det(lgs2) != 0:
            Out1 = Conv.vc2pt(Basic.LGS.solve(lgs1))
            Out2 = Conv.vc2pt(Basic.LGS.solve(lgs2))
            Output = Line(Conv.Ln.Pt.par(Out1,Out2)[0],Conv.Ln.Pt.par(Out1,Out2)[1])
            return Output
        elif Basic.LGS.det(lgs3) != 0 and Basic.LGS.det(lgs4) != 0:
            Out1 = Conv.vc2pt(Basic.LGS.solve(lgs3))
            Out2 = Conv.vc2pt(Basic.LGS.solve(lgs4))
            Output = Line(Conv.Ln.Pt.par(Out1,Out2)[0],Conv.Ln.Pt.par(Out1,Out2)[1])
            return Output
        else:
            Out1 = Conv.vc2pt(Basic.LGS.solve(lgs5))
            Out2 = Conv.vc2pt(Basic.LGS.solve(lgs6))
            Output = Line(Conv.Ln.Pt.par(Out1, Out2)[0], Conv.Ln.Pt.par(Out1, Out2)[1])
            return Output

