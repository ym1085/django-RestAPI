from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Address
from .serializers import AddressSerializer
from rest_framework.parsers import JSONParser

'''
@Date: 21.11.22
@Desc: 전체 주소록 조회 및 생성
@Author: ymkim
'''
@csrf_exempt
def address_list(req):
    if req.method == 'GET':
        query_set = Address.objects.all()
        serializer = AddressSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

'''
@Date: 21.11.22
@Desc: 주소록 단건 조회, 수정, 삭제 
@Author: ymkim
'''
@csrf_exempt
def address(req, pk):
    obj = Address.objects.get(pk=pk)

    if req.method == 'GET':
        serializer = AddressSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = AddressSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif req.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

'''
@Date: 21.11.22
@Desc: 주소록 'name'과 'phone_number'를 id, pwd로 생각하고 로그인 기능 구현 
@Author: ymkim
'''
@csrf_exempt
def login(req):
    if req.method == 'POST':
        try:
            data = JSONParser().parse(req)
            search_name = data['name']
            obj = Address.objects.get(name=search_name)

            if data['phone_number'] == obj.phone_number:
                print("Is same {0}, {1}".format(data['phone_number'], obj.phone_number))
                return HttpResponse(status=200)
            else:
                print("Is not same {0}, {1}".format(data['phone_number'], obj.phone_number))
                return HttpResponse(status=400)

        except Exception:
            raise Http404('페이지를 찾을 수 없습니다.')


