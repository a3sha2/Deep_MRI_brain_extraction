"""
This software is an implementation of

Deep MRI brain extraction: A 3D convolutional neural network for skull stripping

You can download the paper at http://dx.doi.org/10.1016/j.neuroimage.2016.01.024

If you use this software for your projects please cite:

Kleesiek and Urban et al, Deep MRI brain extraction: A 3D convolutional neural network for skull stripping,
NeuroImage, Volume 129, April 2016, Pages 460-469.

The MIT License (MIT)

Copyright (c) 2016 Gregor Urban, Jens Kleesiek

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from .file_reading import *
from .helper_seg import helper_seg
from .maxPool3D import maxPool3D
from .NN_Analyzer import NN_Analyzer
from .NN_ConvLayer_2D import NN_ConvLayer_2D
from .NN_ConvLayer_3D import NN_ConvLayer_3D
from .NN_ConvNet import NN_ConvNet
from .NN_Optimizers import NN_Optimizers
from .NN_PerceptronLayer import NN_PerceptronLayer
from .NN_regularizers import NN_regularizers
from .save_scores_in_r_format import save_scores_in_r_format
from .Segmentation_predictor  import Segmentation_predictor
from .Segmentation_trainer  import Segmentation_trainer
from .TransferFunctions import TransferFunctions
from .utilities import  utilities






