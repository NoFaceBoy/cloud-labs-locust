from locust import FastHttpUser, task, between

endpoints = ['/api/actors',
             '/api/awards',
             '/api/companies',
             '/api/countries',
             '/api/directors',
             '/api/genres',
             '/api/movies',
             '/api/nominations',
             '/api/roles']


class Test(FastHttpUser):
    wait_time = between(1, 2)

    @task
    def cloud_load(self):
        for endpoint in endpoints:
            self.client.get(f"{endpoint}", auth=('user', 'password'))
        self.client.get(f"{endpoints[3]}/2")
        for id in range(6, 9):
            self.client.get(f"{endpoints[6]}/{id}")
