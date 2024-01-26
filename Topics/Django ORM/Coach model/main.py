import django.db.models as models


class Coach(models.Model):
    name = models.CharField(max_length=50)
    experience = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


    class Meta:
        app_label = 'tournament'
        def __str__(self):
            return self.app_label

    def __str__(self):
        return self.name