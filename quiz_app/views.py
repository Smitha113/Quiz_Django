from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Quiz, Question, Answer, QuizResult
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Get the password from the form
        user = authenticate(request, username=username, password=password)  # Authenticate with both username and password
        if user is not None:
            login(request, user)
            return redirect('quiz_list')  # Redirect to quiz list page after login
        else:
            # Invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})  # Notify about invalid credentials
    else:
        return render(request, 'login.html')


@login_required
def quiz_list(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'quiz_app/quiz_list.html', context)

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz, 'questions': questions})

@login_required
def quiz_answer(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    score = 0
    
    if request.method == 'POST':
        for question in questions:
            selected_answer_id = request.POST.get(str(question.id))
            if selected_answer_id:
                selected_answer = get_object_or_404(Answer, pk=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
        
        # Save the quiz result
        quiz_result = QuizResult.objects.create(
            user=request.user,  # Assuming you're using authentication
            quiz=quiz,
            score=score
        )
        quiz_result.save()
        
        # Redirect to the result page
        return redirect('quiz_result', result_id=quiz_result.id)
    else:
        # If it's not a POST request, redirect back to the quiz detail page
        return redirect('quiz_detail', quiz_id=quiz_id)

@login_required
def quiz_result(request, result_id):
    result = get_object_or_404(QuizResult, pk=result_id)
    return render(request, 'quiz_app/quiz_result.html', {'result': result})



