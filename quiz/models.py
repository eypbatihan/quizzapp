from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=25)

  class Meta:
    verbose_name_plural = "Categories"

  def __str__(self):
      return self.name

DIFF_CHOICES = (
  ('easy','easy'),
  ('medium','medium'),
  ('hard','hard'),
) 

class Quiz(models.Model):
  name = models.CharField(max_length=100)
  number_of_questions = models.IntegerField()
  time = models.IntegerField(help_text="duration of the quiz in minutes")
  required_score_to_pass = models.IntegerField(help_text="required score in %")
  category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
  difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

  class Meta:
    verbose_name_plural = "Quizzes"

  def __str__(self):
    return f'{self.name} {self.category}'   
  
  def get_questions(self):
    return self.questions_set.all()
  
  

class Questions(models.Model):
  data_created = models.DateTimeField(auto_now_add=True)
  text = models.CharField(max_length=200)
  quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="question")

  class Meta:
    verbose_name_plural = "Questions"

  def __str__(self):
    return f'{self.text}' 
  
  def get_answers(self):
    return self.answer_set.all()

class Answer(models.Model):
  data_created = models.DateTimeField(auto_now_add =True)
  text = models.TextField(max_length=200)
  question = models.ForeignKey(Questions,on_delete=models.CASCADE,related_name="answer")
  is_correct = models.BooleanField(default=False)

  def __str__(self):
    return f'questions : {self.question.text}, answer: {self.text}, is_correct : {self.is_correct}' 

