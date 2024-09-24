table_to_columns = {
    "person": [
        "person_id",
        "year_of_birth",
        "birth_datetime",
        "race_concept_id",
        "ethnicity_concept_id",
        "state_of_residence_concept_id",
    ],
    "death": [
        "person_id",
        "death_date",
    ],
    "condition_occurrence": ["person_id", "condition_concept_id"],
    "drug_exposure": ["person_id", "drug_concept_id"],
    "visit_occurrence": ["person_id", "visit_concept_id"],
    "observation_period": [
        "person_id",
        "observation_period_start_date",
        "observation_period_end_date",
    ],
}
