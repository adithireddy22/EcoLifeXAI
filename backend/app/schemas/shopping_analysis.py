from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, model_validator


class NutrientInfo(BaseModel):
    # Nutritional values should be expressed per 100 g,
    # per 100 ml, or per serving, as specified by the user.

    energy_kcal: float | None = Field(default=None, ge=0)
    sugar_g: float | None = Field(default=None, ge=0)
    fat_g: float | None = Field(default=None, ge=0)
    saturated_fat_g: float | None = Field(default=None, ge=0)
    protein_g: float | None = Field(default=None, ge=0)
    fiber_g: float | None = Field(default=None, ge=0)
    salt_g: float | None = Field(default=None, ge=0)
    sodium_mg: float | None = Field(default=None, ge=0)


class ShoppingAnalysisCreate(BaseModel):
    user_id: str = Field(..., min_length=1)
    product_name: str = Field(..., min_length=1, max_length=200)

    # Product identification
    barcode: str | None = None

    # Where the product information came from
    data_source: Literal["barcode", "image", "manual"] = "manual"

    # Basis for interpreting nutrient values
    basis: Literal["per_100g", "per_100ml", "per_serving"] = "per_100g"

    # Product information
    ingredients: list[str] = Field(default_factory=list)
    nutrients: NutrientInfo = Field(default_factory=NutrientInfo)

    # Scores may be unavailable until analysis is implemented
    nutrition_score: float | None = Field(default=None, ge=0, le=100)
    environmental_score: float | None = Field(default=None, ge=0, le=100)

    recommendations: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_nutrients(self):
        # Energy values are expressed in kcal, so the field name
        # is energy_kcal rather than energy_kcal_100g.
        return self


class ShoppingAnalysisResponse(ShoppingAnalysisCreate):
    id: str
    created_at: datetime