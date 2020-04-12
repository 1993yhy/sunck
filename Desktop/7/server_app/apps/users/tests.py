from django.test import TestCase

# Create your tests here.
from datetime import datetime,timedelta

print(datetime.now())
print(timedelta(hours=0, minutes=5, seconds=0))
a = datetime.now()-timedelta(hours=0, minutes=5, seconds=0)
print(datetime.now()-timedelta(hours=0, minutes=5, seconds=0))
if a>datetime.now():
    print("sdas")
else:
    print("sdsadasdasd")

