from zntrack import config
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, confusion_matrix
from zntrack import Node, NodeConfig, dvc, nodify, utils, zn


class DatasetPreparation(Node):
    """Loads dataset from scikit-learn and splits into train/test"""
    
    # Parameters
    seed: int = zn.params("seed")
    split: float = zn.params("split")
    
    # Outputs
    x_train: np.ndarray = zn.outs()
    y_train: np.ndarray = zn.outs()
    x_test: np.ndarray = zn.outs()
    y_test: np.ndarray = zn.outs()
    
    def run(self):
        """The run method defines what the node process looks like"""
        
        # Get dataset
        dataset = load_breast_cancer()
        
        # Extract everything
        feature_names = dataset["feature_names"]
        X = dataset["data"]
        Y = dataset["target"]
        
        # Split dataset and assign to outs
        splitted = train_test_split(X, Y, train_size=self.split, random_state=self.seed)
        self.x_train = splitted[0]
        self.x_test = splitted[1]
        self.y_train = splitted[2]
        self.y_test = splitted[3]


# ### Model training
# 
# __Tasks__
# - Initialize model using given parameters
# - Fit the model to the training dataset

# In[5]:


# zntrack: break
class GradientBoosting(Node):
    """Sets up the ML model and trains it using the data dependency object"""
    
    # Dependencies
    data: DatasetPreparation = zn.deps(DatasetPreparation)
    
    # Parameters
    learning_rate: float = zn.params()
    max_depth: int = zn.params()
    n_estimators: int = zn.params()

    # Outputs
    model: xgb.XGBClassifier = zn.outs()
    
    def run(self):
        self.model = xgb.XGBClassifier(
            learning_rate = self.learning_rate,
            max_depth = self.max_depth,
            n_estimators = self.n_estimators
        )
        
        self.model.fit(self.data.x_train, self.data.y_train)


# ### Model evaluation
# 
# __Tasks__
# - Calculate accuracy and F1 score to determine performance

# In[6]:


# zntrack: break
class ModelEvaluation(Node):
    """Tests the ML model and gathers performance metrics"""
    
    # Dependencies
    data: DatasetPreparation = zn.deps(DatasetPreparation)
    gb: GradientBoosting = zn.deps(GradientBoosting)
    
    # Metrics
    acc: float = zn.metrics()
    f1_score: float = zn.metrics()
    
    def run(self):
        
        # Get predictions on test
        preds = self.gb.model.predict(self.data.x_test)
        
        # Derive metrics
        self.acc = accuracy_score(self.data.y_test, preds)
        self.f1_score = f1_score(self.data.y_test, preds)
        


# ### Building the workflow
# 
# Now that all classes have beenm set up, the DAG graph has to be written. ZnTrack takes care to preserve dependencies and any other in- and output that was specified within these classes. Ultimately, ZnTrack takes care of all necessary DVC operations that may otherwise have been carried out in a terminal.
# 
# Optionally, all changes could be pushed onto a GitHub/GitLab repository, where one can make use of Actions to perform parameter studies. See `.github/workflows/cml.yaml` for the workflow. Use this workflow as a template for your own examples!

# In[7]:


# Write a DAG graph to gain DVC compatibility
