from locust import HttpLocust, TaskSet, task


class AtlasTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/about/")

    @task
    def api_casy(self):
        self.client.get("/api/export/usa/all/show/2012/?lang=en&amp;product_classification=hs4&amp;data_type=json&amp;single_year=true")


class AtlasUser(HttpLocust):
    task_set = AtlasTasks
