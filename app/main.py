import datetime
from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            continue
    else:
        try:
            for person in friends:
                cafe.visit_cafe(person)
        except NotWearingMaskError:
            masks_to_buy = sum([1
                                for visitor in friends
                                if visitor["wearing_a_mask"] is False
                                ])
            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"
