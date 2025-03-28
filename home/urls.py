from django.urls import path
from .views import bill_visualization, bill_data_json ,chart_Q1,chart_Q2, chart_Q3, chart_Q4, chart_Q5, chart_Q6, chart_Q7, chart_Q8, chart_Q9, chart_Q10, chart_Q11, chart_Q12

urlpatterns = [
    path('visualization/', bill_visualization, name='bill_visualization'),
    path('data/', bill_data_json, name='bill_data_json'),
    path('Q1/', chart_Q1, name='Q1'),
    path('Q2/', chart_Q2, name='Q2'),
    path('Q3/', chart_Q3, name='Q3'),
    path('Q4/', chart_Q4, name='Q4'),
    path('Q5/', chart_Q5, name='Q5'),
    path('Q6/', chart_Q6, name='Q6'),
    path('Q7/', chart_Q7, name='Q7'),
    path('Q8/', chart_Q8, name='Q8'),
    path('Q9/', chart_Q9, name='Q9'),
    path('Q10/', chart_Q10, name='Q10'),
    path('Q11/', chart_Q11, name='Q11'),
    path('Q12/', chart_Q12, name='Q12'),
]
