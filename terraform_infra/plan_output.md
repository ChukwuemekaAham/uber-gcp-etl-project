MINGW64 ~/Downloads/Cloud/data-current-projects/uber-gcp-etl-project/terraform_infra       
$ terraform plan

Terraform used the selected providers to generate the  
following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.output_dataset will be created
  + resource "google_bigquery_dataset" "output_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "uber_dataset"    
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "US"
      + max_time_travel_hours      = (known after apply)
      + project                    = "clear-router-390022"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)

      + access {
          + domain         = (known after apply)       
          + group_by_email = (known after apply)       
          + iam_member     = (known after apply)       
          + role           = (known after apply)       
          + special_group  = (known after apply)       
          + user_by_email  = (known after apply)       

          + dataset {
              + target_types = (known after apply)     

              + dataset {
                  + dataset_id = (known after apply)   
                  + project_id = (known after apply)   
                }
            }

          + routine {
              + dataset_id = (known after apply)       
              + project_id = (known after apply)       
              + routine_id = (known after apply)       
            }

          + view {
              + dataset_id = (known after apply)       
              + project_id = (known after apply)       
              + table_id   = (known after apply)       
            }
        }
    }

  # google_storage_bucket.input_bucket will be created
  + resource "google_storage_bucket" "input_bucket" {  
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "uber-data-bucket-clear-router-390022"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"       
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }

          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }

      + website {
          + main_page_suffix = (known after apply)     
          + not_found_page   = (known after apply)     
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + input_bucket_name = "uber-data-bucket-clear-router-390022"
  + output_dataset_id = "uber_dataset"

────────────────────────────────────────────────────── 

Note: You didn't use the -out option to save this      
plan, so Terraform can't guarantee to take exactly     
these actions if you run "terraform apply" now.