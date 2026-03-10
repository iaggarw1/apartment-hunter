from __future__ import annotations

from pydantic import BaseModel


class Profile(BaseModel):
    user_id: str
    name: str
    preferences: Preferences


class Preferences(BaseModel):
    beds: int
    bath: int
    locations: list[Location]
    poi: list[Location]
    pets: PetPreferences


class PetPreferences(BaseModel):
    dogs: bool
    cats: bool
    others: bool


class Location(BaseModel):
    district: str
    city: str
    state: str
