from haystack import indexes
from events.models import Event

class EpisodeIndex(indexes.SearchIndex, indexes.Indexable, query_title):
    
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Event

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(title = query_title)

