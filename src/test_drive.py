import azure.ai.ml
import azure.identity
import mlflow
import torch
import torchvision

print(f"Azure AI ML version: {azure.ai.ml.__version__}.")
print(f"Azure Identity version: {azure.identity.__version__}.")
print(F"MLFlow version: {mlflow.__version__}.")
print(f"Torch version: {torch.__version__}.")
print(f"Torchvision version: {torchvision.__version__}.")
