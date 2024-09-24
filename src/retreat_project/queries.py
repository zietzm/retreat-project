from enum import StrEnum


class Query(StrEnum):
    ALL = """
        SELECT *
        FROM `{CDR}.person`
        """
    AgeSex = """
        SELECT *
        FROM `{CDR}.person`
        WHERE year_of_birth is not null AND gender_source_concept_id is not null
        """
    AgeCutOff_21 = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 21
        """
    AgeCutOff_18 = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) >= 18
        """
    AgeCutoff_65 = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) >= 65
        """
    AgeCutoff_40 = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 40
        """
    AgeCutoff_65L = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 65
        """
    AgeCutoff_80 = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 80
        """
    Race = """
        SELECT *
        FROM `{CDR}.person`
        WHERE race_concept_id is not null
        """
    Alive = """
        SELECT *
        FROM `{CDR}.person`
        WHERE person_id NOT IN (SELECT person_id from `{CDR}.death`)
        """
    Diagnoses = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_concept_id != 0
        """
    Medication = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.drug_exposure` USING (person_id)
        WHERE drug_concept_id != 0 AND drug_concept_id is not null
        """
    OutpatientVisits = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.visit_occurrence` USING (person_id)
        WHERE visit_concept_id = 9202
        """
    ZipOrAddress = """
        SELECT *
        FROM `{CDR}.person`
        WHERE state_of_residence_concept_id != 0 AND
              state_of_residence_concept_id is not null
        """
    ObsPeriod1Week = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) >= 7
        """
    ObsPeriod2Weeks = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 14
        """
    ObsPeriod1Month = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 30
        """
    ObsPeriod6Month = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 6*30
        """
    ObsPeriod1Year = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 365
        """
    ObsPeriod2Years = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 2*365.25
        """
    ObsPeriod6Years = """
        SELECT *
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 6*365.25
        """


class GroupField(StrEnum):
    Ethnicity = "ethnicity_concept_id"
    Race = "race_concept_id"
    Gender = "gender_source_concept_id"


def group_query_by(query: Query, person_field: GroupField) -> str:
    return f"""
        SELECT
            {person_field},
            COUNT(DISTINCT person_id) AS count
        FROM (
            {query}
        ) AS subquery
        GROUP BY {person_field}
        """
