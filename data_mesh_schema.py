from typing import Literal

# ============================================================
# 1. ENTITY TYPES (≈ 54 entities, all uppercase)
# ============================================================

Entity = Literal[
    # --- Organization & Business ---
    "BUSINESS_DOMAIN",
    "SUBDOMAIN",
    "PRODUCT",
    "PROJECT",
    "TEAM",
    "CAPABILITY",

    # --- Data Assets & Analytics ---
    "DATA_DOMAIN",
    "DATA_PRODUCT",
    "DATASET",
    "TABLE",
    "COLUMN",
    "DATA_MODEL",
    "SCHEMA_VERSION",
    "METRIC",
    "KPI",
    "REPORT",
    "DASHBOARD",
    "DATA_QUALITY_RULE",
    "DATA_QUALITY_ISSUE",
    "DATA_CLASSIFICATION",
    "PII_FIELD",

    # --- Platform & Infrastructure ---
    "DATA_PLATFORM",
    "STORAGE_SYSTEM",
    "COMPUTE_CLUSTER",
    "DATABASE_INSTANCE",
    "DATA_PIPELINE",
    "DATA_JOB",
    "STREAMING_TOPIC",
    "MESSAGE_QUEUE",
    "FILE_SYSTEM_PATH",
    "SERVICE_ENDPOINT",
    "API_SPECIFICATION",
    "WORKFLOW",

    # --- Governance & ITSM ---
    "BUSINESS_PROCESS",
    "IT_PROCESS",
    "CHANGE_REQUEST",
    "INCIDENT",
    "PROBLEM_RECORD",
    "SERVICE_LEVEL_AGREEMENT",
    "POLICY",
    "STANDARD",
    "CONTROL",
    "RISK",
    "AUDIT_FINDING",

    # --- People & Roles ---
    "PERSON",
    "TECH_ROLE",
    "DATA_OWNER",
    "DATA_STEWARD",

    # --- Tools & Technology ---
    "TOOL",
    "TECHNOLOGY",
    "SOFTWARE_COMPONENT",

    # --- Events & Runs ---
    "PIPELINE_RUN",
    "JOB_RUN",
    "DQ_CHECK_EXECUTION",
]

# ============================================================
# 2. RELATION TYPES (uppercase, schema-safe)
# ============================================================

Relation = Literal[
    # Business structure
    "BELONGS_TO_BUSINESS_DOMAIN",
    "BELONGS_TO_DATA_DOMAIN",
    "SERVES_BUSINESS_DOMAIN",

    # Data asset structure
    "PART_OF_DATA_PRODUCT",
    "IMPLEMENTS_DATASET",
    "COLUMN_OF_TABLE",
    "VERSION_OF_MODEL",
    "MODELS_DATASET",
    "HAS_CLASSIFICATION",
    "IS_PII_FIELD",

    # Lineage / data flows
    "UPSTREAM_OF",
    "UPSTREAM_OF_TABLE",
    "READS_FROM_DATASET",
    "WRITES_TO_DATASET",
    "READS_FROM_TABLE",
    "WRITES_TO_TABLE",
    "FEEDS_DATASET",
    "PART_OF_PIPELINE",

    # Platform dependencies
    "USES_STORAGE_SYSTEM",
    "USES_COMPUTE_CLUSTER",
    "RUNS_ON_STORAGE_SYSTEM",
    "RESIDES_IN_DATABASE",
    "RUNS_ON_CLUSTER",
    "ORCHESTRATES_PIPELINE",
    "DEFINED_BY_API_SPEC",
    "EXPOSED_VIA_ENDPOINT",

    # Governance & quality
    "APPLIES_TO_DATA_PRODUCT",
    "APPLIES_TO_DATASET",
    "APPLIES_TO_TABLE",
    "VIOLATES_RULE",
    "FOUND_IN_DATASET",
    "EXECUTION_OF_RULE",
    "EXECUTION_ON_DATASET",
    "RELATES_TO_CONTROL",
    "MITIGATES_RISK",
    "AFFECTS_DATA_PRODUCT",
    "AFFECTS_SYSTEM",
    "RELATED_TO_PIPELINE",
    "VIOLATES_SLA",
    "COVERS_DATA_PRODUCT",

    # People & ownership
    "MEMBER_OF_TEAM",
    "HAS_TECH_ROLE",
    "OWNS_DATA_PRODUCT",
    "OWNS_DATASET",
    "STEWARD_OF_DATASET",
    "OWNS_PLATFORM",
    "OWNS_TOOL",

    # ITSM / change management
    "ROOT_CAUSE_OF_INCIDENT",
    "IMPLEMENTS_FIX_FOR_PROBLEM",
    "CHANGES_PIPELINE",
    "RUN_OF_PIPELINE",
    "RUN_OF_JOB",
    "GENERATED_DQ_EXECUTION",
]

# ============================================================
# 3. OUTGOING RELATIONS PER ENTITY
# (kg_validation_schema for SchemaLLMPathExtractor)
# ============================================================

