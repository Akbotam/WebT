from django.http import JsonResponse
from api.models import TaskList, Task

def task_lists(request):
    lists = TaskList.objects.all()
    json_tasklists = [t.to_json() for t in lists]
    return JsonResponse(json_tasklists, safe=False)

def tasklist_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(task_list.to_json())

def tasklist_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    tasks = task_list.tasks.all()
    json_tasks = [tt.to_json_list() for tt in tasks]

    return JsonResponse(json_tasks, safe=False)

def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(task.to_json_detail())


