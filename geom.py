# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Paul Norman
# <penorman@mac.com>
# Released under the MIT license: http://opensource.org/licenses/mit-license.php

class ItemWithParents(object):
    
    def __init__(self):
        self.parents = set()
        
        
    def addparent(self, parent):
        self.parents.add(parent)


    def removeparent(self, parent, shoulddestroy=True):
        self.parents.discard(parent)
        if shoulddestroy and len(self.parents) == 0:
            self.remove_object(self)


    def replacejwithi(self, i, j):
        j.removeparent(self)
        i.addparent(self)
        
    @classmethod
    def remove_object(cls):
        pass

    
# Classes
class Geometry(ItemWithParents):
    elementIdCounterIncr = -1
    geometries = []


    @classmethod
    def getNewID(cls):
        cls.elementIdCounter += cls.elementIdCounterIncr
        return cls.elementIdCounter
        
    @classmethod
    def append_to_geometries(cls, geom):
        cls.geometries.append(geom)


    @classmethod
    def remove_object(cls):
        cls.geometries.remove(geom)


    def __init__(self):
        super(Geometry, self).__init__()
        self.id = self.getNewID()
        Geometry.append_to_geometries(self)


class Point(Geometry):

    elementIdCounter = 0
    
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x = x
        self.y = y
        
        

class Way(Geometry):

    elementIdCounter = 0

    def __init__(self):
        super(Way, self).__init__()
        self.points = []
        
        
    def replacejwithi(self, i, j):
        self.points = [i if x == j else x for x in self.points]
        super(Way, self).replacejwithi(i, j)


class Relation(Geometry):

    elementIdCounter = 0

    def __init__(self):
        super(Relation, self).__init__()
        self.members = []
        
        
    def replacejwithi(self, i, j):
        self.members = [(i, x[1]) if x[0] == j else x for x in self.members]
        super(Relation, self).replacejwithi(i, j)        


class Feature(ItemWithParents):
    features = []

    def __init__(self):
        super(Feature, self).__init__()
        self.geometry = None
        self.tags = {}
        Feature.features.append(self)


    def set_geometry(self, geometry):
        self.geometry = geometry
        if geometry:
            geometry.addparent(self)


    # ?????
    def replacejwithi(self, i, j):
        if self.geometry == j:
            self.geometry = i
        super(Feature, self).replacejwithi(i, j)

