from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
import json


def get_transactions(request):
    data = list(Transaction.objects.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_transaction(request):
    if request.method == "POST":
        body = json.loads(request.body)
        Transaction.objects.create(
            title=body["title"],
            amount=body["amount"],
            type=body["type"]
        )
        return JsonResponse({"message": "Transaction saved"})