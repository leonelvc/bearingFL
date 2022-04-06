#Leonel Villafranca

import logging

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#imports from ibmfl
from ibmfl.data.data_handler import DataHandler


logger = logging.getLogger(__name__)


class CustomDataHandler(DataHandler):

    def __init__(self,data_config=None):
        super().__init__()
        self.file_name = None
        if data_config is not None:
            if 'csv_file' in data_config:
                self.file_name = data_config['csv_file']
                

        #load dataset
        training_dataset = self.load_dataset()

        #pre-process the data
        self.training_dataset = self.preprocess(training_dataset)
        X,y = training_dataset.drop('rms',axis=1), training_dataset['rms']
        X = np.array(X)
        y = np.array(y)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X,y,test_size=0.2, random_state=42)
        
        

    def get_data(self):

        return (self.x_train, self.y_train),(self.x_test,self.y_test)

    def load_dataset(self):
        try:
            logger.info('Loaded training data from' + str(self.file_name))
            training_dataset = pd.read_csv(self.file_name)
        except Exception:
            raise IOError('Unable to load training data from path provided in config file:' + self.file_name)
        return training_dataset

        
                
                
