import numpy as np
import wradlib.util as util
import unittest


#-------------------------------------------------------------------------------
# testing the filter helper function
#-------------------------------------------------------------------------------
class TestUtil(unittest.TestCase):

   def img_setup(self):
        img = np.zeros((36,10), dtype=np.float32)
        img[2,2] = 1    # isolated pixel
        img[5,6:8] = 1 # line
        img[20,:] = 1     # spike
        img[9:12,4:7] = 1 # precip field
        #img[15:17,5:7] = np.nan # nodata as nans
        self.img = img
        pass
   def test_filter_window_polar(self):
        self.img_setup()
        np.set_printoptions(precision=3)
        rscale = 250
        nrays, nbins = self.img.shape
        ascale = 2*np.pi/self.img.shape[0]
        mean = util.filter_window_polar(self.img,300,"maximum",rscale)
        correct = np.array([[ 0.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                   [ 0.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                          [ 0.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                                 [ 0.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                                        [ 0.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.,  0.],
                                               [ 0.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,  1.,  0.],
                                                      [ 1.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  1.,  0.],
                                                             [ 1.,  1.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                    [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
                                                                           [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
                                                                                  [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
                                                                                         [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
                                                                                                [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
                                                                                                       [ 1.,  0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                                                              [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                     [ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                            [ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                   [ 1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                          [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                 [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
                                                                                                                                                        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
                                                                                                                                                               [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
                                                                                                                                                                      [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                             [ 1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                    [ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                           [ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                  [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                         [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                       [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                              [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                                     [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                                            [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                                                   [ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                                                          [ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                                                                                                                                                                                                                 [ 0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
        self.assertTrue((mean == correct).all())