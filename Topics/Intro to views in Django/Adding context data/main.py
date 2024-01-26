def detail_book(request):
    return render(request, "book_detail.html", {'greetings_to': 'Anonymous','num_articles': 10,})