CREATE DATABASE IF NOT EXISTS Generative_AI;
USE Generative_AI;

CREATE TABLE IF NOT EXISTS generative_ai_tools (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tool_name VARCHAR(255),
    company VARCHAR(255),
    category_canonical VARCHAR(255),
    modality_canonical VARCHAR(255),
    open_source INT,
    api_available INT,
    api_status VARCHAR(255),
    website VARCHAR(255),
    source_domain VARCHAR(255),
    release_year INT,
    years_since_release INT,
    mod_text INT,
    mod_image INT,
    mod_video INT,
    mod_audio INT,
    mod_code INT,
    mod_design INT,
    mod_infra INT,
    mod_productivity INT,
    mod_safety INT,
    mod_multimodal INT,
    modality_count INT
);
