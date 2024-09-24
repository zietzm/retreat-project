from enum import StrEnum


class Query(StrEnum):
    ALL = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        """
    AgeSex = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        WHERE year_of_birth is not null AND gender_source_concept_id is not null
        """
    AgeCutOff_21 = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 21
        """
    AgeCutOff_18 = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) >= 18
        """
    AgeCutoff_65 = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) >= 65
        """
    AgeCutoff_40 = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 40
        """
    AgeCutoff_65L = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 65
        """
    AgeCutoff_80 = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 80
        """
    Race = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        WHERE race_concept_id is not null
        """
    Alive = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        WHERE person_id NOT IN (SELECT person_id from `{CDR}.death`)
        """
    Diagnoses = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.condition_occurrence`
        WHERE condition_concept_id != 0
        """
    Medication = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.drug_exposure`
        WHERE drug_concept_id != 0 AND drug_concept_id is not null
        """
    OutpatientVisits = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.visit_occurrence`
        WHERE visit_concept_id = 9202
        """
    ZipOrAddress = """
        SELECT COUNT(DISTINCT person_id)
        FROM `{CDR}.person`
        WHERE state_of_residence_concept_id != 0 AND
              state_of_residence_concept_id is not null
        """
    ObsPeriod1Week = """
        SELECT COUNT(distinct person_id)
        FROM `{CDR}.observation_period`
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) >= 7
        """
    ObsPeriod2Weeks = """
        SELECT COUNT(distinct person_id)
        FROM `{CDR}.observation_period`
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 14
        """
    ObsPeriod1Month = """
        SELECT COUNT(distinct person_id)
        FROM `{CDR}.observation_period`
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 30
        """
    ObsPeriod6Month = """
        SELECT COUNT(distinct person_id)
        FROM `{CDR}.observation_period`
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 6*30
        """
    ObsPeriod1Year = """
        SELECT COUNT(distinct person_id)
        FROM `{CDR}.observation_period`
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 365
        """
    ObsPeriod2Years = """
        SELECT COUNT(distinct person_id)
        FROM `{CDR}.observation_period`
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 2*365.25
        """
    ObsPeriod6Years = """
        SELECT COUNT(distinct person_id)
        FROM `{CDR}.observation_period`
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 6*365.25
        """
