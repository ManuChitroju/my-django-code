from django.shortcuts import render
from . forms import puzzle_form
from .msquare import square
from . models import Tambola2
import random
from collections import OrderedDict

# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hello Manu</h1>")
    return render(request, 'myapp/home.html')

def puzzle(request):
    if request.method == 'POST':
            form = puzzle_form(request.POST)
            if form.is_valid():
                    number=form.cleaned_data['number']

                    if number < 0:
                        return HttpResponse("<h1><center>Enter a positive odd number</center></h1>")
                    elif number%2==0:
                        return render(request, 'myapp/even_replay.html')
                        #return render(request, 'personal/form2.html', {'form': form,'text':'Enter a positve odd number'})
                    elif number >1000:
                        return render(request, 'myapp/limit_replay.html')
                    else:
                        if number %2!=0:
                            x=square(number)
                            t='Total across any row and column including main diagonal is same'
                            s=sum(x[0])
                            return render(request,'myapp/puzzle.html',{'x':x,'number':number,'t':t,'sum':s})
            else:
                    return render(request, 'myapp/replay.html')
    else:
        #print("in else")
        form = puzzle_form()
    return render(request, 'myapp/form.html', {'form': form})

def delete_tambola():
    details = Tambola2.objects.all()
    L=[]
    for i in details:
        L.append(i.str1)
    L2=[]
    for i in L:
        if i not in L2:
            L2.append(i)
    print(L2)


def tambola(request):

    #if not request.session.exists(request.session.session_key):
    #    s=request.session.create()
    #if request.session.exists(request.session.session_key):
    #    print(request.session.exists(request.session.session_key))
    #delete_tambola()
    #Tambola2.objects.all().delete()
    x='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQXYZ'
    new_str=""
    for i in range(52):
        n=random.randint(0,51)
        new_str=new_str+x[n]

    str1=new_str
    return render(request, 'myapp/tambola.html',{'string':str1})

def start_tambola(request,str1):
    cap={
    1: 'Son of Gun', 2: 'You and me',3: 'Buy 2 get 1 free', 4: 'Murgi chor',5: 'Hum Panch',6: 'In a fix/ bottom heavy',
    7: 'Lucky for all', 8: 'One fat lady',9: 'U are mine', 10: 'badmash number 10',11: 'Those beautiful legs', 12: 'Mid night',
    13: 'Lucky for some', 14: 'Valentines', 15: 'Independence',16: 'Sweet 16', 17: 'Not so sweet', 18: 'Voting age',
    19: 'Last of the teens', 20: 'Blind one score', 21: 'Marriageable age',22: 'Two little ducks', 23: 'You & me',
    24: 'Two doz number', 25: 'Silver Jublee',26: 'Bole mere lips I love 26',27: 'A black raven', 28: 'Out on a date',
    29: 'Rise & shine', 30: 'Dont play dirty',31: "Baskin Robins", 32: 'Binaca smile',33: 'Dirty knee', 34: 'Lions roar',
    35: 'A flirty wife', 36: 'Popular number', 37: 'Lime & Lemon',38: 'Me & my fat mate', 39: 'Watch your waist line',
    40: 'Men get naughty at 40', 41: 'Kiss and run', 42: 'Quit India',43: 'Climb a tree', 44: 'Dil ke chor', 45: 'Half way thru',
    46: 'Choke,chake maro', 47: 'Independence', 48: 'You are not late', 49: 'Your waistline', 50: 'Golden Jubliee',
    51: 'Auspicious', 52: 'Pack of the cards', 53: 'Pack with joker', 54: 'House of bamboo door', 55: 'Dono bhai',
    56: 'Whisky, Beer do not mix', 57: 'Banegi baat at panch aur saat', 58: 'Retirement age', 59: 'Just retired',
    60: 'Five dozen', 61: 'Done-dana-dan done', 62: 'Over haul is due', 63: 'Kisses come free', 64: 'Hardcore', 65: 'Harem of wives',
    66: 'All the 6s', 67: 'Haath mein haath 6 aur 7', 68: 'Mota seth', 69: 'Ulta pulta', 70: 'Lucky Blind',71: 'Setting sun',
    72: 'A different view', 73: 'Savitriji', 74: 'Still want more', 75: 'Diamond jubilee', 76: 'Run out of tricks', 77: 'Thanda lemon',
    78: 'Wipe the slate', 79: 'Old and senile', 80: 'Blind 4 score', 81: 'Said and done', 82: 'Down with flu', 83: 'Grandmas age',
    84: 'Haggard and bored', 85: 'Still alive',86: 'Pick up a walking stick', 87: 'Nearing heaven', 88: 'Two fat majors', 89: 'Penultimate',
    90: 'Top of the house blind 90'
    }

    ## check count if 90 pass html
    details = Tambola2.objects.filter(str1=str1)
    L=[]
    for i in details:
        L.append(i.random_number)
    while True:
        n=random.randint(1,90)
        if n not in L:
            Tambola2.objects.create(str1=str1,random_number=n)
            L.append(n)
            c=cap[n]
            break

    details = Tambola2.objects.filter(str1=str1)
    for i in details:
        print(i.random_number)

    D=OrderedDict()
    for i in range(1,91):
        #print(i)
        if i in L:
            D[i]=i
        else:
            D[i]=""

    print(D)

    D2=OrderedDict()
    L2=[]
    i=0
    for k, v in D.items():
        D2[k]=v
        print(k,v)
        i+=1
        if i==10:
            L2.append(D2)
            D2=OrderedDict()
            i=0
    #print(D2)

    if len(L)!=90:
        return render(request, 'myapp/start_tambola.html',{'string':str1,'L':L2,'last_number':n,'cap':c})
    if len(L)!=91:
        Tambola2.objects.filter(str1=str1)
        return render(request, 'myapp/gameover_tambola.html')


