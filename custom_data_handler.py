# your import statements

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from ibmfl.data.data_handler import DataHandler

class custom_data_handler(DataHandler):
    """
    Data handler for your dataset.
    """
    def __init__(self, data_config=None):
        super().__init__()
        self.file_name = None
        if data_config is not None:
            if 'csv_file' in data_config:
                self.file_name = data_config['csv_file']
            # extract other additional parameters from `info` if any.

        # load and preprocess the training and testing data
        self.load_and_preprocess_data()

        """
        # Example:
        # (self.x_train, self.y_train), (self.x_test, self.y_test) = self.load_dataset()
        """

    def load_and_preprocess_data(self):
        """
        Loads and pre-processeses local datasets, 
        and updates self.x_train, self.y_train, self.x_test, self.y_test.
 
        # Example:
        # return (self.x_train, self.y_train), (self.x_test, self.y_test)
        """
        if self.file_name is None:
            raise FLException(
            'No data file name is provided to load the dataset.')
        else:
                print('Loaded training data from' + str(self.file_name))
                rms_data = pd.read_csv(self.file_name, allow_pickle=True)
                X, y = rms_data.drop('rms',axis=1), rms_data['rms']
                print('Shape of X:', X.shape)
                print('Shape of y:', y.shape)
                X = np.array(X)
                y = np.array(y)
                #80-20 split
                self.x_train, self.x_test, self.y_train, self.y_test =\
                    train_test_split(X,y,test_size=0.2, random_state=42)


    
    def get_data(self):
        """
        Gets the prepared training and testing data.
        
        :return: ((x_train, y_train), (x_test, y_test)) # most build-in training modules expect data is returned in this format
        :rtype: `tuple` 

        This function should be as brief as possible. Any pre-processing operations should be performed in a separate function and not inside get_data(), especially computationally expensive ones.

        # Example:
        # X, y = load_somedata()
        # x_train, x_test, y_train, y_test = \
        # train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)
        # return (x_train, y_train), (x_test, y_test)
        """
        return (self.x_train, self.y_train), (self.x_test, self.y_test)