kg_validation_schema = {
    # --- Organization & Business ---
    "BUSINESS_DOMAIN": [],
    "SUBDOMAIN": ["BELONGS_TO_BUSINESS_DOMAIN"],
    "PRODUCT": [],
    "PROJECT": [],
    "TEAM": ["OWNS_PLATFORM", "OWNS_TOOL"],
    "CAPABILITY": [],

    # --- Data Assets & Analytics ---
    "DATA_DOMAIN": ["BELONGS_TO_BUSINESS_DOMAIN"],
    "DATA_PRODUCT": [
        "BELONGS_TO_DATA_DOMAIN",
        "SERVES_BUSINESS_DOMAIN",
        "EXPOSED_VIA_ENDPOINT",
        "APPLIES_TO_DATA_PRODUCT",
        "COVERS_DATA_PRODUCT",
        "AFFECTS_DATA_PRODUCT",
    ],
    "DATASET": [
        "PART_OF_DATA_PRODUCT",
        "MODELS_DATASET",
        "IMPLEMENTS_DATASET",
        "HAS_CLASSIFICATION",
        "IS_PII_FIELD",
    ],
    "TABLE": [
        "IMPLEMENTS_DATASET",
        "COLUMN_OF_TABLE",
        "UPSTREAM_OF_TABLE",
        "RESIDES_IN_DATABASE",
        "APPLIES_TO_TABLE",
    ],
    "COLUMN": ["HAS_CLASSIFICATION", "IS_PII_FIELD"],
    "DATA_MODEL": ["MODELS_DATASET"],
    "SCHEMA_VERSION": ["VERSION_OF_MODEL"],
    "METRIC": ["DERIVED_FROM_DATASET"],
    "KPI": ["BASED_ON_METRIC"],
    "REPORT": ["TRACKS_KPI"],
    "DASHBOARD": [],
    "DATA_QUALITY_RULE": [
        "APPLIES_TO_DATASET",
        "APPLIES_TO_TABLE",
    ],
    "DATA_QUALITY_ISSUE": [
        "VIOLATES_RULE",
        "FOUND_IN_DATASET",
    ],
    "DATA_CLASSIFICATION": [],
    "PII_FIELD": [],

    # --- Platform & Infrastructure ---
    "DATA_PLATFORM": [
        "USES_STORAGE_SYSTEM",
        "USES_COMPUTE_CLUSTER",
    ],
    "STORAGE_SYSTEM": [],
    "COMPUTE_CLUSTER": [],
    "DATABASE_INSTANCE": ["RUNS_ON_STORAGE_SYSTEM"],
    "DATA_PIPELINE": [
        "READS_FROM_DATASET",
        "WRITES_TO_DATASET",
        "CHANGES_PIPELINE",
        "RELATED_TO_PIPELINE",
        "RUNS_ON_CLUSTER",
    ],
    "DATA_JOB": [
        "PART_OF_PIPELINE",
        "READS_FROM_TABLE",
        "WRITES_TO_TABLE",
    ],
    "STREAMING_TOPIC": ["FEEDS_DATASET"],
    "MESSAGE_QUEUE": [],
    "FILE_SYSTEM_PATH": [],
    "SERVICE_ENDPOINT": ["DEFINED_BY_API_SPEC"],
    "API_SPECIFICATION": [],
    "WORKFLOW": ["ORCHESTRATES_PIPELINE"],

    # --- Governance & ITSM ---
    "BUSINESS_PROCESS": [],
    "IT_PROCESS": [],
    "CHANGE_REQUEST": [
        "IMPLEMENTS_FIX_FOR_PROBLEM",
        "CHANGES_PIPELINE",
    ],
    "INCIDENT": [
        "AFFECTS_DATA_PRODUCT",
        "AFFECTS_SYSTEM",
        "ROOT_CAUSE_OF_INCIDENT",
        "RELATED_TO_PIPELINE",
        "VIOLATES_SLA",
    ],
    "PROBLEM_RECORD": ["ROOT_CAUSE_OF_INCIDENT"],
    "SERVICE_LEVEL_AGREEMENT": [
        "APPLIES_TO_DATASET",
        "COVERS_DATA_PRODUCT",
    ],
    "POLICY": [
        "APPLIES_TO_DATA_PRODUCT",
        "APPLIES_TO_DATASET",
    ],
    "STANDARD": ["APPLIES_TO_TABLE"],
    "CONTROL": ["MITIGATES_RISK"],
    "RISK": [
        "AFFECTS_SYSTEM",
        "MITIGATES_RISK",
    ],
    "AUDIT_FINDING": ["RELATES_TO_CONTROL"],

    # --- People & Roles ---
    "PERSON": [
        "MEMBER_OF_TEAM",
        "HAS_TECH_ROLE",
        "STEWARD_OF_DATASET",
    ],
    "TECH_ROLE": [],
    "DATA_OWNER": [
        "OWNS_DATA_PRODUCT",
        "OWNS_DATASET",
    ],
    "DATA_STEWARD": ["STEWARD_OF_DATASET"],

    # --- Tools & Technology ---
    "TOOL": [],
    "TECHNOLOGY": [],
    "SOFTWARE_COMPONENT": [],

    # --- Events & Runs ---
    "PIPELINE_RUN": [
        "RUN_OF_PIPELINE",
        "GENERATED_DQ_EXECUTION",
    ],
    "JOB_RUN": ["RUN_OF_JOB"],
    "DQ_CHECK_EXECUTION": [
        "EXECUTION_OF_RULE",
        "EXECUTION_ON_DATASET",
    ],
}
