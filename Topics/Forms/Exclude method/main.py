class BikeModelForm(ModelForm):
    class Meta:
        model = Bike
        exclude = ["engine", "color"]