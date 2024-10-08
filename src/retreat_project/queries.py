from enum import Enum

import bigframes.pandas


class Query(str, Enum):
    ALL = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        """
    AgeSex = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        WHERE year_of_birth is not null AND
              gender_source_concept_id is not null
        """
    AgeCutOff_21 = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND
              birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 21
        """
    AgeCutOff_18 = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND
              birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) >= 18
        """
    AgeCutoff_65 = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND
              birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) >= 65
        """
    AgeCutoff_40 = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND
              birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 40
        """
    AgeCutoff_65L = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND
              birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 65
        """
    AgeCutoff_80 = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_start_date is not null AND
              birth_datetime is not null AND
              DATE_DIFF(condition_start_date, DATE(birth_datetime), YEAR) <= 80
        """
    Race = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        WHERE race_concept_id is not null
        """
    Alive = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        WHERE person_id NOT IN (SELECT
          person_id from `{CDR}.death`)
        """
    Diagnoses = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.condition_occurrence` USING (person_id)
        WHERE condition_concept_id != 0
        """
    Medication = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.drug_exposure` USING (person_id)
        WHERE drug_concept_id != 0 AND drug_concept_id is not null
        """
    OutpatientVisits = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.visit_occurrence` USING (person_id)
        WHERE visit_concept_id = 9202
        """
    ZipOrAddress = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        WHERE state_of_residence_concept_id != 0 AND
              state_of_residence_concept_id is not null
        """
    ObsPeriod1Week = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) >= 7
        """
    ObsPeriod2Weeks = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 14
        """
    ObsPeriod1Month = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 30
        """
    ObsPeriod6Month = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 6*30
        """
    ObsPeriod1Year = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 365
        """
    ObsPeriod2Years = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 2*365.25
        """
    ObsPeriod6Years = """
        SELECT
          person_id, ethnicity_concept_id, race_concept_id, gender_source_concept_id
        FROM `{CDR}.person`
        JOIN `{CDR}.observation_period` USING (person_id)
        WHERE DATE_DIFF(observation_period_end_date,
                        observation_period_start_date, DAY) > 6*365.25
        """


class GroupField(str, Enum):
    Ethnicity = "ethnicity_concept_id"
    Race = "race_concept_id"
    Gender = "gender_source_concept_id"


def ungrouped_query(query: Query) -> str:
    return f"""
        SELECT
            'Ungrouped' AS group_variable,
            'All' AS group_id,
            COUNT(DISTINCT person_id) AS count
        FROM (
            {query}
        ) AS subquery
        """


def group_query_by(query: Query, person_field: GroupField) -> str:
    return f"""
        SELECT
            '{person_field}' AS group_variable,
            {person_field} AS group_id,
            COUNT(DISTINCT person_id) AS count
        FROM (
            {query}
        ) AS subquery
        GROUP BY {person_field}
        """


def execute_query(query: str, cdr: str):
    return bigframes.pandas.read_gbq(query.format(CDR=cdr))


class PhenotypeQuery(str, Enum):
    IschemicStroke = """
        SELECT
          person_id, condition_concept_id, condition_start_date, ancestor_concept_id
        FROM `{CDR}.condition_occurrence`
        JOIN `{CDR}.concept_ancestor` ON condition_concept_id = descendant_concept_id
        WHERE ancestor_concept_id IN (372924, 375557, 443454, 441874)
        """


class CovariateQuery(str, Enum):
    GwasCovar = """
        SELECT
          person_id,
          IF(concept_name = 'Male', 1, 2) AS sex,
          DATE_DIFF(
            COALESCE(death_date, CURRENT_DATE),
            DATE(birth_datetime),
            YEAR
          ) AS age
        FROM `{CDR}.person`
        INNER JOIN `{CDR}.concept` ON sex_at_birth_concept_id = concept_id
        LEFT JOIN `{CDR}.death` USING (person_id)
        WHERE concept_name in ('Female', 'Male')
    """
