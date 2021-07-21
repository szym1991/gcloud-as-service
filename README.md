# gcloud-as-a-service
```bash
gcloud builds submit --tag gcr.io/<project_id>/<function_name>
gcloud run deploy --image gcr.io/<project_id>/<function_name> --platform managed
```
e.g.
```bash
gcloud builds submit --tag gcr.io/lively-pursuit-320419/lstm
gcloud run deploy --image gcr.io/lively-pursuit-320419/lstm --platform managed
```

inspired from https://github.com/python-engineer/ml-deployment/tree/main/google-cloud-run
