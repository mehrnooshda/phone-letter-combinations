import json
from itertools import product

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

nums = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


@csrf_exempt
def get_combs(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone_number = data.get('phoneNumber', None)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        if phone_number is not None:
            result = ["".join(combo) for combo in product(*[nums[d] for d in phone_number])]
            return JsonResponse({"combinations": result})
        else:
            return JsonResponse({"error": "Phone number is required"}, status=400)

    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)
