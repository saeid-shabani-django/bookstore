from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from .forms import CommentForm
from django.shortcuts import render,get_object_or_404,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
class BookListView(generic.ListView):
    model = Book
    template_name = 'Books/book_list.html'
    context_object_name = 'books'
    paginate_by = 2
# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'Books/book_detail.html'
@login_required()
def book_detail_view(request,pk):
        book = get_object_or_404(Book,pk=pk)
        comments = book.comments.all()
        print(request.method)
        if request.method == 'POST':
            book = get_object_or_404(Book, pk=pk)
            cmt_form = CommentForm(request.POST)

            if cmt_form.is_valid():
                cmt_form.save(commit = False)
                cmt_form.book = book
                cmt_form.user = request.user
                cmt_form.save()
                return reverse('book_list')


        else:
            cmt_form = CommentForm()

        return render(request, 'Books/book_detail.html', {
                'book': book,
                'comments': comments,
                'cmt_form': cmt_form,
            })


class BookCreateView(LoginRequiredMixin,generic.CreateView):
    model = Book
    fields = ['title','description','price','author','cover']
    template_name = 'Books/book_create.html'
class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'Books/book_create.html'
    fields = '__all__'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'Books/book_delete.html'
    success_url = reverse_lazy('book_list')

