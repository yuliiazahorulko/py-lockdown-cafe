from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    masks = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError()
        elif not visitor["wearing_a_mask"]:
            Cafe.masks += 1
            raise NotWearingMaskError(Cafe.masks)
        else:
            return f"Welcome to {self.name}"
