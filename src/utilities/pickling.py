# Copyright (C) 2020 Yiqiu Shen, Nan Wu, Jason Phang, Jungkyu Park, Kangning Liu,
# Sudarshini Tyagi, Laura Heacock, S. Gene Kim, Linda Moy, Kyunghyun Cho, Krzysztof J. Geras
#
# This file is part of GMIC.
#
# GMIC is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# GMIC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with GMIC.  If not, see <http://www.gnu.org/licenses/>.
# ==============================================================================

"""
Defines utility functions for saving and loading pickles and tensorflow networks.
"""

import pickle


def pickle_to_file(file_name, data, protocol = pickle.HIGHEST_PROTOCOL):
    with open(file_name, 'wb') as handle:
        pickle.dump(data, handle, protocol)


def unpickle_from_file(file_name):
    with open(file_name, 'rb') as handle:

        return pickle.load(handle)

def unpickling_data():
    file = open(filename,'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data

def pickle_data():
    data  = [{'horizontal_flip': 'NO', 'L-CC': ['0_L-CC'],'best_center': {'L-CC': [(1011.0, -222.0)]}, 'cancer_label': {'benign': 1, 'right_benign': 1, 'malignant': 0, 'left_benign': 0, 'unknown': 0, 'right_malignant': 0, 'left_malignant': 0}, 'L-CC_benign_seg': ['0_L-CC_benign'], 'L-CC_malignant_seg': ['0_L-CC_malignant']}]
    filename = 'data_new'
    outfile = open(filename, 'wb')
    pickle.dump(data,outfile)
    outfile.close()
    
#pickle_data()
