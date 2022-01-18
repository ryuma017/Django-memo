from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ContactForm, MemoForm
from .models import Memo


class IndexView(generic.ListView):
    model = Memo #get_queryset()があればmodelは指定しなくてもいい
    template_name = 'app/index.html'
    context_object_name = 'memos'
    """Return the last published memos."""
    def get_queryset(self):
        return Memo.objects.all().order_by('-updated_datetime')


class DetailView(generic.DetailView):
    model = Memo
    template_name = 'app/detail.html'


class MemoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'app/new_memo.html'
    success_url = reverse_lazy('app:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MemoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Memo
    form_class = MemoForm
    success_url = reverse_lazy('app:index')


class MemoEditView(LoginRequiredMixin, generic.UpdateView):
    model = Memo
    form_class = MemoForm
    template_name = 'app/edit_memo.html'
    success_url = reverse_lazy('app:index')


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'app/contact.html'
    success_url = reverse_lazy('app:contact_success')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactSuccessView(generic.TemplateView):
    template_name = 'app/contact_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = '正常に送信されました。'
        return context
