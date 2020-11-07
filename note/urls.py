from django.views.decorators.csrf import csrf_exempt
from . import views
from django.urls import path

urlpatterns = [
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('api/note/', views.NoteView),
]
