import dvc.api
import json
import yaml
import os

from sdRDM import DataModel
from sdRDM.linking.nodes import ClassNode, AttributeNode
from sdRDM.tools.utils import YAMLDumper


def parse_dvc_repo():
    """
    Parses a Data Version Control repository and returns an EasyDataverse
    Dataset object that can be uploaded to a Dataverse installation.
    """

    # Load all necessary files
    dvc_file = yaml.safe_load(open("dvc.yaml"))
    params = dvc.api.params_show()
    MetaNode = DataModel.from_git(url="https://github.com/JR-1991/dvc-data-model.git")
    dataset = MetaNode()

    for step, (node, stage) in enumerate(dvc_file["stages"].items()):
        # Add node information
        dataset.add_to_nodes(
            step=step + 1,
            name=node,
            dependencies=stage["deps"],
            inputs=[],
            command=stage["cmd"],
        )

        # Add parameters
        if node in params:
            add_parameters(params[node], node, dataset=dataset)

        # Add metrics
        if "metrics" in stage:
            for metric in stage["metrics"]:
                for metric_path in metric.keys():
                    add_metrics(metric_path, dataset)

    return dataset


def add_parameters(parameters, stage, dataset):
    for name, value in parameters.items():
        # Add parameters
        dataset.add_to_parameters(name, value)

        # Add to inputs
        node = dataset.nodes.get(stage, "name")
        node[0].inputs.append(name)


def add_metrics(path, dataset):
    metrics = json.load(open(path))
    for name, value in metrics.items():
        dataset.add_to_metrics(name=name, value=value)


def main():
    print(os.listdir())
