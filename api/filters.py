from rest_framework.filters import BaseFilterBackend


class PostFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('group'):
            group_id = request.query_params.get('group')
            return queryset.filter(group_id=group_id)
        return queryset
