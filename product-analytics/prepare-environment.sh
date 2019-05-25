#!/usr/bin/env bash

export BUCKET_NAME="sandbox-datalake-123455"

# create buckets
gsutil mb -b on gs://${BUCKET_NAME}

# ${BUCKET_NAME}/incoming
# ${BUCKET_NAME}/datalake
# ${BUCKET_NAME}/processing