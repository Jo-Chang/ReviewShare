from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/index.html', context)


def redirect_index(request):
    return redirect('reviews:index')

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review':review,
        'comment_form': comment_form,
        'comments':comments,
    }
    
    return render(request, 'reviews/detail.html', context)

def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
        
    context = {
        'form':form,
    }
    
    return render(request, 'reviews/create.html', context)


def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('reviews:index')


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
        
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


def comment_create(request, review_pk):
    if request.method == 'POST':
        review = Review.objects.get(pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
            
    return redirect('reviews:detail', review.pk)


def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    
    return redirect('reviews:detail', review_pk)
    