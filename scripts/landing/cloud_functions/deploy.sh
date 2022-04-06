#!/bin/sh
# Deploy load_ftbl_data_uk
gcloud functions deploy load_ftbl_data_uk --entry-point run --runtime python39 --trigger-http --timeout=540s --source="./load_ftbl_data_uk/" --memory=1024MB --region=australia-southeast1
