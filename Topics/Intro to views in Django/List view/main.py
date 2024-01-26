from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    queryset = Book.objects.all()
    template_name = "books_preview.html"