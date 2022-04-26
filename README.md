<h1 align="center">
  Data Version Control and ZnTrack for ML
</h1>

<h4 align="center">ML-Session 27.4.2022, University of Stuttgart
</h4>

[![DVC](https://img.shields.io/badge/-tracked-white.svg?logo=data-version-control&link=https://dvc.org/?utm_campaign=badge)](https://studio.iterative.ai/user/JR-1991/views/MLSession_Boosting_DVC-dj8z1mdwzf)
 [![ZnTrack](https://img.shields.io/badge/Powered%20by-ZnTrack-%23007CB0)](https://zntrack.readthedocs.io/en/latest/)

The following notebook will demonstrate how to implement a simple Gradient Boosting workflow using [ZnTrack](https://github.com/zincware/ZnTrack) and [DVC](https://dvc.org). These libraries/concepts faciliate a convenient way to set up workflows using Directed Acyclic Graphs that represent steps in the Machine Learning life cycle.

The following steps will be implemented using an OOP-based approach:

- Dataset loading and preparation
- Model training
- Model evaluation

For the sake of demonstration, the following workflow is held simple on purpose yet DVC and ZnTrack are capable of far more complex workflows. See [this example](https://github.com/PythonFZ/SimTech_2022_04) for an advanced example.
