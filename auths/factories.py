from .models import UserProfile,Report,User
import factory
from faker import Factory
from django.utils import timezone

faker = Factory.create()

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile
    name = factory.LazyAttribute(lambda _: faker.name())
    password=faker.password(length=12)
    email = factory.LazyAttribute(lambda _: faker.email())


report_type = [x[0] for x in Report.CHOICES]
gender=[x[0] for x in User.GENDER]
class ReportFactory(factory.DjangoModelFactory):
    class Meta:
        model = Report
    
    name = factory.LazyAttribute(lambda _: faker.word())
    types=factory.LazyAttribute(lambda _: faker.text())
    reporter_user_id = factory.SubFactory(UserProfile) #foreign key
    mark_as = factory.Iterator(report_type)
    created_on=factory.Faker("date_time", tzinfo=timezone.get_current_timezone())

    #maked_as=factory.Faker('random_element', elements=[x[0] for x in Report.CHOICES])


class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    user=factory.SubFactory(UserProfile) #foreign key
    bio = faker.text()
    gender=factory.Iterator(gender)
