from django.db import models

# Create your models here.
class Predict_Fim_App(models.Model):
    sex = models.SmallIntegerField(default=1)
    age = models.SmallIntegerField(default=60)
    disease = models.SmallIntegerField(default=1)
    pre_hospitalization_status = models.SmallIntegerField(default=1)
    days = models.SmallIntegerField(default=1)
    family = models.SmallIntegerField(default=1)
    motivation = models.SmallIntegerField(default=1)
    helper = models.SmallIntegerField(default=1)
    meal = models.SmallIntegerField(default=1)
    hygienic = models.SmallIntegerField(default=1)
    wipingClean = models.SmallIntegerField(default=1)
    upperBodyDressing = models.SmallIntegerField(default=1)
    lowerBodyDressing = models.SmallIntegerField(default=1)
    toiletAction = models.SmallIntegerField(default=1)
    urinationControl = models.SmallIntegerField(default=1)
    defecationControl = models.SmallIntegerField(default=1)
    bedsChairsWheelchairs = models.SmallIntegerField(default=1)
    toilet = models.SmallIntegerField(default=1)
    bathtubShower = models.SmallIntegerField(default=1)
    walkingWheelchair = models.SmallIntegerField(default=1)
    stairs = models.SmallIntegerField(default=1)
    understanding = models.SmallIntegerField(default=1)
    expression = models.SmallIntegerField(default=1)
    socialCommunication = models.SmallIntegerField(default=1)
    problemSolving = models.SmallIntegerField(default=1)
    memory = models.SmallIntegerField(default=1)
    
    
