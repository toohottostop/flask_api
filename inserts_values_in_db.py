from datetime import date

from src import db
from src.models import Bike


def insert_bikes():
    nukeproof_reactor = Bike(
        model="Nukeproof reactor 290 Comp",
        riding_style="Cross country",
        description="""At home on all trails, whether you're smashing down a descent or attacking a tough climb, the 
        Reactor Comp 29er uses its light and strong aluminium/carbon frame to deliver an agile and efficient ride. 
        The advanced frame is enhanced by a trail-smoothing Marzocchi/RockShox suspension package and a Shimano Deore 
        1x12-speed groupset""",
        release_date=date(2020, 11, 3),
        price=313553.73,
        rating=4.7,
    )
    commencal_absolut = Bike(
        model="Commencal Absolut",
        riding_style="Dirt",
        description="""When you order a bike, one of our trained mechanics will carefully prepare and pack your bike 
        for shipping. Upon delivery, the assembly is simple and all necessary tools are conveniently included in the 
        box.""",
        release_date=date(2021, 1, 30),
        price=135873.28,
        rating=0.0,
    )
    commencal_clash = Bike(
        model="Commencal Clash",
        riding_style="Freeride",
        description="""Now bringing you even better control, the ride quality of the Clash Race has an updated and 
        improved geometry, plus an awesome components package. Ready for today’s aggressive enduro, bike park and 
        downhill riders, its RockShox ZEB Ultimate forks combine with its RockShox Super Deluxe Ultimate rear shock to 
        soak up the worst that the trails can throw at you.""",
        release_date=date(2019, 11, 3),
        price=418071.63,
        rating=4.9,
    )
    gt_force = Bike(
        model="GT Force",
        riding_style="Downhill",
        description="""The GT Force Elite is the ideal full-suspension bike for enduro racing, all-mountain epics and 
        backcountry explorations. This long-travel suspension bike features an alloy frame, Marzocchi 170mm travel 
        forks, a Fox Float performance rear shock and a SRAM SX Eagle 12-Speed groupset with Tektro hydraulic disc 
        brakes. Plus, it rolls upon Formula Boost hubs, WTB i29 TCS Tubeless Ready rims and Maxxis Minion DHF and DHRII 
        EXO tyres. Do not underestimate this bikes power, agility and aggression, it is a force to be reckoned with.""",
        release_date=date(2020, 5, 15),
        price=313553.73,
        rating=4.9,
    )
    specialized_demo = Bike(
        model="Specialized Demo",
        riding_style="Downhill",
        description="""	M5 alloy, Style-Specific DH Geometry, horst pivot flip chip for 27.5 or 29 rear wheel, BSA 
        threaded BB, full internal cable routing with option for full external brake, 148mm rear spacing, sealed 
        cartridge bearing pivots, replaceable derailleur hanger, 200mm of travel""",
        release_date=date(2020, 4, 3),
        price=441590.0,
        rating=4.95,
    )

    db.session.add(nukeproof_reactor)
    db.session.add(commencal_absolut)
    db.session.add(commencal_clash)
    db.session.add(gt_force)
    db.session.add(specialized_demo)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Insert in db...')
    insert_bikes()
    print('Successfully inserted!')
