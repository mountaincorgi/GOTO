def seed():
    from src.Goals.models import Goal, Milestone, Update
    from src.Users.models import Friendship, Message, UserProxy

    Goal.objects.all().delete()
    Message.objects.all().delete()
    Friendship.objects.all().delete()
    UserProxy.objects.all().delete()

    # Profiles
    u1 = UserProxy.objects.create(
        email="tom@example.com",
        username="tomcat",
        password="tomcat",
    )
    p1 = u1.profile
    u2 = UserProxy.objects.create(
        email="jerry@example.com",
        username="jerrymouse",
        password="jerrymouse",
    )
    p2 = u2.profile
    f1 = Friendship.objects.create(
        requestor=p1,
        requestee=p2,
        confirmed=True,
    )
    m1 = Message.objects.create(
        sender=p1,
        receiver=p2,
        text="Hello!",
    )
    m2 = Message.objects.create(
        sender=p1,
        receiver=p2,
        text="I said hello. Are you there?",
    )
    m3 = Message.objects.create(
        sender=p2,
        receiver=p1,
        text="Hey! I'm here!",
    )

    # Goals
    # Profile 1
    g1_german = Goal.objects.create(
        profile=p1,
        name="Learn German",
    )
    u1_german = Update.objects.create(
        goal=g1_german,
        text="Learned 5 words on Duolingo today"
    )
    u2_german = Update.objects.create(
        goal=g1_german,
        text="Learned 7 words on Duolingo today"
    )
    g1_piano = Goal.objects.create(
        profile=p1,
        name="Practise piano",
    )
    m1_piano = Milestone.objects.create(
        goal=g1_piano,
        name="Pass grade 3"
    )
    u1_piano = Update.objects.create(
        goal=g1_piano,
        text="Practised all songs for Grade 3 exam from memory"
    )
    g1_maths = Goal.objects.create(
        profile=p1,
        name="Prepare for maths exam",
    )
    m1_maths = Milestone.objects.create(
        goal=g1_maths,
        name="Study imaginary numbers"
    )
    m2_maths = Milestone.objects.create(
        goal=g1_maths,
        name="Finish calculus notes for C219"
    )

    # Profile 2
    g2_micro = Goal.objects.create(
        profile=p2,
        name="Microservices project",
    )
    m1_micro = Milestone.objects.create(
        goal=g2_micro,
        name="Set up NestJS microservices"
    )
    m2_micro = Milestone.objects.create(
        goal=g2_micro,
        name="Set up messaging with Apache Kafka"
    )
    m3_micro = Milestone.objects.create(
        goal=g2_micro,
        name="Implement Linkerd service mesh"
    )
    u1_micro = Update.objects.create(
        goal=g2_micro,
        text="Set up comments service and orders service as NestJS projects with Dockerfiles"
    )
    u2_micro = Update.objects.create(
        goal=g2_micro,
        text="Configured Kubernetes cluster deployment and service YAML files and set up CircleCI for project"
    )
    u3_micro = Update.objects.create(
        goal=g2_micro,
        text="Integrated comments service with Elasticsearch and orders service with AWS postgres Aurora"
    )
    g2_ml = Goal.objects.create(
        profile=p2,
        name="Learn ML",
    )
    m1_ml = Milestone.objects.create(
        goal=g2_ml,
        name="Complete exercise 1 of book using SciKit-Learn"
    )
    m2_ml = Milestone.objects.create(
        goal=g2_ml,
        name="Make notes on lectures 1-5 from edX course"
    )
    u1_ml = Update.objects.create(
        goal=g2_ml,
        text="Read chapter 1 of ML book"
    )
