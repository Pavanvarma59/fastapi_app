# TODO - Iris Flower Classification (Classic ML) FastAPI

- [x] Install classic ML deps (scikit-learn, numpy, pandas) and update `requirements.txt`.


- [x] Update `app/schemas.py` to define request/response models for Iris prediction.

- [x] Rewrite `app/main.py`:

  - [x] Train/load a classic ML model on Iris dataset at startup.


  - [x] Add `POST /predict` endpoint accepting 4 numeric features.
  - [x] Keep `GET /health` and update `GET /`.

- [x] Update `README.md` with run + example `curl`.

- [x] Run `uvicorn` and perform a quick prediction test.


