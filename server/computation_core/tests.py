from django.test import TestCase
import computation_core.math_core as mc
import json
import numpy as np
import time


class MathCoreTestCase(TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        """Simple test case"""
        expr = "x**2"
        mvars = [{'name': 'x', 'min': 1, 'max':1, 'step': 1}]
        mvars_json = json.dumps(mvars)
        mvars_obj = mc.mvars_from_json(mvars_json)
        res = list(mc.compute_math(expr, mvars_obj))
        self.assertEquals(res, [({'x': 1}, np.array(1, dtype='int64'))])

    def test_few_simple(self):
        expr = "x**2"
        mvars = [{'name': 'x', 'min': 1, 'max': 10, 'step': 1}]
        mvars_json = json.dumps(mvars)
        mvars_obj = mc.mvars_from_json(mvars_json)
        res = list(mc.compute_math(expr, mvars_obj))
        self.assertEquals(res, [
            ({'x': 1}, np.array(1, dtype='int64')),
            ({'x': 2}, np.array(4, dtype='int64')),
            ({'x': 3}, np.array(9, dtype='int64')),
            ({'x': 4}, np.array(16, dtype='int64')),
            ({'x': 5}, np.array(25, dtype='int64')),
            ({'x': 6}, np.array(36, dtype='int64')),
            ({'x': 7}, np.array(49, dtype='int64')),
            ({'x': 8}, np.array(64, dtype='int64')),
            ({'x': 9}, np.array(81, dtype='int64')),
            ({'x': 10}, np.array(100, dtype='int64')),
            ])
    
    def test_complex(self):
        """One test  with 2 vars """
        expr = "x**2 + y**2"
        mvars = [{'name': 'x', 'min': 1, 'max': 1, 'step': 1},
                 {'name': 'y', 'min': 1, 'max': 1, 'step': 1},]
        mvars_json = json.dumps(mvars)
        mvars_obj = mc.mvars_from_json(mvars_json)
        res = list(mc.compute_math(expr, mvars_obj))
        self.assertEquals(res, [({'x': 1, 'y': 1}, np.array(2, dtype='int64'))])

    def test_few_complex(self):
        """Few test  with 2 vars """
        expr = "x**2 + y**2"
        mvars = [{'name': 'x', 'min': 1, 'max': 2, 'step': 1},
                 {'name': 'y', 'min': 1, 'max': 3, 'step': 1},
                 ]
        mvars_json = json.dumps(mvars)
        mvars_obj = mc.mvars_from_json(mvars_json)
        res = list(mc.compute_math(expr, mvars_obj))
        self.assertEquals(res, [
                                ({'x': 1, 'y': 1}, np.array(2, dtype='int64')),
                                ({'x': 2, 'y': 1}, np.array(5, dtype='int64')),
                                ({'x': 1, 'y': 2}, np.array(5, dtype='int64')),
                                ({'x': 2, 'y': 2}, np.array(8, dtype='int64')),
                                ({'x': 1, 'y': 3}, np.array(10,
                                                            dtype='int64')),
                                ({'x': 2, 'y': 3}, np.array(13,
                                                            dtype='int64')),
                                ])
    
   
