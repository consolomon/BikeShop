class BikeModelForm(ModelForm):
    class Meta:
        model = Bike
        fields = ["engine", "color"]