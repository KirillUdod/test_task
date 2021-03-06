from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView
from django.core.context_processors import csrf
from bank.models import MyUser
from decimal import Decimal

def send_money(request):

    users = MyUser.objects.all()
    if request.POST:
        args = {}
        args.update(csrf(request))
        cname = request.POST.get('dropdown')
        args['dropdown'] = users
        cIDD = request.POST.get('IDD')
        args['IDD'] = cIDD
        needed_Amount = Decimal(request.POST.get('Amount'))
        args['Amount'] = needed_Amount
        from_User = MyUser.objects.get(username = cname)
        from_User_Amount = Decimal(from_User.money_amount)
        to_Users = MyUser.objects.filter(IDD = cIDD)
        if (to_Users):
            if (needed_Amount < from_User_Amount):
#               определим кол. акков, на которые нужно перевести 
                q_of_Users = to_Users.count()
                
#               проверим, нет ли в их кол. акка, с которого 
#               производится перевод. Если есть, уменьшим кол.
#               людей на 1
                for to_User in to_Users:
                    if  (to_User == from_User):
                        q_of_Users -= 1
#               Если кол-во акков стало 0 - ошибка    
                if (q_of_Users == 0):
                    print(args)
                    args['login_error'] = "Вы не можете перевести деньги себе же"
                    return render_to_response('index.html', args)

#               списываем деньги со счета 
                from_User.money_amount -= needed_Amount
                from_User.save()

#               Если кол-во акков назначения больше 1, то определим
#               сколько должно на каждый прийти 
                if (q_of_Users > 1):
                    needed_Amount = needed_Amount / q_of_Users
                for to_User in to_Users:
#               пополняем счета
                    if  (to_User == from_User):
                         continue    
                    to_User.money_amount += needed_Amount
                    to_User.save()
            else:
                print(args)
                args['login_error'] = "Недостаточная сумма"
                return render_to_response('index.html', args)
        else:
            print(args)
            args['login_error'] = "Данный IDD не найден"
            return render_to_response('index.html', args)
    return render(request, 'index.html', {'users':users})
