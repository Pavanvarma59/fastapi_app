# Iris Flower Classification (Classic ML) - FastAPI

Classic ML API that predicts the Iris species using a scikit-learn Logistic Regression model trained on the built-in Iris dataset.

## Endpoints

- `GET /`
  - Returns API info
- `GET /health`
  - Returns `{ "status": "ok" }`
- `POST /predict`
  - JSON body:
    - `sepal_length: number`
    - `sepal_width: number`
    - `petal_length: number`
    - `petal_width: number`
  - Response:
    - `predicted_class: string`
    - `probabilities: { class_name: probability }`

## Run (local)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Then open:
- http://localhost:8000/

## Docker (deploy)

### Build
```bash
docker build -t iris-api .
```

### Run
```bash
docker run -p 8000:8000 iris-api
```

Then open:
- http://localhost:8000/

## Example (curl)

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

