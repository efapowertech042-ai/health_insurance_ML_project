# Insurance Charges Predictor — Django

Collects age, sex, BMI, children, smoker status, and region from a user and
returns a predicted annual insurance charge, a 90% confidence interval, and a
low-confidence flag for predictions the model is less certain about.

## 1. Add the model artifacts

Run **Section 9 ("Deployment Prep")** of the training notebook. It exports:

```
gb_model.pkl      # point-estimate model (mean prediction)
gb_lower.pkl      # 5th percentile quantile model
gb_upper.pkl      # 95th percentile quantile model
metadata.pkl      # feature order, encoding maps, flag threshold, test metrics
```

Download `model_artifacts.zip` from Colab and unzip its contents into:

```
predictor/model_artifacts/
```

## 2. Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate        # creates db.sqlite3 (admin/auth tables only)
python manage.py runserver
```

Visit http://127.0.0.1:8000/

## 3. Deploy

Any host that runs Django works (Render, Railway, PythonAnywhere, Fly.io).
General steps for Render/Railway:

1. Push this project to GitHub (model artifacts included, or fetched at build time).
2. Set environment variables: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`,
   `DJANGO_ALLOWED_HOSTS=yourapp.onrender.com`.
3. Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
4. Start command: `gunicorn charges_project.wsgi:application`

`whitenoise` is included in requirements so static files serve correctly in
production without extra configuration — add it to `MIDDLEWARE` in
`settings.py` (right after `SecurityMiddleware`) and set
`STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"`
if you deploy this.

## How the confidence flag works

Two extra models were trained with quantile loss (5th and 95th percentile)
alongside the main model. Their prediction gap is a per-input confidence
interval, computed with no ground truth needed. Inputs whose interval is
wider than the 90th-percentile threshold observed on the test set get
flagged as "low confidence — recommend manual review." See Section 8 and 9
of the training notebook for the full reasoning and validation.
