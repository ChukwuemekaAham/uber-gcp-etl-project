locals {
  data_lake_bucket = "uber-data-bucket"
}

variable "credentials" {
  description = "My Credentials"
  default     = "../clear-router-390022-c10e818eac2e.json"
}

variable "project" {
  description = "Project"
  default     = "clear-router-390022"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "us-central1"
}

variable "zone" {
  description = "Region"
  #Update the below to your desired zone
  default     = "us-central1-a"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "uber_dataset"
}
