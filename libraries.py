 ############################# needed library ############################
from natsort import natsorted
import csv
import numpy as np
import os
import scipy.io
import scipy as sp 
import matplotlib.pyplot as plt
from scipy import signal
from pywt import wavedec
from sklearn.decomposition import FastICA, PCA
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pywt
from sklearn import metrics
from scipy.signal import welch
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import timeit
import numpy as np, cmath,scipy as sp
import scipy.io
from matplotlib import pyplot as plt
from scipy.signal import butter, lfilter
from numpy import pi, sin, cos, exp, sqrt, log, log10, random, angle  #import basic functions from numpy that we'll need
from numpy.fft import fft, ifft
import pickle
import seaborn as sns
sns.set_palette('muted')
sns.set_style('darkgrid')
from IPython import display
from sklearn.model_selection import cross_val_score
from sklearn import svm
import pandas as pd
from sklearn.decomposition import FastICA
############################ global variables used  ##################################