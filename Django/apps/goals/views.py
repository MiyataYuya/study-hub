from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import StudyGoal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class GoalListView(ListView):
    model = StudyGoal
    template_name = 'goals/goal_list.html'
    context_object_name = 'goals'

class GoalDetailView(DetailView):
    model = StudyGoal
    template_name = 'goals/goal_detail.html'

class GoalCreateView(LoginRequiredMixin, CreateView):
    model = StudyGoal
    template_name = 'goals/goal_form.html'
    fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']
    success_url = reverse_lazy('goal_list')
    
    def form_valid(self, form):
        # 現在のログインユーザーを設定
        if not self.request.user.is_authenticated:
            raise ValueError("User is not authenticated.")
        form.instance.user = self.request.user
        print(f"request.user: {self.request.user}")  # 現在のユーザーを出力
        print(f"Is authenticated: {self.request.user.is_authenticated}")  # 認証状態を出力

        return super().form_valid(form)

class GoalUpdateView(UpdateView):
    model = StudyGoal
    template_name = 'goals/goal_form.html'
    fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']
    success_url = reverse_lazy('goal_list')

class GoalDeleteView(DeleteView):
    model = StudyGoal
    template_name = 'goals/goal_confirm_delete.html'
    success_url = reverse_lazy('goal_list')

@login_required
def create_goal(request):
    if not request.user.is_authenticated:
        raise ValueError("User is not authenticated.")  # デバッグ用エラー

    if request.method == 'POST':
        form = StudyGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = StudyGoalForm()
    print(f"Logged-in user: {request.user}")  # または self.request.user
    return render(request, 'goals/goal_form.html', {'form': form})
