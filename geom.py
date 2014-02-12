# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Paul Norman
# <penorman@mac.com>
# Released under the MIT license: http://opensource.org/licenses/mit-license.php

# Classes
class Geometry(object):
    elementIdCounterIncr = -1
    roundingDigits = 9
    geometries = []


    @classmethod
    def getNewID(cls):
        cls.elementIdCounter += cls.elementIdCounterIncr
        return cls.elementIdCounter
        
        
    @classmethod
    def append_to_geometries(cls, geom):
        cls.geometries.append(geom)


    @classmethod
    def round_coord(cls, coord):
        return round(coord, cls.roundingDigits)
        


    def __init__(self):
        self.id = self.getNewID()
        Geometry.append_to_geometries(self)
        
        

        
class Node(Geometry):

    elementIdCounter = 0
    node_index = {}
    
    # Never build a Node directly, use Node.get_node(x, y) instead
    def __init__(self, x, y):
        super(Node, self).__init__()
        self.x = x
        self.y = y
        
    @classmethod
    def get_node(cls, x, y):
        rx = cls.round_coord(x)
        ry = cls.round_coord(y)
        node = cls.node_index.get((rx, ry), None)
        if not node:
            node = Node(x, y)
            cls.node_index[(rx, ry)] = node
        return node
        
    
    @property
    def lon(self):
        return self.round_coord(self.x)
        
        
    @property
    def lat(self):
        return self.round_coord(self.y)
        
        
        

class Way(Geometry):

    elementIdCounter = 0

    def __init__(self):
        super(Way, self).__init__()
        self.nodes = []
        
        
    def append_node(self, node):
        if len(self.nodes) == 0 or node != self.nodes[-1]:
            self.nodes.append(node)
        

class Relation(Geometry):

    elementIdCounter = 0

    def __init__(self):
        super(Relation, self).__init__()
        self.members = []
        
    def append_member(self, member):
        self.members.append(member)
        
        
class Feature(object):
    features = []

    def __init__(self):
        super(Feature, self).__init__()
        self.geometry = None
        self.tags = {}
        Feature.features.append(self)


    def set_geometry(self, geometry):
        self.geometry = geometry


