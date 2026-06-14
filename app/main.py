from __future__ import annotations

from typing import Dict, List

import numpy as np
from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from .schemas import IrisFeatures, IrisPrediction

app = FastAPI(title="Iris Flower Classification (Classic ML)", version="0.1.0")


MODEL = None
CLASS_NAMES: List[str] = []


@app.on_event("startup")
def load_and_train_model() -> None:
    """Train a classic ML model on the built-in Iris dataset."""

    global MODEL, CLASS_NAMES

    iris = load_iris()
    X = iris.data  # shape: (150, 4)
    y = iris.target

    # Logistic Regression is fast and works well as a classic baseline.
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    MODEL = model
    CLASS_NAMES = list(iris.target_names)


def _predict(features: IrisFeatures) -> IrisPrediction:
    if MODEL is None or not CLASS_NAMES:
        raise RuntimeError("Model not loaded. Server startup may not have finished.")

    x = np.array(
        [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width,
        ]],
        dtype=float,
    )

    pred_idx = int(MODEL.predict(x)[0])
    probs = MODEL.predict_proba(x)[0]

    probabilities: Dict[str, float] = {
        CLASS_NAMES[i]: float(probs[i]) for i in range(len(CLASS_NAMES))
    }

    return IrisPrediction(
        predicted_class=CLASS_NAMES[pred_idx],
        probabilities=probabilities,
    )


@app.get("/")
def read_root():
    return {
        "message": "Iris Flower Classification (Classic ML) API",
        "predict_endpoint": "/predict",
        "features": {
            "sepal_length": "float",
            "sepal_width": "float",
            "petal_length": "float",
            "petal_width": "float",
        },
    }


# @app.get("/health")
# def health():
#     return {"status": "ok"}


@app.post("/predict", response_model=IrisPrediction)
def predict(payload: IrisFeatures):
    return _predict(payload)

