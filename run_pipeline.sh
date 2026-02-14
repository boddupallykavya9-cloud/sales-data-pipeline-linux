#!/bin/bash

echo "Pipeline started at $(date)" >> logs/pipeline.log
python scripts/clean_data.py >> logs/pipeline.log 2>&1
python scripts/generate_report.py >> logs/pipeline.log 2>&1

echo "Pipeline completed at $(date)" >> logs/pipeline.log

