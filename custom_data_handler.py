{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "dd1b316e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_18124/2988493917.py, line 52)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\cix139\\AppData\\Local\\Temp/ipykernel_18124/2988493917.py\"\u001b[1;36m, line \u001b[1;32m52\u001b[0m\n\u001b[1;33m    pass\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# your import statements\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "from ibmfl.data.data_handler import DataHandler\n",
    "\n",
    "class custom_data_handler(DataHandler):\n",
    "    \"\"\"\n",
    "    Data handler for your dataset.\n",
    "    \"\"\"\n",
    "    def __init__(self, data_config=None):\n",
    "        super().__init__()\n",
    "        self.file_name = None\n",
    "        if data_config is not None:\n",
    "            if 'csv_file' in data_config:\n",
    "                self.file_name = data_config['csv_file']\n",
    "            # extract other additional parameters from `info` if any.\n",
    "\n",
    "        # load and preprocess the training and testing data\n",
    "        self.load_and_preprocess_data()\n",
    "\n",
    "        \"\"\"\n",
    "        # Example:\n",
    "        # (self.x_train, self.y_train), (self.x_test, self.y_test) = self.load_dataset()\n",
    "        \"\"\"\n",
    "\n",
    "    def load_and_preprocess_data(self):\n",
    "        \"\"\"\n",
    "        Loads and pre-processeses local datasets, \n",
    "        and updates self.x_train, self.y_train, self.x_test, self.y_test.\n",
    " \n",
    "        # Example:\n",
    "        # return (self.x_train, self.y_train), (self.x_test, self.y_test)\n",
    "        \"\"\"\n",
    "        if self.file_name is None:\n",
    "            raise FLException(\n",
    "            'No data file name is provided to load the dataset.')\n",
    "        else:\n",
    "            try:\n",
    "                print('Loaded training data from' + str(self.file_name))\n",
    "                rms_data = pd.read_csv(self.file_name, allow_pickle=True)\n",
    "                X, y = rms_data.drop('rms',axis=1), rms_data['rms']\n",
    "                print('Shape of X:', X.shape)\n",
    "                print('Shape of y:', y.shape)\n",
    "                X = np.array(X)\n",
    "                y = np.array(y)\n",
    "                #70-30 split\n",
    "                self.x_train, self.x_test, self.y_train, self.y_test =\\\n",
    "                    train_test_split(X,y,test_size=0.2, random_state=42)\n",
    "            pass\n",
    "\n",
    "\n",
    "    \n",
    "    def get_data(self):\n",
    "        \"\"\"\n",
    "        Gets the prepared training and testing data.\n",
    "        \n",
    "        :return: ((x_train, y_train), (x_test, y_test)) # most build-in training modules expect data is returned in this format\n",
    "        :rtype: `tuple` \n",
    "\n",
    "        This function should be as brief as possible. Any pre-processing operations should be performed in a separate function and not inside get_data(), especially computationally expensive ones.\n",
    "\n",
    "        # Example:\n",
    "        # X, y = load_somedata()\n",
    "        # x_train, x_test, y_train, y_test = \\\n",
    "        # train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)\n",
    "        # return (x_train, y_train), (x_test, y_test)\n",
    "        \"\"\"\n",
    "        return (self.x_train, self.y_train), (self.x_test, self.y_test)\n",
    "        \n",
    "        pass\n",
    "\n",
    "    def preprocess(self, X, y):\n",
    "        pass\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "096fcf80",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
