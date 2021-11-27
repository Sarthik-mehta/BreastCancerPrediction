from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.staticfiles.storage import staticfiles_storage

from django.templatetags.static import static
from django.conf import settings


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from .forms import CreateUserForm
from .models import userData


def registerPage(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already Registered. Please logout to register with different user account.')
        return redirect('predict')
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already Logged In. Please logout to sign in with different user account.')
        return redirect('predict')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('predict')
        else:
            messages.info(request, 'Username or Password is incorrect! ')
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html')


#@login_required(login_url='login')
def predict(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first in order to use prediction tool.')
        return redirect('login')

    currentuser = request.user
    radiusMean = 0.00
    textureMean = 0.00
    perimeterMean = 0.00
    areaMean = 0.00
    smoothnessMean = 0.00
    compactnessMean = 0.00
    concavityMean = 0.00
    concavePointMean = 0.00
    symmetryMean = 0.00
    fractalDimensionMean = 0.00
    if userData.objects.filter(user=currentuser).exists():
        userdata = userData.objects.get(user=currentuser)
        radiusMean = userdata.radiusMean
        textureMean = userdata.textureMean
        perimeterMean = userdata.perimeterMean
        areaMean = userdata.areaMean
        smoothnessMean = userdata.smoothnessMean
        compactnessMean = userdata.compactnessMean
        concavityMean = userdata.concavityMean
        concavePointMean = userdata.concavePointMean
        symmetryMean = userdata.symmetryMean
        fractalDimensionMean = userdata.fractalDimensionMean

    userstats = [radiusMean, textureMean, perimeterMean, areaMean, smoothnessMean, compactnessMean, concavityMean,
                 concavePointMean, symmetryMean, fractalDimensionMean]
    return render(request, 'predict.html', {'userstats': userstats})


def result(request):
    # p = staticfiles_storage.path('BreastCancerPrediction/files/data.csv')
    df = pd.read_csv(r'C:\Users\Sarthik Mehta\Desktop\FRT\BreastCancerPrediction\BreastCancerPrediction\static\BreastCancerPrediction\files\data.csv')
    df.drop('id', axis=1, inplace=True)
    df.drop('Unnamed: 32', axis=1, inplace=True)
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
    traindf, testdf = train_test_split(df, test_size=0.3)
    outcome = 'diagnosis'
    predictors = list(df.columns[1:11])
    model = RandomForestClassifier(n_estimators=100, min_samples_split=25, max_depth=7, max_features=2)
    model.fit(traindf[predictors], traindf[outcome])

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])

    currentuser = request.user

    if userData.objects.filter(user=currentuser).exists():
        userData.objects.filter(user=currentuser).update(radiusMean=format(val1, ".2f"),
                                                         textureMean=format(val2, ".2f"),
                                                         perimeterMean=format(val3, ".2f"),
                                                         areaMean=format(val4, ".2f"),
                                                         smoothnessMean=format(val5, ".2f"),
                                                         compactnessMean=format(val6, ".2f"),
                                                         concavityMean=format(val7, ".2f"),
                                                         concavePointMean=format(val8, ".2f"),
                                                         symmetryMean=format(val9, ".2f"),
                                                         fractalDimensionMean=format(val10, ".2f"))
    else:
        userdata = userData(user=currentuser, radiusMean=format(val1, ".2f"), textureMean=format(val2, ".2f"),
                            perimeterMean=format(val3, ".2f"), areaMean=format(val4, ".2f"),
                            smoothnessMean=format(val5, ".2f"), compactnessMean=format(val6, ".2f"),
                            concavityMean=format(val7, ".2f"), concavePointMean=format(val8, ".2f"),
                            symmetryMean=format(val9, ".2f"), fractalDimensionMean=format(val10, ".2f"))
        userdata.save()

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]])
    testcolor=""
    result2 = ""

    if pred == [1]:
        result2 = "Result: The Patient is more likely to have a malignant cancer."
        testcolor="red"
    else:
        result2 = "Result: The patient is more likely to have a benign cancer."
        testcolor="green"

    recommendation = "Our Recommendations: Our system gives the result with high accuracy, however it is recommended to seek opinion of a professional doctor as well."

    currentuser = request.user
    radiusMean = 0.00
    textureMean = 0.00
    perimeterMean = 0.00
    areaMean = 0.00
    smoothnessMean = 0.00
    compactnessMean = 0.00
    concavityMean = 0.00
    concavePointMean = 0.00
    symmetryMean = 0.00
    fractalDimensionMean = 0.00

    userdata = userData.objects.get(user=currentuser)
    radiusMean = userdata.radiusMean
    textureMean = userdata.textureMean
    perimeterMean = userdata.perimeterMean
    areaMean = userdata.areaMean
    smoothnessMean = userdata.smoothnessMean
    compactnessMean = userdata.compactnessMean
    concavityMean = userdata.concavityMean
    concavePointMean = userdata.concavePointMean
    symmetryMean = userdata.symmetryMean
    fractalDimensionMean = userdata.fractalDimensionMean

    userstats = [radiusMean, textureMean, perimeterMean, areaMean, smoothnessMean, compactnessMean, concavityMean,
                 concavePointMean, symmetryMean, fractalDimensionMean]

    return render(request, 'predict.html', {"result2": result2,'userstats':userstats,'recommendation':recommendation,'testcolor':testcolor})
