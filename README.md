# Data Version Control and ZnTrack for ML
#### ML-Session 27.4.2022, University of Stuttgart

The following notebook will demonstrate how to implement a simple Gradient Boosting workflow using [ZnTrack](https://github.com/zincware/ZnTrack) and [DVC](https://dvc.org). These libraries/concepts faciliate a convenient way to set up workflows using Directed Acyclic Graphs that represent steps in the Machine Learning life cycle.

The following steps will be implemented using an OOP-based approach:

- Dataset loading and preparation
- Model training
- Model evaluation

For the sake of demonstration, the following workflow is held simple on purpose yet DVC and ZnTrack are capable of far more complex workflows. See [this example](https://github.com/PythonFZ/SimTech_2022_04) for an advanced example.