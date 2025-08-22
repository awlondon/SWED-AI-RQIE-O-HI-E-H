# Datasets

This directory stores structured datasets used by the project.

## Schema

Both CSV and JSON datasets should use the following fields:

- `profile_id`: Unique identifier for a profile or record.
- `sector`: The sector or industry related to the entry.
- `source`: Origin of the data (e.g., OSINT, report, internal).

CSV files must include a header row with these columns. JSON files should contain an array of objects with these keys.

## Files

- `fake_profiles.csv`: placeholder for profile records.
- `indictments.csv`: placeholder for legal indictment information.
