# -*- coding: utf-8 -*-
"""Testing fmu-ensemble."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from fmu import config
from fmu.tools import sensitivities

fmux = config.etc.Interaction()
logger = fmux.basiclogger(__name__)

if not fmux.testsetup():
    raise SystemExit()


def test_designsummary():
    """Test import and summary of design matrix"""

    if '__file__' in globals():
        # Easen up copying test code into interactive sessions
        testdir = os.path.dirname(os.path.abspath(__file__))
    else:
        testdir = os.path.abspath('.')

    snorrebergdesign = sensitivities.summarize_design(
                      testdir +
                      '/data/sensitivities/distributions/' +
                      'design.xlsx',
                      'DesignSheet01')
    # checking dimensions and some values in summary of design matrix
    assert snorrebergdesign.shape == (7, 9)
    assert snorrebergdesign['sensname'][0] == 'seed'
    assert snorrebergdesign['startreal2'][6] == 100
    assert snorrebergdesign['endreal2'][6] == 109
    assert snorrebergdesign['endreal1'].sum() == 333

    # Test same also when design matrix is in .csv format
    designcsv = sensitivities.summarize_design(
                testdir +
                '/data/sensitivities/distributions/' +
                'design.csv')

    # checking dimensions and some values in summary of design matrix
    assert designcsv.shape == (7, 9)
    assert designcsv['sensname'][0] == 'seed'
    assert designcsv['startreal2'][6] == 100
    assert designcsv['endreal2'][6] == 109
    assert designcsv['endreal1'].sum() == 333