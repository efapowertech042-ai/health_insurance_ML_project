from django.shortcuts import render

from .forms import ChargesPredictionForm
from .ml_model import predict_charges


def predict_view(request):
    result = None

    if request.method == "POST":
        form = ChargesPredictionForm(request.POST)
        if form.is_valid():
            result = predict_charges(
                age=form.cleaned_data["age"],
                sex=form.cleaned_data["sex"],
                bmi=form.cleaned_data["bmi"],
                children=form.cleaned_data["children"],
                smoker=form.cleaned_data["smoker"],
                region=form.cleaned_data["region"],
            )
    else:
        form = ChargesPredictionForm()

    return render(
        request,
        "predictor/predict.html",
        {"form": form, "result": result},
    )
