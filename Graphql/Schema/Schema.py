from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from rx import Observable
import graphene
from core import models
from test_app.models import Cars
from ..Query.Club import AllClub, GetClub, MyClub
# from ..Query.Duration import searchOnReservation
from ..Query.Duration import GetAllowDuration
from ..Query.Section import AllSectionByClub, GetSection
from ..Query.Stadium import AllStadiumByType, GetStadium, GetStadiumByType
from ..Query.Friend import GetFriend, AllFriend
from ..Auth.graphql_auth import AuthMutation
from ..Mutation.SignUp import signup
from ..Mutation.club import AddClub, UpdateClub, DeleteClub
from ..Mutation.section import AddSection, UpdateSection, DeleteSection
from ..Mutation.stadium import AddStadium, UpdateStadium
# from ..Mutation.service import AddService, UpdateService
from ..Mutation.duration import AddDurationList
from ..Mutation.stadiumService import AddServicesForStadiums, ModificationsToStadiumServices
from ..Query import Player, Type, sub_manager
from ..Mutation.FriendMutat import addFriend, rejectFriend, acceptFriend
from ..Mutation.Team import createTeam, deleteTeam
from ..Mutation import search_on_map


class User_model(DjangoObjectType):

    class Meta:
        model = models.User
        fields = ['username']


class Query(ObjectType):
    # token_auth = mutations.ObtainJSONWebToken.Field()

    hello = graphene.Field(User_model)

    def resolve_hello(root, info, **kwargs):
        print('ppppppppppppppp')
        print(kwargs)
        return models.User.objects.filter(pk=2)

    AllClub = graphene.Field(AllClub)
    GetClub = graphene.Field(GetClub)
    allSectionByClub = graphene.Field(AllSectionByClub)
    GetSection = graphene.Field(GetSection)
    getFriend = graphene.Field(GetFriend)
    allFriend = graphene.Field(AllFriend)
    getAllowDuration = graphene.Field(GetAllowDuration)
    serchPlayer = graphene.Field(Player.SerchPlayer)
    type_ = graphene.Field(Type.AllType)
    clubSubManager = graphene.Field(sub_manager.ClubSubManagerd)
    myClub = graphene.Field(MyClub)
    playerMe = graphene.Field(Player.me)
    findPlayerOnMap = graphene.Field(Player.GeoPlayer)

    def resolve_AllClub(root, info, **kwargs):
        return AllClub()

    def resolve_GetClub(root, info, **kwargs):
        return GetClub()

    def resolve_allSectionByClub(root, info, **kwargs):
        return AllSectionByClub()

    def resolve_GetSection(root, info, **kwargs):
        return GetSection()

    def resolve_getFriend(root, info, **kwargs):
        return GetFriend()

    def resolve_allFriend(root, info, **kwargs):
        return AllFriend()

    # def resolve_getTeam(root, info, **kwargs):
    #     return GetTeam()

    def resolve_getAllowDuration(root, info, **kwargs):
        return GetAllowDuration()

    def resolve_clubSubManager(root, info, **kwargs):
        return sub_manager.ClubSubManagerd()

    def resolve_serchPlayer(root, info, **kwargs):
        return Player.SerchPlayer()

    def resolve_myClub(root, info, **kwargs):
        return MyClub()

    def resolve_type_(root, info, **kwargs):
        return Type.AllType()

    def resolve_playerMe(root, info, **kwargs):
        return Player.me()

    def resolve_findPlayerOnMap(root, info, **kwargs):
        return Player.GeoPlayer()


class Mutation (AuthMutation, graphene.ObjectType):
    SignUpPlyer = signup.SignUpPlayer.Field(description='SignUpPlyer')
    SignUpManager = signup.SignUpManager.Field()
    SignUpSubManager = signup.SignUpSubManager.Field()
    addclub = AddClub.Field()
    updateclub = UpdateClub.Field()
    deleteclub = DeleteClub.Field()
    addsection = AddSection.Field()
    updatesection = UpdateSection.Field()
    deletesection = DeleteSection.Field()
    addstadium = AddStadium.Field()
    updatestadium = UpdateStadium.Field()
    addservicesforstadiums = AddServicesForStadiums.Field()
    modificationstostadiumservices = ModificationsToStadiumServices.Field()
    addFreind = addFriend.addRequestFriend.Field()
    rejectFriend = rejectFriend.RejectFriend.Field()
    acceptFriend = acceptFriend.AcceptFriend.Field()
    createTeam = createTeam.CreateTeam.Field()
    deleteTeam = deleteTeam.DeleteTeam.Field()
    addDurationList = AddDurationList.Field()
    changeSearchMap = search_on_map.ChangeSearchOnMap.Field()


class Subscription(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        print('ssssssssssssssssssssssss')

        return Observable.interval(3000).map(lambda i: i)

    def resolve_cars_created(root, info):
        print('create cars')

        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Cars)
        ).map(lambda event: event.instance)


schema = graphene.Schema(query=Query, mutation=Mutation,
                         subscription=Subscription)
